from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.


def home(request):
    # return HttpResponse("Hello World,Django")
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    # return HttpResponse("You're looking at my_args %s" % my_args)
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post' : post})


# def test(request):
#    return render(request, 'test.html', {"current_time": datetime.now()})
