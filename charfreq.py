string=input("enter a string:")
freq=[None]*len(string)
for i in range(0,len(string)):
    freq[i]=1
    for j in range(i+1,len(string)):
        if(string[i]==string[j]):
            freq[i]=freq[i]+1
            string=string[:j]+'0'+string[j+1:]
print("characaters and their corresponding frequenices:")
for i in range(0,len(freq)):
    if(string[i]!=""and string[i]!='0'):
       print(string[i]+"-"+str(freq[i]))
       
