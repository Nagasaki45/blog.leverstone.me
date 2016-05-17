My blog
=======

Static pelican_ generated site, based on the medius_ theme.

.. code-block:: bash

    # You need to fetch medius
    git submodule init
    git submodule update
    # virtualenv is highly recommended
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Regenerate, serve, and sync the site to my server with:

.. code-block:: bash

    make regenerate
    make serve
    make rsync_upload

Moreover, autoenv_ is really fun. Use it!

Deployment
----------

I'm using Codeship_ to deploy. Use the followin setup commands:

.. code-block:: bash

    # Replace default virtualenv with python3
    rm -rf ${HOME}/.virtualenv
    virtualenv -p $(which python3) "${HOME}/.virtualenv"
    pip install -r requirements.txt

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
.. _medius: https://github.com/onur/medius
.. _autoenv: https://github.com/horosgrisa/autoenv
.. _Codeship: https://codeship.com
