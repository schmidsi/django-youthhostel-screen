import random

from datetime import datetime, time
from dateutil import parser

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils import simplejson

from feincms.module.page.models import Page
from feincms.templatetags.feincms_tags import _render_content

from newswall.models import Source

from contents import SimpleGalleryContent


def get_region(request, path):
    content = request.GET.get('content', 'all')
    region = request.GET.get('region', 'main')
    page = Page.objects.best_match_for_path(path, raise404=True)

    if region == 'ticker':
        return ticker_combined(request, region, page)
    elif content == 'random':
        return random_content(request, region, page)
    elif content == 'all':
        response = u''.join(_render_content(content, request=request, context={})\
            for content in getattr(page.content, region))
        return HttpResponse(response)


def random_content(request, region, page):
    last = request.GET.get('last', None)

    contents = getattr(page.content, region)

    if len(contents) == 1:
        return HttpResponse(contents[0].render(request=request))
    elif len(contents) == 0:
        return HttpResponse('<div class="dummy" data-duration="10">&nbsp;</div>')

    if last != None:
        last = contents.pop(int(last))
        ignored_last = True
    else:
        ignored_last = False

    now = datetime.now()

    filtered_contents = []

    total_prio = 0
    for content in contents:
        if content.boost_end and content.boost_start and content.boost_priority:
            if content.boost_start <= now.time() <= content.boost_end:
                content.priority = content.boost_priority

        # do not add empty galleries
        if isinstance(content, SimpleGalleryContent):
            if content.category.mediafile_set.count() == 0:
                break

        if 6 <= now.hour < 10:
            if content.morning:
                total_prio += content.priority
                filtered_contents.append(content)
        elif time(10, 0) <= now.time() < time(13, 30):
            if content.afternoon:
                total_prio += content.priority
                filtered_contents.append(content)
        elif time(13, 30) <= now.time() < time(23, 0):
            if content.evening:
                total_prio += content.priority
                filtered_contents.append(content)
        elif 23 <= now.hour or now.hour < 6:
            if content.night:
                total_prio += content.priority
                filtered_contents.append(content)

    rand_picker = random.randint(0, total_prio)

    floor = 0
    picked_content = None
    random.shuffle(filtered_contents)
    for content in filtered_contents:
        if floor <= rand_picker <= (floor + content.priority):
            picked_content = content
            break
        floor += content.priority

    if picked_content:
        response = picked_content.render(request=request)
    else:
        if ignored_last:
            response = last.render(request=request)
        else:
            response = '<div class="error">Kein Inhalt gefunden</div>'

    return HttpResponse(response)


def weather(request):
    city = request.GET.get('city', 'basel,switzerland')
    return render(request, 'weather.html', {'city' : city})


def modified(request):
    page_id = request.GET.get('page_id', 0)
    page = Page.objects.get(pk=page_id)
    live_revision = request.GET.get('last_modified', '2000-11-05 18:59:00.54936+00')
    live_revision_parsed = parser.parse(live_revision)
    changed = False

    if page.modification_date > live_revision_parsed:
        changed = True

    return HttpResponse(simplejson.dumps(changed))


def ticker_combined(request, region, page, string_response=False):
    sources = Source.objects.filter(newswallcontent__in=page.newswallcontent_set.all())
    stories = list()

    for source in sources:
        stories += list(source.stories.all().order_by('-timestamp')[:10])

    random.shuffle(stories)

    if string_response:
        return render_to_string('ticker.html', {'stories' : stories})
    else:
        return render(request, 'ticker.html', {'stories' : stories})

