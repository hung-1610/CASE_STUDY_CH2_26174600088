ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = float(cong_suat_w) * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Lỗi thường gặp: Quên ép kiểu cong_suat_w sang float/int trước khi thực hiện phép nhân, 
# dẫn đến lỗi TypeError: unsupported operand type(s) for *: 'str' and 'int'.