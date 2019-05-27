# ChatBot Using Rasa Stack/Framework
A chatbot using Rasa framework has been built. It is an assignment chabot project to help customers book flight tickets easily and quickly.
Here, I was facing some issues with importing JSON data into rasa, mainly due to some version issues. So, I have imported json file to Postgresql and then I have fetched relevant information from Postgresql. 
Due to time limitation, I could not implement it on Flask but I can do it. Other issue is that, I have excluded some of the requirements from this chatbot like: giving options to the users to opt for cheaper/faster way, date range, etc.
Now, it can only process/ answer questions if it has departure airport, destination airport and date of departure available.
I have not added exception handling as well. These all are the issues which could be handled given I have more time. But, since I am busy on weekdays with my current organization's workload so I could do only this much. 
Please feel free to reach out to me if you have any doubts.
We can definitely make it robust, like it would handle date in any format, it may ask for user details before confirmation, it may ask for payment methods and details, etc.
I have also shared a screenshot of postgresql console where I have shown how I have stored it there ('DataStoredInPostgres.png').

### Example Conversation

```
User: Hi, I want to book a flight ticket from Kochi to Pune on 30/08/2019.
Bot will show a dictionary with relevant info and will ask the user to type the index number to book the flight.
User: 24
Bot will show a confirmation of booked ticket with reference number.
User: Thanks
Bot will ask if you need to book more tickets.
User: Nope
Bot: Happy to serve you.

```

### Version of Python used is 3.6.0

### Versions of Rasa-NLU and Rasa-Core
Rasa-NLU = 0.14.1
Rasa-Core = 0.13.0
Versions for all libraried could be found in 'requirements.txt' file.

### Installation

#### Installing RASA-NLU + spacy

```
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en

```

Other possible ways :

```
git clone https://github.com/RasaHQ/rasa_nlu.git
cd rasa_nlu
pip install -r requirements.txt
pip install -e .
pip install -r alt_requirements/requirements_full.txt

Please refer: 'https://rasa.com/docs/nlu/installation/' for more details.

```

#### Installing RASA Core

```
pip install rasa_core

```

Other possible ways

```
git clone https://github.com/RasaHQ/rasa_core.git
cd rasa_core
pip install -r requirements.txt
pip install -e .
pip install -r dev-requirements.txt
pip install -e .

Please refer: 'https://rasa.com/docs/core/installation/' for more details.

```

### Running the server in the backend
#### To train Rasa-NLU
```
python nlu_model.py

```

#### To train Rasa-Core
```
python -m rasa_core.train -d chatbot_domain.yml -s data/stories.md -o models/dialogue/ -c policy_config.yml

```

#### To run the action server
```
python -m rasa_core_sdk.endpoint --actions action

```

#### To run the bot on command line (in run mode)
```
python -m rasa_core.run -d models/dialogue -u models/nlu/default/chatbotnlu --endpoints endpoints.yml --debug

```

#### To run the bot on command line (in debug mode)
```
python -m rasa_core.run -d models/dialogue -u models/nlu/default/chatbotnlu --endpoints endpoints.yml --debug

```
