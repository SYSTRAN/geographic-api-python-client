#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import src
import src.configuration

class InspirationsApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        src.configuration.load_api_key(api_key_file)
        self.api_client = src.ApiClient()
        self.inspirations_api = src.InspirationsApi(self.api_client)

    def test_geographic_inspirations_get(self):
        result = self.inspirations_api.geographic_inspirations_get()
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()


