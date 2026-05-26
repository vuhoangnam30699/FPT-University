X = ['chó', 'mèo', 'lợn', 'gà']

# In ra các loài vật trong danh sách

for w in X:
     print(w)

# In ra các loài vật trong danh sách trừ mèo
    
for x in X:
    if x == 'mèo':
        continue
    print(x)
    
# In ra các loài vật trong danh sách, nếu gặp mèo thì dừng lại
for z in X:
    if z == 'mèo':
        break
    print (z)
