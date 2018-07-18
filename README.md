# Fuel watch

## Library documentation
- Flask: http://flask.pocoo.org/docs/1.0/

## Requirements
- python 3.x is geinstalleerd op je machine
- pip install virtualenv

## Aanmaken virtual environment
- Open de command line en ga naar de directory waar je de virtualenv geinstalleerd wilt hebben.
- Run het commando om een nieuwe virtualenv aan te maken: "virtualenv <i>naam omgeving</i>". 

De nieuwe omgeving zal nu geinstalleerd worden.

## Starten virtuele omgeving
- Open de command line
- Ga naar de ~\<virtualenv>\Scripts folder
- type in "activate" om de omgeving op te starten

## Installeren benodigde packages
- Open de command line
- Ga naar de root folder van het project
- Typ het volgende commando in: pip install -r requirements.txt

## Running local server
- Open de command line
- Ga naar de src folder in het project
- Geef het commando: set FLASK_APP=src
- Geeft het command0: flask run
- Ga in de browser naar http://localhost:5000