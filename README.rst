My blog
=======

Static pelican_ generated site.

In a virtual environment, run:

.. code-block:: bash

    pip install pip-tools
    pip-sync

Now, in two terminals with activated environment, run:

.. code-block:: bash

    pipenv run make regenerate
    pipenv run make serve

Deployment
----------

I'm using Codeship_ to deploy. Use the followin setup commands:

.. code-block:: bash

    pip install pip-tools
    pip-sync

And custom deployment script:

.. code-block:: bash

    make rsync_upload

Here is the nginx configuration file, copy this to ``/etc/nginx/sites-available/blog.tomgurion.me``:

.. code-block::

    server {
        listen 80;
        server_name blog.tomgurion.me;
        root /home/nagasaki45/sites/blog.tomgurion.me/output;
        index index.html;
        access_log /home/nagasaki45/sites/blog.tomgurion.me/access.log;
    }

Don't forget to add a link to ``sites-enabled`` and restart nginx.

.. _pelican: http://docs.getpelican.com/
.. _Codeship: https://codeship.com
