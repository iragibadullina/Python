#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

num = 7.3245678 
  
# using "%" operator 
print('The value is: %.2f'%num)  
  
# using format() function 
print("The value is: {0:.5f}".format(num))  
  
# using round() function 
print("The value is:",round(num,1)) 
