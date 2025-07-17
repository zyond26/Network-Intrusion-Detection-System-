from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict

# Biến đếm để phát hiện tấn công
port_scan_counts = defaultdict(set)  # Lưu các cổng mà 1 IP truy cập
syn_counts = defaultdict(int)       # Đếm số gói SYN từ 1 IP

def detect_attacks(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        # Phát hiện Port Scanning
        port_scan_counts[src_ip].add(dst_port)
        if len(port_scan_counts[src_ip]) > 20:  # Nếu 1 IP scan > 20 cổng
            print(f"ALERT: Port Scan detected from {src_ip}")

        # Phát hiện DDoS (SYN Flood)
        if packet[TCP].flags == 'S':  # Gói SYN
            syn_counts[src_ip] += 1
            if syn_counts[src_ip] > 100:  # Nếu 1 IP gửi > 100 SYN
                print(f"ALERT: DDoS attack from {src_ip}")

# Bắt gói tin và phân tích
sniff(prn=detect_attacks, filter="tcp", store=0, count = 100)
