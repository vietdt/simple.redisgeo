# simple.redisgeo

Sample implementation of Redis Geo commands to store user specific location data i.e. last place a user visited in Redis, and support Geolocation query that fetches all the users within a certain radius.

Requirements
------------------------

Redis Geo commands are only available since 3.2.0. Make sure you have Redis 3.2.0 or later installed.

We used redis-py package as Python interface to the Redis. It also supported Redis Geo commands but you have to install from source to get latest updates.

    $ git clone https://github.com/andymccurdy/redis-py.git
    $ cd redis-py/
    $ python setup.py install


