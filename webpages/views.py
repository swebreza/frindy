from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
 return render(request,'webpages/welcome.html')

def messages(request):
 return render(request,'webpages/messages.html')

def profile(request):
 return render(request,'webpages/profile.html')

def post(request):
 return render(request,'webpages/post.html')

def resume(request):
 return render(request,'webpages/resume/resume1.html')

def resume2(request):
 return render(request,'webpages/resume/resume2.html')