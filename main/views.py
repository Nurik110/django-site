from django.shortcuts import render
from .models import Heroes
from .models import Images
from .models import Equipment
from .models import Feature
from .models import Ability

# Подключение стандартной формы для регистрации
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.
def index(request):
    hero = Heroes.objects.all()
    return render(
        request,
        'index.html',
        context={'hero': hero, },
    )

def equipment(request):
    equip = Equipment.objects.all()
    return render(
        request,
        'equipment.html',
        context={'equip': equip},
    )
   
def hero_hero(request):
    heroes = Heroes.objects.all()
    id = request.GET.get("id")
    hero = Heroes.objects.get(id=id)
    heroClass = request.GET.get("heroClass")
    imag = Images.objects.filter(post = id)
    heroe = Feature.objects.filter(name = id)
    abil = Ability.objects.filter(name = id)
    return render(
        request, 
        'hero_hero.html', 
        context={
            'heroes': heroes, 
            'hero': hero, 
            'id': id, 
            'heroClass': heroClass, 
            'imag': imag,
            'heroe': heroe,
            'abil': abil

        },
    )
def hero_class(request):

    heroClass = request.GET.get("heroClass")
    heroes = Heroes.objects.filter(group=heroClass)
   
    return render(
        request, 
        'hero_class.html', 
        context={
            'heroes': heroes, 

            'heroClass': heroClass 
        },

    )
 

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})