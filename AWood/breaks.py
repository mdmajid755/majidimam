def stopHere():
    myVar= 1
    print(myVar)
    myVar +=1
    print(myVar)
    return 5

if __name__=='__main__':
    myMainVar = 7
    myMainVar += stopHere()
print(myMainVar)

