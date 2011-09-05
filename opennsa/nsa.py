"""
Core abstractions used in OpenNSA.

Author: Henrik Thostrup Jensen <htj@nordu.net>
Copyright: NORDUnet (2011)
"""


import urlparse

from opennsa import error


STP_PREFIX = 'urn:ogf:network:stp:'
NSA_PREFIX = 'urn:ogf:network:nsa:'



class STP: # Service Termination Point

    def __init__(self, network, endpoint):
        self.network = network
        self.endpoint = endpoint


    def urn(self):
        return STP_PREFIX + self.network + ':' + self.endpoint


    def __eq__(self, other):
        if not isinstance(other, STP):
            return False
        return self.network == other.network and self.endpoint == other.endpoint


    def __str__(self):
        return '<STP %s:%s>' % (self.network, self.endpoint)



class SDP: # service demarcation point

    def __init__(self, stp1, stp2):
        self.stp1 = stp1
        self.stp2 = stp2


    def __eq__(self, other):
        if not isinstance(other, SDP):
            return False
        return self.stp1 == other.stp1 and self.stp2 == other.stp2


    def __str__(self):
        return '<SDP %s:%s-%s:%s>' % (self.stp1.network, self.stp1.endpoint, self.stp2.network, self.stp2.endpoint)



class Path:
    """
    Represent a path from a source and destitionation STP, with the endpoint pairs between them.
    """
    def __init__(self, source_stp, dest_stp, endpoint_pairs):
        self.source_stp      = source_stp
        self.dest_stp        = dest_stp
        self.endpoint_pairs  = endpoint_pairs

    def __str__(self):
        return '%s - %s - %s' % (self.source_stp, ' - '.join( [ str(e) for e in self.endpoint_pairs ] ), self.dest_stp)



class NetworkEndpoint(STP):

    def __init__(self, network, endpoint, config, dest_stp=None, max_capacity=None, available_capacity=None):
        STP.__init__(self, network, endpoint)
        self.config = config
        self.dest_stp = dest_stp
        self.max_capacity = max_capacity
        self.available_capacity = available_capacity

    def __str__(self):
        return '<NetworkEndpoint %s:%s-%s#%s>' % (self.network, self.endpoint, self.dest_stp, self.config)



class NetworkServiceAgent:

    def __init__(self, identity, endpoint): #, service_attributes=None):
        assert type(identity) is str, 'NSA identity type must be string'
        assert type(endpoint) is str, 'NSA endpoint type must be string'
        self.identity = identity
        self.endpoint = endpoint


    def getHostPort(self):
        url = urlparse.urlparse(self.address)
        host, port = url.netloc.split(':',2)
        port = int(port)
        return host, port


    def url(self):
        return self.endpoint


    def urn(self):
        return NSA_PREFIX + self.identity


    def __str__(self):
        return '<NetworkServiceAgent %s>' % self.identity



class Network:

    def __init__(self, name, nsa):
        self.name = name
        self.nsa = nsa
        self.endpoints = []


    def addEndpoint(self, endpoint):
        self.endpoints.append(endpoint)


    def getEndpoint(self, endpoint_name):
        for ep in self.endpoints:
            if ep.endpoint == endpoint_name:
                return ep

        raise error.TopologyError('No such endpoint (%s)' % (endpoint_name))


    def __str__(self):
        return '<Network %s,%i>' % (self.name, len(self.endpoints))



class BandwidthParameters:

    def __init__(self, desired=None, minimum=None, maximum=None):
        self.desired = desired
        self.minimum = minimum
        self.maximum = maximum



class ServiceParameters:

    def __init__(self, start_time, end_time, source_stp, dest_stp, stps=None, directionality='unidirectional', bandwidth_params=None):

        # should probably make path object sometime..

        # schedule
        self.start_time = start_time
        self.end_time   = end_time
        # path
        self.source_stp = source_stp
        self.dest_stp   = dest_stp
        self.stps       = stps
        self.directionality = directionality

        self.bandwidth_params = bandwidth_params or BandwidthParameters()


    def protoSP(self):
        return { 'start_time' : self.start_time,
                 'end_time'   : self.end_time,
                 'source_stp' : self.source_stp.urn(),
                 'dest_stp'   : self.dest_stp.urn(),
                 'stps'       : self.stps        }


    def __str__(self):
        return '<ServiceParameters %s>' % str(self.protoSP())

