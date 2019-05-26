# ChatBot Using Rasa Stack/Framework
A chatbot using Rasa framework has been built. It would be implemented on CREST ERP product to help customers fetch the relevant information easily and quickly.

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
python -m rasa_core.train -d crestbot_domain.yml -s data/stories.md -o models/dialogue/ -c policy_config.yml

```

#### To run the action server
```
python -m rasa_core_sdk.endpoint --actions action

```

#### To run the app
```
python app.py

```

#### To run the bot on command line
```
python -m rasa_core.run -d models/dialogue -u models/nlu/default/cresterpbotnlu --endpoints endpoints.yml --debug

```
