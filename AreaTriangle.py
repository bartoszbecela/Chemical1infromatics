
def triangle_area(base,height):
    if base and height not in range(1,100):
        print("yours values are wrong")
    else:
        print(base * height / 2 )


base = int(input("enter value of triangle base"))
height = int(input("enter value of triangle height"))


triangle_area(base,height)