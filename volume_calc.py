len = float(input("가로 : "))
wid = float(input("세로 : "))
hei = float(input("높이 : "))
print("박스의 부피는",len*wid*hei,"입니다.")

sum = len+wid+hei

print('전체 길이:',sum)
if sum >160:
    print('부피초과')
elif sum > 120:
    print('13,000원')
elif sum > 100:
    print('10,000월')
elif sum > 80:
    print('8,000원')
else:
    print('5,000원')
