from datetime import timezone, datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from op.models import Bonus

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from bon.settings import EMAIL_HOST_USER

from django.core import mail
from django.template.loader import render_to_string
from django.template import RequestContext, Template




@login_required(login_url='/accounts/login') # Check login
def index(request):
    context = {

    }
    return render(request, 'index.html', context)


@csrf_exempt
def check(request):
    code = request.POST.get('code')
    if Bonus.objects.filter(code=code, checko=False).exists():
        bon = Bonus.objects.get(code=code, checko=False)
        value = True
        text = 'Ce bonus est attribué à ' + str(bon.agent.nom) + ' ' + str(bon.agent.prenom)
    elif Bonus.objects.filter(code=code, checko=True).exists():
        value = 'Checked'
        text = 'Ce bonus a déjà été utilisé'
    else:
        value = False
        text = "Ce code de bonus n'existe pas"

    return JsonResponse({'value': value, 'text':text})


@csrf_exempt
def checked(request):
    code = request.POST.get('code')
    mount = request.POST.get('mount')
    user = request.user
    if Bonus.objects.filter(code=code, checko=False).exists():
        bon = Bonus.objects.get(code=code, checko=False)
        if int(mount) <= bon.valeur:
            bon.checko =True
            bon.valeur_deduite =mount
            bon.partenaire = user
            bon.check_at =datetime.now()
            bon.save()
            value = True
            text = ''
        else:
            value = 'Solde'
            text = 'La valeur du bon ne peut pas dépasser ' + str(bon.valeur) + ' dollars américains'
    elif Bonus.objects.filter(code=code, checko=True).exists():
        value = 'Checked'
        text = 'Ce bonus a déjà été utilisé'
    else:
        value = False
        text = "Ce code de bonus n'existe pas"

    return JsonResponse({'value': value, 'text':text})


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


def email(request):
    context = {
            "title": "Your IP Address",
        }
    msg_txt = render_to_string('mail.txt')
    msg_html = render_to_string('mail.html', context, request=request)

    # to = ['akabamba.ext@orange.com', ]
    to = ['kabambaarthur1@gmail.com',]
    mail.send_mail('title', msg_txt, 'kabambaarthur1@gmail.com', to, html_message=msg_html, )

    return redirect('/')