"Defines URL patterns for morse_logs"

from django.urls import path, include
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
    path(r'correct/', views.correct, name='correct'),
    path(r'incorrect/', views.incorrect, name='incorrect'),
    path(r'game1/', views.game1, name='game1'),
    path(r'game2/', views.game2, name='game2'),
    path(r'game3/', views.game3, name='game3'),
    path(r'game4/', views.game4, name='game4'),
    path(r'game5/', views.game5, name='game5'),
    path(r'game6/', views.game6, name='game6'),
    path(r'game7/', views.game7, name='game7'),
    path(r'game8/', views.game8, name='game8'),
    path(r'game9/', views.game9, name='game9'),
    path(r'leaderboard/', views.leaderboard, name='leaderboard'),
]
