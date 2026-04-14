"""
QoS Priority Controller for SDN Mininet Project

What this controller does:
- Listens to PacketIn events from switches
- Identifies traffic type (ICMP / HTTP / iperf)
- Logs priority (HIGH / MEDIUM / LOW)
- Uses POX learning switch for forwarding

NOTE:
We are NOT installing flow rules here.
Forwarding is handled by forwarding.l2_learning module.
"""

# Import POX core module (main controller framework)
from pox.core import core

# Import OpenFlow library (used for communication with switches)
import pox.openflow.libopenflow_01 as of

# Create logger to print messages in POX terminal
log = core.getLogger()


class QoSController(object):
    """
    This class is created for each switch connection.

    It listens to PacketIn events from that switch.
    """

    def __init__(self, connection):
        """
        Constructor runs when a switch connects.
        """

        # Save switch connection object
        self.connection = connection

        # Register this class to listen for events (like PacketIn)
        connection.addListeners(self)

        # Print log message
        log.info("QoS controller attached to switch %s", connection)


    def _handle_PacketIn(self, event):
        """
        This function runs whenever a packet comes to controller
        (i.e., switch sends PacketIn message)
        """

        # Extract packet from event
        packet = event.parsed

        # If packet parsing failed → ignore
        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        # Try to extract IPv4 packet
        ip_packet = packet.find('ipv4')

        # If not IPv4 → ignore
        if ip_packet is None:
            return

        # ------------------------------------
        # HIGH PRIORITY → ICMP traffic
        # ------------------------------------
        icmp_packet = ip_packet.find('icmp')

        # If ICMP exists → HIGH priority
        if icmp_packet:
            log.info("HIGH PRIORITY: ICMP packet detected")
            return

        # ------------------------------------
        # Check for TCP traffic
        # ------------------------------------
        tcp_packet = ip_packet.find('tcp')

        if tcp_packet:
            # Get source and destination ports
            src_port = tcp_packet.srcport
            dst_port = tcp_packet.dstport

            # LOW PRIORITY → iperf (port 5001)
            if src_port == 5001 or dst_port == 5001:
                log.info("LOW PRIORITY: TCP bulk traffic (port 5001)")
                return

            # MEDIUM PRIORITY → HTTP (port 8080)
            if src_port == 8080 or dst_port == 8080:
                log.info("MEDIUM PRIORITY: HTTP traffic (port 8080)")
                return

            # Other TCP traffic
            log.info("MEDIUM PRIORITY: Other TCP traffic")
            return


def launch():
    """
    This function runs when POX loads this module.
    """

    # Function to handle new switch connections
    def start_switch(event):
        # Create controller object for each switch
        QoSController(event.connection)

    # Register ConnectionUp event
    core.openflow.addListenerByName("ConnectionUp", start_switch)

    # Log module loaded
    log.info("QoS priority controller module loaded")
