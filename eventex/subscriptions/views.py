from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':

        context = dict(name='Paulo Cesar', cpf='12345678901',
                       email='paulo@cesar.net', phone='62-9413-0086')

        body = render_to_string('subscriptions/subscription_email.txt',
                                context)

        mail.send_mail('Confirmação da inscrição',
                        body,
                       'contato@eventex.com.br',
                       ['contato@eventex.com.br', 'paulo@cesar.net'])

        return HttpResponseRedirect('/inscricao/')
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)

