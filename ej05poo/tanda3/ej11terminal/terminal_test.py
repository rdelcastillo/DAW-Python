from terminal import Terminal

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)