from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.
def home(request):
    blogDatas = Blog.objects.all()
    contex= {
        'blogDatas' : blogDatas
    }
    return render(request,'home.html',contex)

def createForm(request):
    return render(request,'createForm.html')

def saveForm(request):
    albumName = request.POST.get('albumName')
    content = request.POST.get('content')
    Blog.objects.create(title = albumName,post_body=content)
    return redirect('/home')

def detail(request,id):
    blogWithID=Blog.objects.get(id =id)
   
    contex = {
        'blogWithID' : blogWithID 
    }
    return render(request,'detail.html',contex)

def edit(request,id):
     blogWithID=Blog.objects.get(id =id)
     context = {
     'blog' : blogWithID
     }
 
     return render(request,'edit.html',context)

def update(request,id):
    blogWithID=Blog.objects.get(id =id)
    if request.method == 'POST':
       albumName = request.POST.get('albumName')
       content = request.POST.get('content')
       blogs = Blog.objects.filter(id =id)       
       blogs.update(title =albumName,post_body=content)#UpdateThoseDataToDatabase
     
    return redirect('/home')
    context = {
     'blog' : blogWithID
     }
 
    return render(request,'edit.html',context)
   
   




