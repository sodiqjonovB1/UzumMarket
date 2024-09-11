from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import *
from .models import *







class CategoryCreateListView(ListCreateAPIView):
	queryset = Category.objects,all()
	serializer_class = CategorySerializer



class CategoryDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	lookup_field = id



	def delete(self,request,*args,**kwargs):
		Category.objects.all()
		return Response("deleted")

class ProductCreateList(APIView):
	def get(self,request):
		books = Product.objects.all()
		serializer = ProductSerializer(books,many = True)
		return Response(serializer.data)

	def post(self,request):
		serializer = ProductSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			return Response(
				serializer.data)

		return Response(serializer.errors)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_field = 'id'
	def delete(self,request,id):
		Product.objects.get(id=id)
		return Response("deleted")


class Change_Password_Function(APIView):
	def post(self,request):
	serializer = Change_Password_Serializer(request.data)
	if serializer.is_valid():
		old_password = request.data['old_password']
		if request.user.chack_password(old_password):
			if request.data['new_password']==request.data['confirm_password']:
				request.user.set_password(request.data['new_password'])
				request.user.save()
				return Response	(
				{'message':"Your Password Changes SuccessFully !"}
				)
			return Response({
					'message':"NOt Matched !"
					})
		return Response({
			'message': "Your Old Password is Incorrect !"
			})
	return Response({
		'message':'Please fill out the blanks !'
		})




















