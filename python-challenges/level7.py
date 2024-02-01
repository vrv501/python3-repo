start = "90052"
numX = 1
while True:
    with open(f"/workspaces/python3-repo/zipper/{start}.txt", "r") as f:
        con = f.read()
    con = con.split()
    print(con)
    numFound = False
    for num in con:
        if num.isnumeric():
            start = num
            numFound = True 
    
    if not numFound:
        break

    numX +=1
print(numX)



