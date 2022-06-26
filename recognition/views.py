import json
import os

import recognition
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
from recognition.emotion_detection.videotester import get_video_expression

#importing the firebase config file
from FirebaseConfig import *
from recognition.emotion_detection.recognition import user_name,date_time


def home(request):
    return HttpResponse(f'Hello {user_name}. Youre at the recognition home.')


@api_view(['POST'])
def uploadImage(request):
    #get all images from request
    image=request.FILES.getlist('image')
    link=""
    
    
    #save image to firebase storage in try except block
    try:

        for i in image:
            
            storage.child("images").child(i.name).put(i)
            #get link of images
            link=link+storage.child("images").child(i.name).get_url(None)+" ,"
            
        #download the images from firebase storage and save them to local directory
            storage.child("images").child(i.name).download(path=f"{desktop}/server/recognition/downloads/",filename="new_"+i.name,)
            
        #get the emotion of the image
            expression=get_expression(os.path.abspath("new_"+i.name))
        #save the
        #retun response with the emotion of the image + link of the image and success message
        
        return Response({"success":True,"data":expression,"original_image_url":link},status=status.HTTP_200_OK)
        
        
    except Exception as e:
        return Response("Error: "+str(e), status=status.HTTP_400_BAD_REQUEST)
               
@api_view(['POST'])
def uploadVideo(request):
    #get the video from request
    video=request.FILES.getlist('video')
    print(video)
    #save video to firebase storage in try except block
    try:
        storage.child("videos").child(video[0].name).put(video[0])
        #get link of video
        link=storage.child("videos").child(video[0].name).get_url(None)
        #download the video from firebase storage and save it to local directory
        storage.child("videos").child(video[0].name).download(path=f"{desktop}/server/recognition/downloads/",filename="new_"+video[0].name,)
        #get the emotion of the video
        expression_video=get_video_expression(os.path.abspath("new_"+video[0].name))
        #save the expression_video to firebase storage
        
        
        storage.child("treated_video").child(video[0].name).put(f'{expression_video["path_for_video"]}')
        print("storage saved")
        #save json emotions to firebase realtime database
        data={"name":"Melek","age":"23","emotions":f'{expression_video["final_list"]}'}
        print("data object saved")
        db.child(user_name).child(date_time).push(data)
        print("data saved")
        #get the link of the video
        link_video=storage.child("treated_video").child(video[0].name).get_url(None)
        print("link saved")
        #retun response with the emotion of the video + link of the video and success message
        return Response({"success":True,"original_video_url":link,"treated_video_url":link_video,"emotions list":f'{expression_video["final_list"]}'},status=status.HTTP_200_OK)
    except Exception as e:
        return Response("Error: "+str(e), status=status.HTTP_400_BAD_REQUEST)


    
    

    
    
