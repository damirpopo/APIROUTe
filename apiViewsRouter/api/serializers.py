from rest_framework import serializers
from .models import Pet,Zakaz


class Petserializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class Zakazserializer(serializers.ModelSerializer):
    class Meta:
        model = Zakaz
        fields = '__all__'
