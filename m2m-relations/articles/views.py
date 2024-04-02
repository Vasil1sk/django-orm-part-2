from django.shortcuts import render

from articles.models import Article

def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().order_by('-published_at')  # получаем список статей
    for article in object_list:
        article.tags_list = article.tags.all()  # получаем список тегов для каждой статьи
    context = {'object_list': object_list}
    return render(request, template, context)
