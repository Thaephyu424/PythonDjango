from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here
def about(request):
    return render(request,'about.html')


def home(request):
    title = "My Blog Title"
    cat_data = Category.objects.all()
    blogs = MyBlog.objects.all()
    contex = {
        'abc':title,
        'name':'Mg Mg',
        'datas':cat_data,
        'blogs':blogs
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

def filterblog(request):
    cid = request.GET.get('cid')
    cat_obj = Category.objects.get(id=cid) 
    filter_data = MyBlog.objects.filter(category=cat_obj) #selectFromMyBlogDatabase
    context = {
        'blogs' : filter_data 
    }
    return render(request,'home.html',context)

def detailblog(request,blogid):
    blog = MyBlog.objects.get(id =blogid )
    if request.method == 'POST':
        title = request.POST.get('title') #theseAreDataFromInputOfHTMLFile
        pbody = request.POST.get('post_blog')#theseAreDataFromInputOfHTMLFile
        blogs = MyBlog.objects.filter(id =blogid )
        blogs.update(title=title,post_blog=pbody)#UpdateThoseDataToDatabase
        # blogs.save() #wedon'tNeedToSaveThoseDataInUpdate 
        return redirect('/home')
        
    context = {
        'blog' : blog
    }
 
    return render(request,'detailblog.html',context)






