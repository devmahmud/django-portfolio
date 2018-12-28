from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Quotes


def index(request):
    if request.method == 'GET' and request.GET.get('query') != None:
        query = request.GET.get('query')
        posts = Post.objects.filter(
            title__icontains=query)
        quotes = Quotes.objects.order_by('-pk')[:1]

        for quote in quotes:
            quote = get_object_or_404(Quotes, pk=quote.id)
        return render(request, 'blog/index.html', {'posts': posts, 'quote': quote})

    else:
        posts = Post.objects.order_by('-pub_date')
        quotes = Quotes.objects.order_by('-pk')[:1]
        for quote in quotes:
            quote = get_object_or_404(Quotes, pk=quote.id)
        return render(request, 'blog/index.html', {'posts': posts, 'quote': quote})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
