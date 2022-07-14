import math

test_h = int(input("Height of Wall: "))
test_w = int(input("Width of Wall: "))
coverage = 5

def paint_calc(wall_height, wall_width  ):
    number_cans = math.ceil((wall_height * wall_width)/coverage)    
    print(f"You need {number_cans} of cans")

paint_calc(wall_height = test_h, wall_width = test_w)