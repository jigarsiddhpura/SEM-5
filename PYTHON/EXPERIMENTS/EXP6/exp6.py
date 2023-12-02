def getValueAtIndex(content,index):
    return int(content[index].strip())



#     open('sort.txt','a') as s:
# def addValueInFile(value):
#         s.write(str(value)+"\n")

with open('file1.txt','r') as f, open('file2.txt','r') as g, open('sort.txt','w') as s:
    i = j = 0
    k = 1

    content1, content2 = f.readlines(), g.readlines()

    len1 = len(content1)
    len2 = len(content2)

    while(i<len1 and j<len2):
        value1, value2 = int(content1[i].strip()), int(content2[j].strip())
        if value1 < value2:
            s.write(str(value1)+"\n")
            i+=1
        elif value1 > value2:
            s.write(str(value2)+"\n")
            j+=1
        else: 
            s.write(str(value1)+"\n")
            s.write(str(value2)+"\n")
            i+=1
            j+=1

        
    
    while(i<len1):
        value1 = content1[i].strip()
        s.write(str(value1)+"\n")
        i+=1
    
    while(j<len2):
        value2 = content2[j].strip()
        s.write(str(value2)+"\n")
        j+=1
        
    
        