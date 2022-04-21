from blog.helper import IdValidatorHelper
from django.shortcuts import render
from functools import wraps


def user_has_valid_id(view):
    # copia os métodos mágicos (__name__) para o decorador, 
    # lembrando que tudo em python herda de object
    @wraps(view)
    def inner(request, *args, **kwargs):
        unique_id = request.GET.get('id')
        if IdValidatorHelper.validate(unique_id):
            return view(request, *args, **kwargs)
        return render(request, "blog/invalid_id_error.html")
    return inner
