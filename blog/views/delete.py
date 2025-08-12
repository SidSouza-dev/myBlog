from django.shortcuts import get_object_or_404,redirect
from django.views.decorators.http import require_POST
from blog.models.post import Post

@require_POST
def post_delete_view(request,post_id):
    post=get_object_or_404(Post, post_id=post_id)
    post.delete()
    return redirect('home')