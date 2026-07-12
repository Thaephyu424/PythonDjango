from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here
def about(request):
    return render(request,'about.html')


def home(request):
    title = "My Blog Title"
    cat_data = Category.objects.all()
    name=Student.objects.all()
    contex = {
        'abc':title,
        'name':'Mg Mg',
        'datas':cat_data,
        'name':name
    }
    return render(request,'home.html',contex)

# def createBlog(request):
#     return render(request,'createBlog.html')

# def saveBlog(request):
#     # SAVE DATA TO CATEGORY table
#     # catch the data form the form
#     cate = request.POST.get('category')
#     # Push the data to the model
#     Category.objects.create(category_name=cate)
   
#     # return render(request,'createBlog.html')
#     # //redirect to home page
#     return redirect('/home')
# # retun redirect({% urls home%})//redirectToHomePageInURLSName

def createBlog(request):
    if request.method =='POST':
        cate = request.POST.get('category')
        Category.objects.create(category_name=cate)
        return redirect('/home')
    return render(request,'createBlog.html')

def saveBlog(request):
    # SAVE DATA TO CATEGORY table
    # catch the data form the form
    cate = request.POST.get('category')
    # Push the data to the model
    Category.objects.create(category_name=cate)
   
    # return render(request,'createBlog.html')
    # //redirect to home page
    return redirect('/home')
# retun redirect({% urls home%})//redirectToHomePageInURLSName

def createStudent(request):
    return render(request,'createStudent.html')

def saveStudent(request):
    stuName = request.POST.get('name')
    Student.objects.create(stu_name=stuName)
    # return render(request,'createStudent.html')
    return redirect('/home')

