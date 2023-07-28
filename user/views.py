from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Homepage, homepage_default_content
from learning.views import to_markdown


def user_view(request, username):
    user = get_object_or_404(User, username=username)
    homepage, created = Homepage.objects.get_or_create(owner=user)
    context = {
        'username': user.username,
        'homepage': to_markdown(homepage.content),
        'homepage_default_content': f'<p>{homepage_default_content}</p>',
        'homepage_content': homepage.content,
    }
    return render(request, 'user/user.html', context=context)


@login_required
def edit_homepage_view(request):
    user = request.user
    homepage, created = Homepage.objects.get_or_create(owner=user)
    homepage.content = request.POST.get('edit-content', '').strip()
    homepage.save()
    kwargs = {
        'username': user.username,
    }
    return redirect(reverse('user:user', kwargs=kwargs))
