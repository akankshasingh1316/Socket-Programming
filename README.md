# SocketProgramming
Server Load Testing and Network Analysis

### Objective Of the Project

  Load testing is the process of putting demand on a software system or computing device and measuring its response. It is performed to determine a system's behavior under both normal and anticipated peak load conditions. It helps to identify the maximum operating capacity of an application as well as any bottlenecks and determine which element is causing degradation. The load is usually so great that error conditions are the expected result, although no clear boundary exists. Load and performance testing analyses software intended for a multi-user audience by subjecting the software to different numbers of virtual and live users while monitoring performance measurements under these different loads. Load and performance testing is usually conducted in a test environment identical to the production environment before the software system is permitted to go live.
  
  The objective of this project is to create a client-server connection and implement server load testing using major protocol (TCP). Along with Server Load testing, this project aims to analyze performance of the network connection through packet access and modification and report it to it to the user. The application uses the concept of a file (any format- .mp3, .mp4, .txt etc) as a load, which shall be rendered to multiple connecting clients repeatedly as per their requests. The server being tested can have ‘N Number of clients’ connected to it, each of them making ‘M Number of Requests’ to the server. The file is transferred to the client and performance parameters like Response Time and Throughput are computed for multiple packet sizes. Congestion can be visualized during the transfer on the graph.
  
  Since the server can handle only a limited amount of load, the number of clients connecting is also limited and additional clients are rejected based upon a predefined limit. This limit shall be determined on the memory of the server which shall be allocated to each of the clients upon request. If a client makes a request that needs more memory than the server can allocate, this client will be rejected and not allowed to connect altogether. In the other scenario, once a client request has been processed completely, the previously allocated memory will be freed and made available for new connections. The application would also have packet level access to allow the user to choose the size of the packet, in making requests, so that the number of bytes exchanged per packet is as defined by the user. Our Network Analysis tool will allow the user to view and save the actual TCP/IP Header details of the packets received from the server such as – sequence number, acknowledgement number and number of lost packets and retransmissions.

### How To Run The Code

1. Download the complete repository.
2. In Client.py - Line 117 and 118 : Edit the path of the file Sniffer.py and TraceRoute.py (as per the file path in your computer).
3. Run Server.py in cmd.
4. Run Client.py in cmd.
5. Follow the prompts of the GUI.
