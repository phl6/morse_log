from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse

from users.models import userScore
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
                       '?': '..--..', '-': '-....-'
                       }

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
                       '?': '..--..', '-': '-....-'
                       }
    # https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
    MORSE_CODE_DICT_REV = {v: k for k, v in MORSE_CODE_DICT.items()}

    def decrypt(message):
        # extra space added at the end to access the last morse code
        message += ' '
        decipherMsg = ''
        citext = ''
        space = 0
        for letter in message:
            # checks for space
            if letter != ' ':
                # keep track of space
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
    if request.user and not request.user.is_anonymous:
        user = request.user

    user_score, created = userScore.objects.get_or_create(user=user)
    cScore = user_score

    return render(request, 'morse_logs/gameDirectory.html', {'currentS': cScore})

@login_required()
def correct(request):
    """The answer correct page"""
    return render(request, 'morse_logs/correct.html')

@login_required()
def incorrect(request):
    """The answer incorrect page"""
    return render(request, 'morse_logs/incorrect.html')

@login_required()
def game1(request):
    if request.method == "GET":
        return render(request, 'morse_logs/game1.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == '..-.':
            # user's score declared in model increase 5points
            # display correct and 5 points added to user
            user_score.score += 5
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game2(request):
    """The Game2 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game2.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == 'X' or ans2 == 'x':
            # user's score declared in model increase 5points
            # display correct and 5 points added to user
            user_score.score += 5
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))


@login_required()
def game3(request):
    """The Game3 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game3.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == 'u' or ans2 == 'U':
            # user's score declared in model increase 5points
            # display correct and 5 points added to user
            user_score.score += 5
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game4(request):
    """The Game4 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game4.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == '.... . -.--':
            # user's score declared in model increase 5points
            # display correct and 10 points added to user
            user_score.score += 10
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game5(request):
    """The Game5 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game5.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == 'help' or ans2 == 'HELP' or ans2 == 'Help':
            # user's score declared in model increase 5points
            # display correct and 10 points added to user
            user_score.score += 10
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game6(request):
    """The Game6 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game6.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == 'sos' or ans2 == 'SOS':
            # user's score declared in model increase 5points
            # display correct and 10 points added to user
            user_score.score += 10
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game7(request):
    """The Game7 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game7.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == '-- ---..':
            # user's score declared in model increase 5points
            # display correct and 15 points added to user
            user_score.score += 15
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game8(request):
    """The Game8 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game8.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == 'I LOVE YOU' or ans2 == 'i love you' or ans2 == 'I Love You':
            # user's score declared in model increase 5points
            # display correct and 15 points added to user
            user_score.score += 15
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def game9(request):
    """The Game9 page"""
    if request.method == "GET":
        return render(request, 'morse_logs/game9.html')
    elif request.method == "POST":
        if request.user and not request.user.is_anonymous:
            user = request.user

        user_score, created = userScore.objects.get_or_create(user=user)

        ans2 = request.POST.get('ans2', '') #fetch the POST data from template
        if ans2 == '':
            ans2 = 0

        if ans2 == 'I LOVE YOU' or ans2 == 'i love you' or ans2 == 'I Love You':
            # user's score declared in model increase 5points
            # display correct and 15 points added to user
            user_score.score += 15
            user_score.save()
            return redirect(reverse('morse_logs:correct'))
        else:
            # user's score declared in model has no point
            # display incorrect and 0 point added to user
            return redirect(reverse('morse_logs:incorrect'))

@login_required()
def leaderboard(request):
    """The Leaderboard page"""
    #retrieve the objects with top 5 highest score in descending order
    scores = userScore.objects.order_by('score').reverse()[:5]

    args = {'topFiveUserScores': scores}

    return render(request, 'morse_logs/leaderboard.html', args)
