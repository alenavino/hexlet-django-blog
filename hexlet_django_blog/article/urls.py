from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView
from hexlet_django_blog.article.views import ArticleFormCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view(), name='article_detail'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
