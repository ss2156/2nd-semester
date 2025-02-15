Faculty: Sai Kiran G
Course code: EEL7200

[Lecture1](https://github.com/VenkySharma/Mtech-CSE/blob/main/Course/Data%20Communication%20%26%20Networking/about.md#lecture1-)
[Lecture2](https://github.com/VenkySharma/Mtech-CSE/blob/main/Course/Data%20Communication%20%26%20Networking/about.md#lecture2)
[Lecture3](https://github.com/VenkySharma/Mtech-CSE/blob/main/Course/Data%20Communication%20%26%20Networking/about.md#lecture3-100124-wed)
[Lecture4](https://github.com/VenkySharma/Mtech-CSE/blob/main/Course/Data%20Communication%20%26%20Networking/about.md#lecture4-120124-fri)

### Lecture1-

### Lecture2
What is circuit switching and Packet Switching

### Lecture3-10/01/24 Wed
- How and why we moved from packet switching to Arpanet model
- Why we needed model like OSI
- what is physical layer and what are functions of it
  - Physical Connection
  - Data Transmission
  - Modulation & Demodulation
  - Bit level(Forward) Error correction, Scrambling
- what is Data Link Layer and what are functions of it
  - Flow control
  - Access Control
  - Retransmission
  - Physical Addressing(MAC)
  - what are the ways to access channel
    - contention Free Acess- e.g TDMA,FDMA
    - contention Based Access- e.g CSMA, Aloha
    - what is CSMA/CA & where it is used
    - what is CSMA/CD & where it is used
- What is Network layer and what are functions of it
  - Routing
  - IP addressing
  - *why currently there is shift in network routing from Distributed Routing to Centralized Routing*
    - Separate Bandwidth Requirement

### Lecture4-12/01/24 Fri
- what is transport layer and what are the functions of it
  - Process to Process Delivery
  - Port Adressing
  - End to End Delivery(TCP/UDP)
  - Error and Congestion Control
- what is Session layer
  - Login Session Management
  - cookies
- what is Presentation layer
  - Encryption/Decryption
  - Compression
  - Formatting-ascii,ebcdic
- What is Application Layer
- what are real world used model of internet
  - Zigbi-Physical, Data Link, Application
  - TCP/IP-(Physical, Data link), Network, Transport, (Session,Presntation,Application)
### Lecture5-16/01/24 Tue
- Quality of Service(QOS) what is it?
- Quality of experience
- How we will quantify QOS
  - *Throughput*-what is it & how it affect qos? where is it more considerable-e.g EMBB
  - *Reliability*-what(Packet Loss) is it & how it affect qos? where is it more considerable-e.g URLLC
  - *Latency*-what is it & how it affect qos? how to remediate more latency?
  - *Jitter*-what is it-difference of latency b/w diff packets.Imapact of Jitter. e.g in Drone n/w we need no jitter.
    
- Does OSI layer affect QOS & how?
  - **Physical Layer**-Different medium, Different modulation & Demodulation scheme, Diff Error handling mechanism.
  - **Data Link Layer**-How we handle retransmission, diff channel access mechanism.
  - **Network Layer**-Routing algo.
  - **Transport Layer**-Flow Control,Error Handling, Congestion Handling
  - **Application Layer**
  - Cross layer Optimization- what & Why. 
    
${\color{red}Next one is coming}$
