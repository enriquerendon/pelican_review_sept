Title: Intro to Scapy
Date: 2019-11-13 17:00
Author: Enrique Rendón Fuentes
Category: blog
Tags: python, scapy
Slug: intr-to-scapy
Status: published
Summary: Scapy is a packet manipulation tool for computer networks...

According to [Wikipedia](https://en.wikipedia.org/wiki/Scapy)):

>"[Scapy](https://scapy.net/) is a packet manipulation tool for computer networks, written in Python by Philippe Biondi. It can forge or decode packets, send them on the wire, capture them, and match requests and replies. It can also handle tasks like scanning, tracerouting, probing, unit tests, attacks, and network discovery. Scapy provides a Python interface into libpcap, (WinPCap/Npcap on Windows), in a similar way to that in which Wireshark provides a view and capture GUI. It can interface with a number of other programs to provide visualisation including Wireshark for decoding packets, GnuPlot for providing graphs, graphviz or VPython for visualisation, etc. Scapy supports Python 3 since 2018 (scapy 2.4.0+). Kamene was an independent and outdated fork of scapy originally named scapy3k."

### Installing Scapy in Anaconda
1. Create a new environment. e.g.: "scapy-python"
2. In your new environment, select "All" or "Not installed" and Search Packages: "scapy"
3. Select the scapy version and click "Apply" to start the installation


For additional information visit: https://scapy.net/

Investigate other Apps/Terms/BuzzWords:

1. Wireshark
2. dpkt
3. Address Resolution Protocol (arp): traduce direcciones IP a direcciones MAC
4. neo4j
5.


>pkg = IP(dst = "8.8.8.8")/ICMP(type=8)/"Payload Data
>pkg.show()"
