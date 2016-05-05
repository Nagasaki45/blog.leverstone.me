My Jupyter (tmpnb) server and Thebe
###################################
:date: 2015-09-20 19:42
:author: Tom Gurion
:tags: data analysis, jupyter, python, scientific computing, web
:slug: my-jupyter-tmpnb-server-and-thebe

.. raw:: html

   <p>

.. raw:: html

   <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>

.. raw:: html

   <script charset="utf-8" src="https://rawgit.com/oreillymedia/thebe/master/static/main-built.js" type="text/javascript"></script>

.. raw:: html

   <script>    $(function(){         new Thebe({             url: "https://oreillyorchard.com:8000/",             debug: true         });     }); </script>



::

    %matplotlib inlineimport matplotlib.pyplot as pltimport numpy as npfrom IPython.html.widgets import interactdef plot_sine(frequency=1.0, amplitude=1.0):    plt.ylim(-1.0, 1.0);    x = np.linspace(0, 10, 1000)    plt.plot(x, amplitude*np.sin(x*frequency));interact(plot_sine, frequency=(0.5, 10.0), amplitude=(0.0, 1.0));


Isn't that amazing?!?
I've recently installed an
`tmpnb <https://github.com/jupyter/tmpnb>`__ sever on my digitalocean
server, you can access it at nagasaki45.com:8000.
So, what's the big deal?
This configuration allow anyone to use python (or one of the other
supported / installed kernels) on the web, using my server. You don't
have to ask for permission; you can just go to the provided address and
start to code without any local installation.
And it goes way beyond:

-  You can open new terminal, 'git clone' your project, and demonstrate
   it to someone else. And you can do it on mobile devices too. Again,
   no installation required, everything is running on the server.
-  You can use `thebe <https://github.com/oreillymedia/thebe>`__ to add
   code snippets as the one above to any static html page (your blog, as
   example). Even interactive widgets will run the computation back and
   fourth from the server to the web frontend for presentation.

So go ahead, write some code, let me execute it for you ;-)

::

    # your python playground 



Edit 1.9.15:
~~~~~~~~~~~~

My digitalocean VM has "only" 512MB of RAM. I decided to span tmpnb
with 4 docker containers, 50MB RAM each, to keep the server load on
minimum. Apparently, it possessed some issues as 50MB are probably not
enough.
Right now the example above uses the same tmpnb server has the one in
thebe example
(`here <https://oreillymedia.github.io/thebe/examples/matplotlib.html>`__),
namely https://oreillyorchard.com:8000/. It works much better now as
there are no kernal failures when running the examples.

Edit 20.9.15:
~~~~~~~~~~~~~

I'm stopping the service on my server due to some number crunching tasks
I'm running on it.

.. raw:: html

   </p>

