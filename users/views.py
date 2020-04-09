from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from users.forms import (
    RegistrationForm,
    EditProfileForm
)
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = RegistrationForm()
    else:
        # Process completed form
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page
            login(request, new_user)
            return redirect('morse_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required()
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'users/profile.html', args)


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('.')  # back to the current page: 8000/users/profile
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/edit_profile.html', args)


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('./profile')  # if succesful, back to the current page: 8000/users/profile
        else:
            return redirect('./change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'users/change_password.html', args)

# @login_required()
# def updateScore(request):



#  render the initial form on a page that user can
#  enter an email that associates to their account
#  so that reset pw email can be sent

