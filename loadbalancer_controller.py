# Copyright (C) 2011 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 
from ryu.base import app_manager
from ryu.controller import mac_to_port
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.ofproto import ofproto_v1_3_parser
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib import mac
 
from ryu.topology.api import get_switch, get_link
from ryu.app.wsgi import ControllerBase
from ryu.topology import event, switches
import networkx as nx
 
class ProjectController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]
 
    def __init__(self, *args, **kwargs):
        super(ProjectController, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.topology_api_app = self
        self.net=nx.DiGraph()
        self.nodes = {}
        self.links = {}
        self.no_of_nodes = 0
        self.no_of_links = 0
        self.i=0
  
    # Handy function that lists all attributes in the given object
    def ls(self,obj):
        print("\n".join([x for x in dir(obj) if x[0] != "_"]))

    def add_flow(self, datapath, in_port, dst, actions):
        """
        Pushes a new flow to the datapath (=switch)
        :type datapath: ryu.controller.controller.Datapath
        :type in_port: input port
        :type dst: destination information 
        :type actions: list
        :return: None
        :rtype: None
        """
        #TODO: 1) Get the OpenFlow protocol from the datapath
        ofproto = 
        #TODO: 1) Get the Parser for the protocol from the datapath
        parser =       
        #TODO: 1) Generate the Match Rule for the flow
        match = 
        #TODO: 1) Create the required instruction that indicates the operation
        inst =  
        #TODO: 1) Create the modify flow message with fields: datapath, match, cookie=0, command, idle_timeout =0, hard_timeout=0, priority=1 and instructions
        ## Why do you think priority is one?
        mod = 
        
        datapath.send_msg(mod)
 
    #TODO: 1) Do you know what is a decorator? What is it use in a Ryu Controller?
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures , CONFIG_DISPATCHER)
    def switch_features_handler(self , ev):
        """
        Called during handshake, defines rule to send all unknown packets to controller
        :type ev: ryu.controller.ofp_event.EventOFPSwitchFeatures
        :return: None
        :rtype: None
        """
        print "switch_features_handler is called"
        #TODO: 1) Get the datapath (switch) from the ev object
	datapath = 
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        #TODO: 1) Why do you think we need the empty Match?
        #TODO: 1) Why is it call "table-miss flow entry"?
	match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS , actions)]
	#TODO: 1) Why is the priority zero here?
        mod = datapath.ofproto_parser.OFPFlowMod(
        datapath=datapath, match=match, cookie=0,
        command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
        priority=0, instructions=inst)
        datapath.send_msg(mod)
  
	'''
		TODO
		Multi Path Transmission
		It behaves as a load balancer for the topology of the workshop
	'''
        ###add rule for multipath transmission in s1
        if ev.msg.datapath.id == 1:
            #in_port=1,src=10.0.0.1,dst=10.0.0.2,udp,udp_dst=5555--->group id 50
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser
            #TODO: Complete switch one  
            #group 50--> port3:30%, port2:70%  
   
        ###add rule for multipath transmission in s2     
        if ev.msg.datapath.id == 2:
            #in_port=1,src=10.0.0.1,dst=10.0.0.2--->output port:2
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser
            #TODO: Complete the match and actions for switch 2
            match = 
            actions = 
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
            mod = datapath.ofproto_parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
            priority=3, instructions=inst)
            datapath.send_msg(mod)
       
        ###add rule for multipath transmission in s3
        if ev.msg.datapath.id == 3:
            #in_port=1,src=10.0.0.1,dst=10.0.0.2--->output port:2
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser
            #TODO: Complete the match and actions for switch 3 
            match = 
            actions = 
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
            mod = datapath.ofproto_parser.OFPFlowMod(
            datapath=datapath, match=match, cookie=0,
            command=ofproto.OFPFC_ADD, idle_timeout=0, hard_timeout=0,
            priority=3, instructions=inst)
            datapath.send_msg(mod)
       
        ###add rule for multipath transmission in s4
        if ev.msg.datapath.id == 4:
	    #TODO: Complete all the required code for switch 4 
            #in_port=1,src=10.0.0.1,dst=10.0.0.2--->output port:3
            #in_port=2,src=10.0.0.1,dst=10.0.0.2--->output port:3
  
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
       """
        Called every time, when the controller receives a PACKET_IN message
        :type ev: ryu.controller.ofp_event.EventOFPPacketIn
        :return: None
        :rtype: None
        """	
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        # create a Packet object out of the payload
	# TODO: 1) Create a Packet from the message data 
        pkt = 
        eth = pkt.get_protocol(ethernet.ethernet)

        # source and destination mac address of the ethernet packet
        dst = eth.dst
        src = eth.src

        # DPID is just like the number of the switch
        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})
       if src not in self.net:
            self.net.add_node(src)
            self.net.add_edge(dpid,src,{'port':in_port})
            self.net.add_edge(src,dpid)        
        
        # "Known destination MAC address" -> We have seen this before
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]

        if dst in self.net:
            path=nx.shortest_path(self.net,src,dst)  
            next=path[path.index(dpid)+1]
            out_port=self.net[dpid][next]['port']
        else:
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        # "Install a flow to avoid packet_in next time">
        if out_port != ofproto.OFPP_FLOOD:
            #AAdd the flow to the switch
            self.add_flow(datapath, in_port, dst, actions)

        out = datapath.ofproto_parser.OFPPacketOut(
            datapath=datapath, buffer_id=msg.buffer_id, in_port=in_port,
            actions=actions)
        datapath.send_msg(out)
  
    @set_ev_cls(event.EventSwitchEnter)
    def get_topology_data(self, ev):
        switch_list = get_switch(self.topology_api_app, None)  
        switches=[switch.dp.id for switch in switch_list]
        self.net.add_nodes_from(switches)
        links_list = get_link(self.topology_api_app, None)
        links=[(link.src.dpid,link.dst.dpid,{'port':link.src.port_no}) for link in links_list]
        self.net.add_edges_from(links)
        links=[(link.dst.dpid,link.src.dpid,{'port':link.dst.port_no}) for link in links_list]
        self.net.add_edges_from(links)
