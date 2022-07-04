
from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import *

from app.models import Student
# Create your views here.
def Signup(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'GET':
        form =UserCreationForm()
        return render(request,'signup.html',context={'form':form})
    if request.method == 'POST':
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/login')
        return render(request,'signup.html',context={'form':form})


class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request,'login.html')
    def post(self,request):
        
        
        try:
            user=User.objects.get(username=request.POST.get('username'))

        except:
            return render(request,'login.html',context={'error':'please enter correct username'})
            
        if user:
            password=request.POST.get('password')
            if not user.check_password(password):
                return render(request,'login.html',context={'error':'please enter correct password'})

            auth.login(request,user)
            return redirect('/signup')

class logout(View):
 def get(self,request):
    if request.user.is_authenticated:
        user=User.objects.get(id=request.user.id)
        auth.logout(request,user)
        return redirect('/login')
    return redirect('/login')

class ProfileEdit(View):
    def get(self,request):
        if request.user.is_authenticated:
            user=Student.objects.get(user=request.user)
            

            return render(request,'form.html',context={'user':user})

        return redirect('login')
    def post(self,request):
        if request.user.is_authenticated:
            print(request.POST.get('last_name'))
            us=User.objects.get(id=request.user.id)
            us.first_name=request.POST.get('first_name')
            us.last_name=request.POST.get('last_name')
            us.save()
            user=Student.objects.get(user=request.user)
            user.mobile_number=request.POST.get('mobile_number')
            user.gender=request.POST.get('gender')
            user.course=request.POST.get('course')
            user.current_address=request.POST.get('address')
            user.save()
            return redirect('mark')
        return redirect('login')

        


class Marks(View):
    def get(self,request):
        if request.user.is_authenticated:
            user=Student.objects.get(user=request.user)
            

            return render(request,'document.html',context={'user':user})

        return redirect('login')
    def post(self,request):
        if request.user.is_authenticated:
            user=Student.objects.get(user=request.user)
            user.marks_te=request.POST.get('ClassX_Board')
            user.percentage_te=request.POST.get('ClassX_Percentage')
            user.passing_year_te=request.POST.get('ClassX_YrOfPassing')

            user.marks_tw=request.POST.get('ClassXII_Board')
            user.percentage_tw=request.POST.get('ClassXII_Percentage')
            user.passing_year_tw=request.POST.get('ClassXII_YrOfPassing')

            user.marks_ug=request.POST.get('Graduation_Board')
            user.percentage_ug=request.POST.get('Graduation_Percentage')
            user.passing_year_ug=request.POST.get('Graduation_YrOfPassing')

            user.marks_m=request.POST.get('Masters_Board')
            user.percentage_m=request.POST.get('Masters_Percentage')
            user.passing_year_m=request.POST.get('Masters_YrOfPassing')
            user.save()
            return redirect('document')
        return redirect('login')



class document(View):
    def get(self,request):
        if request.user.is_authenticated:
            user=Student.objects.get(user=request.user)
            return render(request,'documents.html',context={'user':user})

        return redirect('login')
    def post(self,request):
        if request.user.is_authenticated:
            print(request.FILES.get('x'))
            user=Student.objects.get(user=request.user)
            user.marksheet_te=request.FILES.get('x')
            user.marksheet_tw=request.FILES.get('xii')
            user.marksheet_ug=request.FILES.get('ug')
            user.marksheet_m=request.FILES.get('m')
           
            user.save()
            return render(request,'documents.html',context={'message':"add successfully"})
        return redirect('login')





        