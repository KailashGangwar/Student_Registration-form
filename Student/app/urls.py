from xml.dom.minidom import Document
from django.urls import path
from .views import *
urlspattern=[
    # path('signup/',Signup)
]
urlpatterns = [
    path('signup',Signup,name='signup'),
    path('login',Login.as_view(),name='login'),
    path('profile',ProfileEdit.as_view(),name='profile'),
    path('mark',Marks.as_view(),name='mark'),
    path('document',document.as_view(),name='document'),
    path('logout',logout.as_view(),name='logout')
]
