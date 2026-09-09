a = ['apel', 'kunyit', 'ceri', 'durian']

print(len(a))
print(a[1])
print(a[1:3])
# ganti 
a[3] = 'beri'
a.insert(3, 'mangga')
a.pop(2)
print(a)
b = ['manggis', 'pepaya']
a.extend(b)
print(a)