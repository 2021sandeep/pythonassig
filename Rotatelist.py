list=[]
num=int(input("enter the number insert in list \n")
        for i in range(1,num+1)
            print("enter",i,"elements")
            list.append(int(input()))
        print("list before swaping \n",list)
        lenth=len(list)
        list[0],list[length-1]=list[length-1],list[0]
        print("\n list after swapping\n",list)
