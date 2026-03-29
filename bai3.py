# Bài 3. Sử dụng list comprehension và dict comprehension

diem_mau = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

# Tạo danh sách mới chỉ gồm các điểm đạt (>= 5)
diem_dat = [d for d in diem_mau if d >= 5]
print("Điểm đạt:", diem_dat)

# Tạo danh sách bình phương của các điểm đạt
diem_binh_phuong = [d**2 for d in diem_dat]
print("Bình phương điểm đạt:", diem_binh_phuong)

# Tạo từ điển có khóa là số thứ tự sinh viên và giá trị là xếp loại
xep_loai = {i+1: ('A' if d >= 8 else 'B' if d >= 6.5 else 'C' if d >= 5 else 'F') for i, d in enumerate(diem_mau)}
print("Xếp loại:")
for stt, xl in xep_loai.items():
    print(f"Sinh viên {stt}: {xl}")