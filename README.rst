###########
irbis-books
###########
Требования
==========
* Django >= 2.0.2
* Python >= 3.5.2

Установка
=========
**1.** Установите Git и дополнительные системные пакеты Python
::
    sudo apt install git python3-dev python3-pip python3-setuptools python3-venv

**2.** Обновите pip и setuptools, а так же установите pipenv
::
    pip3 install --upgrade --user pip setuptools pipenv

**3.** Склонируйте Git репозиторий в папку проектов
::
    git clone https://github.com/ri-gilfanov/irbis-books.git

**4.** Перейдите в папку проекта
::
    cd irbis-books

**5.** Создайте виртуальное окружение и установите необходимые пакеты
::
    pipenv install --dev

**6.** Активируйте виртуальное окружение
::
    pipenv shell

**7.** Запустите веб-сервис
::
    python3 irbisbooks/manage.py runserver