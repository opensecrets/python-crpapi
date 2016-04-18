"""
	Python library for interacting with the CRP API.

    The CRP API (http://www.opensecrets.org/action/api_doc.php) provides campaign
	finance and other data from the Center for Responsive Politics.

	See README.rst for methods and usage
"""

__author__ = "James Turk (jturk@sunlightfoundation.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2009 Sunlight Labs"
__license__ = "BSD"

import urllib
import requests

class CRPApiError(Exception):
    """ Exception for CRP API errors """

# results #
class CRPApiObject(object):
    def __init__(self, d):
        self.__dict__ = d

# namespaces #

class CRP(object):

    apikey = None

    @staticmethod
    def _apicall(func, params):
        if CRP.apikey is None:
            raise CRPApiError('Missing CRP apikey')

        url = 'http://www.opensecrets.org/api/' \
            '?method=%s&output=json&apikey=%s&%s' % \
            (func, CRP.apikey, urllib.urlencode(params))

        print url

        try:
            response = requests.get(url)
            return response.json()['response']
        except requests.HTTPError, e:
            raise CRPApiError(e.read())
        except (ValueError, KeyError), e:
            raise CRPApiError('Invalid Response')

    class getLegislators(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('getLegislators', kwargs)['legislator']
            return results

    class memPFDprofile(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('memPFDprofile', kwargs)['member_profile']
            return results

    class candSummary(object):
        @staticmethod
        def get(**kwargs):
            result = CRP._apicall('candSummary', kwargs)['summary']
            return result['@attributes']

    class candContrib(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('candContrib', kwargs)['contributors']['contributor']
            return results

    class candIndustry(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('candIndustry', kwargs)['industries']['industry']
            return results

    class candSector(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('candSector', kwargs)['sectors']['sector']
            return results

    class candIndByInd(object):
        @staticmethod
        def get(**kwargs):
            result = CRP._apicall('CandIndByInd', kwargs)['candIndus']
            return result['@attributes']

    class getOrgs(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('getOrgs', kwargs)['organization']
            return results

    class orgSummary(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('orgSummary', kwargs)['organization']
            return results

    class congCmteIndus(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('congCmteIndus', kwargs)['committee']['member']
            return results

    class presCandContrib(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('prescandContrib', kwargs)
            return results

    class presCandIndustry(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('prescandIndustry', kwargs)
            return results

    class presCandSector(object):
        @staticmethod
        def get(**kwargs):
            results = CRP._apicall('prescandSector', kwargs)
            return results
