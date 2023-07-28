import pygal
from django.shortcuts import render, Http404
from django.contrib.auth import logout

from .models import Token, Branch, Archbishop, Event
from learning.views import to_markdown


def generate() -> pygal.Line:
    events = Event.objects.all()
    view = pygal.Line(interpolate='hermite',
                      interpolation_parameters={'type': 'kochanek_bartels', 'b': -1, 'c': 1, 't': 1})
    view.title = '老教历程'
    values = []
    dates = []
    for event in events:
        values.append({
            'value': event.value,
            'label': event.name,
        })
        dates.append(event.time)
    view.x_labels = dates
    view.x_title = '日期'
    view.y_title = '影响力'
    view.add('老教历程', values)
    return view


def is_allowed(request):
    user = request.user
    if user.is_authenticated:
        for token in Token.objects.all():
            if token.owner == user:
                return True
    return False


def index_view(request):
    if is_allowed(request):
        events = []
        for event in Event.objects.all():
            events.append({
                'name': event.name,
                'time': event.time,
                'value': event.value,
                'description': to_markdown(event.description),
            })
        context = {
            'branches': Branch.objects.all(),
            'archbishops': Archbishop.objects.all(),
            'events': events,
            'events_chart': generate().render_data_uri(),
        }
        return render(request, 'religion/index.html', context=context)
    raise Http404


def logout_view(request):
    if is_allowed(request):
        logout(request)
        return render(request, 'religion/logout.html')
    raise Http404
