# Criar o arquivo requirements.txt e adicionar Django~=3.2.10
# Depois no terminal pip install -r requirements.txt
# Criar o ambiente django-admin.exe startproject mysite .
# Abrir o arquivo settings.py editar
# Criar o banco de dados python manage.py migrate
# Iniciar o servidor python manage.py runserver
# Colar o endereço no browser http://127.0.0.1:8000/
# Precione CTRL+C no terminal para encerrar o servidor
# Criar uma aplicação python manage.py startapp blog
# Adicionar nossa aplicação no settings.py
# Criar um modelo de postagem para o blog no arquivo models.py
# Criar tabelas para nossos modelos no banco de dados
# digitar python manage.py makemigrations blog
# Aplicar as alterações no banco digitar python manage.py migrate blog
# Editar o blog/admin.py
# Para manipular o Admin digite antes python manage.py createsuperuser
# Executar o servidor e colar o endereço http://127.0.0.1:8000/admin/ no browser
# Deploy!
# Configurando o seu blog no PythonAnywhere
# Criar uma conta no PythonAnywhere
# Criar um token de API
# Navegue para a Dashboard do PythonAnywhere clicar em $ Bash
# No terminal digitar pip3.6 install --user pythonanywhere
# pa_autoconfigure_django.py https://github.com/<your-github-username>/my-first-blog.git
