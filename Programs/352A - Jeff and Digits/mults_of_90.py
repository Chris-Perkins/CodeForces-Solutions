# used to help me figure out 352a

for i in range(int(1e20)):
    f = False
    t_i = i*90
    while(t_i > 0):
        if t_i % 10 != 5 and t_i != 0:
            f = True
            break
        t_i //= 10
    if not f:
        print("%d" % (i * 90))
        
    if i % 1000000 == 0:
        print("reached index %d" % i)