#  ----------------------- Day 12 ----------------------
#  ----- Loops  -------------------------
#  --- Date: 28.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def main():
    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\n(Enter 'quit' when you are finished.) "
    while True:
        city = input(prompt)
        
        if city == 'quit':
           break
        else:
            print("I'd love to go to " + city.title() + "!")
        
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)

    
if __name__ == "__main__":
    main()


# Sample output
    # Please enter the name of a city you have visited:
    # (Enter 'quit' when you are finished.) LAHORE
    # I'd love to go to Lahore!

    # Please enter the name of a city you have visited:
    # (Enter 'quit' when you are finished.) quit
    # 1
    # 3
    # 5
    # 7
    # 9