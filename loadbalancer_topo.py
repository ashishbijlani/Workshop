from mininet.topo import Topo
 
 
class SimpleTopo(Topo):
    "Simple loop topology example."
 
    def __init__(self):
        "Create custom loop topo."
 
        # Initialize topology
        Topo.__init__(self)
 
        # Add hosts and switches
        ## Add hosts        

        ## Add switches


        # Add links (Use the switches in then node1 space)
 
 
topos = {'topology': (lambda: SimpleTopo())}
