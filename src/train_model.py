import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# 1. Đọc dữ liệu với tên cột (header)
# Danh sách tên cột đầy đủ cho KDD Cup 1999
col_names = ["duration", "protocol_type", "service", "flag", "src_bytes",
             "dst_bytes", "land", "wrong_fragment", "urgent", "hot",
             "num_failed_logins", "logged_in", "num_compromised", "root_shell",
             "su_attempted", "num_root", "num_file_creations", "num_shells",
             "num_access_files", "num_outbound_cmds", "is_host_login",
             "is_guest_login", "count", "srv_count", "serror_rate",
             "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
             "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
             "dst_host_srv_count", "dst_host_same_srv_rate",
             "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
             "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
             "dst_host_srv_serror_rate", "dst_host_rerror_rate",
             "dst_host_srv_rerror_rate", "outcome"]

# Đọc file dữ liệu
data = pd.read_csv('kddcup.data_10_percent', header=None, names=col_names)

# 2. Tiền xử lý dữ liệu
# Chuyển đổi các cột categorical sang numerical
le = LabelEncoder()
data['protocol_type'] = le.fit_transform(data['protocol_type'])
data['service'] = le.fit_transform(data['service'])
data['flag'] = le.fit_transform(data['flag'])

# Tạo nhãn nhị phân (0: normal, 1: attack)
data['is_malicious'] = data['attack_type'].apply(lambda x: 0 if x == 'normal' else 1)

# 3. Chọn features và nhãn
# Chọn các features quan trọng (có thể điều chỉnh)
features = data[['duration', 'protocol_type', 'service', 'src_bytes', 'dst_bytes', 
                'wrong_fragment', 'logged_in', 'count', 'srv_count']]
labels = data['is_malicious']

# 4. Chia dữ liệu train/test
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# 5. Huấn luyện mô hình
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Đánh giá mô hình
# Độ chính xác tổng thể
accuracy = model.score(X_test, y_test)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Báo cáo chi tiết
y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. Lưu model (tuỳ chọn)
import joblib
joblib.dump(model, 'kdd_model.pkl')
print("\nModel saved as 'kdd_model.pkl'")