"""
3-switch QoS topology for the SDN Mininet project.

Topology used:

    h1      
     |       
     |       
     s1 ----- s2 ----- s3
     |        |         |
     |        h3        h4
    h2
Meaning:
- h1 and h2 are connected to switch s1
- h3 is connected to switch s2
- h4 is connected to switch s3
- s2 is the middle switch and acts as the bottleneck point

This topology is chosen because traffic from the left side to the right side
must pass through the middle switch s2, so contention and priority behavior
can be observed more clearly.
"""

# Import the Topo base class from Mininet
from mininet.topo import Topo


# Define a custom topology class
class QoSTopo(Topo):
    """
    Custom topology for the QoS priority scheduling project.
    """

    def build(self):
        """
        Build the full network topology.
        """

        # -------------------------
        # Add end hosts to Mininet
        # -------------------------
        # h1 will mainly be used for ICMP / high-priority traffic
        h1 = self.addHost('h1', ip='10.0.0.1/24')

        # h2 will mainly be used for HTTP / medium-priority traffic
        h2 = self.addHost('h2', ip='10.0.0.2/24')

        # h3 will mainly be used for iperf / low-priority traffic
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        # h4 will mainly act as the destination/client host
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        # -----------------------------
        # Add OpenFlow switches
        # -----------------------------
        # s1 is the left-side access switch
        s1 = self.addSwitch('s1')

        # s2 is the middle switch and acts as the bottleneck switch
        s2 = self.addSwitch('s2')

        # s3 is the right-side access switch
        s3 = self.addSwitch('s3')

        # --------------------------------
        # Add host-to-switch connections
        # --------------------------------
        # Connect h1 to s1
        self.addLink(h1, s1)

        # Connect h2 to s1
        self.addLink(h2, s1)

        # Connect h3 to s2
        self.addLink(h3, s2)

        # Connect h4 to s3
        self.addLink(h4, s3)

        # --------------------------------
        # Add inter-switch connections
        # --------------------------------
        # Connect s1 to s2
        self.addLink(s1, s2)

        # Connect s2 to s3
        self.addLink(s2, s3)


# Expose the topology to Mininet using the short name "qos"
topos = {'qos': (lambda: QoSTopo())}
