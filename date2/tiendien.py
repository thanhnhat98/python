print("nhập chi số cũ")
kwhcu = float(input())
print("nhập chi số mới")
kwhmoi = float(input())

print("tien")
tien = kwhmoi - kwhcu
if tien < 50:
    tongtien = tien * 1.678
elif tien < 100:
    tongtien = 50 * 1.678 + (tien - 50)  * 1.734 
    print(f"Tổng số tiền của bạn là {tongtien}")
elif tien < 200:
    tongtien = 50 * 1.678 + (tien - 50)  * 1.734 + (tien - 100) * 2.014
    print(f"Tổng số tiền của bạn là {tongtien}")
elif tien < 300:
    tongtien = 50 * 1.678 + (tien - 50)  * 1.734 + (tien - 100) * 2.014 + (tien - 200) * 2.536
    print(f"Tổng số tiền của bạn là {tongtien}")
elif tien < 400:
    tongtien = 50 * 1.678 + (tien - 50)  * 1.734 + (tien - 100) * 2.014 + (tien - 200) * 2.536 + (tien - 300) * 2.834
    print(f"Tổng số tiền của bạn là {tongtien}")
else:
    tongtien = 50 * 1.678 + (tien - 50)  * 1.734 + (tien - 100) * 2.014 + (tien - 200) * 2.536 + (tien - 300) * 2.834 + (tien - 400) * 2.934
    print(f"Tổng số tiền của bạn là {tongtien}")