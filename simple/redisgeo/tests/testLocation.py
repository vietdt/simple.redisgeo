import os
import unittest
import redis

from simple.redisgeo.location import User

class TestUserLocation(unittest.TestCase):

    def setUp(self):
        self.redisHost = os.getenv('TEST_REDIS_HOST', 'localhost')
        self.redisPort = int(os.getenv('TEST_REDIS_PORT', '6379'))
        self.redisDB = int(os.getenv('TEST_REDIS_DBNUMBER', '8'))
        self.redis = redis.Redis(self.redisHost, self.redisPort, self.redisDB)

    def test1_addLastVisitedPlaces(self):
        sample_places = (40.747533, -73.9454966, 'lic market',
                40.7648057, -73.9733487, "central park n/q/r",
                40.7362513, -73.9903085, "union square",
                40.7126674, -74.0131604, "wtc one",
                40.6428986, -73.7858139, "jfk",
                40.7498929, -73.9375699, "q4",
                40.7480973, -73.9564142, '4545',
                13.361389, 38.115556, "Palermo",
                15.087269, 37.502669, "Catania",
                )
        d = User.addLastVisitedPlace(self.redis, 43.6667, -79.4167, 'Toronto')
        d = User.addLastVisitedPlace(self.redis, *sample_places)
        self.assertGreater(d, -1)

    def test_getNearbyVistors(self):
        userids = User.getNearbyVistors(self.redis, 40.7598464, -73.9798091, 3, 'km')
        self.assertIn('4545', userids)


