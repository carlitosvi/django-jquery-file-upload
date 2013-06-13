

Features
========

* Drag and drop files
* Select multiple files
* Cancel upload
* Delete uploaded file (from database only)
* No flash (or other browser plugins) needed
* … more at the [upstream's features page](http://aquantum-demo.appspot.com/file-upload#features)

Requirements
============

* Django
* Python Imaging Library

If you do not get PIL to work (_pillow_ is a replacement package that works
with virtulalenvs), use FileField instead of ImageField in
fileupload/models.py as commented in the file.

Installation
============

* pip install -r requirements.txt (will install django and pillow)
* python manage.py syncdb
* python manage.py runserver
* go to localhost:8000/upload/new/ and upload some files

License
=======
MIT, as the original project. See LICENSE.txt.
