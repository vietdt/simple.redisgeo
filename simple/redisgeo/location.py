# -*- coding: utf-8 -*-

class User(object):
    """
    Wrapper for a user location object
    """

    LAST_VISITED_INDEX = 'user_last_visited_place'

    @classmethod
    def addLastVisitedPlace(cls, redisConn, *values):
        """
        Insert location's latitude, longitude and userid into redis geo index
        """
        return redisConn.geoadd(cls.LAST_VISITED_INDEX, *values)

    @classmethod
    def getNearbyVistors(cls, redisConn, lat, lon, radius, unit=None):
        """
        Return a list of user ids nearby a location within a radius.
        The units must be one of the following : m, km mi, ft
        """
        return redisConn.georadius(cls.LAST_VISITED_INDEX, lat, lon, radius, unit)
