# BoardGameStats

Welcome to **BoardGameStats**! This app will help you organize your board game plays. It uses BoardGameGeek API to obtain infromation about board games.  It is still under development procedure, but you can try use a prototype of it today. Just follow these steps to install **BoardGameStats**:

-  Install Python3 
-  Install virtualenv - it's a virtual environment which will help you avoid conflicts due to different versions of Django or Python
- Clone this repostery to desired destination
-  Create new virtual environment through command line (*virtualenv -p python3 env*)
-  Activate the virtual environment (*source env/bin/activate*) in the location of your freshly created virutal environent
- Go to cloned repository (in virtual environment), find requirements.txt and install them (*pip install -r requirements.txt*) - this will install all the stuff used by the app
-  Go to manage.py location and run *python manage.py makemigrations* and after that *python manage.py migrate*
-  Create your admin account by running *python manage.py createsuperuser* - follow the instructions displayed in command line
-  Run *python manage.py runserver* to start development server and that's it! Visit localhost:8000 to see main page. Port 8000 is a default port for Django, but if for some reasone you have to change it just run *python manage.py runserver port number*
-  All information about URLs you can find in urls.py file

Implemented features:
- registration
- search view