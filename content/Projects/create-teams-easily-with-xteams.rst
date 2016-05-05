Create teams easily with Xteams!
################################
:date: 2015-05-22 20:40
:author: Tom Gurion
:tags: django, python, web
:slug: create-teams-easily-with-xteams

|image0|\ I've been playing volleyball recently with a group of
amateur players. In the last two months the size of our group has
increased so much that it became very hard to create teams. And if you
think that size is the only issue I can assure you that there are many
more:
- How can one create teams when Dana doesn't want to play with Haim,
who must play with Jacob but not with Yossi... You've got the idea.
- No one will ever want to help in creating teams as he may end up
insulting a not-so-good player by choosing him last.
- Maybe you have too many players around for one game, but just enough
for a tournament of 4 teams.
In order to solve these inconveniences I've created
`Xteams! <http://xteams.herokuapp.com/>`__ a web-app with one goal in
mind:

.. raw:: html

   <div style="text-align: center;">

***Create teams automatically based on discrete scores of the players***

.. raw:: html

   </div>


Using Xteams, group managers can give scores to players in the
management panel. Players of the group can't access this panel but can
see the list of players, mark which of them arrived to the game and
create teams easily.
At the time of writing, the algorithm behind the teams' allocation was
pretty simple. It takes all of the available players, and the number of
teams to create, and tries to find teams with equal or close to equal
strength (sum of the players scores) by generating several random
allocations and choosing the best of them.

For devs
^^^^^^^^

The app is still under development (aren't they all?), and many more
modifications, improvements and features are considered. Any help in the
development process is more than welcome (`github
repo <https://github.com/Nagasaki45/Xteams>`__).

Thanks
^^^^^^

To the players of Nahlaot Veshut volleyball team, who consistently help
with new ideas for features and additional improvements.

.. raw:: html

   </p>

.. |image0| image:: http://4.bp.blogspot.com/-8SH4bkEX0_0/VBcgI0EiKtI/AAAAAAAAQBg/lsCvWbhdkn4/s1600/volley_edit.jpg
   :target: http://4.bp.blogspot.com/-8SH4bkEX0_0/VBcgI0EiKtI/AAAAAAAAQBg/lsCvWbhdkn4/s1600/volley_edit.jpg
