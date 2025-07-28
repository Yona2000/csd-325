#Jonathan Davila 6/10/2025/ assignemnt1_3 100 bottles of beer on the wall
# This script prints the reverse countdown song per the user input.

#This functions take a number and counts down to 1
def countdown(bottles):
    #Loop starts at the number of bottles and counts down by 1 until it hits 1
    for num in range(bottles, 0, -1):
        if num == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("take one down and pass it around, no more bottles of beer on the wall.\n")
        else:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer.")
            print(f"take one down and pass it around, {num -1} bottles of beer on the wall.\n")





def main():
    #try run this code to catch errors
    try:
        #asks the user to enter a number and converts it to an integer
        bottles = int(input("ENTER NUMBER OF BEER BOTTLES: "))
        #calls the function and passes the numbers the user gave
        countdown(bottles)
        print("Go to the store to buy some more.")
    except ValueError:
        print("Enter a vaild number")



if __name__ == "__main__":
    main()