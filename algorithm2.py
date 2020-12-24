def fastest_way(x,y):
    for i in range(y) :
        x=x*2
        print("double",x)
        if x == y or x > y :
            break
        while y/2 < x and y%2==0:
            x=x-1
            print('minus',x)
            if x == y/2:
                print('double',x)    
                print("done")
    while x > y :
        x=x-1
        print('minus',x)
        if x==y:
            print("done")

if __name__ == "__main__":
    fastest_way(3,12)
            

        
    
    

        





    