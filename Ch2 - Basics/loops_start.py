#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    # while(x<5):
    #     print(x)
    #     x += 1

    # TODO: define a for loop
    # for i in range(5,10):
    #     print(i)

    # TODO: use a for loop over a collection
    # days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # for i in days:
    #     print(i)

    # TODO: use the break and continue statements
    # for i in range(5,10):
    #     # if i == 7:
    #     #     break
    #     if i % 2 == 0:
    #         continue
    #     print(i)

    # TODO: using the enumerate() function to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, d in enumerate(days):
        print(i,d)
  
if __name__ == "__main__":
    main()
