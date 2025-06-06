# Inverted Maze
A game where the user controls a maze using handles in order to get the pool ball to the end of the maze. The camera in each level gets progressively more inverted, making each level more difficult.

# Architecture

This project is equipped with a Raspberry Pi 3 and an HP Z2 Mini G4 Workstation. The HP workstation (server) is the main processor and powers the main monitor of the project. On the other hand, the Raspberry Pi (client) communicates with the hardware (sensors and buttons) and relays these events to the socket server, which is hosted on the main workstation.  

- [dpea_p2p](./dpea_p2p/): Standardized DPEA peer-to-peer communication wrapper for socket communications, used on both the workstation and the Raspberry Pi.
- [client.py](): Interface used to link the server to the buttons connected to the Raspberry Pi
- [main.py](): A monolithic main file that contains all Kivy code, including the Main Screen, Game Screen, Leadeboard, Instructions, and camera vision
- [server.py](): Gets user input from the buttons; used in main.py to determine button status
- [my_logging.py](): Proof of the loss of Joey's sanity

# Protocols

Turning off the project is probably a good thing. However, you may not need to fully power off the Raspberry Pi (step 3) unless you are experiencing incredibly strange errors.

This project needs to be started in a very particular sequence:
1. Turn on the power strip
2. Press and hold the main power supply until you hear 2 beeps in succession. 
3. Optionally toggle the lever next to the battery on the Raspberry Pi shield

# Authors

Current seniors :D
- Lauren Lee 
- Cindy Tat

Bug fixing
- Aayush Kokate
- Joey Malvinni

Past seniors
- Erik Radulov


# License

[MIT](./LICENSE)