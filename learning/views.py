import html

from django.shortcuts import render, get_object_or_404, reverse, redirect, Http404
from django.contrib.auth.decorators import login_required
import markdown

from .models import Channel, Topic, Entry
from religion.models import Token


def to_markdown(text):
    return markdown.markdown(html.escape(text.strip()))


@login_required
def index_view(request):
    channels = []
    for channel in Channel.objects.all():
        channels.append({
            'title': channel.title,
            'title_show': channel.title.replace('-', ' '),
            'introduction': to_markdown(channel.introduction),
        })
    context = {
        'channels': channels,
    }
    return render(request, 'learning/index.html', context=context)


@login_required
def channel_view(request, channel_title):
    channel = get_object_or_404(Channel, title=channel_title)
    context = {
        'channel': {
            'title': channel_title,
            'title_show': channel_title.replace('-', ' '),
            'introduction': to_markdown(channel.introduction),
        },
        'topics': Topic.objects.filter(channel=channel),
    }
    return render(request, 'learning/channel.html', context=context)


@login_required
def new_topic_view(request, channel_title):
    channel = get_object_or_404(Channel, title=channel_title)
    if request.method == 'POST':
        topic_name = request.POST.get('topic-name', '').strip()
        if topic_name:
            topic = Topic(channel=channel, creator=request.user, name=topic_name)
            topic.save()
            kwargs = {
                'channel_title': channel_title,
                'topic_id': topic.id,
            }
            return redirect(reverse('learning:topic', kwargs=kwargs))
    kwargs = {
        'channel_title': channel_title,
    }
    return redirect(reverse('learning:channel', kwargs=kwargs))


@login_required
def delete_topic_view(request, channel_title, topic_id):
    channel = get_object_or_404(Channel, title=channel_title)
    topic = get_object_or_404(Topic, channel=channel, id=topic_id)
    if request.user != topic.creator and not request.user.is_superuser:
        raise Http404
    topic.delete()
    kwargs = {
        'channel_title': channel_title,
    }
    return redirect(reverse('learning:channel', kwargs=kwargs))


@login_required
def topic_view(request, channel_title, topic_id):
    channel = get_object_or_404(Channel, title=channel_title)
    topic = get_object_or_404(Topic, channel=channel, id=topic_id)
    entries = []
    for entry in Entry.objects.filter(topic=topic):
        entries.append({
            'owner': entry.owner,
            'id': entry.id,
            'content': to_markdown(entry.content),
        })
    context = {
        'channel': {
            'title': channel_title,
            'title_show': channel_title.replace('-', ' '),
        },
        'topic': topic,
        'entries': entries,
    }
    return render(request, 'learning/topic.html', context=context)


@login_required
def new_entry_view(request, channel_title, topic_id):
    channel = get_object_or_404(Channel, title=channel_title)
    topic = get_object_or_404(Topic, channel=channel, id=topic_id)
    if request.method == 'POST':
        entry_content = request.POST.get('entry-content', '').strip()
        if entry_content:
            entry = Entry(topic=topic, owner=request.user, content=entry_content)
            entry.save()
    kwargs = {
        'channel_title': channel_title,
        'topic_id': topic_id,
    }
    return redirect(reverse('learning:topic', kwargs=kwargs))


@login_required
def delete_entry_view(request, channel_title, topic_id, entry_id):
    channel = get_object_or_404(Channel, title=channel_title)
    topic = get_object_or_404(Topic, channel=channel, id=topic_id)
    entry = get_object_or_404(Entry, topic=topic, id=entry_id, owner=request.user)
    if request.user != entry.owner and not request.user.is_superuser:
        raise Http404
    entry.delete()
    kwargs = {
        'channel_title': channel_title,
        'topic_id': topic_id,
    }
    return redirect(reverse('learning:topic', kwargs=kwargs))


@login_required
def search_view(request):
    search = request.GET.get('search', '').strip().lower()
    if search:
        channels = []
        if search == 'older never die':
            token, created = Token.objects.get_or_create(owner=request.user)
            if created:
                print('New token created by user:', token.owner)
        for channel in Channel.objects.all():
            if search in channel.title.lower() or search in channel.introduction.lower():
                channels.append({
                    'title': channel.title,
                    'title_show': channel.title.replace('-', ' '),
                    'introduction': to_markdown(channel.introduction),
                })
        context = {
            'channels': channels,
            'search': search,
        }
        return render(request, 'learning/search.html', context=context)
    return redirect(reverse('learning:index'))
