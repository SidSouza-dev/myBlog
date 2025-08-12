from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

def home_view(request):
    posts= Post.objects.all()
    context={
      
        'titulo': 'Página Inicial',
        'mensagem': 'Bem-vindo ao meu blog!',
        'posts': posts,  
    
    }
    return render(request ,'blog/home.html',context)