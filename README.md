# simple.redisgeo

Sample implementation of Redis Geo commands to store user specific location data i.e. last place a user visited in Redis, and support Geolocation query that fetches all the users within a certain radius.

Requirements
------------------------

Redis Geo commands are only available since 3.2.0. Make sure you have Redis 3.2.0 or later installed.

We used redis-py package as Python interface to the Redis. It also supported Redis Geo commands but you have to install from source to get latest updates.

    $ git clone https://github.com/andymccurdy/redis-py.git
    $ cd redis-py/
    $ python setup.py install

Installation
-------------------------

Install from source

    $ git clone ttps://github.com/vietdt/simple.redisgeo.git
    $ cd simple.redisgeo/
    $ python setup.py install

Run tests

    $ python setup.py test

Getting Started
------------------------

Add a last user's visited place

    >>> import redis
    >>> from simple.redisgeo.location import User
    >>> conn = redis.Redis()

    >>> User.addLastVisitedPlace(conn, 40.7648057, -73.9733487, 'user1')
    1

Search for nearby users within a certain radius

    >>> User.getNearbyVistors(conn, 40.7598464, -73.9798091, 3, 'km')
    ['user1']


