# django-vuejs-01-vue-inner-django

Neste projeto eu uso [Django][1] e sua renderização tradicional de templates, e uso o [VueJS][2] apenas como um arquivo estático via CDN. Inclui também [axios][3] via CDN.


## Como rodar o projeto?

Em Dev rodar dois servidores, back e front.

Depois fazer `npm run build` para gerar os arquivos pra rodar somente com Django.

### Backend

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-vuejs-01-vue-inner-django.git
cd django-vuejs-01-vue-inner-django
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```


## Comandos pra criar o projeto do zero

### Criando o projeto Django

```
python -m venv .venv
source .venv/bin/activate
pip install -U pip; pip install django python-decouple
django-admin startproject myproject .
cd myproject
python ../manage.py startapp core
cd ..
```

#### Criando uma pasta chamada contrib com um env_gen.py

O comando a seguir pega `env_gen.py` do gist e clona na pasta `/tmp`.

```
git clone https://gist.github.com/22626de522f5c045bc63acdb8fe67b24.git /tmp/contrib; if [ ! -d contrib ]; then mkdir contrib; fi; cp /tmp/contrib/env_gen.py contrib/
# rode este comando para gerar o .env (variáveis de ambiente).
python contrib/env_gen.py
```

Em `settings.py` insira `'myproject.core'`, em `INSTALLED_APPS`.

Se você mudar a pasta default dos estáticos, então faça:

```
# opcional
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'myproject/core/templates/static/',
]
```

Depois entre na pasta

```
cd myproject/core/
```

e vamos editar o `views.py`.

```
cat << EOF > views.py
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
EOF
```

Agora vamos criar um `urls.py` na pasta `core`.

```
cat << EOF > urls.py
from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
]
EOF
```

Volte para a pasta `myproject` e edite o `urls.py` principal:

```
cat << EOF > urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myproject.core.urls')),
    path('admin/', admin.site.urls),
]
EOF
```

### Criando os templates




### Criando os arquivos estáticos




#### Rodando o servidor Django

Vá para a mesma pasta onde está o `manage.py`.

```
python manage.py runserver
```



[1]: https://www.djangoproject.com/
[2]: https://vuejs.org/
[3]: https://github.com/axios/axios
[4]: https://gist.github.com/rg3915/6fad3d19f2b511ec5da40cef5a168ca5
