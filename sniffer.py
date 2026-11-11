from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("TCP") and packet.haslayer("Raw"):
        print(f"[Captured Payload]: {packet['Raw'].load}")

# Sniff traffic on loopback targeting port 8080
sniff(filter="tcp port 8080", prn=packet_callback, store=0)