from rest_framework import serializers,fields
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    #time = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model=Task
        fields=['employee_name','task','time']
