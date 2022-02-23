# GLB - Load Balancer
The project consists in creating a practical fully functioning environment in P4. In this case, the system designed is a Load Balancer which must parse the packets received and forward them into several backends. The system's topology is as follows:

![Topology](images/Topology.png "Topology")

Therefore, a client will be the one sending traffic to the backends. The switch must receive the packets, parse the information and forward them to the servers. To do so, a protocol layer has been created, called GLB, which has a 16-bit field called **ncon**. This field contains a value that determines which server the packet should be forwarded to.

