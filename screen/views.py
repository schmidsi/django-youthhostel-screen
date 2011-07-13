import random

from datetime import datetime

from django.http import HttpResponse

from feincms.module.page.models import Page


def random_content(request, path):
    region = request.GET.get('region', 'main')
    last = request.GET.get('last', None)
    
    page = Page.objects.best_match_for_path(path, raise404=True)
    
    contents = getattr(page.content, region)
    
    if last != None:
        contents.pop(int(last))
    
    now = datetime.now()
    
    total_prio = 0
    for content in contents:
        if content.boost_end and content.boost_start and content.boost_priority:
            if content.boost_start <= now <= content.boost_end:
                content.priority = content.boost_priority
        
        if 6 <= now.hour < 13:
            if content.morning:
                total_prio += content.priority
            else:
                contents.remove(content)
        elif 13 <= now.hour < 17:
            if content.afternoon:
                total_prio += content.priority
            else:
                contents.remove(content)
        elif 17 <= now.hour < 23:
            if content.evening:
                total_prio += content.priority
            else:
                contents.remove(content)
        elif 23 <= now.hour or now.hour < 6:
            if content.night:
                total_prio += content.priorit
            else:
                contents.remove(content)
        
    rand_picker = random.randint(0, total_prio)
    
    floor = 0
    random.shuffle(contents)
    for content in contents:
        if floor <= rand_picker <= (floor + content.priority):
            picked_content = content
            break
        floor += content.priority
    
    return HttpResponse(picked_content.render(request=request))