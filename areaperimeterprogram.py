# author: Elisabeta Bayer
# date: 4/11/2025
# Yr 10 DGT Area Perimeter program

# TODO 
# write a program that calculates the area and perimeter
# ask user for width and loop until they enter a number that is more than zero
def num_check():
    keep_going = ""
    while keep_going == "":
            while True:
                width = input("width: ")
                try:
                     width = float(width)
                     if width > 0:
                        break 
                except (ValueError, TypeError):
                    print("Please enter a number more than 0\n")

            while True:
                height = input("height: ")
                try:
                     height = float(height)
                     if height > 0:
                        break 
                except (ValueError, TypeError):
                    print("Please enter a number more than 0\n")    

            perimeter = 2 * (width + height)
            area = width * height    
            print(f"Perimeter: {perimeter}units, area: {area}units")
            keep_going = input(f"press <ENTER> to continue, or any other key to quit. Thank you!")
            if keep_going == "":
                print("Program loops")
            else:
                print("Program ends") 
    

num_check()



        
            




 
    

    

