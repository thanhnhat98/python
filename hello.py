"""# Nhập họ tên, Năm sinh, in ra chào bạn ? tuổi
# ép chuỗi
# xử lý lỗi try: except Exception as e:
try:
    ho_ten = input(" Nhập họ tên:")
    print(type(ho_ten))
    nam_sinh = int(input("Nhập Năm sinh"))
    print(type(nam_sinh))
    print(f"chào bạn {ho_ten}, {2022 - nam_sinh} tuổi.")
except Exception as e:
    print("Lỗi: ", e )"""
print("nhập sô tờ:")
tien_candoi = int(input())
mang_menh_gia = [100,50,20,10,5,200]
mang_menh_gia.sort()
mang_menh_gia.reverse()
mang_so_to = []
for m_gia in mang_menh_gia :
    print(m_gia)
    so_to = tien_candoi // m_gia
    mang_so_to.append(so_to)
    tien_candoi = tien_candoi % m_gia
print("số tờ: ", mang_so_to)
print("Dư: ", tien_candoi)