# Eventex

Sistema de ventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/paulocesarcsdev/eventex-paulocesar2.svg?branch=master)](https://travis-ci.org/paulocesarcsdev/eventex-paulocesar2)
[![Code Health](https://landscape.io/github/paulocesarcsdev/eventex-paulocesar2/master/landscape.svg?style=flat)](https://landscape.io/github/paulocesarcsdev/eventex-paulocesar2/master)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Insatle as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:paulocesarcsdev/eventex-paulocesar2.git
cd wttd
python -m venv .wttd
source .wttd/bin/active
pip install -r requirements.txt
cp contrib/env-sample .env
```

## Como fazer o deploy?

1. Cire uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```