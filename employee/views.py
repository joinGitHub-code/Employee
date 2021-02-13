from django.shortcuts import render,redirect


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .serializers import *
# Create your views here.

@api_view(['GET'])
def api_overview(request):

    api_urls = {        
        
        'List': '/task-list/',
        'Create': '/task-create/',
        'Update and Delete':'/task-update-delete/<int:pk>',
        'SuperAdmin_Login':'/login/',
        'SuperAdmin_Add_comment':'/add-comment/<int:pk>',
        'SuperAdmin_LogOut':'/logout/',      
        
        }

    return Response(api_urls)


class emptask_CreateView(ListCreateAPIView):
    """
    API view to retrieve list of task or create new
    """
    model=Task
    queryset=Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        bill_data = request.data
        print(bill_data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('/task-create')

    
class emptask_UpdateView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve list of task and update 
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    
    
class emptask_list(APIView):
    """
    API view to retrieve list of task 
    """
    
    def get(self,request,*args,**kwargs):
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
