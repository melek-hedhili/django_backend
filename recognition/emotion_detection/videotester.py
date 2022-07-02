import os
#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #get desktop path (problems encountered when saving image to a path , must give full path)

import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from tensorflow.keras.utils import img_to_array 
from keras.models import  load_model
import numpy as np
list=[]
from recognition.emotion_detection.recognition import user_name,date_time
# load model
def get_video_expression(video_path):
  
    path_for_video=f'{user_name}_{date_time}_video.avi'

    model = load_model("./recognition/emotion_detection/best_model_2.h5")
    face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter(path_for_video, cv2.VideoWriter_fourcc(*"X264"), 20, (640,480))
    # duration = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # duration=duration/10  
    # print("durataion",duration)
    while True:
        ret, test_img = cap.read()
         
        if ret:
            gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)
            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
            for (x, y, w, h) in faces_detected:
                cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
                roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
                roi_gray = cv2.resize(roi_gray, (224, 224))
                img_pixels = img_to_array(roi_gray)
                img_pixels = np.expand_dims(img_pixels, axis=0)
                img_pixels /= 255
                predictions = model.predict(img_pixels)
                max_index = np.argmax(predictions[0])
                emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
                predicted_emotion = emotions[max_index]
                cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            list.append(predicted_emotion)
            resized_img = cv2.resize(test_img, (640, 480))  
            predicted_video=out.write(resized_img)
        else:
            break
    cap.release()
    out.release()
    
    print("The video was successfully saved")
    
    print(list)
    
    return {"path_for_video":path_for_video,"final_list":list}

