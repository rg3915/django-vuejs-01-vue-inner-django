from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'index.html', context)


def api_users(request):
    users = User.objects.all()
    data = [
        {'username': user.username}
        for user in users
    ]
    response = {'data': data}
    return JsonResponse(response)
