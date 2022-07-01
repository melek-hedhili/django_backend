import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.utils import img_to_array , load_img
from keras.models import load_model
import os
#importing the firebase config file
from FirebaseConfig import *
user_name="Melek Hedhili"
import datetime
date_time = datetime.datetime.now()
date_time = date_time.strftime("%Y-%m-%d")
# Working with pre trained model 
url=""
expression=""
def get_expression(image_path):
  global url,expression
  model = load_model("./recognition/emotion_detection/best_model.h5")
  op = {0: 'Angry', 1: 'Disguist', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}
  img = load_img(image_path, target_size=(224,224) )
  i = img_to_array(img)/255
  input_arr = np.array([i])
  input_arr.shape
  pred = np.argmax(model.predict(input_arr))
  expression= expression+op[pred]+","
  print(f"{expression}")
# to display the image  
  plt.imshow(input_arr[0])
  plt.title(op[pred])
  #get date and time
  path = "./treated_image/"+user_name+" is "+op[pred]+".png"
  plt.savefig(path)
  #save image to firebase storage
  storage.child(f"treated_image/{user_name}/{date_time}/{expression}.png").put(path)
  #get the url of the image
  url = url+storage.child(f"treated_image/{user_name}/{date_time}/{expression}.png").get_url(None)+" ,"
  print({"expression":expression,"treated_image_url":url})
  os.remove(path)
  
  return {"expression":expression,"treated_image_url":url}
