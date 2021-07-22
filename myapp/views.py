from django.shortcuts import render,get_object_or_404
from .models import Article
from .serializers import ArticleSerializer,UserSerializer
from rest_framework import status,mixins,generics,viewsets
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


#ModelViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    authentication_classes = (TokenAuthentication)

    #ViewSet
'''
class ArticleViewSet(viewsets.ViewSet):
    def list(self,request):
        art=Article.objects.all()
        serializer=ArticleSerializer(art,many=True)
        return Response(serializer.data)


    def create(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk=None):
        queryset=Article.objects.all()
        article=get_object_or_404(queryset,pk=pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article=Article.objects.get(pk=pk)
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article=Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_201_CREATED)

'''

#mixin Generic View Set
'''
class Articless(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
    
class  Article_detail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    lookup_field='id'
    def get(self,request,id):
        return self.retrieve(request,id=id)
    def put(self,request,id):
        return self.update(request,id=id)
    def delete(self,request,id):
        return self.destroy(request,id=id)

'''
#Class Based Views
'''
class Articless(APIView):
    def get(self,request):
        art=Article.objects.all()
        serializer=ArticleSerializer(art,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Article_detail(APIView):
    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        articles=self.get_object(id)
        serializer=ArticleSerializer(articles)
        return Response(serializer.data) 

    def put(self,request,id):
        article=self.get_object(id)
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article=self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_201_CREATED)
'''









#Function Based Views
'''


@api_view(['GET','POST'])
def Articless(request):
    if request.method=='GET':
       art=Article.objects.all()
       serializer=ArticleSerializer(art,many=True)
       
       return Response(serializer.data)

    elif request.method=='POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','PUT','DELETE'])

def article_detail(request,pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method=='GET':
       serializer=ArticleSerializer(article)
       return Response(serializer.data) 

    elif request.method=='PUT':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_201_CREATED)

'''


