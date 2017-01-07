from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Paulo Cesar', cpf='12345678901',
                    email='paulo@cesar.net', phone='62-9413-0086')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação da inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'paulo@cesar.net']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Paulo Cesar',
            '12345678901',
            'paulo@cesar.net',
            '62-9413-0086',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
