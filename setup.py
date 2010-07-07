from distutils.core import setup

setup(name='django-xpower',
    version='0.1.0',
    description='Adds the X-Powered-By header to your Django site',
    long_description=open('README.rst').read(),
    author='Justin Quick',
    author_email='justquick@gmail.com',
    url='http://github.com/justquick/django-xpower',
    packages=['xpower'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)
