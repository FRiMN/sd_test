#!/usr/bin/env bash

venv_python=./venv/bin/python

${venv_python} ./manage.py migrate
(${venv_python} ./manage.py parse_server &) &
(${venv_python} ./manage.py runserver 8000 &) &
