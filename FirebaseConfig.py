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
  "apiKey": "AIzaSyC0JCd3vkI320V6BRj0ZJABviJfNKq_JeM",
  "authDomain": "dwave-52e42.firebaseapp.com",
  "projectId": "dwave-52e42",
  "storageBucket": "dwave-52e42.appspot.com",
  "messagingSenderId": "471249806784",
  "appId": "1:471249806784:web:96b6d56cbc9037f2cd5425",
  "measurementId": "G-7FT6CL03TR",
"databaseURL": "gs://dwave-52e42.appspot.com",

}
firebase = pyrebase.initialize_app(config)
storage=firebase.storage()
db=firebase.database()