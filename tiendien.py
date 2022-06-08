print("nhập chi số cũ")
kwhcu = float(input())
print("nhập chi số mới")
kwhmoi = float(input())

print("tien")
tien = kwhmoi - kwhcu
if tien < 50:
    tongtien = tien * 1.678
elif tien < 100:
    tongtien = tien * 1.734
elif tien < 200:
    tongtien = tien * 2.014
elif tien < 300:
    tongtien = tien * 2.536
elif tien < 400:
    tongtien = tien * 2.834
else: 
    tongtien = tien * 2.927
    print(f"Tổng số tiền của bạn là {tongtien}")
