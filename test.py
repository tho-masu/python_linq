from python_linq import enumerable

lst=[[0,'a'],[1,'b'],[2,'c'],[3,'d'],[4,'e'],[5,'f']]
dct={0:1}
enumerable(lst).where(lambda x:x[0]>=1).skip(1).print()
print(enumerable(lst).lastCall(lambda x:x[0]<=-1))
enumerable(lst).reverse().print()