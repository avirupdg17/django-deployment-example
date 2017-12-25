from django.shortcuts import render
from . import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'ProTwo/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('you are logged in!!')



def other(request):
    return render(request,'ProTwo/other.html')

def relative(request):
    return render(request,'ProTwo/relative_url_template.html')


def base(request):
    return render(request,'ProTwo/base.html')


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:

            print(user_form.errors, profile_form.errors)

    else:

        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request,'ProTwo/registration.html',{'user_form': user_form, 'profile_form':profile_form, 'registered':registered})




def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))

            else:
                return HttpResponse('Account not active')
        else:
            print("Login failed")
            print(username)
            print(password)
            return HttpResponse('Invalid login details')
    else:
        return render(request, 'ProTwo/login.html', {})
# def newUser(request):
#     #users_list = User.objects.all()
#     #users_dict = {'user_record':users_list}
#     form = forms.NewUserForm()
#
#     if(request.method == 'POST'):
#         form = forms.NewUserForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#
#
#     return render(request, 'ProTwo/users.html',{'form':form})






