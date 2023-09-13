from django.urls import path
from .views import PersonCreate, PersonRUD

app_name = 'api'

urlpatterns = [
    path('api/', PersonCreate.as_view(), name='create'),
    path('api/<str:identifier>/', PersonRUD.as_view(), name='detail'),
]
