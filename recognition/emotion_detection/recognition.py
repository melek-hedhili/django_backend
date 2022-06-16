import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #get desktop path (problems encountered when saving image to a path , must give full path)
from keras.layers import Flatten, Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.utils import img_to_array , load_img
from keras.applications.mobilenet import MobileNet, preprocess_input 
from keras.losses import categorical_crossentropy
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import load_model
from pyrebase import pyrebase
#importing the firebase config file
from FirebaseConfig import *
user_name="Melek Hedhili"
import datetime
date_time = datetime.datetime.now()
date_time = date_time.strftime("%Y-%m-%d")

# Working with pre trained model 
def get_expression(image_path):
  base_model = MobileNet( input_shape=(224,224,3), include_top= False )

  for layer in base_model.layers:
    layer.trainable = False


  x = Flatten()(base_model.output)
  x = Dense(units=7 , activation='softmax')(x)

  # creating our model.
  model = Model(base_model.input, x)

  model.compile(optimizer='adam', loss= categorical_crossentropy , metrics=['accuracy']  )

  train_datagen = ImageDataGenerator(
      zoom_range = 0.2, 
      shear_range = 0.2, 
      horizontal_flip=True, 
      rescale = 1./255
     
)

  train_data = train_datagen.flow_from_directory(directory= "./recognition/emotion_detection/train", 
                                               target_size=(224,224), 
                                               batch_size=32,)


  train_data.class_indices

  val_datagen = ImageDataGenerator(rescale = 1./255 )

  val_data = val_datagen.flow_from_directory(directory= "./recognition/emotion_detection/test", 
                                           target_size=(224,224), 
                                           batch_size=32,)




# early stopping
  es = EarlyStopping(monitor='val_accuracy', min_delta= 0.01 , patience= 5, verbose= 1, mode='auto')

# model check point
  mc = ModelCheckpoint(filepath="best_model.h5", monitor= 'val_accuracy', verbose= 1, save_best_only= True, mode = 'auto')

# puting call back in a list 
  call_back = [es, mc]


  model = load_model("./recognition/emotion_detection/best_model.h5")


  op = dict(zip( train_data.class_indices.values(), train_data.class_indices.keys()))
  #path = "sp.png"
  img = load_img(image_path, target_size=(224,224) )

  i = img_to_array(img)/255
  input_arr = np.array([i])
  input_arr.shape

  pred = np.argmax(model.predict(input_arr))
  expression= user_name+op[pred]

  print(f" the image is of {expression}")

# to display the image  
  
  
  plt.imshow(input_arr[0])
  plt.title(op[pred])
  #save the image with different names
  
  #get date and time


  
  path = desktop+"/server/treated_image/"+expression+".png"
  plt.savefig(path)
  #save image to firebase storage

  storage.child(f"treated_image/{user_name}/{date_time}/{expression}.png").put(path)
  #get the url of the image
  url = storage.child(f"treated_image/{user_name}/{date_time}/{expression}.png").get_url(None)
  #print current directory
  



  #return op[pred]
  return {"expression":expression,"treated_image_url":url}
  
