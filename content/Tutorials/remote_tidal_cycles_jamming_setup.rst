Remote TidalCycles jamming setup
################################
:date: 2020-09-18 00:00
:author: Tom Gurion
:tags: live coding,network,hack
:slug: remote-tidal-cycles-jamming-setup
:description: Getting ready for the 2nd wave and setting up TidalCycles for remote jamming w/ digital selves.

.. image:: https://upload.wikimedia.org/wikipedia/commons/8/80/TidalCycles_identity.svg
  :alt: TidalCycles logo
  :width: 100%

`TidalCycles <https://tidalcycles.org/i>`_ (tidal in short) is a live coding language for music performance / composition.
I don't use it myself but been playing with a live coder, Lizzie, AKA `digital selves <https://lwlsn.github.io/digitalselves-web/>`_, for the last year and a half.
Check her out!
With a COVID 2nd wave around the corner we decided to search for a solution for remote jamming together.
This blog post is a summary of what seems to work.
It's written mainly as a documentation for Lizzie and self.
Hopefully others will find it useful as well.

So, what we want to achieve?
We want Lizzie to run tidal code on her laptop and having the audio generated on my laptop at the other side of town.
The clock to sync my hardware synth will be generated with the audio.
So, audio-wise, both Lizzie's output and my hardware synth will generate locally on my side, fully in sync.

How do we plan to do it?
Tidal uses a client / server architecture with the tidal haskell library as the client and SuperCollider (SC) running the audio as the server.
Communication is done over UDP on port 57120 by default.
Our idea is to route the messages from tidal, through a server, to my machine, which runs the SC server.
With such a solution there won't be any need to change anything around tidal, nor around SC, just set up the network properly.

On to the nitty gritty details - forwarding UDP messages between two local machines
-----------------------------------------------------------------------------------

Prepare the server
==================

For a server we created a droplet on `digital ocean <https://digitalocean.com/>`_.
There's almost no setup for the droplet, so we can create one for jamming and delete it later to keep the cost low.

The only configuration needed on the server is to change the SSH settings on the server to allow forwarded ports to bind to the wildcard address (meaning that the address will be publicly accessible).

Edit ``/etc/ssh/sshd_config`` and add:

.. code::

  GatewayPorts yes

Now reload the SSH settings on the server with

.. code::

  systemctl reload ssh.service

Creating an SSH reverse tunnel from the server to the laptop running SC
=======================================================================

SSH tunnelling doesn't support UDP, so we'll create a tunnel for TCP and convert the UDP messages sent by tidal to TCP on one machine, and back to UDP on the other machine.

On the machine that runs SC run

.. code::

  ssh -R 12345:localhost:12345 root@SERVER_IP

The port doesn't really matter, 12345 is used here for convenience.

Converting TCP messages back to UDP on the laptop running SC
============================================================

.. code::

  socat TCP-LISTEN:12345,fork UDP4:localhost:57120

Sending the UDP messages from the laptop running tidal to the server
====================================================================

.. code::

  socat UDP-LISTEN:57120,fork TCP4:SERVER_IP:12345

That's it!
==========

Spin up tidal on one side, SC on the other side, put some patterns in and it should work.

Advice on testing things locally
--------------------------------

If you want to test things on a single computer make sure to change the port SC is listening to.
Otherwise you are trying to use the same port twice: once listening to tidal and sending the messages to the server, and again listening to the messages coming from the server.
To do so, start the SuperDirt synth in SC as follows:

.. code::

  SuperDirt.start(port: 57121)

You'll also have to change the port that the TCP stream is converted to, so replace


.. code::

  socat TCP-LISTEN:12345,fork UDP4:localhost:57120

with

.. code::

  socat TCP-LISTEN:12345,fork UDP4:localhost:57121

**Enjoy jamming and keep safe!**
