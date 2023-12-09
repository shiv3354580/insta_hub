#!/usr/bin/bash 

sed -i 's/\[]/\["3.110.121.131"]/' /home/ubuntu/insta_hub/insta_hub/settings.py

python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic
sudo service gunicorn restart
sudo service nginx restart
