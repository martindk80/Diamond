#!/usr/bin/python
################################################################################

from test import *

from diamond.collector import Collector
from openvpn import OpenVPNCollector

################################################################################

class TestOpenVPNCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('OpenVPNCollector', {
            'interval': 10,
            'method':   None,
            'instances': 'file://'+self.getFixturePath('status.log'),
        })

        self.collector = OpenVPNCollector(config, None)

    @patch.object(Collector, 'publish')
    def test_should_work_with_real_data(self, publish_mock):
        self.collector.collect()

        self.assertPublishedMany(publish_mock, {
            'status.clients.a_example_org.bytes_rx' : 109619579.000000,
            'status.clients.a_example_org.bytes_tx' : 935436488.000000,
            'status.clients.b_example_org.bytes_rx' : 25067295.000000,
            'status.clients.b_example_org.bytes_tx' : 10497532.000000,
            'status.clients.c_example_org.bytes_rx' : 21842093.000000,
            'status.clients.c_example_org.bytes_tx' : 20185134.000000,
            'status.clients.d_example_org.bytes_rx' : 4559242.000000,
            'status.clients.d_example_org.bytes_tx' : 11133831.000000,
            'status.clients.e_example_org.bytes_rx' : 13090090.000000,
            'status.clients.e_example_org.bytes_tx' : 13401853.000000,
            'status.global.max_bcast-mcast_queue_length' : 14.000000,
        })

################################################################################
if __name__ == "__main__":
    unittest.main()
