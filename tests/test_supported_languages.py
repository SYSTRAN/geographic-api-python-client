#!/usr/bin/env python
# coding: utf-8

import os
import unittest

import systran_geographic_api
import systran_geographic_api.configuration

class SupportedLanguagesApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systran_geographic_api.configuration.load_api_key(api_key_file)
        self.api_client = systran_geographic_api.ApiClient()
        self.supported_languages_api = systran_geographic_api.SupportedLanguagesApi(self.api_client)

    def test_geographic_supported_languages_get(self):
        result = self.supported_languages_api.geographic_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

if __name__ == '__main__':
    unittest.main()


