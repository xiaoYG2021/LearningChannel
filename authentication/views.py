from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_slug, ValidationError


def login_view(request):
    nxt = request.GET.get('next', reverse('index:index'))
    if request.user.is_authenticated:
        return redirect(nxt)
    username = error = ''
    if request.method == 'POST':
        nxt = request.POST.get('next')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(nxt)
        else:
            error = '用户名或密码错误！'
    context = {
        'username': username,
        'error': error,
        'next': nxt,
    }
    return render(request, 'authentication/login.html',
                  context=context)


def logout_view(request):
    nxt = request.GET.get('next')
    if not nxt:
        nxt = reverse('index:index')
    logout(request)
    return redirect(nxt)


def register_view(request):
    # return redirect(reverse('authentication:login'))
    nxt = request.GET.get('next', reverse('index:index'))
    if request.user.is_authenticated:
        return redirect(nxt)
    username = error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if 4 <= len(username) <= 20:
            try:
                validate_slug(username)
            except ValidationError:
                error = '用户名不合规！'
            else:
                if password == password2:
                    if len(password) <= 100:
                        usernames = [
                            user.username for user in User.objects.all()
                        ]
                        if username not in usernames:
                            user = User.objects.create_user(
                                username=username, password=password
                            )
                            group_names = [
                                group.name for group in Group.objects.all()
                            ]
                            group_name = '普通用户'
                            if group_name in group_names:
                                group = Group.objects.get(name=group_name)
                            else:
                                group = Group.objects.create(name='普通用户')
                                group.save()
                            user.groups.add(group)
                            user.save()
                            login(request, user)
                            return redirect(nxt)
                        else:
                            error = '用户名已存在！'
                    else:
                        error = '密码过长！'
                else:
                    error = '密码不一致！'
        else:
            error = '用户名长度不正确！'
    context = {
        'username': username,
        'error': error,
        'next': nxt,
    }
    return render(request, 'authentication/register.html',
                  context=context)


@login_required
def change_password_view(request):
    user = request.user
    info = error = ''
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if user.check_password(old_password):
            if password == password2:
                if len(password) <= 100:
                    user.set_password(password)
                    user.save()
                    info = '密码修改成功！'
                    login(request, user)
                else:
                    error = '新密码过长！'
            else:
                error = '新密码不一致！'
        else:
            error = '旧密码不正确！'
    context = {
        'username': user.username,
        'info': info,
        'error': error,
    }
    return render(request, 'authentication/change_password.html',
                  context)
