
from django.contrib import admin
from django.urls import path,include
from myapp import views
#from myapp.views import Articless
from myapp.views import ArticleViewSet,UserViewSet
from rest_framework.routers import DefaultRouter
#Article_detail
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register('articles',ArticleViewSet,basename='articles')
router.register('register',UserViewSet,basename='register')
urlpatterns = [
    path('admin/', admin.site.urls),
    #path ('article/',views.Articless),
    #path ('article/<int:pk>',views.article_detail),
    #path('article/',Articless.as_view()),
    #path('article/<int:id>',Article_detail.as_view())
    path('',include(router.urls)),
    path('auth/',ObtainAuthToken)
]
 