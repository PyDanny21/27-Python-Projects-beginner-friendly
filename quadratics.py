#ax**2+bx+c=0
import math
def quadratic_equt(a,b,c):
    rt = b ** 2 - (4 * a * c)
    ans1 =math.sqrt(rt)
    #print(ans1)
    top=-b+ans1
    down=2*a
    result1 = top / down

    rt2 = b ** 2 - (4 * a * c)
    ans2 =math.sqrt(rt2)
    #print(ans2)
    top2=-b-ans2
    down2=2*a
    result2 = top2 / down2

    print ('x1={} x2={}'.format(result1,result2))

a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))


quadratic_equt(a,b,c)