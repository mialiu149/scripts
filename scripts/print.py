f = open("test.log")
for line in f:
    froot = line.strip().split()[7]
    print 'hadoop fs -get ' + froot +' /nfs-7/userdata/mliu/onelepbabies/'+ froot.split('/')[-1]
