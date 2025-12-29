from django.shortcuts import render, redirect
from .models import Applicant, Cycle, TreatmentFacility, ProcessingCenter, Purpose
from .forms import RegistrationForm, CycleForm, MtfForm, PcForm, SignUpForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your views here.

#Login_User
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request,("There was an error, please try again"))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

#Logout_User
def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out!"))
    return redirect('login_user')

#Register_User
def register_user(request):
    form = SignUpForm()
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("You have registered successfully!"))
            return redirect('home')
        else:
            messages.success(request,("There was a problem registering, please try again!"))
            return redirect('register_user')
    return render(request, 'register.html',{'form':form})

#Registration
def updateRegistration(request, updateReg_id):
    reg = Applicant.objects.get(pk=updateReg_id)
    form = RegistrationForm(request.POST or None, instance=reg)
    if form.is_valid():
        form.save()
        messages.success(request,('Updated Successfully!'))
        return redirect('home')
    return render(request,'updateReg.html',{'reg':reg,'form':form})

def deleteRegistration(request, delReg_id):
    delReg = Applicant.objects.get(pk=delReg_id)
    delReg.delete()
    return redirect('home')

def registration(request):
    submitted = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('New Entry Submitted Successfully!'))
            return redirect('home')
            #return HttpResponseRedirect('/registration?submitted=True')
    else:
        form = RegistrationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'registration.html',{'form':form, 'submmitted':submitted})


def home(request):
    #applicant = Applicant.objects.all()
    if request.user.is_superuser:
        applicant = Applicant.objects.all()
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "ABAB":
        applicant = Applicant.objects.filter(pc__pcName='ABAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "BAB":
        applicant = Applicant.objects.filter(pc__pcName='BAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "BGBNEAB":
        applicant = Applicant.objects.filter(pc__pcName='BGBNEAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "CAB":
        applicant = Applicant.objects.filter(pc__pcName='CAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "CJVAB":
        applicant = Applicant.objects.filter(pc__pcName='CJVAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "EAAB":
        applicant = Applicant.objects.filter(pc__pcName='EAAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    if request.user.username == "FAB":
        applicant = Applicant.objects.filter(pc__pcName='FAB')
        context = {'applicant':applicant}
        return render(request, 'home.html', context)
    
    else:
        return render(request, 'homepage.html', {})

    


def about(request):
    return render(request, 'about.html',{})

#Recruitment Cycle
def cycle(request):
    cycle = Cycle.objects.all()
    return render(request, "cycle.html", {"cycle": cycle})

def createCycle(request):
    submitted = False
    if request.method == 'POST':
        form = CycleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('New Entry Submitted Successfully!'))
            return redirect('cycle')
            #return HttpResponseRedirect('/createCycle?submitted=True')
    else:
        form = CycleForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'createCycle.html',{'form':form, 'submmitted':submitted})

def deleteCycle(request, cycle_id):
    cycle = Cycle.objects.get(pk=cycle_id)
    cycle.delete()
    return redirect('cycle')

#Military Treatment Facility
def mtf(request):
    mtf = TreatmentFacility.objects.all()
    return render(request, 'mtf.html',{"mtf":mtf})

def createMtf(request):
    if request.method == "POST":
        form = MtfForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('New Entry Submitted Successfully!'))
        return redirect('mtf')
    else:
        return render(request, 'createMtf.html',{})

def deleteMtf(request, mtf_id):
    mtf = TreatmentFacility.objects.get(pk=mtf_id)
    mtf.delete()
    return redirect('mtf')

def updateMtf(request, mtf_id):
    mtf = TreatmentFacility.objects.get(pk=mtf_id)
    form = MtfForm(request.POST or None, instance=mtf)
    if form.is_valid():
        form.save()
        messages.success(request,('Updated Successfully!'))
        return redirect('mtf')
    return render(request,'updateMtf.html',{'mtf':mtf,'form':form})

#Processing Center
def pc(request):
    pc = ProcessingCenter.objects.all()
    return render(request, 'pc.html',{'pc':pc})

def createPc(request):
    if request.method == "POST":
        form = PcForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('New Entry Submitted Successfully!'))
        return redirect('pc')
    else:
        return render(request, 'createPc.html',{})

def deletePc(request, pc_id):
    pc = ProcessingCenter.objects.get(pk=pc_id)
    pc.delete()
    return redirect('pc')

def updatePc(request, pc_id):
    pc = ProcessingCenter.objects.get(pk=pc_id)
    form = PcForm(request.POST or None, instance=pc)
    if form.is_valid():
        form.save()
        messages.success(request,('Updated Successfully!'))
        return redirect('pc')
    return render(request,'updatePc.html',{'pc':pc,'form':form})
    
#Purpose
def purpose(request):
    purpose = Purpose.objects.all()
    return render(request, 'purpose.html',{'purpose':purpose})






