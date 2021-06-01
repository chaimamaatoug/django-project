from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def login(request):
    if request.session.has_key('gest'):
        return redirect('home')
    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.filter(email = email,password = password).first()
            if user:
                request.session['gest'] = user.id
                return redirect('home')
            else:
                msg = "email or password invalide"
                return render(request,'login.html',{"msg":msg})
        else:
            return render(request,'login.html',{})

def home(request):
    if request.session.has_key('gest'):
        user = User.objects.filter(id = request.session['gest']).first()
        
        return render(request,'home.html',{'user':user})
    else:
        return redirect('login')

def viewproject(request,id):
    if request.session.has_key('gest'):
        project = Project.objects.filter(id = id).first()
        return render(request,'viewproject.html',{'proj':project,'id':id})

def deleteproject(request,id):
    if request.session.has_key('gest'):
        project = Project.objects.filter(id = id).first()
        project.delete()
        return redirect('home')

def addproject(request):
    if request.session.has_key('gest'):
        user = User.objects.filter(id = request.session['gest']).first()
        if request.method == "POST":
            p = Project()
            p.name = request.POST['name']
            p.descrp = request.POST['descrp']
            p.save()
            user.project.add(p)
            return redirect('home')
        else:
            form = ProjectForm()
            return render(request,'addproject.html',{"form":form})
    else:
        return redirect('login')

def addTask(request,id):
    if request.session.has_key('gest'): #verify if there is a session or not which mean there is a client connected or not
        p = Project.objects.filter(id = id).first() #get project data
        if request.method == 'POST':
            task = Task()
            task.name = request.POST['name']
            task.descr =request.POST['descr']
            task.save()

            p.tasks.add(task)
            return redirect('home')
        else:
            form = TaskForm()
            return render(request,'addtask.html',{'form':form})

    else:
        return redirect('login')

def deleteTask(request,id):
    if request.session.has_key('gest'):
        task = Task.objects.filter(id = id).first() 
        task.delete() #delete task from models
        return redirect('home')

def cpmlte(request,id):
    if request.session.has_key('gest'):
        task = Task.objects.filter(id = id).first()
        task.cmplte = True
        task.save(update_fields=['cmplte']) #update model
        return redirect('home')
    else:
        return redirect('login')

def editeproject(request,id):
    if request.session.has_key('gest'):
        p = Project.objects.filter(id = id).first() #get project data from model with the id
        if request.method == 'POST':
            p.name = request.POST['name'] #change the fields with the new values from formulaire
            p.descrp = request.POST['descrp']
            p.save(update_fields=['name','descrp'])
            return redirect('home')
        else:
            return render(request,'editproject.html',{'proj': p}) #render the html page with a dict have values to edit
    else:
        return redirect('login')

def edittask(request,id):
    if request.session.has_key('gest'):
        task = Task.objects.filter(id = id).first() #get project data from model with the id
        if request.method == 'POST':
            task.name = request.POST['name'] #change the fields with the new values from formulaire
            task.descr = request.POST['descr']
            task.save(update_fields=['name','descr'])
            return redirect('home')
        else:
            return render(request,'edittask.html',{'proj': task}) #render the html page with a dict have values to edit
    else:
        return redirect('login')

def logout(request):
    if not request.session.has_key('gest'):
        return redirect('login')
    try:
        del request.session['gest'] #delete the session gest
        return redirect('login')
    except:
        pass 

def signup(request):
    if request.method == "POST":
        user = User()
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save() # inser into user('email','password)
        request.session['gest'] = user.id #set up new session
        return redirect('home')
    else:
        return render(request,'inscri.html',{})