from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','Title','Description']
   # Title=serializers.CharField(max_length=100)
   # Description=serializers.CharField(max_length=100)

   # def create(self, validated_data):
       # return Article.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{
            'write_only':True,
            'required':True
        }
        }
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user



   
    
    #def update(self,instance,validated_data):
        #instance.Title=validated_data.get('Title',instance.Title)
        #instance.Description=validated_data.get('Description',instance.Description)
        #instance.save()
        #return instance
 


