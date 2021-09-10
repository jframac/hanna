from django.shortcuts import render


def index(request):

    context = {
        'title': 'Hanna Garduño - Coach Transformacional',
        'home_active': 'active',
    }

    return render(request, 'index.html', context=context)


def cursos(request):

    context = {
        'title': 'Hanna Garduño - Cursos',
        'cursos_active': 'active',
    }

    return render(request, 'cursos.html', context=context)

def about(request):

    context = {
        'title': 'Hanna Garduño - Acerca de mí',
        'about_active': 'active',
    }

    return render(request, 'about.html', context=context)