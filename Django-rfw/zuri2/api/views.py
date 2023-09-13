from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from .models import Person
from rest_framework.response import Response
from .serializers import PersonSerializer


class PersonCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = 'name'  # Specify 'name' as the lookup field

    def get_queryset(self):
        return Person.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        identifier = self.kwargs.get('identifier')

        # Determine whether 'identifier' is a name or a user_id
        if identifier.isdigit():
            return queryset.get(id=identifier)
        else:
            return queryset.get(name=identifier)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Person deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
