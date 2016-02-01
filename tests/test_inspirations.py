#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systranGeographicApi
import systranGeographicApi.configuration

class InspirationsApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systranGeographicApi.configuration.load_api_key(api_key_file)
        self.api_client = systranGeographicApi.ApiClient()
        self.inspirations_api = systranGeographicApi.InspirationsApi(self.api_client)

    def test_geographic_inspirations_list_get(self):
        result = self.inspirations_api.geographic_inspirations_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_inspirations_dossiers_list_get(self):
        result = self.inspirations_api.geographic_inspirations_dossiers_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_inspirations_events_list_get(self):
        result = self.inspirations_api.geographic_inspirations_events_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_inspirations_get_get(self):
        id = "56600afb14c46414e0275eb3"
        print 'Use a valid "id" and uncomment below codes to test'
        # result = self.inspirations_api.geographic_inspirations_get_get(id=id)
        # self.assertIsNotNone(result)
        # print result.__repr__()

    def test_geographic_inspirations_news_in_brief_list_get(self):
        result = self.inspirations_api.geographic_inspirations_news_in_brief_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_inspirations_slide_shows_list_get(self):
        result = self.inspirations_api.geographic_inspirations_slide_shows_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_geographic_inspirations_tests_list_get(self):
        result = self.inspirations_api.geographic_inspirations_tests_list_get()
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()


