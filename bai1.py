import numpy as np

print("=" * 70)
print("BÀI 1: THỐNG KÊ MÔ TẢ TRÊN DỮ LIỆU ĐIỂM SINH VIÊN")
print("=" * 70)

# Dữ liệu đầu vào: Ma trận điểm của 5 sinh viên ở 4 môn học
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("\n1. IN RA MA TRẬN ĐIỂM")
print("-" * 70)
print(scores)

print("\n2. TÍNH ĐIỂM TRUNG BÌNH CỦA TOÀN BỘ MA TRẬN")
print("-" * 70)
print("Điểm trung bình toàn bộ:", np.mean(scores))

print("\n3. TÍNH ĐIỂM TRUNG BÌNH THEO TỪNG SINH VIÊN")
print("-" * 70)
avg_by_student = np.mean(scores, axis=1)
print("Điểm trung bình từng sinh viên:", avg_by_student)

print("\n4. TÍNH ĐIỂM TRUNG BÌNH THEO TỪNG MÔN")
print("-" * 70)
avg_by_subject = np.mean(scores, axis=0)
print("Điểm trung bình từng môn:", avg_by_subject)

print("\n5. TÌM ĐIỂM CAO NHẤT VÀ THẤP NHẤT TRONG MA TRẬN")
print("-" * 70)
print("Điểm cao nhất:", np.max(scores))
print("Điểm thấp nhất:", np.min(scores))

print("\n6. TÍNH ĐỘ LỆCH CHUẨN THEO TỪNG MÔN")
print("-" * 70)
std_by_subject = np.std(scores, axis=0)
print("Độ lệch chuẩn từng môn:", std_by_subject)

print("\n7. XÁC ĐỊNH SINH VIÊN CÓ ĐIỂM TRUNG BÌNH CAO NHẤT")
print("-" * 70)
best_student = np.argmax(avg_by_student)
print(f"Sinh viên có điểm TB cao nhất là vị trí: {best_student}")
print(f"Sinh viên {best_student} (thứ {best_student + 1}): {avg_by_student[best_student]:.2f}")

print("\n" + "=" * 70)
