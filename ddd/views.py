from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Alertas
from .forms import AlertForm, ResetPassForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
import logging

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)-23s %(levelname)-8s %(name)-12s %(message)s'
            # 'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
})

logger = logging.getLogger(__name__)

# Create your views here.
def redirect_login(request):
    return redirect('login')
    # return render(request, '/login.html', {})

@login_required
def home(request):
    alerts = Alertas.objects.filter(estado='P').order_by('-falta')
    return render(request, 'ddd/home.html', {'alerts':alerts, 'home_page':'active'})

@login_required
def examples(request):
    logger.info('Logger, Iniciando view: examples')
    return render(request, 'ddd/prueba.html', {'examples_page':'active'})

@login_required
def alert_detail(request, pk):
    alert = get_object_or_404(Alertas, pk=pk)
    if request.method == "POST":
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            alert = form.save()
            alert.estado = 'R'
            alert.ffin = timezone.now()
            alert.save()
            return redirect('alerts')
    else:
        form = AlertForm(instance=alert)
    return render(request, 'ddd/alert_detail.html', {'form': form})

@login_required
def reset_pass(request):
    form = ResetPassForm()
    if request.method == 'POST':
        logger.debug('Request POST')
        form = ResetPassForm(request.POST)
        if form.is_valid():
            logger.debug('Formulario es valido')
            data = form.cleaned_data

            if data.get('pass_user')!=data.get('pass_confirm'):
                logger.debug(form)
                return render(request, 'ddd/reset_pass.html', {'form': form,'error':'Las claves deben coincidir'})

            logger.debug('User: ' + str(request.user))
            
            user = User.objects.get(username=request.user)
            logger.debug('Objeto USER recuperado')
            logger.debug('Nuevo pass: ' + str(data.get('pass_user')))
            
            user.set_password(data.get('pass_user'))
            user.save()
            logger.debug('User modificado')

            # Hacemos login para que no nos redireccione a la página de login
            user = authenticate(username=request.user, password=data.get('pass_user'))
            if user is not None:
                login(request, user)
                alerts = Alertas.objects.filter(estado='P').order_by('-falta')
                return render(request, 'ddd/home.html', {'alerts':alerts, 'home_page':'active', 'mensaje':'La contraseña se ha cambiado con éxito'})
            else:
                return redirect('home')
    return render(request, 'ddd/reset_pass.html', {'form': form, 'dropdown_page':'active'})

@login_required
def alerts(request):
    if request.method == 'POST':
        findpass = request.POST['q']
        # logger.debug(request.POST['q'])
        alerts = Alertas.objects.filter(Q(titulo__contains=findpass) | Q(descrip__contains=findpass)).order_by('-falta')
    else:
        findpass = ''
        alerts = Alertas.objects.order_by('-falta')
    return render(request, 'ddd/alerts.html', {'alerts':alerts, 'dropdown_page':'active', 'findpass':findpass})
