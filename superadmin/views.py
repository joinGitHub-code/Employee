from django.shortcuts import render,redirect


from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from .serializers import *
from employee.models import *

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
#from rest_framework.permissions import IsAuthenticated

# Create your views here.

##class admintask_list(APIView):
##    
##    def get(self,request,*args,**kwargs):
##        tasks = Task.objects.all().order_by('-id')
##        serializer = TaskSerializer(tasks, many=True)
##        return Response(serializer.data)

@method_decorator(login_required, name='dispatch')
class admintask_UpdateCommentView(RetrieveUpdateDestroyAPIView):
    """
    API view to add comment of a task 
    """
    #permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = CommentSerializer  


def user_logout(request):
	logout(request)
	return redirect('/task-list')
