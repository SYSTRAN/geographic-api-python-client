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

# import models into model package
from .boundaries import Boundaries
from .full_position import FullPosition
from .position import Position
from .poi_address_components import POIAddressComponents
from .poi_address import POIAddress
from .address_components import AddressComponents
from .address import Address
from .lite_location import LiteLocation
from .full_poi_location import FullPOILocation
from .full_location import FullLocation
from .opening_dates import OpeningDates
from .phone_number import PhoneNumber
from .mail import Mail
from .contact import Contact
from .opening_hours import OpeningHours
from .photo import Photo
from .video import Video
from .description import Description
from .review import Review
from .booking import Booking
from .lite_poi import LitePOI
from .full_poi import FullPOI
from .destination import Destination
from .full_destination import FullDestination
from .chapter import Chapter
from .inspiration import Inspiration
from .full_inspiration import FullInspiration
from .poi_response import PoiResponse
from .destination_response import DestinationResponse
from .inspiration_response import InspirationResponse
from .poi_details_response import PoiDetailsResponse
from .poi_types_response import PoiTypesResponse
from .destination_details_response import DestinationDetailsResponse
from .inspiration_details_response import InspirationDetailsResponse
from .supported_languages_response import SupportedLanguagesResponse
from .api_version_response import ApiVersionResponse
from .error_response import ErrorResponse

