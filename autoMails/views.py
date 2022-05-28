import django
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import is_valid_path

def index(request):
    return render(request, 'oneclick.html')

def index2(request):
    return render(request, 'index.html')

def MultiTime(request):
   if request.method == 'POST':
        value = [request.POST['email'] ]
        for i in range(int(request.POST['no'])):
            for n in value:
                send_mail(
                request.POST['subject'],
                request.POST['message'],
                'jinusaini9@gmail.com',
                [n],
                fail_silently=False
                )
                response = {'response' : 'Done'}
        return JsonResponse(response)



def MultiSender(request):
   if request.method == 'POST':
        var = list(request.POST['emails'].split(','))
        for n in var:
            send_mail(
            request.POST['subject'],
            request.POST['message'],
            'jinusaini9@gmail.com',
            [n],
            fail_silently=False
            )
            response = {'response' : n}
        return JsonResponse(response)

def open(request):
    return render(request, 'login.html')

def signUp(request):
    data = {
        'user' : request.POST['user'],
        'email' : request.POST['email'],
        'pswd' : request.POST['pswd'],
        'token' : request.POST['csrfmiddlewaretoken']
    }
    return JsonResponse(data)

def signIn(request):
    data = {
        'email' : request.POST['email'],
        'pswd' : request.POST['pswd'],
        'token' : request.POST['csrfmiddlewaretoken']
    }
    return JsonResponse(data)