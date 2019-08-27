from django.shortcuts import render, reverse
from .models import Category, Article, Comment, ReplyComment
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
   newest = Article.objects.latest()
   last_three = Article.objects.order_by("-id")[:3]
   context = {'newest': newest, 'last_three' : last_three}
   return render(request, 'main/index.html', context)


def categories(request, slug):
    # get selected category; whether JS, React or jQuery
   categories = Category.objects.all()
   category = Category.objects.get(slug=slug)

    # Get all articles in selected category
   articles = Article.objects.filter(category=category)

   context = {'articles': articles,
               'category': category, 'categories': categories}
   return render(request, 'main/category.html', context)


def article(request, slug):
   article = Article.objects.get(slug=slug)
   comments = Comment.objects.filter(article=article)

    # comment form
   if request.method == 'POST':
      form = CommentForm(request.POST or None)
      
      if form.is_valid():
         text = form.cleaned_data['text']
         email = form.cleaned_data['email']
         name = form.cleaned_data['name']

            # create the comment
         comment = Comment(article=article, text=text,
                              email=email, name=name)
         comment.save()

         return HttpResponseRedirect(article.get_absolute_url())
   


   else:
      form = CommentForm()

   context = {'article': article, 'form': form, 'comments': comments}

   return render(request, 'main/article.html', context)

