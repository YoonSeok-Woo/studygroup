N= int(input())
if N%2:
    print("SK")
else:
    print("CY")


'''
N==1:
SK 승
N==2:
SK 1 CY 1
CY 승
N==3:
SK 3
SK 승
N==4:
SK 1 CY 3
SK 3 CY 1
CY 승
N==5:
N==2(CY)+3(SK)
N==3(SK)+2(SK)
SK 승
N==6:
N==3(SK)+3(CY)
N==2(CY)+4(CY)
N==4(CY)+2(CY)
N==1(SK)+5(CY)
N==5(SK)+1(CY)
CY 승
대충 짝수면 CY가 이기고 홀수면 SK가 이긴다
'''