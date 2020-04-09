from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from users.models import UserScore
from .models import Topic
from django.contrib.auth.decorators import login_required


# Create your views here.
# Business logic here
@login_required()
def index(request):
    """The home page for Morse Code Education app"""
    return render(request, 'morse_logs/index.html')

@login_required()
def topics(request):
    """The topics page"""
    """topics = Topic.objects.order_by('date_added')"""
    context = {'topics': topics}
    return render(request, 'morse_logs/topics.html', context)

@login_required()
def cipher(request):
    """The Cipher page"""
    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',

                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

    def encrypt(message):
        cipher = ''
        message = message.upper()
        for letter in message:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                cipher += ' '
        return cipher

    val1 = request.GET.get('a1', '')
    res = encrypt(val1)

    return render(request, 'morse_logs/cipher.html', {'result': res})

@login_required()
def decipher(request):
    """The Decipher Page"""
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',

                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    # https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
    MORSE_CODE_DICT_REV = {v: k for k, v in MORSE_CODE_DICT.items()}

    def decrypt(message):
        # extra space added at the end to access the
        # last morse code
        message += ' '
        decipherMsg = ''
        citext = ''
        space = 0
        for letter in message:
            # checks for space
            if letter != ' ':
                # counter to keep track of space
                space = 0
                # storing morse code of a single character
                citext += letter
                # in case of space
            else:
                # if i = 1 that indicates a new character
                space += 1
                # if i = 2 that indicates a new word
                if space == 2:
                    # adding space to separate words
                    decipherMsg += ' '
                elif citext != '':
                    # accessing the keys using their values (reverse of encryption)
                    decipherMsg += MORSE_CODE_DICT_REV[citext]
                    citext = ''
        return decipherMsg

    val1 = request.GET.get('a1', '')
    res = decrypt(val1)

    return render(request, 'morse_logs/decipher.html', {'result': res})

@login_required()
def tutorialIndex(request):
    """The tutorial index page"""
    return render(request, 'morse_logs/tutorialIndex.html')

@login_required()
def gameDirectory(request):
    """The Game Directory page"""
    return render(request, 'morse_logs/gameDirectory.html')

@login_required()
def game1(request):

    if request.user and not request.user.is_anonymous:
        user = request.user
    #else:
        #throw exception

    """The Game 1 page"""
    val1 = request.GET.get('ans1', '')
    res = "Incorrect"

    user_score = UserScore.objects.get_or_create(user=user)

    if val1 == 2:
        #user's score declared in model increase 5 points
        #display correct and 5 points added to user
        res = "Correct"
        user_score.score = int(user_score.score) + 5
        user_score.save()
    else:
        #user's score declared in model has no point
        #display incorrect and 0 point added to user
        res = "Incorrect"

    return render(request, 'morse_logs/game1.html', {'result': res})

