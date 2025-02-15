Opened the **** interface in wireshark and protocols traced were following:
- SSDP: Simple Service Discovery Protocol
- ICMP: Internet Control Message Protocol
- ARP: Address resolution Protocol
- DNS: Domain Name system
- TCP: Transmission Control protocol
- TLS: Transport Layer Security

I Sent request to 3 websites using HTTP and capture the packets using Wireshark as mentioned below

Website | IP & Mac Source Address | IP & Mac Destination Address | Http response code| Round Trip Time for http 200|Http response code after reloading | Round trip time after reloading|Transport layer protocol(tcp/udp)|Source(client) port|Desination(server) port 
--------|--------------|----------------|-------------------|----------|-----|------|------|-----|---------
http://www.example.com|172.22.45.7-08:00:27:cb:7e:f5|93.184.216.34- 00:15:5d:59:c7:03 |200 ok|0.543665463 sec|304 not modified|0.227996837 |TCP|41010|80
http://www.jaduniv.edu.in|172.22.45.7-08:00:27:cb:7e:f5|136.232.79.162-00:15:5d:59:c7:03|200 ok|2.693430646|404|0.053492501|TCP|35640|80
http://www.roughlydrafted.com|172.22.45.7-08:00:27:cb:7e:f5|45.55.58.72-00:15:5d:59:c7:03|200 ok|0.449966139|200 ok|0.402523232|TCP|58818|80
http://web.archive.org|172.22.45.7-08:00:27:cb:7e:f5|207.241.237.3-00:15:5d:59:c7:03|200 ok|0.998223257|Continuation|0.454898362|TCP|42416|80


``` 
No.   Time            Source    Destination   Protocol  Length   Info
26   1.652050633   172.22.45.7  45.55.58.72     HTTP      412    GET / HTTP/1.1

Frame 26: 412 bytes on wire (3296 bits), 412 bytes captured (3296 bits) on interface eth0, id 0
Ethernet II, Src: PcsCompu_cb:7e:f5 (08:00:27:cb:7e:f5), Dst: Microsof_9b:58:5c (00:15:5d:9b:58:5c)
Internet Protocol Version 4, Src: 172.22.45.7, Dst: 45.55.58.72
Transmission Control Protocol, Src Port: 45496, Dst Port: 80, Seq: 1, Ack: 1, Len: 346
Hypertext Transfer Protocol


No.  Time          Source       Destination   Protocol  Length   Info
30  2.097800131   45.55.58.72   172.22.45.7       HTTP    1057   HTTP/1.1 200 OK (text/html)

Frame 30: 1057 bytes on wire (8456 bits), 1057 bytes captured (8456 bits) on interface eth0, id 0
Ethernet II, Src: Microsof_9b:58:5c (00:15:5d:9b:58:5c), Dst: PcsCompu_cb:7e:f5 (08:00:27:cb:7e:f5)
Internet Protocol Version 4, Src: 45.55.58.72, Dst: 172.22.45.7
Transmission Control Protocol, Src Port: 80, Dst Port: 45496, Seq: 1355, Ack: 347, Len: 991
[2 Reassembled TCP Segments (2345 bytes): #28(1354), #30(991)]
Hypertext Transfer Protocol
Line-based text data: text/html (87 lines) ```
