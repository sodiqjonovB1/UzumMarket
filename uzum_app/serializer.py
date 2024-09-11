from rest_framework import serializers
from .models import User, Category, Product, ProductImages


class ChangepasswordSerializer(serializers.Serializer):
	old_password = serializers.CharField(max_lenth = 15)
	new_password = serializers.CharField(max_lenth = 15)
	confirm_password = serializers.CharField(max_lenth = 15)

class UserSerial(serializers.Serializer):
	class Meta :
		model = User
		field = ['id','username','password','photo' ]
		extra_kwargs = {'password':{'write_only': True}}
	def create(self,validated_data):
		password = validated_data.pop('password')
		user = User.objects.create(**validated_data)
		user.set_password(password)
		user.save()
		return user



class User_Detail(serializers.ModelSerializer):
	class Meta:
		model = User
		field = ['']


class Change_Password_Serial(serializers.Serializer):
	old_password = serializers.CharField(max_lenth = 15)
	new_password = serializers.CharField(max_lenth = 15)
	confirm_password = serializers.CharField(max_lenth= 15)


class ProductSerial(serializers.Serializer):
	class Meta :
		model = Product
		field = ['id','name','batafsil','price','rasm']
	def create(self,validated_data):
		product = Product.objects.create(**validated_data)
		return product


class CategorySerial(serializers.Serializer):
	class Meta :
		model = Category
		field = ['id','name','rasm','parent']