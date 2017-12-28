# Chartflo notebooks

Demo notebooks and generator example for [django-chartflo](https://github.com/synw/django-chartflo)

### Online notebooks

To run online click the badge:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/synw/django-chartflo-notebooks/master)

### Generator example

To install the example: clone, `pip install -r requirements.txt` and go to the `demo` folder to run the server. Create
a superuser, login to the admin and go to `/dashboards/inflation/`.

### Offline Django notebooks

To run the offline notebooks inside the Django environnement install 
[django-extensions](https://github.com/django-extensions/django-extensions) and run:

   ```
   python3 manage.py shell_plus --notebook
   ```


