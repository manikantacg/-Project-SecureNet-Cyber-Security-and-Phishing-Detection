from scapy.all import sniff

# Simulate intrusion detection system
def detect_phishing(packet):
    # Check for suspicious patterns in packet (simplified example)
    if 'phishing' in str(packet).lower():
        print('Phishing attempt detected!')
        send_alert()

def send_alert():
    print('Alert: Possible phishing attack detected!')

# Start sniffing network packets (note: root privileges are required)
sniff(prn=detect_phishing, store=0)

# Simulate network traffic for testing
from scapy.all import send, IP, UDP

# Sending a fake phishing packet for testing
packet = IP(dst="10.0.0.1") / UDP(dport=12345) / "Phishing attempt detected!"
send(packet)
