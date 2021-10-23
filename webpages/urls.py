from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('post', views.post,name="post"),
    path('message', views.messages,name="message"),
    path('profile', views.profile,name="profile"),
    path('resume', views.resume,name="resume"),
    path('resume2', views.resume2,name="resume2"),
]