
presents = []
with open("in", "r") as file:
    presents = list((int(l),int(w),int(h)) for l,w,h in (x.split("x") for x in file.read().split("\n")))

total_area = 0
total_length = 0
for present in presents:
    l,w,h = present
    slack = min(l*w,w*h,h*l)
    area = (2*l*w) + (2*w*h) + (2*h*l)
    total_area += area + slack    
    s,b = sorted([l,w,h])[:2]
    total_length += s*2 + b*2 + (l*w*h)


print(total_area)
print(total_length)

