# g_b = 3
def t1():
    global g_b
    g_b = 2
def t2():
    # global g_b
    print(g_b)
if __name__ == '__main__':
    t1()
    t2()