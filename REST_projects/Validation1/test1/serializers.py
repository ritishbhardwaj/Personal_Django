from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['name','roll','city']



# def start_with_r(value:str):
#     if value[0].lower() != 'r':
#       raise serializers.ValidationError('Name Should start with R')

# class StudentSerializer(serializers.Serializer):
#  name= serializers.CharField(max_length=100,validators =[start_with_r])
#  roll = serializers.IntegerField()
#  city= serializers.CharField(max_length=100)

#  def create(self, validated_data):
#   return Student.objects.create(**validated_data)

#  def update(self, instance, validated_data):
#   # print(instance.name)
#   instance.name = validated_data.get('name', instance.name)
#   # print(instance.name)
#   instance.roll = validated_data.get('roll', instance.roll)
#   instance.city = validated_data.get('city', instance.city)
#   instance.save()
#   return instance
 
#  #Field Validation for roll
#  def validate_roll(self, value : int):
#   if value >= 200:
#    raise serializers.ValidationError('Seat Full')
#   return value
 
#  def validate(self, data:dict):
#   nm:str=data.get('name')
#   ct:str=data.get('city')

#   if nm.lower() ==  'rohit' and ct.lower()!='ranchi':
#     raise serializers.ValidationError('City must be ranchi')   
#   return data