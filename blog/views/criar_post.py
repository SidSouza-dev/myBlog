from django.shortcuts import render, redirect
from blog.forms.form import PostForm
from django.http import HttpRequest

def criar_post_view(request:HttpRequest):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
            mensagem = "Post criado com sucesso!"
            return render(request,'blog/criar_post.html',{'form':form,'mensagem':mensagem})
    else:
        form = PostForm()  
          
    return render(request,'blog/criar_post.html',{'form':form})