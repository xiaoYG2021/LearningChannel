from .models import Token


def judge(request):
    user = request.user
    is_allowed = False
    for token in Token.objects.all():
        if token.owner == user and token.effective:
            is_allowed = True
    context = {
        'is_allowed': is_allowed,
    }
    return context
