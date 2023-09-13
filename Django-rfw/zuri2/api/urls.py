from django.urls import path
# from .views import PersonCreate, PersonRUD



from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('api', views.PersonCreate.as_view(), name='create'),  
    path('api/<str:identifier>', views.PersonRUD.as_view(), name='detail')
]