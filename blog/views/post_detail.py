from django.shortcuts import render , get_object_or_404
from blog.models.post import Post


def post_detail_view(request,post_id):
    post= get_object_or_404(Post,post_id=post_id)
    context={
        'titulo':post.title,
        'data':post.created_at,
        'mensagem':'Esse foi o post escolhido',
        'conteudo':post.content,
        'post_id': post.post_id

    }
    return render(request,'blog/post_detail.html',context)