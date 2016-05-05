Web Audio API - some thoughts and experiments
#############################################
:date: 2015-12-17 12:47
:author: Tom Gurion
:tags: javascript, python, tornado, web, web audio API
:slug: web-audio-api-some-thoughts-and-experiments

For me, being able to use advance audio programming on the web looks
like a dream just a couple of weeks ago, and I'm not the only one for
sure.
Doing audio programming, I've mainly experienced with Max/MSP and Pd
but my interest in shared music creation / consumption and interactive
systems have long seems to demand the extension of this skill set; as
Udi Oron rightly argued in
"`Hackita <http://tomgurion.blogspot.co.il/2013/12/hackita.html>`__\ "
two months ago: you have no chance to convince someone to download your
desktop app (Max or Pd patches for example), give them a web app
instead!
I'm not sure if I've heard of the `Web Audio
API <http://www.w3.org/TR/webaudio/>`__ before last week, but even if I
did I probably wouldn't had a clue of how to use it back then (before
learning web development and JavaScript at Hackita). Today I can say
that it looks like a great solution for audio programming, and a good
way to look for if you interesting in designing systems for public wide
usage because of the next reasons:

-  As claimed before, no one downloads and install desktop application
   anymore unless it came from known source and the one that download it
   knows for sure that he wants to use it (as opposed to just trying
   things out).
-  It's probably the easiest way to go if you want shared behavior and
   interaction between users of the system.
-  Web standards are here to stay. You can be sure that organizations
   like Google, Mozilla, and Microsoft will compete to provide the best
   implementation possible.
-  The API itself looks very promising. I hope that I will be able to
   summarize pros and cons soon.

.. raw:: html

   <div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

|image0|

.. raw:: html

   </div>

That's being said, `here <http://web-audio.nagasaki45.com/>`__ are my
experiment with the API. If you are interesting in more information and
tutorials be sure to take a look at the "Useful links" menu (top
navigation bar). And as always, source code can be found at
`github <https://github.com/Nagasaki45/Web-Audio>`__.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. |image0| image:: http://2.bp.blogspot.com/-KZi_5wGhqSs/Uv5p85iWcwI/AAAAAAAAOPQ/-AmGHb1TnEc/s1600/web-audio+screen.png
   :target: http://web-audio.herokuapp.com/
