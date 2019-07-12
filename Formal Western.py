MP = int(input("Enter Market Price: "))
LP = int(input("Enter Lender Price: "))
sum = MP + LP
avg1 =sum/2

Rateprice = int(input(" Rating for Price: "))
Ratework = int(input(" Rating for Work: "))
Ratefashion = int(input(" Rating for Fashion: "))
Ratebrand = int(input(" Rating for Brand: "))
Ratedep = int(input(" Rating for Depreciation: "))
minper = int(input(" Min percentage for average price: "))
maxper = int(input(" Max percentage for average price: "))

weigtage4price= 19
wightage4work= 14
weightage4fashion= 25
weightage4brand=22
weightage4depreciation= 20

rent1=minper*Rateprice*weigtage4price+minper*Ratework*wightage4work+minper*weightage4fashion*Ratefashion+minper*Ratebrand*weightage4brand+minper*weightage4depreciation*Ratedep

rent2=maxper*Rateprice*weigtage4price+maxper*Ratework*wightage4work+maxper*weightage4fashion*Ratefashion+maxper*Ratebrand*weightage4brand+maxper*weightage4depreciation*Ratedep

print"Max rent range is",rent1
print"Min rent rent",rent2

