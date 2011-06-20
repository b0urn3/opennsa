from twisted.trial import unittest
from twisted.internet import defer

from opennsa import error as nsaerror
from opennsa.proxies import dud as dudproxy




class DUDBackendTest(unittest.TestCase):

    def setUp(self):
        self.backend = dudproxy.DUDNSIProxy('TestDUD')
        pass


    @defer.inlineCallbacks
    def testBasicUsage(self):

        res_id = yield self.backend.reserve('a', 'b', {})

        conn_id = yield self.backend.provision(res_id)

        new_res_id = yield self.backend.releaseProvision(conn_id)

        yield self.backend.cancelReservation(new_res_id)


    @defer.inlineCallbacks
    def testBasicMissage(self):

        fake_id = '1234stuff'

        try:
            _ = yield self.backend.cancelReservation(fake_id)
            self.fail('Cancelling non-existing reservation did not raise exception')
        except nsaerror.CancelReservationError:
            pass # expected
        except Exception, e:
            self.fail('Cancelling non-existing reservation raised unexpected exception (%s)' % str(e))

        try:
            _ = yield self.backend.provision(fake_id)
            self.fail('Provisioning non-existing reservation did not raise exception')
        except nsaerror.ProvisionError:
            pass # expected
        except Exception, e:
            self.fail('Provisioning non-existing reservation raised unexpected exception (%s)' % str(e))

        try:
            _ = yield self.backend.releaseProvision(fake_id)
            self.fail('Releasing non-existing connection did not raise exception')
        except nsaerror.ReleaseProvisionError:
            pass # expected
        except Exception, e:
            self.fail('Releasing non-existing connection raised unexpected exception (%s)' % str(e))
