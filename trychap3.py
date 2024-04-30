guests=['brian','alex','allan','sharon']

print(f"hello,{guests[0].title()} you have been invited to Lucy's dinner")
print(f"hello,{guests[1].title()} you have been invited to Lucy's dinner")
print(f"hello,{guests[2].title()} you have been invited to Lucy's dinner")
print(f"hello,{guests[3].title()} you have been invited to Lucy's dinner")

not_make=guests.pop(0)
print(not_make)
guests.insert(0,'waweru')
print(f"hello,{guests[0].title()} you have been invited to Lucy's dinner")
print(f"hello,{guests[1].title()} you have been invited to Lucy's dinner")
print(f"hello,{guests[2].title()} you have been invited to Lucy's dinner")
print(f"hello,{guests[3].title()} you have been invited to Lucy's dinner")

