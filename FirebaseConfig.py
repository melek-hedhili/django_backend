from pyrebase import pyrebase
# config={
#     'apiKey': "AIzaSyDmJejXUysb0UaireG1qk5PQsFMGziHgGI",
#     'authDomain': "recognition-6a44f.firebaseapp.com",
#     'projectId': "recognition-6a44f",
#     'storageBucket': "recognition-6a44f.appspot.com",
#     'messagingSenderId': "585141364281",
#     'appId': "1:585141364281:web:0391e9e33ff0aed06c0fe8",
#     'measurementId': "G-472DL2PVDH",
#     'databaseURL': "https://recognition-6a44f-default-rtdb.firebaseio.com/",
    
# }

config = {
  "apiKey": "AIzaSyCKl4tCOcWR7apRdJN9f90Zm6EoEtk4akE",
  "authDomain": "dwave2-ba3cd.firebaseapp.com",
  "databaseURL": "https://dwave2-ba3cd-default-rtdb.firebaseio.com",
  "projectId": "dwave2-ba3cd",
  "storageBucket": "dwave2-ba3cd.appspot.com",
  "messagingSenderId": "525608993922",
  "appId": "1:525608993922:web:1ead465c6c5bb376f4e09b",
  "measurementId": "G-T7SBL9TBQT"
};
firebase = pyrebase.initialize_app(config)
storage=firebase.storage()
db=firebase.database()