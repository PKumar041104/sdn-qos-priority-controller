from pox.core import core
import pox.openflow.libopenflow_01 as of

from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.ipv4 import ipv4
from pox.lib.packet.icmp import icmp
from pox.lib.packet.tcp import tcp

log = core.getLogger()


class QoSController(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)
        log.info("Switch connected: %s", connection)

    def _handle_PacketIn(self, event):
        packet = event.parsed

        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        ip_packet = packet.find('ipv4')

        if ip_packet is None:
            log.info("Non-IPv4 packet received")
            return

        # Check ICMP
        icmp_packet = ip_packet.find('icmp')
        if icmp_packet:
            log.info("ICMP packet detected")
            return

        # Check TCP
        tcp_packet = ip_packet.find('tcp')
        if tcp_packet:
            log.info("TCP packet detected | src port=%s dst port=%s",
                     tcp_packet.srcport, tcp_packet.dstport)
            return

        log.info("IPv4 packet detected, but not ICMP/TCP")


def launch():
    def start_switch(event):
        log.info("Controlling %s", event.connection)
        QoSController(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
