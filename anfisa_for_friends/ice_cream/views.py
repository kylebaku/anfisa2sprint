from django.shortcuts import render
from django.http import Http404

from ice_cream.models import IceCream

def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    # Готовимся перехватить исключение. 
    try:
        # Пытаемся получить объект с заданным pk:
          ice_cream = IceCream.objects.get(pk=pk)
    # Если объект не найден...
    except IceCream.DoesNotExist:
        # ...выбрасываем исключение Http404
        raise Http404('Такого мороженого не существует.')
        # Специальный обработчик перехватит выброшенное исключение
        # и среагирует установленным образом; 
        # по умолчанию - вернёт пользователю стандартную страницу ошибки 404.
    
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template, context) 


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
