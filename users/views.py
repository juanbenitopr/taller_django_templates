from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from django.views import View


class UserView(View):

    def get(self, request: WSGIRequest):
        return render(request, 'user_list.html', context={'users': User.objects.all()})


class UserDetailView(View):

    def get(self, request: WSGIRequest, id: int):
        return render(request, 'user_detail.html', context={'users': User.objects.get(pk=id)})
