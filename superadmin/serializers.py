from rest_framework import serializers,fields
from employee.models import Task

class CommentSerializer(serializers.ModelSerializer):
    #time = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model=Task
        fields=['employee_name','task','time','comments']
