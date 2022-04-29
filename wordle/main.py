gword = 'nitin'

uword = 'niton'


g=[]
gi=[]
y=[]
yi=[]

for i in gword:
    green =[]
    green_index = []
    yellow = []
    yellow_index = []
    for j in uword:
        if i==j:
            if gword.index(i)==uword.index(j):
                green.append(i)
                green_index.append(uword.index(i))
            
            else:
                yellow.append(i)
                yellow_index.append(uword.index(i))
    if len(list(set(green)))>0:g.append(list(set(green))[0])
    if len(list(set(green_index)))>0:gi.append(list(set(green_index))[0])
    if len(list(set(yellow)))>0:y.append(list(set(yellow))[0])
    if len(list(set(yellow_index)))>0:yi.append(list(set(yellow_index))[0])   

print(g)                    
print(gi)
print(y)
print(yi)
# print(list(set(green)))                    
# print(list(set(green_index)))
# print(list(set(yellow)))
# print(list(set(yellow_index)))