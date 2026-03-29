# Bài 1. Quản lý danh sách điểm sinh viên bằng list và tuple

# Tạo danh sách sinh viên, mỗi sinh viên là một tuple (mã SV, họ tên, điểm)
danh_sach_sv = [
    ("SV01", "Nguyễn Văn A", 8.5),
    ("SV02", "Trần Thị B", 7.0),
    ("SV03", "Lê Văn C", 9.0),
    ("SV04", "Phạm Thị D", 6.5),
    ("SV05", "Hoàng Văn E", 8.0),
    ("SV06", "Đỗ Thị F", 5.5),
    ("SV07", "Bùi Văn G", 9.5),
    ("SV08", "Vũ Thị H", 7.5)
]

# In toàn bộ danh sách sinh viên
print("Danh sách sinh viên:")
for sv in danh_sach_sv:
    print(f"Mã SV: {sv[0]}, Họ tên: {sv[1]}, Điểm: {sv[2]}")

# Tìm sinh viên có điểm cao nhất
max_diem = max(danh_sach_sv, key=lambda x: x[2])
print(f"\nSinh viên có điểm cao nhất: {max_diem[0]} - {max_diem[1]} với điểm {max_diem[2]}")

# Tính điểm trung bình của cả lớp
tong_diem = sum(sv[2] for sv in danh_sach_sv)
diem_tb = tong_diem / len(danh_sach_sv)
print(f"Điểm trung bình của lớp: {diem_tb:.2f}")

# In danh sách sinh viên có điểm >= 8
print("\nSinh viên có điểm >= 8:")
for sv in danh_sach_sv:
    if sv[2] >= 8:
        print(f"Mã SV: {sv[0]}, Họ tên: {sv[1]}, Điểm: {sv[2]}")