import pandas as pd


def bai1_series_diem():
    print("=" * 70)
    print("BÀI 1: LÀM QUEN VỚI SERIES")
    print("=" * 70)

    diem = pd.Series(
        [7.5, 8.0, 6.5, 9.0, 8.5],
        index=["SV01", "SV02", "SV03", "SV04", "SV05"],
        name="Diem"
    )

    print("\nDanh sách điểm:")
    print(diem)

    print("\nHai phần tử đầu:")
    print(diem.head(2))

    print("\nĐiểm lớn nhất:", diem.max())
    print("Điểm trung bình:", diem.mean())

    print("\nSinh viên có điểm >= 8:")
    print(diem[diem >= 8])
    print()


def bai2_tao_dataframe():
    print("=" * 70)
    print("BÀI 2: TẠO DATAFRAME TỪ DICT")
    print("=" * 70)

    data = {
        "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05"],
        "HoTen": ["An", "Bình", "Chi", "Dũng", "Hà"],
        "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1"],
        "DiemQT": [7.0, 8.5, 6.0, 9.0, 8.0],
        "DiemThi": [7.5, 8.0, 6.5, 9.5, 8.5]
    }
    df = pd.DataFrame(data)

    print("\nDataFrame ban đầu:")
    print(df)

    print("\nChọn cột HoTen và DiemThi:")
    print(df[["HoTen", "DiemThi"]])

    df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]
    print("\nDataFrame sau khi thêm cột DiemTB:")
    print(df)
    print()


def bai3_doc_csv_kham_pha(filepath="diem_sinhvien.csv"):
    print("=" * 70)
    print("BÀI 3: ĐỌC FILE CSV VÀ KHÁM PHÁ DỮ LIỆU")
    print("=" * 70)

    df = pd.read_csv(filepath)

    print("\n5 dòng đầu:")
    print(df.head())

    print("\n5 dòng cuối:")
    print(df.tail())

    print("\nThông tin dữ liệu:")
    print(df.info())

    print("\nThống kê mô tả:")
    print(df.describe(include="all"))

    print("\nKích thước dữ liệu:", df.shape)
    print("Tên các cột:", df.columns.tolist())
    print()
    return df


def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.5:
        return "Trung binh"
    else:
        return "Yeu"


def bai4_tien_xu_ly(filepath="diem_sinhvien.csv"):
    print("=" * 70)
    print("BÀI 4: LỌC DỮ LIỆU, THÊM CỘT, ĐỔI TÊN VÀ ĐẶT INDEX")
    print("=" * 70)

    df = pd.read_csv(filepath)
    df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]
    df["XepLoai"] = df["DiemTB"].apply(xep_loai)

    print("\nSinh viên có DiemTB >= 8:")
    print(df[df["DiemTB"] >= 8])

    df = df.rename(columns={"HoTen": "TenSinhVien"})
    df = df.set_index("MaSV")

    print("\nDataFrame sau khi đổi tên cột và đặt MaSV làm index:")
    print(df)
    print()
    return df


def bai5_du_lieu_khao_sat():
    print("=" * 70)
    print("BÀI 5: DỮ LIỆU KHẢO SÁT HỌC TẬP")
    print("=" * 70)

    data = {
        "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10"],
        "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
        "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
        "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
        "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
    }

    df = pd.DataFrame(data)
    df["DiemTB"] = 0.3 * df["DiemCC"] + 0.7 * df["DiemCuoiKy"]

    def nhom_hoc_tap(row):
        if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
            return "Tich cuc"
        elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
            return "Binh thuong"
        else:
            return "Can ho tro"

    df["NhomHocTap"] = df.apply(nhom_hoc_tap, axis=1)

    print("\nDataFrame khảo sát học tập:")
    print(df)

    print("\nSinh viên tự học > 2 giờ và nghỉ <= 2 buổi:")
    print(df[(df["GioTuHoc"] > 2) & (df["SoBuoiNghi"] <= 2)])

    print("\nNhận xét: ")
    print("- Những sinh viên học tự học nhiều và nghỉ ít thường có DiemTB cao.")
    print("- Nhóm tích cực chiếm tỉ lệ nhỏ hơn nhưng đạt điểm tốt nhất.")
    print("- Nhóm bình thường vẫn có thể đạt điểm khá nếu duy trì chuyên cần.")
    print("- Nhóm cần hỗ trợ thường có giờ tự học thấp và nghỉ nhiều.")
    print("- Dữ liệu cho thấy việc tự học đều đặn và ít nghỉ là yếu tố quan trọng.")
    print()
    return df


