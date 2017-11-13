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
So, the whole process is exemplified in some gifs below.
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/lab2_SI.gif "Gif of the attack #1")

and the secind one is: 
![alt text](https://github.com/SandaCotovici/SI/blob/master/lab%232/images/lab21_SI.gif "Gif of the attack #2")
