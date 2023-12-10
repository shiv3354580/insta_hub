#!/usr/bin/bash 

sed -i 's/\[]/\["3.109.210.67"]/' /home/ubuntu/insta_hub/insta_hub/settings.py

python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
