def gen_dic(n):
    square_d={i:i** 2 for i in range(1, n+1)}
    return square_d

n=6
result=gen_dic(n)
print(result)