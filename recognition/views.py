
import os
#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #get desktop path (
    #problems encountered when saving image to a path , must give full path)
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import jsonresonse
from django.http import JsonResponse

#import get_expression from recognition.py
from recognition.emotion_detection.recognition import get_expression
from recognition.emotion_detection.videotester import get_video_expression
#importing the firebase config file
from FirebaseConfig import *

user_name="Melek Hedhili "
import datetime
date_time = datetime.datetime.now()
date_time = date_time.strftime("%Y-%m-%d")
def home(request):
    
    return HttpResponse(f'Hello Youre at the recognition home.')


@api_view(['POST'])
def uploadImage(request):
    if request.method == 'POST':
        expression=[]
        image = request.FILES.getlist('image')
        print(image)
        
        #save image to firebase storage in try except block
        try:
            for i in image:
                link=""
                print("i=",i)
                path=user_name+i.name
                storage.child(f"{user_name}/{date_time}/{i.name}").put(i)
                #get link of images
                link=link+(storage.child(f"{user_name}/{date_time}/{i.name}").get_url(None))
                #download the images from firebase storage and save them to local directory
                storage.child(f"{user_name}/{date_time}/{i.name}").download(path=f"./recognition/downloads/{path}",filename=path)
                #get the emotion of the image
                result=get_expression(os.path.abspath(path))
                print("type of",type(result))
                result["link"]=link
                expression.append(result)

                
                #expression.append({'image_url':link})
            #retun response with the emotion of the image + link of the image and success message
            os.remove(path)
            return Response({"success":True,"data":expression},status=status.HTTP_200_OK)      
        except Exception as e:
            return Response("Error: "+str(e), status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Error: Method not allowed", status=status.HTTP_400_BAD_REQUEST)
    
               
@api_view(['POST'])
def uploadVideo(request):
    
    #get the video from request
    video=request.FILES.getlist('video')
    print(video)
    path=user_name+video[0].name
    #save video to firebase storage in try except block
    try:
        storage.child("videos").child(video[0].name).put(video[0])
        #get link of video
        link=storage.child("videos").child(video[0].name).get_url(None)
        #download the video from firebase storage and save it to local directory
        storage.child("videos").child(video[0].name).download(path=f"./recognition/downloads/{path}",filename=path)
        #get the emotion of the video
        expression_video=get_video_expression(os.path.abspath(path))
        #save the expression_video to firebase storage
        print(expression_video)
        
        
        storage.child("treated_video").child(video[0].name).put(f'{expression_video["path_for_video"]}')

        #get the link of the video
        link_video=storage.child("treated_video").child(video[0].name).get_url(None) 
        #retun response with the emotion of the video + link of the video and success message
        #.remove(path)
        #os.remove(expression_video["path_for_video"])
        return Response({"success":True,"original_video_url":link,"treated_video_url":link_video,"emotions list":f'{expression_video["final_list"]}'},status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response("Error: "+str(e), status=status.HTTP_400_BAD_REQUEST)


    
    

    
    
