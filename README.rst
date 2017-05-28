HAUM's Twitter microservice
===========================

.. image:: https://travis-ci.org/haum/hms_twitter.svg?branch=master
    :target: https://travis-ci.org/haum/hms_twitter

.. image:: https://coveralls.io/repos/github/haum/hms_twitter/badge.svg?branch=master
    :target: https://coveralls.io/github/haum/hms_twitter?branch=master

A microservice that handles twitter interaction.

IRC commands
------------
 * !spacestatus : displays the state's space
 * !spacestatus help : displays the commands
 * !spacestatus open : open the space and tweet it
 * !spacestatus open_silent : open the space without tweeting
 * !spacestatus close : close the space and tweet it
 * !spacestatus close_silent : close the space without tweeting
 * !spacestatus toggle : change the space's state and tweet it
 * !spacestatus toggle_silent : change the space's state without tweeting


Using
-----

Create a Python 3 virtualenv and install software::

    $ virtualenv -ppython3 venv
    $ source venv/bin/activate
    (venv) $ pip install .

Then start the daemon inside the virtual env::

    $ hms_twitter

License
-------

This project is brought to you under MIT license. For further information,
please read the provided ``LICENSE.txt`` file.
