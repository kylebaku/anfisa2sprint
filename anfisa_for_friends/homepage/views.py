from django.shortcuts import render
from django.db.models import Q 
from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.select_related('wrapper').values('id', 'title', 'description','wrapper__title').filter(Q(is_published=True)&Q(is_on_main=True)).order_by('title')
    context = {
        'ice_cream_list': ice_cream_list,        
    }
    return render(request, template_name, context)
