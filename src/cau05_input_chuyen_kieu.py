ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = input("Nhập số phút: ")
don_gia_kwh = input("Nhập đơn giá kWh: ")

# Chuyển đổi kiểu dữ liệu
cong_suat_w = float(cong_suat_w)
so_phut = int(so_phut)
don_gia_kwh = float(don_gia_kwh)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng tính lại:", dien_nang_kwh)
print("Chi phí tính lại:", chi_phi)