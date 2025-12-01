
n = int(input())
for i in range(1,n+1):
    if i == 1 :
        print(' '*(n-i) + '*'*i + '*'*(i-1))
    elif i == n :
        print(' '*(n-i) + '*'*i + '*'*(i-1))
    else :
        print (' '*( n - i) + '*'+' '*(i-1) + ' '*(i-2)+'*')
