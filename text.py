'''def getdifference(a, b):
    if isinstance(a, (int)):
        return a - b
    else:
        return "press either int or float"
def getsum(a,b):
    return a+b

def getValues(a,pi=3.141,c=None):
    if c is not None:
        print(c)
        return a+pi+c
    return a+pi


print("hi")
if __name__ == '__main__':
    a = 4
b = 5
 print((a == b))
    print(id(a))
    print(id(b))
    print(getdifference(a, b))

    print(getsum(a,b))

print(getValues(a,10,5))



import xlrd
loc=("sample1.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)

for i in range(sheet.nrows):
    print(sheet.cell_value(i,1))
'''

#fo = open("foo.txt", "wb")
#print ("Name of the file: ", fo.name)
#print ("Closed or not : ", fo.closed)
#print ("Opening mode : ", fo.mode)
#fo = open("foo.txt", "w")
#fo.write( "Python is a great language.\nYeah its great!!\n")
#fo = open("foo.txt", "r+")
#str1 = fo.read(10)
#print("Read String is : ", str1)
import os
#os.rename( "foo.txt", "foo1.txt" )
os.remove("foo1.txt")
#fo.close()