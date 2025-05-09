import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('network_traffic.csv')

# Thêm cột nhã ( 0 : bình thường , 1 : tấn công ) - giả lập dữ liệu 
data['is_malicious'] = [0 if  "192.168" in ip else 1 for ip in data['Source_ip']]

# chọn feature ( đặc trưng ) và label ( nhãn )
X = data[['Destination_Port']]
y = data['is_malicious']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

# Tạo mô hình Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Danh giá mô hình
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy * 100:.2f}%")