def bai6_tong_hop(filepath="diem_sinhvien.csv", output="ketqua_xuly.csv"):
    print("=" * 70)
    print("BÀI 6: BÀI TẬP TỔNG HỢP")
    print("=" * 70)

    df = pd.read_csv(filepath)
    df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]
    df["XepLoai"] = df["DiemTB"].apply(xep_loai)

    ket_qua = df[df["XepLoai"].isin(["Gioi", "Kha"])]
    ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)
    ket_qua.to_csv(output, index=False, encoding="utf-8-sig")

    print("\nDanh sách sinh viên loại Khá trở lên (theo DiemTB giảm dần):")
    print(ket_qua)
    print(f"\nĐã lưu file {output}")
    print()
    return ket_qua


def bai7_san_pham():
    print("=" * 70)
    print("BÀI 7: QUẢN LÝ DANH SÁCH SẢN PHẨM")
    print("=" * 70)

    data = {
        "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06", "SP07", "SP08"],
        "TenSP": ["Chuot", "Ban phim", "Man hinh", "USB", "Laptop", "Loa", "Tai nghe", "Webcam"],
        "LoaiHang": ["Phu kien", "Phu kien", "Thiet bi", "Phu kien", "Thiet bi", "Thiet bi", "Phu kien", "Thiet bi"],
        "DonGia": [150000, 300000, 2500000, 180000, 14500000, 750000, 450000, 900000],
        "SoLuongTon": [25, 18, 7, 40, 5, 12, 20, 8]
    }
    df = pd.DataFrame(data)
    df["GiaTriTonKho"] = df["DonGia"] * df["SoLuongTon"]

    print("\nSản phẩm có DonGia > 500000:")
    print(df[df["DonGia"] > 500000])

    print("\nSản phẩm sắp xếp theo GiaTriTonKho giảm dần:")
    print(df.sort_values(by="GiaTriTonKho", ascending=False))

    print("\nSản phẩm có SoLuongTon < 10:")
    print(df[df["SoLuongTon"] < 10])
    print()
    return df


def bai8_hoa_don():
    print("=" * 70)
    print("BÀI 8: QUẢN LÝ HÓA ĐƠN BÁN HÀNG")
    print("=" * 70)

    data = {
        "MaHD": ["HD01", "HD02", "HD03", "HD04", "HD05", "HD06", "HD07", "HD08", "HD09", "HD10"],
        "NgayBan": ["2026-04-01", "2026-04-01", "2026-04-02", "2026-04-02", "2026-04-03", "2026-04-03", "2026-04-04", "2026-04-04", "2026-04-05", "2026-04-05"],
        "TenSP": ["Laptop", "Chuot", "Man hinh", "USB", "Loa", "Tai nghe", "Laptop", "Webcam", "Ban phim", "Man hinh"],
        "SoLuong": [1, 5, 2, 10, 3, 4, 1, 2, 6, 1],
        "DonGia": [14500000, 150000, 2500000, 180000, 750000, 450000, 14500000, 900000, 300000, 2500000],
        "NhanVien": ["An", "Binh", "An", "Chi", "Dung", "Ha", "An", "Chi", "Binh", "Ha"]
    }
    df = pd.DataFrame(data)
    df["ThanhTien"] = df["SoLuong"] * df["DonGia"]

    print("\n5 hóa đơn có giá trị cao nhất:")
    print(df.sort_values(by="ThanhTien", ascending=False).head(5))

    print("\nHóa đơn có ThanhTien >= 3000000:")
    print(df[df["ThanhTien"] >= 3000000])

    print("\nTổng doanh thu:", df["ThanhTien"].sum())
    print()
    return df


def xep_loai_khach_hang(tien):
    if tien >= 20000000:
        return "VIP"
    elif tien >= 10000000:
        return "Than thiet"
    elif tien >= 5000000:
        return "Tiem nang"
    else:
        return "Thuong"


