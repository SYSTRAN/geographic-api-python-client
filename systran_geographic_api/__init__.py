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

# import models into sdk package
from .models.boundaries import Boundaries
from .models.full_position import FullPosition
from .models.position import Position
from .models.poi_address_components import POIAddressComponents
from .models.poi_address import POIAddress
from .models.address_components import AddressComponents
from .models.address import Address
from .models.lite_location import LiteLocation
from .models.full_poi_location import FullPOILocation
from .models.full_location import FullLocation
from .models.opening_dates import OpeningDates
from .models.phone_number import PhoneNumber
from .models.mail import Mail
from .models.contact import Contact
from .models.opening_hours import OpeningHours
from .models.photo import Photo
from .models.video import Video
from .models.description import Description
from .models.review import Review
from .models.booking import Booking
from .models.lite_poi import LitePOI
from .models.full_poi import FullPOI
from .models.destination import Destination
from .models.full_destination import FullDestination
from .models.chapter import Chapter
from .models.inspiration import Inspiration
from .models.full_inspiration import FullInspiration
from .models.poi_response import PoiResponse
from .models.destination_response import DestinationResponse
from .models.inspiration_response import InspirationResponse
from .models.poi_details_response import PoiDetailsResponse
from .models.poi_types_response import PoiTypesResponse
from .models.destination_details_response import DestinationDetailsResponse
from .models.inspiration_details_response import InspirationDetailsResponse
from .models.supported_languages_response import SupportedLanguagesResponse
from .models.api_version_response import ApiVersionResponse
from .models.error_response import ErrorResponse

# import apis into sdk package
from .apis.inspirations_api import InspirationsApi
from .apis.destinations_api import DestinationsApi
from .apis.supported_languages_api import SupportedLanguagesApi
from .apis.poi_api import PoiApi
from .apis.api_version_api import ApiVersionApi

# import ApiClient
from .api_client import ApiClient
