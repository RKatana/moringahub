from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

CHOICES = [(i,i) for i in range(11)]#



class Student(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,related_name='students')
    profile_pic=models.ImageField('profile photo',upload_to='images/',blank=True)
    bio=models.CharField(max_length=250)
    s_class=models.CharField('class',max_length=60)

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            student=Student.objects.create(name=kwargs['instance'])
    post_save.connect(create_profile,sender=User)

    def __str__(self):
        return self.name.username

    @classmethod
    def search_by_class(cls,s_class):
        return cls.objects.filter(s_class__iexact=s_class)

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField('project description')
    student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='projects')
    link= models.URLField("website's link")
    date=models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_class(cls,s_class):
        return cls.objects.filter(student__s_class__iexact=s_class)
    # project =Projects.objects.filter(student__s_class=s_class)
    

    def __str__(self):
        return self.title

    def search_title(self,title):
        return self.objects.filter(title__icontains=title)

class Ideas(models.Model):
    student=models.ForeignKey(Student)
    title=models.CharField(max_length=100)
    raw_idea=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

class Comments(models.Model):

    project=models.ForeignKey(Projects,on_delete=models.CASCADE,related_name='comments')
    title=models.CharField(max_length=60)
    comment=models.TextField()
    rating=models.PositiveIntegerField('general rating/10', choices=CHOICES)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
