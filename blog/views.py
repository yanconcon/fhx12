from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from django.contrib.auth import authenticate,login as auth_login ,logout 
from blog.forms import SignupForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib import auth

# Create your views here.
class LogForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=15)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())


def home(request):
	time = datetime.datetime.now()	
	
	return render(request,'index.html',locals())

def about(request):
	
	return render(request,'about.html',locals())
	
def userli(request):#用于实现函数information的页面
	return render(request,'user.html',locals())
	
user_list = [#建立一个列表用于存放temp
	{"user":"jack","pwd":"abc"},
	{"user":"tom","pwd":"ABC"},
	]

def information(request):#定义用户输入信息的逻辑函数（信息会放入list，并将输入信息展示给输入者）
	if request.method == "POST":
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		temp = {"user":username,"pwd":password}#用user表示username,用pwd表示password
		user_list.append(temp)#把temp放入list中
	return render(request, "user.html",{"data":user_list})#把list放入user.html中的"data"显示给输入者	

def signup(request):
	path=request.get_full_path()
	if request.method=='POST':
		form=SignupForm(data=request.POST,auto_id="%s")
		if form.is_valid():
			UserModel=get_user_model()
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user=UserModel.objects.create_user(username=username,email=email,password=password)
			user.save()
			auth_user = authenticate(username=username,password=password)
			auth_login(request,auth_user)
			return redirect("home")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'signup.html',locals())
	
	
def login(request):
	path=request.get_full_path()
	if request.method == 'POST':
		form = LogForm(data=request.POST,auto_id="%s")
		if form.is_valid():
			UserModel=get_user_model()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
		
			userPassJudge = authenticate(username=username,password=password)
		
			if userPassJudge:
				auth_login(request, userPassJudge)
				form = LogForm(data=request.POST,auto_id="%s")
				return redirect("home")
			else:
				form = LogForm()
				return HttpResponse('Wrong Password!!!')
			
	else:
		form = LogForm()
	return render(request,'login.html',locals())
	
	
def logout_view(request):
	logout(request)
	return redirect('home')

def post(request):
	return render(request,"post.html")
