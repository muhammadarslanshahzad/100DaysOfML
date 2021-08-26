#  ----------------------- Day 10 ----------------------
#  ----- Dictionaries  -------------------------
#  --- Date: 26.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def main():
    player = {'color':'green','points':5}
    print(player['color'])

    player['color'] = 'red'
    print(player)

    del player['points']
    print(player)


if __name__ == "__main__":
    main()


# Sample output
# green
# {'color': 'red', 'points': 5}
# {'color': 'red'}