from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import pre_save,post_save

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length = 30)
    tel   = models.CharField(max_length = 30)
    image = models.ImageField(null= True , blank = True)

    def __str__(self):
        return self.user.username



#start signals

def create_profil(sender,instance,created,**kwargs):
    print("create ******************************")
    print("sender",sender)
    print("insatnce",instance)
    print("created",created)
    if created:
        profile.objects.create(user = insatnce)
        print('profile was created')
    print("after ******************************")
    return

def update_profil(sender,instance,**kwargs):
        print("update ******************************")
        print("sender",sender)
        print("insatnce",instance)
        print('before')
        print("******************************")

        return
post_save.connect(create_profil,sender = User)#weche class models i will lesining
pre_save.connect(update_profil,sender = User)#weche class models i will lesining

#pre_save.connect(update_profil,sender = User)#weche class models i will lesining

#end signals

