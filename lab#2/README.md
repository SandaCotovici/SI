# Lab 2 SI
## Objective: Learn how to use the network as an attack vector.
### Work flow:
1. Necessarry tools:
    - XAMPP (running the Apache WebServer)
    - OWASP Switchblade 4.0 (desinged to test your networks/servers security and ability to withstand an attack)
    - TCPView (will show detailed listings of all TCP and UDP endpoints on your system)
2. Run the "ipconfig" in the Command Prompt to get the localhost address or just use 127.0.0.1.
3. Run the XAMPP Control Panel and start the Apache service.
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/XAMPP.PNG "Apache Control Panel window")
 
4. Open a browser window and check the localhost for the running Apache page
5. Start the Switchblade tool and enter the IPv4 address in the URL field.
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/SwitchBlade.png "The DoS tool window")

6. Now enter the Connections and Connections rate as you desire and press the 'Run attack' button.
     - Use TCPView to view the TCP sockets that are being run in real time.
     - Check the task manager to see the CPU usage during the attack.
     - Refresh the target page to see if it is still up and running.
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/tcpView.png "TCP View")

7. By checking the acces logs, we can check the connections created:
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/accessLog.png "Acces logs")

### Results:
In some gifs below is presented how works Switchblade:
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/lab2_SI.gif "Gif of the attack #1")

and the secind one is: 
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/lab21_SI.gif "Gif of the attack #2")

### Conclusions

In this laboratory were examined different techniques of network attacks. One type is DDoS attack, which I have experimented on a page. A distributed denial-of-service (DDoS) attack is an attack in which multiple compromised computer systems attack a target, such as a server, website or other network resource, and cause a denial of service for users of the targeted resource. The flood of incoming messages, connection requests or malformed packets to the target system forces it to slow down or even crash and shut down, thereby denying service to legitimate users or systems.

