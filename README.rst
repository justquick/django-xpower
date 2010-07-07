Django X Power
===============

:Authors:
   Justin Quick <justquick@gmail.com>
:Version: 0.1


::

    pip install django-xpower==0.1.0

Django X Power is a simple middleware that adds the ``X-Powered-By`` header to any Django site.

    
Install
--------

Install the module using pip/easy_install or whatever you like then add in the middleware into your ``MIDDLEWARE_CLASSES``::

    MIDDLEWARE_CLASSES = (
        'xpower.middleware.XPoweredByMiddleware',
        ...
    )

Configure
----------

In your settings you may define the contents of the ``X-Powered-By`` header::

    X_POWERED_BY = 'Django'
    
If you do not set this it will use the default which is ``'Django/%(version)s``
where ``%(version)s`` is replaced with the version of Django that you are using.

Testing
--------

An example project is provided so just run ``./manage.py runserver`` and then you can
confirm that it is working by running ``curl -i http://localhost:8000 | head``.
You should see something like this::

    HTTP/1.0 200 OK
    Date: Wed, 07 Jul 2010 15:40:59 GMT
    Server: WSGIServer/0.1 Python/2.6.1
    Content-Type: text/html
    X-Powered-By: Django/1.2.1 SVN-13336


Alternates
----------

Some alternatives for the header contents:

 * Ponies with magical powers
 * Who the fuck knows
 * A series of tubes
 * Perfectionists with deadlines
 * Opinionated developers