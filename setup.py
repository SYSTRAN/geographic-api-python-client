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

import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi"]

setup(
    name="geographic-api-python-client",
    version="1.0.1",
    description="REST Geographic API",
    author_email="",
    url="",
    keywords=["Systran", "REST Geographic API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ### Introduction\n\nREST API to retrieve geographic point of interests.\n\n### Cross Domain\n\nGeographic API supports cross-domain requests through the JSONP or the CORS mechanism.\n\nGeographic API also supports the Silverlight client access policy file\n(clientaccesspolicy.xml) and the Adobe Flash cross-domain policy file (crossdomain.xml) that handles cross-domain requests.\n\n#### JSONP Support\n\nGeographic API supports JSONP by providing the name of the callback function as a parameter. The response body will be contained in the parentheses:\n\n```javascript\ncallbackFunctionName(/* response body as defined in each API section */);\n```\n\nFor example, for a supportedLanguages call with the callback set to supportedLanguagesCallback, the response body will be similar to the following:\n\n```javascript\nsupportedLanguagesCallback({\n  \&quot;languages\&quot;: [\&quot;en\&quot;, \&quot;fr\&quot;]\n});\n```\n\n#### CORS\n\nGeographic API supports the CORS mechanism to handle cross-domain requests. The server will correctly handle the OPTIONS requests used by CORS.\n\nThe following headers are set as follows:\n\n```\nAccess-Control-Allow-Origin: *\nAccess-Control-Allow-Headers: X-Requested-With,Content-Type,X-HTTP-METHOD-OVERRIDE\n    ```\n\n\n### Escaping of the input text\n\nThe input text passed as a URL parameter will be escaped with an equivalent of the javascript &#39;encodeURIComponent&#39; function.\n\n### Encoding of the input text\n\nThe input text must be encoded in UTF-8.\n\n### Encoding of the output text\n\nThe output text will be encoded in UTF-8.\n\n### Mobile API keys\n\n** iOS **: If you use an iOS API key, you need to add the following parameter to each request:\n* `bundleId`: Your application bundle ID\n\n&lt;br /&gt;\n\n** Android **: If you use an Android API key, you need to add the following parameters to each request:\n* `packageName`: Your application package name\n* `certFingerprint`: Your application certificate fingerprint\n
    """
)










