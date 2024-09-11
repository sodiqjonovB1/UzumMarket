from django.db import models
from django.contrib.auth import AbstractUser
from mptt.models import MPTTModel, ThreeForeignKey
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	STATUS = (
		('admin', 'Admin'),(
			'user','User'))
	phone_number=  models.CharField(max_length=14)
	photo=models.ImageField(upload_to='users/', default='user.png')
	status = models.CharField(max_length=40, choices=STATUS, default='user')
	def __str__(self):
		return f'{self.first_name/{self.status}}'




class Category(MPTTModel):
	name=  models.CharField(max_length=15)
	rasm=  models.ImageField(upload_to='category/')
	parent=ThreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.name



class Product(models.Model):
	name=models.CharField(max_length=99)
	batafsil=models.TextField()
	updated=models.DateTimeField(auto_now=True)
	price=models.CharField(max_length=52)
	rasm = models.ImageField(upload_to='product_images/')
	user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	views= models.PositiveBigIntegerField(default=0)



class ProductImages(models.Model):
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	image = models.ImageField(upload_to = 'product_images/', null = True,blank= True)



































