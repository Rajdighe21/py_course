nameStr = "Raj TUKARAM DIGHE WELLCOME"

# HOW TO CALLED STRING INDEX
# newNameF=nameStr[0]  #get first index number
# newNameL=nameStr[-1]  #get last index number
# newNameN=nameStr[9]  #get Nineth index number
# print(newNameN)


# HOW TO SLICE IN STRING / MEANS GET DATA FROM : TO
# sliceIng_one = nameStr[0:12]  #ISAME VALUE START 0 SE HOGI OR END 12 PAR
# sliceIng_two = nameStr[0:15:2]  #ISAME VALUE START 0 SE HOGI OR END 15 PAR OR 2 KA INCREMENT HONGA ISME
# sliceIng_three = nameStr[0::1] #######  ISME TIN VALUE HE BICH WALI EMPTY HE USKA MATLAB YE HE KI VO LAST TAK COUNT KARENGI
#
# #REVERSE  SCLICING
# sliceIng_rev_one = nameStr[-1:-10] #ABHI VALUE REVERSE PRINT HOGI
# sliceIng_rev_two = nameStr[-1::-1] #ABHI ULTA PRINT HOGA SAB
#
# print(sliceIng_rev_two)


#STRING ITERATION
# lenTh=len(nameStr)
#
# for i in range(lenTh)
#     print(nameStr[i]) # Yeh string ko print karega
# for i in range(lenTh-1,-1,-1):  #YEH WALA STRING KO REVRSE ME PRINT KARENGA
#     print(nameStr[i])


#STRING FORMATE

# formatesDemo = "hello namste {} dighe".format("raj")
# print(formatesDemo)