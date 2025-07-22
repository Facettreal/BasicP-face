text = (input ('ต้องการส่งหรือไม่: '))
if text == 'N' :
    print('ไม่ถูกจัดส่ง')

elif text == 'Y':
    km = int(input ('โปรดระบุระยะทาง: '))
    if km <= 5 :
        print('ไม่สามารถส่งได้')
    elif km <= 50 :
        print('10 บาท')
    elif km <= 100 :
        print('15 บาท')
    elif km <= 300 :
        print('25 บาท')
    elif km <= 500 :
        print('35 บาท')
    else :
        print ('45 บาท')








# km = int(input ('โปรดระบุระยะทาง: '))
# if km <= 5 :
#     print('ไม่สามารถส่งได้')
# elif km <= 50 :
#     print('10 บาท')
# elif km <= 100 :
#     print('15 บาท')
# elif km <= 300 :
#     print('25 บาท')
# elif km <= 500 :
#     print('35 บาท')
# else :
#     print ('45 บาท')

