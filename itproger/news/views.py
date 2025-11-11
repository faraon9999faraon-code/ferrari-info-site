from django.shortcuts import render
from  .models import Articles
from django.views.generic.detail import DetailView



def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_views.html'
    context_object_name = 'article'