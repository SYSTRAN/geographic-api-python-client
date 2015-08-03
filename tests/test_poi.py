#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import src
import src.configuration

class PoiApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        src.configuration.load_api_key(api_key_file)
        self.api_client = src.ApiClient()
        self.poi_api = src.PoiApi(self.api_client)

    def test_geographic_poi_supported_languages_get(self):
        result = self.poi_api.geographic_poi_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_get(self):
        result = self.poi_api.geographic_poi_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_get_with_parameters(self):
        lat = 47.219510
        lng = -1.553694
        radius = 1000
        result = self.poi_api.geographic_poi_get(latitude=lat, longitude=lng, radius=radius)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_get_with_limit(self):
        lat = 47.219510
        lng = -1.553694
        radius = 1000
        limit = 10
        result = self.poi_api.geographic_poi_get(latitude=lat, longitude=lng, radius=radius, limit=limit)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_get_with_name(self):
        lat = 47.219510
        lng = -1.553694
        radius = 1000
        name = ["OUEST INFO", "RHUMS ET COCKTAILS", "LES SENTIERS DE DAKAR"]
        result = self.poi_api.geographic_poi_get(latitude=lat, longitude=lng, radius=radius, name=name)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_get_with_filter(self):
        lat = 47.219510
        lng = -1.553694
        radius = 1000
        filter = "OUEST INFO"
        result = self.poi_api.geographic_poi_get(latitude=lat, longitude=lng, radius=radius, filter=filter)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_details_get(self):
        id = "556eb3c9d61c8170d8cd6410"
        result = self.poi_api.geographic_poi_details_get(id=id)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_types_get(self):
        result = self.poi_api.geographic_poi_types_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_poi_events_get(self):
        result = self.poi_api.geographic_poi_events_get()
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()


