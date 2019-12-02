from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


def index_view(request, *args, **kwargs):
        return render(request, 'index.html')