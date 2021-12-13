import paho.mqtt.client as client_lib
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate("./serviceKey.json")
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://sistemclimatizator-default-rtdb.europe-west1.firebasedatabase.app/'
})
