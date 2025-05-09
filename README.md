# Network-Intrusion-Detection-System-

# 1. Mục tiêu & Phạm vi
Mục tiêu: Xây dựng hệ thống giám sát lưu lượng mạng, phát hiện tấn công như: Port scanning, DDoS, SQL injection, brute force.</br>
Đầu ra: Cảnh báo real-time + báo cáo phân tích với độ chính xác hơn 95%. </br>

# 2. Công cụ & Thư viện
Python: Scapy, Pandas, Scikit-learn, Flask (giao diện web).</br>
Wireshark/Tshark: Phân tích traffic mẫu.</br>
Jupyter Notebook: Phân tích dữ liệu.</br>


* data set đã dùng : kddcup.data_10_percent tải ở kaggle </br>
# Cách chạy toàn bộ hệ thống 
1. Bắt traffic:</br>
python capture_traffic.py</br>

2. Phát hiện tấn công (mở terminal mới):</br>
python detect_attacks.py</br>

3. Huấn luyện AI (sau khi có dữ liệu):</br>
python train_model.py</br>

4. Mở giao diện web:</br>
python app.py</br>

# Các thuật ngữ đã dùng 
1.Scapy -	Thư viện Python để bắt và phân tích gói tin mạng.</br>
2.SYN Flood -	Kiểu tấn công DDoS bằng cách gửi nhiều gói SYN đến server.</br>
3.Random Forest - 	Mô hình AI dùng nhiều cây quyết định để phân loại dữ liệu.</br>
4.Flask	Framework -  web nhẹ để tạo giao diện.</br>
