import numpy as np

print("=" * 70)
print("BÀI 2: CHUẨN HÓA DỮ LIỆU BẰNG BROADCASTING")
print("=" * 70)

# Dữ liệu đầu vào: Ma trận điểm của 5 sinh viên ở 4 môn học
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("\n" + "-" * 70)
print("PHẦN 1: CHUẨN HÓA BẰNG Z-SCORE")
print("-" * 70)

# 1. Tính vector trung bình từng môn
mean_col = np.mean(scores, axis=0)
print("\n1. Vector trung bình từng môn:")
print(f"   {np.round(mean_col, 2)}")

# 2. Tính vector độ lệch chuẩn từng môn
std_col = np.std(scores, axis=0)
print("\n2. Vector độ lệch chuẩn từng môn:")
print(f"   {np.round(std_col, 2)}")

# 3. Chuẩn hóa toàn bộ ma trận bằng broadcasting
z_scores = (scores - mean_col) / std_col

# 4. In ma trận đã chuẩn hóa, làm tròn 2 chữ số thập phân
print("\n3. Ma trận điểm sau chuẩn hóa Z-score (làm tròn 2 chữ số thập phân):")
print(np.round(z_scores, 2))

# 5. Kiểm tra lại trung bình các cột sau chuẩn hóa
mean_after_norm = np.mean(z_scores, axis=0)
print("\n4. Kiểm tra trung bình các cột sau chuẩn hóa:")
print(f"   TB các cột: {np.round(mean_after_norm, 10)}")
print("   (Các giá trị đều gần bằng 0 ✓)")

print("\n" + "-" * 70)
print("PHẦN 2: CHUẨN HÓA DỮ LIỆU VỀ KHOẢNG [0, 1] (MIN-MAX SCALING)")
print("-" * 70)

# Tính giá trị min và max của từng cột
min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)

print("\n1. Giá trị bé nhất của từng môn:")
print(f"   {np.round(min_col, 2)}")

print("\n2. Giá trị lớn nhất của từng môn:")
print(f"   {np.round(max_col, 2)}")

# Chuẩn hóa về [0, 1]: (x - min) / (max - min)
min_max_scores = (scores - min_col) / (max_col - min_col)

print("\n3. Ma trận điểm sau chuẩn hóa [0, 1] (làm tròn 2 chữ số thập phân):")
print(np.round(min_max_scores, 2))

# Kiểm tra kết quả
print("\n4. Kiểm tra khoảng giá trị:")
print(f"   Min: {np.round(np.min(min_max_scores), 2)}")
print(f"   Max: {np.round(np.max(min_max_scores), 2)}")
print("   (Tất cả các giá trị nằm trong [0, 1] ✓)")

print("\n" + "=" * 70)
