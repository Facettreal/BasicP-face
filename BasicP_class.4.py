# def pnt_hello (year) :
#     print ('hello stater pack', year )

# pnt_hello('dd')
# pnt_hello(31)



# def eat (rice, spoon) :
#     if rice == True and spoon :
#         return ('no eat')
# eat (True , False)
# print (eat)


# def number (num1,num2,num3):
#     if number == 0 :
#         return ('minus')
#     elif number == 20 :
#         return ('possitive')
#     return (num1 + num2 + num3)

# print(number (5,7,8))

# box = ['helo', True, 'koko']
# box .append ('heloiiii')
# box .pop (0)
# print(box)

# for i in range (5):
#     print('helo')
# for i in [0,1,2,3,4]:
#     print('helokub')

# box_friut =  ['mango' ,'apple','durain']
# for i in box_friut :
#     if box_friut == 'apple' :
#         print ('aroi')
#     else :
#         print ('not found')

# box_friut =  ['mango' ,'apple','durian', 'orange']

# def find_fruit (fruit_name) :
#     for i in box_friut :
#         if i == fruit_name :
#             print ('found')
#             return
#     print ('Not found')

# find_fruit ('orange')


# for i in box_friut :
#     if i == 'apple' :
#         print ('aroi')
#     else :
#         print ('not found')



# student = {'name': "teerathat",'age': "18", 'ID' : '68130500031' }

# if student['age'] >= '18' :
#     print ('Pass')
# else :
#     print ('not pass')


students = [{"name": "Thanasorn Dusadeeroj", "age": 17, "ID": 67130500014},
            {"name": "satit", "age": 19, "ID": 6713050047}]

for student in students :
    if student["age"] <= 18 :
        print ('pass')
    else :
        print ('not pass')

