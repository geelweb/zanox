#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from base64 import b64encode
from time import gmtime, strftime, mktime
import urllib2, random, hmac, hashlib

class Client:
    """
    Zanox API client implementation
    """
    connectid = None
    secretkey = None

    zanoxurl = "http://api.zanox.com"
    protocol = "json"
    version  = "2011-03-01"

    def __init__(self, connectid=None, secretkey=None, version=None, protocol=None):
        """
        Init method

        :param connectid: Zanox connect ID
        :type connectid: string

        :param secretkey: Zanox secret key
        :type secretkey: string

        :param version: Zanox API version to use (default to "2011-03-01"
        :type version: string

        :param protocol: Zanox API protocol for returns
        :type protocol: string

        >>> c = Client()
        >>> print c.connectid
        None
        >>> print c.secretkey
        None
        >>> print c.version
        2011-03-01
        >>> print c.protocol
        json

        >>> c = Client(connectid= 'foo', secretkey = 'bar',
        ...     version = '2010-02-09', protocol='xml')
        >>> print c.connectid
        foo
        >>> print c.secretkey
        bar
        >>> print c.version
        2010-02-09
        >>> print c.protocol
        xml
        """
        if connectid != None:
            self.connectid = connectid

        if secretkey != None:
            self.secretkey = secretkey

        if version != None:
            self.version = version

        if protocol != None:
            self.protocol = protocol

    def getAdmedia(self, programid=None, region=None, format=None,
                   partnership=None, purpose=None, admediumtype=None,
                   categoryid=None, adspaceid=None, page=0, items=10):
        params = {'program': programid,
                  'region': region,
                  'format': format,
                  'partnership': partnership,
                  'purpose': purpose,
                  'admediumtype': admediumtype,
                  'category': categoryid,
                  'adspaceid': adspaceid,
                  'page': page,
                  'items': items,
                  }
        return self._doRestfulRequest(resource=['admedia'],
                                      params=params)

    def getAdmedium(self, admediumid, adspaceid=None):
        params = {'adspaceid': adspaceid}
        return self._doRestfulRequest(resource=['admedia', 'admedium', admediumid],
                                      params=params)

    def getAdmediumCategories(self, programid):
        return self._doRestfulRequest(resource=['admedia', 'categories', 'program', programid])

    def createAdspace(self):
        raise Exception('Not yet implemented')

    def deleteAdspace(self):
        raise Exception('Not yet implemented')

    def getAdspace(self):
        raise Exception('Not yet implemented')

    def getAdspaces(self):
        raise Exception('Not yet implemented')

    def updateAdspace(self):
        raise Exception('Not yet implemented')

    def getReportBasic(self, fromdate, todate, datetype=None, currency=None,
                       programid=None, admediumid=None, admediumformat=None,
                       adspaceid=None, reviewstate=None, groupby=None):
        params = {'fromdate': fromdate,
                  'todate': todate,
                  'datetype': datetype,
                  'currency': currency,
                  'programid': programid,
                  'admediumid': admediumid,
                  'admediumformat': admediumformat,
                  'adspaceid': adspaceid,
                  'reviewstate': reviewstate,
                  'groupby' : groupby,
                  }
        return self._doRestfulRequest(resource=['reports', 'basic'],
                                      params=params,
                                      secure=True)

    def getBalance(self):
        raise Exception('Not yet implemented')

    def getBalances(self):
        raise Exception('Not yet implemented')

    def getBankAccount(self):
        raise Exception('Not yet implemented')

    def getBankAccounts(self):
        raise Exception('Not yet implemented')

    def getExclusiveIncentive(self, incentiveid, adspaceid=None):
        params = {'adspaceid': adspaceid}
        return self._doRestfulRequest(resource=['incentives', 'exclusive', 'incentive', incentiveid],
                                      params=params,
                                      secure=True)

    def getIncentive(self, incentiveid, adspaceid=None):
        params = {'adspaceid': adspaceid}
        return self._doRestfulRequest(resource=['incentives', 'incentive', incentiveid],
                                      params=params)

    def searchExclusiveIncentives (self, programid=None, adspaceid=None, incentivetype=None,
                                   region=None, page=0, items=10):
        """
        Returns a list of exclusive incentiveItems.
        """
        params = {'programid': programid,
                  'adspaceid': adspaceid,
                  'incentivetype': incentivetype,
                  'region': region,
                  'page': page,
                  'items': items,
                  }
        return self._doRestfulRequest(resource=['incentives', 'exclusive'],
                                      params=params,
                                      secure=True)

    def searchIncentives(self, program=None, adspace=None, incentiveType=None,
            region=None, items=None, page=None):
        """ Returns a list of publicly available, non-exclusive incentiveItems.
        """
        params = {'adspace': adspace,
                  'program': program,
                  'incentiveType': incentiveType,
                  'region':region,
                  'items':items,
                  'page':page,
                  }
        return self._doRestfulRequest(resource=['incentives'],
                                      params=params)

    def getLead(self, leadid):
        """ Request a leadItem by its ID.
        """
        return self._doRestfulRequest(resource=['reports', 'leads', 'lead', leadid],
                                      secure=True)

    def getLeads(self, date, datetype=None, programid=None, adspaceid=None,
                 reviewstate=None, page=0, items=10):
        params={'datetype': datetype,
                'programid': programid,
                'adspaceid': adspaceid,
                'reviewstate': reviewstate,
                'page': page,
                'items': items,
                }
        return self._doRestfulRequest(resource=['reports', 'leads', 'date', date],
                                      params=params,
                                      secure=True)

    def getSale(self, saleid):
        """ Request a saleItem by its ID.
        """
        return self._doRestfulRequest(resource=['reports', 'sales', 'sale', saleid],
                                      secure=True)

    def getSales(self, date, datetype=None, programid=None, adspaceid=None,
                 reviewstate=None, page=0, items=10):
        params = {'datetype': datetype,
                  'programid': programid,
                  'adspaceid': adspaceid,
                  'reviewstate': reviewstate,
                  'page': page,
                  'items': items,
                  }
        return self._doRestfulRequest(resource=['reports', 'sales', 'date', date],
                                      params=params,
                                      secure=True)

    def getPayment(self):
        raise Exception('Not yet implemented')

    def getPayments(self):
        raise Exception('Not yet implemented')

    def getProduct(self, productid, adspaceid=None):
        """ Request a productItem by its ID.
        """
        params = {'adspaceid': adspaceid}
        return self._doRestfulRequest(resource=['products', 'product', productid],
                                      params=params)

    def getProductCategories(self, rootcategory=0, includechilds=False):
        """ Request a product category list.
        """
        params = {'rootcategory': rootcategory,
                  'includechilds': includechilds,
                  }
        return self._doRestfulRequest(resource=['products', 'categories'],
                                      params=params)

    def searchProducts(self, query, searchtype='phrase', region=None,
                       categoryid=None, programid=[], hasimages=True,
                       minprice=0, maxprice=None, adspaceid=None, page=0,
                       items=10):
        """ Returns a list of productItems.
        """
        params = {'q': query,
                  'searchtype': searchtype,
                  'region': region,
                  'categoryid': categoryid,
                  'programid': programid,
                  'hasimages': hasimages,
                  'minprice': minprice,
                  'maxprice': maxprice,
                  'adspaceid': adspaceid,
                  'page': page,
                  'items': items,
                  }
        return self._doRestfulRequest(resource=['products'],
                                      params=params)

    def getProfile(self):
        raise Exception('Not yet implemented')

    def updateProfile(self):
        raise Exception('Not yet implemented')

    def getProgram(self, programid):
        """ Request a programItem by its ID.
        """
        return self._doRestfulRequest(resource=['programs', 'program', programid])

    def getProgramCategories(self):
        """ Request a program category list.
        """
        return self._doRestfulRequest(resource=['programs', 'categories', programid])

    def searchPrograms(self, query=None, startdate=None, partnership=None,
                       hasproducts=False, region=None, categoryid=None, page=0,
                       items=10):
        params={'q': query,
                'startdate': startdate,
                'partnership': partnership,
                'hasproducts': hasproducts,
                'region': region,
                'categoryid': categoryid,
                'page': page,
                'items': items,
                }
        self._doRestfulRequest(resource=['programs'],
                               params=params)

    def createProgramApplication(self):
        raise Exception("Not yet implemented")

    def getProgramApplications(self, adSpaceId=None, programId=None,
            status=None, page=0, items=10):
        params = {'adspace':adSpaceId,
                  'program':programId,
                  'status':status,
                  'page':page,
                  'items':items,
                  }
        return self._doRestfulRequest(resource=['programapplications'],
                                      params=params,
                                      secure=True)

    def deleteProgramApplication(self):
        raise Exception("Not yet implemented")

    def getTrackingCategories(self, adspaceid, programid, page=0, items=50):
        raise Exception("This resource is not available in REST")

    def _doRestfulRequest(self, resource, params={}, method='GET', secure=False):
        uri = "/" + "/".join(resource) + "/"
        url = "/".join([self.zanoxurl, self.protocol, self.version]) + uri

        authorization = 'ZXWS ' + self.connectid

        query_parameters = []
        for key in params:
            if params[key] != None:
                query_parameters.append("%s=%s" % (key, params[key]))

        url += "?" + "&".join(query_parameters)

        request = urllib2.Request(url)
        opener  = urllib2.build_opener(HttpErrorHandler())

        request.add_header('user-agent', 'geelweb.affiliate.zanox')
        request.add_header('host', 'api.zanox.com')
        request.add_header('authorization', authorization)

        if secure:
            nonce = self._getNonce()
            timestamp = self._getTimestamp()
            signature = self._sign(method + uri + timestamp + nonce)
            request.add_header('nonce', nonce)
            request.add_header('date', timestamp)
            request.add_header('authorization', authorization + ':' + signature)

        datastream = opener.open(request)
        return datastream.read()

    def _getNonce(self):
        h = hashlib.md5()
        h.update("%s" % mktime(datetime.now().timetuple()))
        h.update("%s" % random.random())
        return h.hexdigest()

    def _getTimestamp(self):
        return strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())

    def _sign(self, string2sign):
        sign = hmac.new(self.secretkey, string2sign.encode('utf-8'), hashlib.sha1)
        return b64encode(sign.digest())


class HttpErrorHandler(urllib2.HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, headers):
        result = urllib2.HTTPError(
                req.get_full_url(), code, msg, headers, fp)
        result.status = code
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
