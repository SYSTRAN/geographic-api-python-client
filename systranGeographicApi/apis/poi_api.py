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

class PoiApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def geographic_poi_get(self, **kwargs):
        """
        Get Point of interests\n
        Get `Point of interests`.\n\nThe main criteria can be:\n* a position and a radius\n* a bounding box\n* a textual search\n\nAdditional critera can be added.\n

        :param float latitude: Latitude location 
        :param float longitude: Longitude location 
        :param float radius: Radius in meters 
        :param float maximum_latitude: Latitude of the top (northernmost) side of the bounding box 
        :param float maximum_longitude: Longitude of the right (easternmost) side of the bounding box 
        :param float minimum_latitude: Latitude of the bottom (southernmost) side of the bounding box 
        :param float minimum_longitude: Longitude of the left (westernmost) side of the bounding box 
        :param list[str] filter: Filter on all relevent POI data (name, type, address, ...) 
        :param list[str] name: POI name 
        :param str main_type: POI main type 
        :param list[str] type: POI type 
        :param str address: POI address 
        :param str country: POI country 
        :param str state: POI state 
        :param str county: POI county 
        :param str city: POI city 
        :param str district: POI district 
        :param str postal_code: POI postalCode 
        :param str street: POI street 
        :param str house: POI house 
        :param str rank_by: Ranking criteria 
        :param bool open_now: Only open for business POI 
        :param int minimum_rating: Minimum rating 
        :param int maximum_rating: Maximum rating 
        :param int minimum_price: Minumum price 
        :param int maximum_price: Maximum price 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: PoiResponse
        """
        
        all_params = ['latitude', 'longitude', 'radius', 'maximum_latitude', 'maximum_longitude', 'minimum_latitude', 'minimum_longitude', 'filter', 'name', 'main_type', 'type', 'address', 'country', 'state', 'county', 'city', 'district', 'postal_code', 'street', 'house', 'rank_by', 'open_now', 'minimum_rating', 'maximum_rating', 'minimum_price', 'maximum_price', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_poi_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/poi'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'maximum_latitude' in params:
            query_params['maximumLatitude'] = params['maximum_latitude']
        
        if 'maximum_longitude' in params:
            query_params['maximumLongitude'] = params['maximum_longitude']
        
        if 'minimum_latitude' in params:
            query_params['minimumLatitude'] = params['minimum_latitude']
        
        if 'minimum_longitude' in params:
            query_params['minimumLongitude'] = params['minimum_longitude']
        
        if 'filter' in params:
            query_params['filter'] = params['filter']
        
        if 'name' in params:
            query_params['name'] = params['name']
        
        if 'main_type' in params:
            query_params['mainType'] = params['main_type']
        
        if 'type' in params:
            query_params['type'] = params['type']
        
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
        
        if 'district' in params:
            query_params['district'] = params['district']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'street' in params:
            query_params['street'] = params['street']
        
        if 'house' in params:
            query_params['house'] = params['house']
        
        if 'rank_by' in params:
            query_params['rankBy'] = params['rank_by']
        
        if 'open_now' in params:
            query_params['openNow'] = params['open_now']
        
        if 'minimum_rating' in params:
            query_params['minimumRating'] = params['minimum_rating']
        
        if 'maximum_rating' in params:
            query_params['maximumRating'] = params['maximum_rating']
        
        if 'minimum_price' in params:
            query_params['minimumPrice'] = params['minimum_price']
        
        if 'maximum_price' in params:
            query_params['maximumPrice'] = params['maximum_price']
        
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
                                            response='PoiResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_poi_details_get(self, id, **kwargs):
        """
        Get Point of interest details
        Get `Point of interest` details.

        :param str id: POI identifier (required)
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: PoiDetailsResponse
        """
        
        # verify the required parameter 'id' is set
        if id is None:
            raise ValueError("Missing the required parameter `id` when calling `geographic_poi_details_get`")
        
        all_params = ['id', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_poi_details_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/poi/details'.replace('{format}', 'json')
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
                                            response='PoiDetailsResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_poi_events_get(self, **kwargs):
        """
        Get Events\n
        Get `Events`.\n\nThe main criteria can be:\n* opening dates\n* a position and a radius\n* a bounding box\n* a textual search\n\nAdditional critera can be added.\n

        :param datetime date: Date at which events are available 
        :param datetime begin_date: Date corresponding to the begining of the period where events are available 
        :param datetime end_date: Date corresponding to the end of the period where events are available 
        :param float latitude: Latitude location 
        :param float longitude: Longitude location 
        :param float radius: Radius in meters 
        :param float maximum_latitude: Latitude of the top (northernmost) side of the bounding box 
        :param float maximum_longitude: Longitude of the right (easternmost) side of the bounding box 
        :param float minimum_latitude: Latitude of the bottom (southernmost) side of the bounding box 
        :param float minimum_longitude: Longitude of the left (westernmost) side of the bounding box 
        :param list[str] filter: Filter on all relevent POI data (name, type, address, ...) 
        :param list[str] name: POI name 
        :param str main_type: POI main type 
        :param list[str] type: POI type 
        :param str address: POI address 
        :param str country: POI country 
        :param str state: POI state 
        :param str county: POI county 
        :param str city: POI city 
        :param str district: POI district 
        :param str postal_code: POI postal code 
        :param str street: POI street 
        :param str house: POI house 
        :param str rank_by: Ranking criteria 
        :param bool open_now: Only open for business POI 
        :param int minimum_rating: Minimum rating 
        :param int maximum_rating: Maximum rating 
        :param int minimum_price: Minumum price 
        :param int maximum_price: Maximum price 
        :param int limit: Pagination limit 
        :param int offset: Pagination offset 
        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: EventsResponse
        """
        
        all_params = ['date', 'begin_date', 'end_date', 'latitude', 'longitude', 'radius', 'maximum_latitude', 'maximum_longitude', 'minimum_latitude', 'minimum_longitude', 'filter', 'name', 'main_type', 'type', 'address', 'country', 'state', 'county', 'city', 'district', 'postal_code', 'street', 'house', 'rank_by', 'open_now', 'minimum_rating', 'maximum_rating', 'minimum_price', 'maximum_price', 'limit', 'offset', 'accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_poi_events_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/poi/events'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'date' in params:
            query_params['date'] = params['date']
        
        if 'begin_date' in params:
            query_params['beginDate'] = params['begin_date']
        
        if 'end_date' in params:
            query_params['endDate'] = params['end_date']
        
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        
        if 'radius' in params:
            query_params['radius'] = params['radius']
        
        if 'maximum_latitude' in params:
            query_params['maximumLatitude'] = params['maximum_latitude']
        
        if 'maximum_longitude' in params:
            query_params['maximumLongitude'] = params['maximum_longitude']
        
        if 'minimum_latitude' in params:
            query_params['minimumLatitude'] = params['minimum_latitude']
        
        if 'minimum_longitude' in params:
            query_params['minimumLongitude'] = params['minimum_longitude']
        
        if 'filter' in params:
            query_params['filter'] = params['filter']
        
        if 'name' in params:
            query_params['name'] = params['name']
        
        if 'main_type' in params:
            query_params['mainType'] = params['main_type']
        
        if 'type' in params:
            query_params['type'] = params['type']
        
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
        
        if 'district' in params:
            query_params['district'] = params['district']
        
        if 'postal_code' in params:
            query_params['postalCode'] = params['postal_code']
        
        if 'street' in params:
            query_params['street'] = params['street']
        
        if 'house' in params:
            query_params['house'] = params['house']
        
        if 'rank_by' in params:
            query_params['rankBy'] = params['rank_by']
        
        if 'open_now' in params:
            query_params['openNow'] = params['open_now']
        
        if 'minimum_rating' in params:
            query_params['minimumRating'] = params['minimum_rating']
        
        if 'maximum_rating' in params:
            query_params['maximumRating'] = params['maximum_rating']
        
        if 'minimum_price' in params:
            query_params['minimumPrice'] = params['minimum_price']
        
        if 'maximum_price' in params:
            query_params['maximumPrice'] = params['maximum_price']
        
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
                                            response='EventsResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_poi_supported_languages_get(self, **kwargs):
        """
        Supported Languages
        List of languages in which POI can be localized.

        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SupportedLanguagesResponse
        """
        
        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_poi_supported_languages_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/poi/supportedLanguages'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
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
                                            response='SupportedLanguagesResponse', auth_settings=auth_settings)
        
        return response
        
    def geographic_poi_types_get(self, **kwargs):
        """
        Get available Point of interest types
        Get available `Point of interest` types.

        :param str accept_language: Preferred languages for response localization.\n\nSee [Accept-Language header specification for HTTP\n1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4)\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: PoiTypesResponse
        """
        
        all_params = ['accept_language', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method geographic_poi_types_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/geographic/poi/types'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
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
                                            response='PoiTypesResponse', auth_settings=auth_settings)
        
        return response
        









