from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate(self, data):
        name = data.get('name')
        
        if not name.replace(" ", "").isalpha():
            raise serializers.ValidationError("Name should only contain alphabetical characters (letters) and spaces.")
        
        return data
