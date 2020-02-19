def fileNaming(names):
    arr = []
    for val in names:
        if val not in arr:
            arr.append(val)
            continue
        for i in range(1,len(arr)+1):
            if val+"("+str(i)+")" not in arr:
                arr.append(val+"("+str(i)+")")
                break
    return arr

def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names
