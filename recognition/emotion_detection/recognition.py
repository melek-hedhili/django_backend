
from deepface import DeepFace
user_name="Melek Hedhili"
import datetime
date_time = datetime.datetime.now()
date_time = date_time.strftime("%Y-%m-%d")
# Working with pre trained model 
expression=""
def get_expression(image_path):
  global expression
  expression="" 
  obj = DeepFace.analyze(img_path = image_path, actions = ['emotion'] ,prog_bar=True,detector_backend='mtcnn')
  expression=expression+obj["dominant_emotion"]
  print(obj)
  return obj