from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login


def user_credential(request):
    if request.session.has_key('is_logged'):
        user = User.objects.get(username=request.session['username'])
        userProfile = UserProfile.objects.get(
            user=User.objects.get(username=user))
        firstName = user.first_name
        lastName = user.last_name
        profileImage = userProfile.profile_image
        user_context = {
            'user':   user,
            'userProfile':   userProfile,
            'firstName':   firstName,
            'lastName':   lastName,
            'profileImage':   profileImage
        }
        return user_context
    return {}


def home(request):
    if request.method == 'GET':  # http://127.0.0.1:8000/
        chellenge_list = Chellenge.objects.all()
        context = {
            'chellenge_list':   chellenge_list,
        }
        if request.GET:  # http://127.0.0.1:8000/?chellenge_id=1
            chellenge_id = request.GET['chellenge_id']
            selected_chellenge = Chellenge.objects.get(id=chellenge_id)
            topic_list = TopicList.objects.filter(Chellenge_id=chellenge_id)
            comment_list = Comment.objects.filter(chellenge_id=chellenge_id)
            context = {
                'chellenge_list':   chellenge_list,
                'selected_chellenge':   selected_chellenge,
                'topic_list':   topic_list,
                'comment_list':   comment_list,
                'is_logged':   request.session.has_key('is_logged')
            }
            context.update(user_credential(request))
            return render(request, 'index.html', context=context)
        context.update(user_credential(request))
        return render(request, 'index.html', context=context)
    # Execute this block when user is have just login
    chellenge_list = Chellenge.objects.all()
    context = {'chellenge_list': chellenge_list}
    context.update(user_credential(request))
    return render(request, 'index.html', context=context)


def signin(request):
    if request.method == 'GET':
        if request.session.has_key('is_logged'):
            return home(request)
        else:
            return render(request, 'signin.html', context={})
    else:
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            print(user)
            user.last_login = datetime.today()
            user.save()
            request.session['is_logged'] = True
            request.session['username'] = username
            login(request, user)
            print("Signin successfull and is_logged value is : {}".format(
                request.session.has_key('is_logged')))
            return home(request)
        else:
            context = {"is_SigninFailed": "Sign in failed."}
            return render(request, 'signIn.html', context={})


def signout(request):
    logout(request)
    return home(request)


# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'userAdmin/signup.html', context={})
#     else:
#         FirstName = request.POST['FirstName']
#         LastName = request.POST['LastName']
#         PhoneNumber = request.POST['PhoneNumber']
#         Mail = request.POST['Mail']
#         Password = request.POST['Password']
#         ConfirmPassword = request.POST['ConfirmPassword']
#         UserName = Mail.split('@')[0]
#         u = User(username=UserName, first_name=FirstName,
#                  last_name=LastName, email=Mail)  # Django user model
#         u.save()
#         u.set_password(Password)
#         u.save()
#         e_u = ExtendUser(user=u, phone=PhoneNumber,
#                          dob=datetime.now(),  usr_ip='10.128.100.100')
#         e_u.save()
#         return render(request, 'userAdmin/signin.html', context={})
