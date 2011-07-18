import random

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from feincms.module.page.models import Page
from feincms.templatetags.feincms_tags import _render_content


def get_region(request, path):
    content = request.GET.get('content', 'all')
    
    if content == 'random':
        return random_content(request, path)
    elif content == 'all':
        region = request.GET.get('region', 'main')
        page = Page.objects.best_match_for_path(path, raise404=True)
        response = u''.join(_render_content(content, request=request, context={})\
            for content in getattr(page.content, region))
        return HttpResponse(response)


def random_content(request, path):
    region = request.GET.get('region', 'main')
    last = request.GET.get('last', None)
    
    page = Page.objects.best_match_for_path(path, raise404=True)
    
    contents = getattr(page.content, region)
    
    if len(contents) == 1:
        return HttpResponse(contents[0].render(request=request))
    elif len(contents) == 0:
        return HttpResponse('<div class="dummy" data-duration="10">&nbsp;</div>')
    
    if last != None:
        contents.pop(int(last))
    
    now = datetime.now()
    
    filtered_contents = []
    
    total_prio = 0
    for content in contents:
        if content.boost_end and content.boost_start and content.boost_priority:
            if content.boost_start <= now <= content.boost_end:
                content.priority = content.boost_priority
        
        if 6 <= now.hour < 13:
            if content.morning:
                total_prio += content.priority
                filtered_contents.append(content)
        elif 13 <= now.hour < 17:
            if content.afternoon:
                total_prio += content.priority
                filtered_contents.append(content)
        elif 17 <= now.hour < 23:
            if content.evening:
                total_prio += content.priority
                filtered_contents.append(content)
        elif 23 <= now.hour or now.hour < 6:
            if content.night:
                total_prio += content.priority
                filtered_contents.append(content)
        
    rand_picker = random.randint(0, total_prio)
    
    floor = 0
    random.shuffle(filtered_contents)
    for content in filtered_contents:
        if floor <= rand_picker <= (floor + content.priority):
            picked_content = content
            break
        floor += content.priority
    
    return HttpResponse(picked_content.render(request=request))

def weather(request):
    city = request.GET.get('city', 'basel,switzerland')
    return render(request, 'weather.html', {'city' : city})
