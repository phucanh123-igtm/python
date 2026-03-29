# Bài 6. Đọc file CSV và xử lý lỗi

import csv

# Đọc dữ liệu bằng thư viện csv
du_lieu_hop_le = []
du_lieu_loi = []

with open('diemlop.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ma_sv = row['MaSV']
        ho_ten = row['HoTen']
        diem_str = row['Diem']
        try:
            diem = float(diem_str)
            if 0 <= diem <= 10:
                du_lieu_hop_le.append((ma_sv, ho_ten, diem))
            else:
                du_lieu_loi.append(f"{ma_sv},{ho_ten},{diem_str} - Điểm ngoài khoảng 0-10")
        except ValueError:
            du_lieu_loi.append(f"{ma_sv},{ho_ten},{diem_str} - Điểm không phải số")

# Tính điểm trung bình của dữ liệu hợp lệ
if du_lieu_hop_le:
    diem_tb = sum(sv[2] for sv in du_lieu_hop_le) / len(du_lieu_hop_le)
    print(f"Điểm trung bình dữ liệu hợp lệ: {diem_tb:.2f}")
else:
    print("Không có dữ liệu hợp lệ")

# Ghi các dòng lỗi vào file loi.txt
with open('loi.txt', 'w', encoding='utf-8') as f:
    for loi in du_lieu_loi:
        f.write(loi + '\n')

print("Đã ghi lỗi vào loi.txt")