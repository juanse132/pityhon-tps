def conservation(celsius):
    f= (celsius-32) * (5/9)
    return f


for celsius in range(0,130,10):
    cambio = (conservation(celsius))
    print(f"{celsius} == {cambio}")

    


