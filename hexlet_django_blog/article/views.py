from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect


class IndexView(View):

    def get(self, request, tags, article_id):
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")


def index(request):
    return redirect(
        reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        )
