from pyrebase import pyrebase
config={
    'apiKey': "AIzaSyDmJejXUysb0UaireG1qk5PQsFMGziHgGI",
    'authDomain': "recognition-6a44f.firebaseapp.com",
    'projectId': "recognition-6a44f",
    'storageBucket': "recognition-6a44f.appspot.com",
    'messagingSenderId': "585141364281",
    'appId': "1:585141364281:web:0391e9e33ff0aed06c0fe8",
    'measurementId': "G-472DL2PVDH",
    'databaseURL': "https://recognition-6a44f-default-rtdb.firebaseio.com/",
    
}
firebase = pyrebase.initialize_app(config)
storage=firebase.storage()
db=firebase.database()