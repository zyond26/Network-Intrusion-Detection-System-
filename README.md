# Network-Intrusion-Detection-System-

# 1. Mục tiêu & Phạm vi
Mục tiêu: Xây dựng hệ thống giám sát lưu lượng mạng, phát hiện tấn công như:
Port scanning, DDoS, SQL injection, brute force.
Đầu ra: Cảnh báo real-time + báo cáo phân tích với độ chính xác 95%.

# 2. Công cụ & Thư viện
Python: Scapy, Pandas, Scikit-learn, Flask (giao diện web).
Wireshark/Tshark: Phân tích traffic mẫu.
Jupyter Notebook: Phân tích dữ liệu.


# cách chạy toàn bộ hệ thống 
1. Bắt traffic:
python capture_traffic.py

2. Phát hiện tấn công (mở terminal mới):
python detect_attacks.py

3. Huấn luyện AI (sau khi có dữ liệu):
python train_model.py

4. Mở giao diện web:
python app.py

# Các thuật ngữ đã dùng 
1.Scapy -	Thư viện Python để bắt và phân tích gói tin mạng.
2.SYN Flood -	Kiểu tấn công DDoS bằng cách gửi nhiều gói SYN đến server.
3.Random Forest - 	Mô hình AI dùng nhiều cây quyết định để phân loại dữ liệu.
4.Flask	Framework -  web nhẹ để tạo giao diện.