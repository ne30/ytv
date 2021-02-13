from django.shortcuts import render
from .serializers import VideoSerializer
from .models import Video
from rest_framework import viewsets
from rest_framework.response import Response
from pytube import YouTube
from django.views.static import serve
import os

class VideoViewSet(viewsets.ModelViewSet):
    
    def list(self, request, *args, **kwargs):
        userDetail = request.GET.get('id')
        temp = Video.objects.get(userName = userDetail)
        
        if temp is not None and userDetail is not None:
            if temp.count > 100:
                return Response('Limit', status=401)
            else:
                url = str(request.GET.get('url'))
                try:
                    fileName = str(temp.userName + '_' + str(temp.count))
                    video = YouTube(url).streams.first().download(output_path='./media/' , filename=fileName)
                    print('Downloaded')
                    filepath = './media/' + fileName + '.mp4'
                    temp.count = temp.count + 1
                    temp.save()
                    return serve(request,os.path.basename(filepath), os.path.dirname(filepath))
                except Exception as e:
                    print(e)
                    return Response('Invalid', 404)