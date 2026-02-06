# ===============================
# Linear Regression từ đầu
# Không dùng thư viện
# ===============================
import matplotlib.pyplot as plt
# Dữ liệu huấn luyện
X = [50, 70, 80, 100, 120]
Y = [200, 270, 300, 370, 450]

# Khởi tạo tham số
w = 0.0
b = 0.0

# Siêu tham số
learning_rate = 0.0001
epochs = 1000
n = len(X)

# Hàm dự đoán, với công thức y = wx + b
def predict(x):
    return w * x + b 

# Huấn luyện
for epoch in range(epochs):
    dw = 0.0
    db = 0.0

    for i in range(n):
        y_pred = predict(X[i])
        error = y_pred - Y[i]
    #Đạo hàm MSE theo w và b
        dw += error * X[i]
        db += error

    # Trung bình gradient
    dw = (2 / n) * dw
    db = (2 / n) * db

    # Cập nhật tham số
    w -= learning_rate * dw
    b -= learning_rate * db

    # In loss mỗi 100 epoch, với công thức MSE
    if epoch % 100 == 0:
        loss = 0
        for i in range(n):
            loss += (predict(X[i]) - Y[i]) ** 2
        loss /= n
        print(f"Epoch {epoch}: Loss = {loss:.2f}, w = {w:.4f}, b = {b:.4f}")
        

# ===============================
# Dự đoán thử
# ===============================
x_test = 90
y_test = predict(x_test)
print(f"Dự đoán giá nhà với diện tích {x_test}: {y_test:.2f}")

# Scatter dữ liệu gốc
X_line = []
Y_line = []

x = min(X)
while x <= max(X):
    X_line.append(x)
    Y_line.append(predict(x))
    x += 1

# ===============================
# Vẽ biểu đồ
# ===============================
plt.scatter(X, Y)
plt.plot(X_line, Y_line)

plt.xlabel("Diện tích")
plt.ylabel("Giá nhà")
plt.title("Linear Regression (code tay)")

plt.show()