

# 定长队列 put get合体

class dva_l_queue():
    
    def sum(q):
        out = 0
        for _ ,e in enumerate(q.__list):
            out+=e
        return out
    
    def put(g,a):
        out = g.__list[g.__head]
        g.__list[g.__head] = a
        g.__head += 1
        if(g.__head>= len(g.__list)):
            g.__head = 0
        return out
    
    
    def __init__(g,len,x):
        g.__list = list()
        for _ in range(len):
            g.__list.append(x)
        g.__head = 0