def bai9_khach_hang():
    print("=" * 70)
    print("BÀI 9: PHÂN LOẠI KHÁCH HÀNG THEO GIÁ TRỊ MUA HÀNG")
    print("=" * 70)

    data = {
        "MaKH": ["KH01", "KH02", "KH03", "KH04", "KH05", "KH06", "KH07", "KH08"],
        "TenKH": ["Lan", "Minh", "Hung", "Ha", "Phuong", "Toan", "Ngoc", "Tuan"],
        "SoDonHang": [12, 5, 8, 15, 4, 10, 6, 3],
        "TongChiTieu": [25000000, 7200000, 12500000, 31000000, 4300000, 9800000, 15000000, 2800000]
    }
    df = pd.DataFrame(data)
    df["XepLoaiKH"] = df["TongChiTieu"].apply(xep_loai_khach_hang)

    print("\nKhách hàng VIP và Than thiet:")
    print(df[df["XepLoaiKH"].isin(["VIP", "Than thiet"])])

    print("\nDanh sách sắp xếp theo TongChiTieu giảm dần:")
    print(df.sort_values(by="TongChiTieu", ascending=False))

    print("\nChi tiêu trung bình của khách hàng:", df["TongChiTieu"].mean())
    print()
    return df


def bai10_doanh_thu_nhan_vien():
    print("=" * 70)
    print("BÀI 10: THEO DÕI DOANH THU THEO NHÂN VIÊN")
    print("=" * 70)

    data = {
        "MaHD": ["HD01", "HD02", "HD03", "HD04", "HD05", "HD06", "HD07", "HD08", "HD09", "HD10", "HD11", "HD12"],
        "NhanVien": ["An", "Binh", "Chi", "An", "Dung", "Chi", "An", "Binh", "Dung", "Chi", "An", "Binh"],
        "SoLuong": [1, 5, 2, 3, 1, 4, 2, 6, 1, 2, 1, 3],
        "DonGia": [14500000, 150000, 2500000, 750000, 900000, 450000, 300000, 180000, 2500000, 900000, 14500000, 300000]
    }
    df = pd.DataFrame(data)
    df["DoanhThu"] = df["SoLuong"] * df["DonGia"]

    tong_nv = df.groupby("NhanVien")["DoanhThu"].sum().reset_index()
    tong_nv = tong_nv.sort_values(by="DoanhThu", ascending=False)

    print("\nTổng doanh thu theo nhân viên:")
    print(tong_nv)

    print("\nNhân viên có doanh thu cao nhất:")
    print(tong_nv.iloc[0])

    print("\nNhận xét:")
    print("- Nhân viên đứng đầu thể hiện kết quả bán hàng tốt nhất.")
    print("- Nhân viên khác có thể cải thiện bằng cách tăng tần suất bán hàng hoặc giá trị đơn hàng.")
    print()
    return df, tong_nv


def bai11_nhap_xuat_ton():
    print("=" * 70)
    print("BÀI 11: PHÂN TÍCH NHẬP - XUẤT - TỒN")
    print("=" * 70)

    data = {
        "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06"],
        "TenSP": ["Laptop", "Chuot", "Ban phim", "USB", "Loa", "Webcam"],
        "TonDau": [5, 20, 15, 30, 10, 8],
        "NhapThem": [3, 10, 5, 20, 4, 2],
        "DaBan": [4, 18, 12, 35, 9, 3],
        "DonGia": [14500000, 150000, 300000, 180000, 750000, 900000]
    }
    df = pd.DataFrame(data)
    df["TonCuoi"] = df["TonDau"] + df["NhapThem"] - df["DaBan"]
    df["GiaTriTonCuoi"] = df["TonCuoi"] * df["DonGia"]

    print("\nDataFrame kho hang:")
    print(df)

    print("\nSản phẩm sắp hết hàng (TonCuoi <= 5):")
    print(df[df["TonCuoi"] <= 5])

    print("\nSản phẩm có giá trị tồn cuối lớn nhất:")
    print(df.loc[df["GiaTriTonCuoi"].idxmax()])
    print()
    return df


if __name__ == "__main__":
    bai1_series_diem()
    bai2_tao_dataframe()
    bai3_doc_csv_kham_pha()
    bai4_tien_xu_ly()
    bai5_du_lieu_khao_sat()
    bai6_tong_hop()
    bai7_san_pham()
    bai8_hoa_don()
    bai9_khach_hang()
    bai10_doanh_thu_nhan_vien()
    bai11_nhap_xuat_ton()
