# Bài 4. Viết hàm xử lý dữ liệu sinh viên

def nhap_danh_sach():
    # Giả lập nhập danh sách, trả về danh sách mẫu
    return [
        ("SV01", "Nguyễn Văn A", 8.5),
        ("SV02", "Trần Thị B", 7.0),
        ("SV03", "Lê Văn C", 9.0)
    ]

def tinh_diem_trung_binh(ds):
    if not ds:
        return 0
    return sum(sv[2] for sv in ds) / len(ds)

def tim_sv_max(ds):
    if not ds:
        return None
    return max(ds, key=lambda x: x[2])

def xep_loai(diem):
    if diem >= 8:
        return 'A'
    elif diem >= 6.5:
        return 'B'
    elif diem >= 5:
        return 'C'
    else:
        return 'F'

def in_bao_cao(ds):
    print("Báo cáo tổng hợp:")
    print(f"Số sinh viên: {len(ds)}")
    print(f"Điểm trung bình: {tinh_diem_trung_binh(ds):.2f}")
    max_sv = tim_sv_max(ds)
    if max_sv:
        print(f"Sinh viên điểm cao nhất: {max_sv[0]} - {max_sv[1]} ({max_sv[2]})")
    for sv in ds:
        print(f"{sv[0]}: {xep_loai(sv[2])}")

# Chương trình chính
ds = nhap_danh_sach()
in_bao_cao(ds)