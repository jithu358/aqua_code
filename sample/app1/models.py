from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=40)
    email= models.CharField(max_length=40)
    phone=models.IntegerField()
    address = models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class drivers(models.Model):
    name = models.CharField(max_length=40)
    email= models.CharField(max_length=40)
    phone=models.IntegerField()
    images = models.FileField()
    username=models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    action = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class collab(models.Model):
    usernames = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    status = models.IntegerField()

    def __str__(self):
        return self.usernames

class shop(models.Model):
    pname = models.CharField(max_length=40)
    price = models.IntegerField()
    product = models.FileField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.pname


class cart(models.Model):
    usernames = models.CharField(max_length=40)
    pname = models.CharField(max_length=40)
    price = models.IntegerField()
    quantity = models.IntegerField()
    product = models.FileField()

    def __str__(self):
        return self.pname

class orders(models.Model):
    name=models.CharField(max_length=40)
    usernameu = models.CharField(max_length=40)
    totalamount = models.IntegerField()
    address= models.CharField(max_length=40)
    uphone= models.IntegerField()
    status = models.CharField(max_length=40)
    dusername = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class payments(models.Model):
    usernameu = models.CharField(max_length=40)
    totalamount = models.IntegerField()
    dusername = models.CharField(max_length=40)

    def __str__(self):
        return self.dusername

#contact
class contact(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField()
     contact_no = models.IntegerField()
     message = models.CharField(max_length=50)
     def __str__(self):
         return self.name


#complaint
class complaint(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    complaint = models.CharField(max_length=50)
    def __str__(self):
        return self.name






