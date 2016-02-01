#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class InspirationsApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def geographic_inspirations_dossiers_list_get(self, **kwargs):
        """
        List dossiers
        Get a list of `Inspirations` of type `dossier`.\n\nThe main criteria can be:\n* a position and a radius\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location. Musts be used together with `longitude` and `radius` parameters. 
        :param float longitude: Longitude location. Musts be used together with `latitude` and `radius` parameters. 
        :param float radius: Radius in meters. Musts be used together with `latitude` and `longitude` parameters. 
        :param str address: Address 
        :param str country: Country 
        :param str state: State 
        :param str county: County 
        :param str city: City 
        :param str postal_code: Postal Code 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'address', 'country', 'state', 'county', 'city', 'postal_code', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_dossiers_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/dossiers/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'address' in params:
            query_params['address'] = params['address']
        
        if 'country' in params:
            query_params['country'] = params['country']
        
        if 'state' in params:
            query_params['state'] = params['state']
        
        if 'county' in params:
            query_params['county'] = params['county']
        
        if 'city' in params:
            query_params['city'] = params['city']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'offset' in params:
            query_params['offset'] = params['offset']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_inspirations_events_list_get(self, **kwargs):
        """
        List events
        Get a list of `Inspirations` of type `event`.\n\nThe main criteria can be:\n* a position and a radius\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location. Musts be used together with `longitude` and `radius` parameters. 
        :param float longitude: Longitude location. Musts be used together with `latitude` and `radius` parameters. 
        :param float radius: Radius in meters. Musts be used together with `latitude` and `longitude` parameters. 
        :param str address: Address 
        :param str country: Country 
        :param str state: State 
        :param str county: County 
        :param str city: City 
        :param str postal_code: Postal Code 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'address', 'country', 'state', 'county', 'city', 'postal_code', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_events_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/events/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'address' in params:
            query_params['address'] = params['address']
        
        if 'country' in params:
            query_params['country'] = params['country']
        
        if 'state' in params:
            query_params['state'] = params['state']
        
        if 'county' in params:
            query_params['county'] = params['county']
        
        if 'city' in params:
            query_params['city'] = params['city']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'offset' in params:
            query_params['offset'] = params['offset']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_inspirations_get_get(self, id, **kwargs):
        """
        Get a specific Inspiration
        Get a specific `Inspiration`.

        :param str id: Inspiration identifier (required)
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationDetailsResponse
        """
        
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `geographic_inspirations_get_get`")
        
        all_params = ['id', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_get_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/get'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'id' in params:
            query_params['id'] = params['id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationDetailsResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_inspirations_list_get(self, **kwargs):
        """
        List Inspirations
        Get a list of `Inspirations`.\n\nThe main criteria can be:\n* a position and a radius\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location. Musts be used together with `longitude` and `radius` parameters. 
        :param float longitude: Longitude location. Musts be used together with `latitude` and `radius` parameters. 
        :param float radius: Radius in meters. Musts be used together with `latitude` and `longitude` parameters. 
        :param str address: Address 
        :param str country: Country 
        :param str state: State 
        :param str county: County 
        :param str city: City 
        :param str postal_code: Postal Code 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'address', 'country', 'state', 'county', 'city', 'postal_code', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'address' in params:
            query_params['address'] = params['address']
        
        if 'country' in params:
            query_params['country'] = params['country']
        
        if 'state' in params:
            query_params['state'] = params['state']
        
        if 'county' in params:
            query_params['county'] = params['county']
        
        if 'city' in params:
            query_params['city'] = params['city']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'offset' in params:
            query_params['offset'] = params['offset']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_inspirations_news_in_brief_list_get(self, **kwargs):
        """
        List news in brief
        Get a list of `Inspirations` of type `news in brief`.\n\nThe main criteria can be:\n* a position and a radius\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location. Musts be used together with `longitude` and `radius` parameters. 
        :param float longitude: Longitude location. Musts be used together with `latitude` and `radius` parameters. 
        :param float radius: Radius in meters. Musts be used together with `latitude` and `longitude` parameters. 
        :param str address: Address 
        :param str country: Country 
        :param str state: State 
        :param str county: County 
        :param str city: City 
        :param str postal_code: Postal Code 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'address', 'country', 'state', 'county', 'city', 'postal_code', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_news_in_brief_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/newsInBrief/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'address' in params:
            query_params['address'] = params['address']
        
        if 'country' in params:
            query_params['country'] = params['country']
        
        if 'state' in params:
            query_params['state'] = params['state']
        
        if 'county' in params:
            query_params['county'] = params['county']
        
        if 'city' in params:
            query_params['city'] = params['city']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'offset' in params:
            query_params['offset'] = params['offset']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_inspirations_slide_shows_list_get(self, **kwargs):
        """
        List slide shows
        Get a list of `Inspirations` of type `slide show`.\n\nThe main criteria can be:\n* a position and a radius\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location. Musts be used together with `longitude` and `radius` parameters. 
        :param float longitude: Longitude location. Musts be used together with `latitude` and `radius` parameters. 
        :param float radius: Radius in meters. Musts be used together with `latitude` and `longitude` parameters. 
        :param str address: Address 
        :param str country: Country 
        :param str state: State 
        :param str county: County 
        :param str city: City 
        :param str postal_code: Postal Code 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'address', 'country', 'state', 'county', 'city', 'postal_code', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_slide_shows_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/slideShows/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'address' in params:
            query_params['address'] = params['address']
        
        if 'country' in params:
            query_params['country'] = params['country']
        
        if 'state' in params:
            query_params['state'] = params['state']
        
        if 'county' in params:
            query_params['county'] = params['county']
        
        if 'city' in params:
            query_params['city'] = params['city']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'offset' in params:
            query_params['offset'] = params['offset']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_inspirations_tests_list_get(self, **kwargs):
        """
        List tests
        Get a list of `Inspirations` of type `test`.\n\nThe main criteria can be:\n* a position and a radius\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location. Musts be used together with `longitude` and `radius` parameters. 
        :param float longitude: Longitude location. Musts be used together with `latitude` and `radius` parameters. 
        :param float radius: Radius in meters. Musts be used together with `latitude` and `longitude` parameters. 
        :param str address: Address 
        :param str country: Country 
        :param str state: State 
        :param str county: County 
        :param str city: City 
        :param str postal_code: Postal Code 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: InspirationResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'address', 'country', 'state', 'county', 'city', 'postal_code', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_inspirations_tests_list_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/inspirations/tests/list'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'address' in params:
            query_params['address'] = params['address']
        
        if 'country' in params:
            query_params['country'] = params['country']
        
        if 'state' in params:
            query_params['state'] = params['state']
        
        if 'county' in params:
            query_params['county'] = params['county']
        
        if 'city' in params:
            query_params['city'] = params['city']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'limit' in params:
            query_params['limit'] = params['limit']
        
        if 'offset' in params:
            query_params['offset'] = params['offset']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='InspirationResponse', auth_settings=auth_settings)
        
        return response
        









