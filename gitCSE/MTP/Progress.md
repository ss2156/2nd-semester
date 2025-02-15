meet & greet


# Elastic Distributed SDN

Recent papers have explored architectures for building distributed SDN controllers. focused on building the components necessary to implementa distributed SDN.

key limitation- mapping betweena switch and a controller is statically configured, mak-ing it difficult for the control plane to adapt to traffic load variations.
Real networks-variations in temporal and spa-tial traffic characteristics. Along the temporal dimension-traffic conditionscan depend on the timeof day (e.g.,less traffic duringnight),but variations even in shorter time scales(e.g.,minutesto hours). e.g real data centers, we can estimate that the peak-to-median ratio of flowarrival rates can be  1-2 ordersof magnitude.
spatial traffic variations-depend on applicationsare generating flows, some switches -larger number of flows compared to other portions of n/w.

### Switch Migrations
objective- if load goes up or down the controller added or removed,These required ability to perform switch migration which has no mechanism in sdn standard.

**Some Terminoglogy**
Openflow has 3 modes for controller-master,slave,equal. *Slave*-by default has read only access to switch & doesn't receive asynchronous messages. *Master & Equal*-Can modify swich state, recieve asynchronous message from switch. at most 1 master but many equal controllers per switch.
The controller change role by sending 'Role-change' message. o/p- change one slaves to master and od master shoud be slave(or failed).
*Guarantee*-liveness and Safety, *Liveness* - for a switch at least one controller active(either in mater/equal).For each asynchronous message the controller that issues command remains active untill switch finishes the command processing. *safety*- Exactly one controller process each asynchronous message from switch bcz duplicate processing result in duplicate entries in flow table or inconsistency in distributed data store.

**Naive Protocol** 

# Controller Placement for distributed SDN

*Abstract*- When multiple controllers are in network where each has logically centralized view but physically distributed n/w main challenge is controller scalability also leading to reduced relaibility due to overloads & long propagation delay among controller. With objective of designing scalable control layer & optimizing n/w management the papaer try to improve k-critical algo.it is the minimum number of controllers and their location to create a robust control topology that deals robustly with failures and balances the load among the selected controllers.

## Intro
## Related work
## Principle for designing the control layer
## Controller placement
## K-crtical
## Anlysis & Results
