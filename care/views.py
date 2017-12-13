from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Image, Comment, VoteModel
from .forms import UploadForm, UserProfileForm, CommentForm

def home(request):

    title = 'Patient Care'
    return render(request, 'home.html', {"title":title})