# Bài 5. Đọc file văn bản và thống kê dữ liệu

# Đọc toàn bộ dữ liệu từ file
with open('sinhvien.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Chuyển dữ liệu thành danh sách sinh viên
ds_sv = []
for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 3:
        ma, ten, diem_str = parts
        try:
            diem = float(diem_str)
            ds_sv.append((ma, ten, diem))
        except ValueError:
            print(f"Lỗi: Điểm không hợp lệ cho {ma}")

# Tính số lượng sinh viên, điểm trung bình, số sinh viên đạt và không đạt
so_sv = len(ds_sv)
if so_sv > 0:
    diem_tb = sum(sv[2] for sv in ds_sv) / so_sv
    so_dat = sum(1 for sv in ds_sv if sv[2] >= 5)
    so_khong_dat = so_sv - so_dat
else:
    diem_tb = 0
    so_dat = 0
    so_khong_dat = 0

# Ghi kết quả thống kê ra file baocao.txt
with open('baocao.txt', 'w', encoding='utf-8') as f:
    f.write(f"Số lượng sinh viên: {so_sv}\n")
    f.write(f"Điểm trung bình: {diem_tb:.2f}\n")
    f.write(f"Số sinh viên đạt: {so_dat}\n")
    f.write(f"Số sinh viên không đạt: {so_khong_dat}\n")

print("Đã ghi báo cáo vào baocao.txt")