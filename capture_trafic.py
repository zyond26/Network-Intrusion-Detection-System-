from scapy.all import sniff, IP, TCP
import csv

# Tạo file CSV để lưu dữ liệu
with open('network_traffic.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source_IP", "Destination_Port", "Protocol"])  # Header

    # Hàm xử lý mỗi gói tin
    def packet_callback(packet):
        if packet.haslayer(IP) and packet.haslayer(TCP):
            src_ip = packet[IP].src
            dst_port = packet[TCP].dport
            writer.writerow([src_ip, dst_port, "TCP"])  # Ghi vào CSV

    # Bắt gói tin trong 60 giây (filter chỉ lấy TCP)
    sniff(prn=packet_callback, filter="tcp", timeout=60)

print("Dữ liệu đã được lưu vào network_traffic.csv")