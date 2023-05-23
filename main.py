## 함수(=메서드) 선언부
def add_func(n1, n2) :
    result = n1 + n2
    return result

def sub_func(n1, n2) :
    return n1 - n2

def mul_func(n1, n2) :
    return n1 * n2

def div_func(n1, n2) :
    return n1 / n2

def squ_func(n1) :
    return n1**
    

## 전역 변수부(= 인스턴스 변수)
num1, num2, res = 100, 200, 0

## 메인 코드부 = main()메서드
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = mul_func(num1, num2)
print(num1, '*', num2, '=', res)

res = div_func(num1, num2)
print(num1, '/', num2, '=', res)

res = squ_func(num1)
print(num1, '^ 2 =', res)
