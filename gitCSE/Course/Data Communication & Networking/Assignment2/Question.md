### Topic: Ping, Tracert, and ICMP    *Marks: 20*
1) From the Wireshark capture, select a TCP packet and then describe the relevant fields in the
IP header and their usefulness or meaning.

2) Ping to the website: www.inria.fr 
   - a. Observe the ICMP packets transferred and specify why the ICMP packets do
not have any source and destination port
   - b. Examine one of the ICMP requests and specify the type and code
   - c. What other fields are present in the ICMP packet (only) and mention the uses
of these fields
   - d. What is the type and code of the reply packet
   - e. Does ICMP echo request and reply packets have the same fields

3) Tracert to the website www.inria.fr

   - a. Examine the ICMP response for the first request. What is the type and code?
Explain why?
   - b. Examine the last ICMP response? Does it comprise of an error? How does it
vary from response received in Question 2(a)
   - c. From the latencies discovered from the tracert program, is there a link whose
delay is significantly longer than others? On the basis of their router names or
IP addresses can you guess the location of the routers and what kind of link
this could possibly be.
