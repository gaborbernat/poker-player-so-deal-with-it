import json
import time
import unittest
import urllib2

__author__ = 'bnc'

class RemoteConfig(object):
    lastLoaded = None
    config = None
    reloadTime = 5

    def __init__(self, configUrl):
        self.configUrl = configUrl

    def get(self, key, defaultValue):
        self._load()

        if self.config.has_key(key):
            return self.config[key]

        return defaultValue

    def _load(self):
        currentTime = time.time()
        if self.config == None or self.lastLoaded == None or currentTime - self.lastLoaded > self.reloadTime:
            self.config = json.loads(urllib2.urlopen(self.configUrl, timeout=1.5).read())
            self.lastLoaded = currentTime
            self.reloadTime = self.get('reload_time', self.reloadTime)


class TestRemoteConfig(unittest.TestCase):
    def setUp(self):
        self.config = RemoteConfig("https://dl.dropboxusercontent.com/u/819938/leanpoker/test_config.json")

    def test_config(self):
        startTime = time.time()
        self.assertEqual(True, self.config.get('test_bool', None))
        self.assertEqual(1234, self.config.get('test_int', None))
        self.assertEqual('test value', self.config.get('test_str', None))
        endTime = time.time()

        self.assertLess(endTime - startTime, 0.8)


config = RemoteConfig("https://dl.dropboxusercontent.com/u/819938/leanpoker/config.json")
