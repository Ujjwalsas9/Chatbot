from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted
from list_dict_DB import list_dict_DB
import random
import json
import psycopg2


class ActionShowTicket(Action):
    """
    This action is useful for showing the available flights to users.
    """

    def name(self):
        return "action_show_ticket"

    def run(self, dispatcher, tracker, domain):
        Departure = tracker.get_slot('departure').lower()
        Destination = tracker.get_slot('destination').lower()
        Date = tracker.get_slot('date')
        con = psycopg2.connect(user="postgres", password="abcd1234", host="127.0.0.1", port="5432",
                               database="flight_tickets")
        cur = con.cursor()

        def Convert(string):
            li = list(string.split(","))
            return li

        if Departure != None and Destination != None and Date != None:
            Departure = Departure.lower()
            Destination = Destination.lower()
            Date = Date
            cur.execute("SELECT info ->> 'Row_Number' as Row, info ->> 'From' AS Departure, info ->> 'To' AS Destination, info ->> 'Airlines' AS Airlines, info ->> 'Seats' AS Seats, info ->> 'Flight No' AS Flight_No, info ->> 'Date' AS Date, info ->> 'Ref_no' AS Ref_No, info ->> 'Connection' AS Connection,info ->> 'Price' AS Price FROM tickets where lower(info ->> 'From') = '%s' and lower(info ->> 'To') = '%s' and (info ->> 'Date') = '%s';" % (Departure, Destination, Date))
            rows = cur.fetchall()
            if len(rows) != 0:
                for row in rows:
                    Row_No = row[0]
                    Departure = row[1]
                    Destination = row[2]
                    Airlines = row[3]
                    Seats = row[4]
                    Flight_No = row[5]
                    Date = row[6]
                    #Ref_No = random.choice(Convert(row[6]))
                    Connection = row[7]
                    Price = row[8]

                con.close()
                response = json.dumps([{'Row': Row_No, 'Departure': Departure, 'Destination': Destination, 'Airlines': Airlines,
                                        'Seats': Seats, 'Flight_No': Flight_No, 'Date': Date, 'Connection': Connection, 'Price': Price}])
            else:
                response = "Sorry, could not find any matching results."

        return dispatcher.utter_message(response)


class ActionBookTicket(Action):
    """
    This action is useful for showing the users that they have booked the ticket with reference number.
    """

    def name(self):
        return "action_book_ticket"

    def run(self, dispatcher, tracker, domain):
        Departure = tracker.get_slot('departure').lower()
        Destination = tracker.get_slot('destination').lower()
        Date = tracker.get_slot('date')
        Row_No = tracker.get_slot('row_no')
        con = psycopg2.connect(user="postgres", password="abcd1234", host="127.0.0.1", port="5432",
                               database="flight_tickets")
        cur = con.cursor()

        def Convert(string):
            li = list(string.split(","))
            return li

        if Departure != None and Destination != None and Date != None:
            Departure = Departure.lower()
            Destination = Destination.lower()
            Date = Date
            cur.execute("SELECT info ->> 'From' AS Departure, info ->> 'To' AS Destination, info ->> 'Airlines' AS Airlines, info ->> 'Flight No' AS Flight_No, info ->> 'Date' AS Date, info ->> 'Ref_no' AS Ref_No, info ->> 'Price' AS Price FROM tickets where (info ->> 'Row_Number') = '%s';" % (Row_No))
            rows = cur.fetchall()
            if len(rows) != 0:
                for row in rows:
                    Departure = row[0]
                    Destination = row[1]
                    Airlines = row[2]
                    Flight_No = row[3]
                    Date = row[4]
                    Ref_No = random.choice(Convert(row[5]))
                    Price = row[6]

                con.close()
                response = json.dumps([{'Reference Number': Ref_No, 'Departure': Departure, 'Destination': Destination, 'Airlines': Airlines,
                                        'Flight_No': Flight_No, 'Date': Date, 'Price': Price}])
            else:
                response = "Sorry, could not book your ticket."

        return dispatcher.utter_message(response)


class ActionDefaultFallback(Action):
    """
    This action is used when the intent and entity falls below the given cut-off value as defined in 
    'policy_cofig.yml' file.
    """

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_default', tracker)
        return [UserUtteranceReverted()]


class ActionRenew(Action):
    """
    This action is used to reset the context/slots in the conversation flow.
    """

    def name(self):
        return 'action_renew'

    def run(self, dispatcher, tracker, domain):
        return_slots = []
        for slot in tracker.slots:
            # Here we do not have any slots named 'anything' so it set all the slots to 'None' but
            # I have kept this option here to make it adaptable to the future requirements.
            if slot != "anything":
                return_slots.append(SlotSet(slot, None))
        return return_slots
