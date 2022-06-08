while True:
    try:
        n = int(input("Nhập N: "))
        break
    except:
        print("sai rồi, nhập lại đê")
i = 1
tong = 0
while i <= n:
    tong = tong + i
    i = i + 1
print(f"tổng các số nguyên từ 1 đến {n} là {tong}")