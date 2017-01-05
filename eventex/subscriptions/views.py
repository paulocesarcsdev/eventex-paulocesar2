from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        mail.send_mail('Confirmação da inscrição',
                        MESSAGE,
                       'contato@eventex.com.br',
                       ['contato@eventex.com.br', 'paulo@cesar.net'])

        return HttpResponseRedirect('/inscricao/')
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)


MESSAGE = """
Olá Tudo bem?

Muito obrigado por se inscrever no Eventex.

Estes foram os dados que você nos forneceu
em sua inscrição:

Nome: Paulo Cesar
CPF: 12345678901
Email: paulo@cesar.net
Telefone: 62-9413-0086

Em até 48 horas úteis, a nossa equipe entrará
em contato com você para concluirmos a sua
matrícula.

Antenciosamente,
--
Morena
"""