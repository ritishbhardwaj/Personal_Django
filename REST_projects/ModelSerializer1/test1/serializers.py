

from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    
  def validate_roll(self, value):
    if value >= 200:
      raise serializers.ValidationError('Seat Full')
    return value
  
  def validate(self,data:dict):
    nm :str= data.get('name')
    print(data,"%%%%%%%%%%%%%%%%%")
    ct:str =data.get('city')
    if nm.lower() == 'ritish' and ct.lower()!='amritsar':
      raise serializers.ValidationError('City must be Amritsar')
    return data   
#   name = serializers.CharField(read_only=True)
  class Meta:
    model = Student
    fields = ['id','name','roll','city']
    # read_only_fields= ['name']
    '''or'''
    # extra_kwargs = {'name':{'read_only':True}}
    
  