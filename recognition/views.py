import json
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #get desktop path (
    #problems encountered when saving image to a path , must give full path)

from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.pyplot import get
from pyrebase import pyrebase
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import get_expression from recognition.py

from recognition.emotion_detection.recognition import get_expression

#importing the firebase config file
from FirebaseConfig import *

def home(request):
    return HttpResponse("Hello, world. You're at the recognition home.")
@api_view(['POST'])
def uploadImage(request):
    #get all images from request
    image=request.FILES.getlist('image') 
    print(image)
    
    #save image to firebase storage in try except block
    try:

        for i in image:
            storage.child("images").child(i.name).put(i)
            #get link of images
            link=storage.child("images").child(i.name).get_url(None)
            
        #download the images from firebase storage and save them to local directory
            storage.child("images").child(i.name).download(path=f"{desktop}/server/recognition/downloads/",filename="new_"+i.name,)
            
        #get the emotion of the image
        expression=get_expression(os.path.abspath("new_"+i.name))
        #save the
        #retun response with the emotion of the image + link of the image and success message
        return Response({"success":True,"data":expression,"original_image_url":link},status=status.HTTP_200_OK)
        
        
    except Exception as e:
        return Response("Error: "+str(e), status=status.HTTP_400_BAD_REQUEST)
               
    
    
    

    
    
