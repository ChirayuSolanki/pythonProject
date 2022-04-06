inputData = input("Enter main string : ")
subStringData = input("Enter sub string :")

stopIndex = len(inputData)-len(subStringData)

for i in range(0, stopIndex+1):
    tempStr = []
    for j in range(i,i+len(subStringData)):
        tempStr.append(inputData[j])
    interimData = ''.join(tempStr)
    #print(interimData)
    if(interimData.lower() == subStringData.lower()):
        print("element found at ",i)
        break