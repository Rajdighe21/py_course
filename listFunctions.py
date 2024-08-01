l = [20, 32, 43, 99, 25, 4, 6]
# del l[2]   #del Function
# print(l)


# pop function

# l.pop(3)
# print(l)   #out put [20, 32, 43, 25, 4, 6]
# print(l.pop(2)) #Out Put 43 Jo Value Delete Kiya he vo Return karenga


# #remove function
# l.remove(99)
#
# print(l) #Jo Value Enter Kia hai Vo Value gayab Hoga


# clear Function
# l.clear()  # List Clear  Ho Jayengi
# print(l)


NewList = [10, 12, 13, 44, 55, 67, 43]

# how to add value on index and delete old value
# NewList[2] = 99
# print(NewList)


# insert function
# NewList.insert(2,69)
# print(NewList)


# append() function
# YEH EK LIST ME APPEND KI VALUE JAISI HAI VAISI KE VAISI ADD KARTA HAI

# exampleFirst = [10,20,30,40,50]
# exampleFirst.append(60)
# print(exampleFirst)
#
# exampleSecond = [70,80,90,100]
# exampleFirst.append(exampleSecond)
# print(exampleFirst)


# extend() function
# yeh list ke andar ke values ko last ,me add karrta hai
# exampleFirst = [10,20,30,40,50]
# # exampleFirst.extend(60)
# print(exampleFirst)
# 
# exampleSecond = [70,80,90,100]
# exampleFirst.extend(exampleSecond)
# print(exampleFirst)


# COUNT FUNCTION
# YE COUNT FUNCTION HE JO HAM ARRAY OR STRING KE ANDAR USE KARTE HAI
# LIST KE ANDAR KITNE BAR VALUE REPETED HUI HAI UNKO DHUNDTA HAI
# AGAR LENTH CHECK KARNI HOGI TO len() FUNCTION USE KARET HAI YEH VALA NAHI
# Myarray = [10, 20, 30, 40, 50, 60, 10]
# NewArray = Myarray.count(10)
# print(NewArray)


# MAX FUNCTOIN

# YEH LIST KE ANDAR TEXT RAHENGA TABHI USE KAR SAKTE HAI
# LIST ME MAXIMUM  VALUE KONSI HAI VO FIND KARTA HAI
# Myarray = [10, 20, 30, 40, 50, 60, 10]
# MyText = ['Name', 'Age', 'Gender', 'Address', 'Dob', 'AdharCard', 'PanCard','Zero']
#
# NewArray = max(Myarray)
# print(NewArray)
# #out     60
# NewArray = max(MyText)
# print(NewArray)
# # Out    Zero


# MIN FUNCTOIN
# YEH LIST KE ANDAR TEXT RAHENGA TABHI USE KAR SAKTE HAI
# # LIST ME MINIMUM  VALUE KONSI HAI VO FIND KARTA HAI
# Myarray = [10, 20, 30, 40, 50, 60, 10]
# MyText = ['Name', 'Age', 'Gender', 'Address', 'Dob', 'AdharCard', 'PanCard', 'Zero']
#
# NewArray = min(Myarray)
# print(NewArray)
# # out  10
#
# NewArray = min(MyText)
# print(NewArray)
# out  address


# SORT FUNCTION
# YEH FUNCTON HAM USE KARTE LIST KA DATA SERIALWISE LAGABNE KE LIYE JAISE 1,2,3,4,5 FORMAT ME YA FHIR A,B,C,D FORMATE ME

# Myarray = [10, 50, 80, 0, 90, 9, 10]
# NEWSORT = sorted(Myarray)
# # out : [0, 9, 10, 10, 50, 80, 90]
# MyText = ['Name', 'Age', 'Gender', 'Address', 'Dob', 'AdharCard', 'PanCard', 'Zero']
# NEWSORT = sorted(MyText)
# print(NEWSORT)
# out  : ['Address', 'AdharCard', 'Age', 'Dob', 'Gender', 'Name', 'PanCard', 'Zero']


# reverse() function
# YEH FUNCTION LIST KO  DIRECTLY REVERSE KAR DETA HAI
# AGAR AAP VARIABLE BANAKE REVERSE KARONGE TO MAHI HOGA ISE DIRECTLT KARNA PADTA HAI
# Myarray = [10, 50, 80, 0, 90, 9, 10]
# Myarray.reverse()
# print(Myarray)


# index()   function
# YEH FUNCTION SEARCH KARTA HAI OR BATA HAI KI SEARCH KI HUI VALUE KONSE INDEX PAR HE ISLIYE ISAKA NAM INDEX RAKHA HAU HAI
# MyIndex = [10, 10, 10, 2, 3, 34, 4, 5, 65]
# NewIndex = MyIndex.index(2)
# print(NewIndex)
# Out : 3rd index par value hai


# NEW START
# def nums(a, b):
#     if a < b:
#         out = [x for x in range(b)]
#         print(out)
#
# nums(1,4)

a = "fff"

print (int(a, 16))