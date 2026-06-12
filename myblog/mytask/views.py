from django.shortcuts import render,HttpResponse

# Create your views here
def about(request):
    return render(request,'about.html')


def home(request):
    title = "My Blog Title"
    return render(request,'home.html',{'title':title})

