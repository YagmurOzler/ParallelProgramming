def calculate_pyramid_height(number_of_blocks):
    height = 0
    
    while number_of_blocks >0:
        height += 1
        number_of_blocks -= height  
        
    if number_of_blocks < 0:
      
        print(f"You can not do a pyramid with this number, you have {number_of_blocks+height} extra blocks left. Try again!")
        height = -1

    return height
answer = -1

while answer < 0:
    blocks= int(input("Enter a number for pyramid "))
    answer = calculate_pyramid_height(blocks)
print(f"Your Pyramid's height is {answer}")
