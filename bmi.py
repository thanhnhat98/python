print("nhập chiều cao: ")
chieucao = float(input())
print("Nhập cân nặng: ")
cannang = float(input())
bmi = cannang / (chieucao * chieucao)
if bmi < 15:
 print('Thân hình quá gầy')
elif bmi < 16:
 print('Thân hình gầy')
elif bmi < 18.5:
 print('Thân hình hơi gầy')
elif bmi < 25:
 print('Thân hình bình thường')
elif bmi < 30:
 print('Thân hình hơi béo')
elif bmi < 35:
 print('Thân hình béo')
else:
 print('Thân hình quá béo')
