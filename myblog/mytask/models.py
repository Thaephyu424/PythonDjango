from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

# return in sting
    def __str__(self):
        return self.category_name

class Student(models.Model):
    stu_name = models.CharField(max_length=50)

    # return in sting
    def __str__(self):
        return self.stu_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    
   # return in sting
    def __str__(self):
        return self.teacher_name

class MyBlog(models.Model):
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    post_blog = models.TextField()
    created_date = models.DateField()

    def __str__(self):
        return self.title



