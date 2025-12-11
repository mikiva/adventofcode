answers = []
with open("input.txt", "r") as inp:
    answers = inp.read().split("\n\n")
    
def anyone():
    yes = 0
    
    for ans in [x.replace("\n", "") for x in answers]:
        c = set()
        for a in ans:
            c.add(a)
        yes += len(c)
    return yes

def everyone():
    yes = 0
    tested = set()
    visited = list()

    for group in answers:
        ans = [set(x) for x in group.split("\n")]
        yes += len(ans[0].intersection(*ans))
            
    return yes

print("a", anyone())
print("b", everyone())
