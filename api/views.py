from django.shortcuts import render
<<<<<<< HEAD
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.models import Posts
from api.serializeer import PostSerializer,UserSerializer
from rest_framework import authentication,permissions



# Create your views here.

class PostView(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
=======
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models import Posts
from api.serializer import PostSerializer,UserSerializer
from rest_framework import authentication,permissions

# Create your views here.

class PostsView(ViewSet):
    authentication_classes =[authentication.TokenAuthentication]
>>>>>>> 21a118e6ed0caa28520a683f6e8b2e4c24bfd597
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Posts.objects.all()
        serializer=PostSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        serializer=PostSerializer(qs)
        return Response(data=serializer.data)
<<<<<<< HEAD

    def destroy(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        serializer=PostSerializer(instance=qs,data=request.data)
=======
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=Posts.objects.get(id=id)
        serializer=PostSerializer(instance=instance,data=request.data)
>>>>>>> 21a118e6ed0caa28520a683f6e8b2e4c24bfd597
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
<<<<<<< HEAD
class LoginView(ViewSet):
=======
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Posts.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})
class UserView(ViewSet):
>>>>>>> 21a118e6ed0caa28520a683f6e8b2e4c24bfd597
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
<<<<<<< HEAD
            return Response(data=serializer.errors)
class PostmodelView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
=======
            return Response(data=serializer.errors)
>>>>>>> 21a118e6ed0caa28520a683f6e8b2e4c24bfd597
