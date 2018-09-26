#!/usr/bin/env bash

venv_python=./venv/bin/python

${venv_python} ./manage.py migrate
echo 'Start parse_server and detach...'
(${venv_python} ./manage.py parse_server &) &
echo 'Start runserver and detach...'
(${venv_python} ./manage.py runserver 8000 &) &
