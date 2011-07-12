import random

from django.http import HttpResponse

from feincms.module.page.models import Page


def random_content(request, path):
    region = request.GET.get('region', 'main')
    last = request.GET.get('last', None)
    
    page = Page.objects.best_match_for_path(path, raise404=True)
    
    contents = getattr(page.content, region)
    
    if last != None:
        contents.pop(int(last))
    
    total_prio = 0
    for content in contents:
        total_prio += content.priority
    rand_picker = random.randint(0, total_prio)
    
    floor = 0
    random.shuffle(contents)
    for content in contents:
        if floor <= rand_picker <= (floor + content.priority):
            picked_content = content
            break
        floor += content.priority
    
    return HttpResponse(picked_content.render(request=request))