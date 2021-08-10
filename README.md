### Installing an official release with pip
python -m pip install Django

### Installing the development version
git clone https://github.com/django/django.git

python -m pip install -e django/

### Upgrade Django version
pip install Django --upgrade

### Django version
python -m django --version

### Create a new project
django-admin startproject mysite

### Start the dev server
python manage.py runserver

### 
Next, start your first app by running python manage.py startapp [app_label].

You're seeing this message because you have DEBUG = True in your Django settings file and you haven't configured any URLs. Get to work!

> pip install virtualenv

> virtualenv C:\Python_Virtualenv -p C:\Python26\python.exe
whereas \path\to\env shall be the path where your virtual environment is going to be and \path\to\python_install.exe 
the one where your freshly (presumably) installed Python version resides.
You now have a virtual environment set up! Now, to activate the virtual environment execute the batch file which is 
located inside the \path\to\env\Scripts\activate.bat


python manage.py makemigrations monblog
python manage.py migrate monblog
python manage.py migrate --run-syncdb

