array = []
def feladat1():
    f = open("Meta/Superbowl.txt", "r" , encoding="utf-8")
    f.readline()

    for x in f:
        print(x)
        array.append(x)
    f.close

def feladat2():
    print("Meccsek szama: ",len(array))


def feladat3():
    
    for item in array:
        x = item.split(";")
        print("eredmeny:",x[3])
        y = x[3].split("-")
        
        print('kulonbseg:', int(y[0])-int(y[1]))

    a = (y[0])
    b = (y[1])
    print(sum(int(a))+ sum(int(b)) /2)
    
    
  
  


    
        


feladat1()
feladat2()
feladat3()
