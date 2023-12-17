
with open('D:\\SEM-5\\PYTHON\\EXPERIMENTS\\EXP6\\file1.txt', 'r') as file_a, open('D:\\SEM-5\\PYTHON\\EXPERIMENTS\\EXP6\\file2.txt', 'r') as file_b, open('D:\\SEM-5\\PYTHON\\EXPERIMENTS\\EXP6\\result.txt','w') as file_c:
    fa,fb = file_a.readlines(), file_b.readlines()
    fi,fj = len(fa), len(fb)
    print(fi+fj)
    print(int(fa[1].strip()),type(int(fa[1].strip())))
    i,j = 0,0
    while i<fi and j<fj:
        if int(fa[i].strip()) > int(fb[j].strip()):
            file_c.write((fb[j].strip())+'\n')
            j+=1
        elif  int(fa[i].strip()) < int(fb[j].strip()):
            file_c.write((fa[j].strip())+'\n')
            i+=1
        else:
            file_c.write((fa[i].strip())+'\n')
            file_c.write((fb[j].strip())+'\n')
            i+1
            j+=1
    while i<fi:
        file_c.write(fa[i].strip()+'\n')
        i+=1       
    while j<fj:
        file_c.write(fb[j].strip()+'\n')
        j+=1