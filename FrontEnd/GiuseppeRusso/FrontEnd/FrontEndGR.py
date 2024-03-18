from Finestre.Login import login
import requests

dati = {}
dati['filename'] = '/Users/giusepperusso/Downloads/Python/gitpython/Dati/classe.json'
dati['host'] = 'python.hostingstudenti.fortechance.com'
dati['database'] = 'c3db'
dati['username'] = 'c3python'
dati['password'] = 'ThePythonCourse098'
risposta = requests.put('http://127.0.0.1/init', json = dati)
login()