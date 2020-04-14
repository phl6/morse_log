"Defines URL patterns for morse_logs"

from django.urls import path, include
from django.conf.urls import url
from . import views
from morse_logs import views



app_name = 'morse_logs'

urlpatterns = [
    #The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
    # Home Page
    path(r'', views.index, name='index'),
    # Page that shows all topics
    path(r'topics/', views.topics, name='topics'),
    path(r'cipher/', views.cipher, name='cipher'),
    path(r'decipher/', views.decipher, name='decipher'),
    path(r'tutorialIndex/', views.tutorialIndex, name='tutorialIndex'),
    path(r'gameDirectory/', views.gameDirectory, name='gameDirectory'),
    path(r'game1/', views.game1, name='game1'),

]
