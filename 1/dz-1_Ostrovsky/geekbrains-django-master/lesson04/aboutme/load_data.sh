#!/usr/bin/bash
cp db.sqllite3 db.sqllite3.orig
./manage.py migrate about zero
./manage.py migrate
./manage.py loaddata data.xml