import random , time

#here generate main list with empy items
mainList = []
#for i in range(0,91):
  #mainList.append(0)

#output list
def outputer():
    temp_list = []
    h = 0
    x = 9
    for i in range(0,9):
        for j in range(h,x):
            temp_list.append(mainList[j])
        print(temp_list)
        x+=9
        h+=9
        temp_list = []

#fill list with random number
def rand_filler():
    for i in range(0,81):
        mainList[i] = random.randint(1,9)
        #time.sleep(0.1)
    #print(mainList)

#FILL
def generator_of_normal_things():
    normList = []

    for i in range(0,9):
        step = True
        while step:
            x = random.randint(1,9)
            if(normList.count(x) >= 1):
                pass
            else:
                normList.append(x)
                step = False
        mainList.append(x)
    #print(mainList)

# 12 23 34 45 56 67 78 89 91
#generator with check horizontal and vertical
def checker():
    for i in range(0,9):
        



def main():
    #rand_filler()


    generator_of_normal_things()
    outputer()
    print(mainList)
if __name__ == '__main__':
    main()
