tong_phut = 135
cong_suat_w = 250

# Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"Số giờ: {so_gio}, Số phút: {so_phut_du}")

su_dung_lau = tong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)

print("su_dung_lau:", su_dung_lau)
print("du_lieu_hop_le:", du_lieu_hop_le)

# Kiểm chứng biểu thức toán học
print("100 + 20 * 3 =", 100 + 20 * 3)
print("(100 + 20) * 3 =", (100 + 20) * 3)