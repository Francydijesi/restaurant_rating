# your code goes here
import sys
import random

def rate_restaurant ():
    """ Creates an alterable dictionary of restaurant names and ratings.

    First creates dictionary of restaurants and ratings, then asks the user
    for updated ratings if so wished.

    Prints alphabatized final restaurant names and ratings.
    """
    restaurant_ratings = {}
    restaurant_file = open(sys.argv[1])
    for line in restaurant_file:
        line = line.strip()
        restaurant, rating = line.split(":")
        restaurant_ratings[restaurant] = rating
    raw_input("Hi there! What's your name?")
     
    key = raw_input("Input a Restaurant name: ")
    value = int(raw_input("Insert your rate: "))
    restaurant_ratings[key] = value
    
    # Initiates possible user change of restaurant ratings.
    answer = ''
    random_res = random.choice(restaurant_ratings.keys())
    print "{} : {}".format(random_res, restaurant_ratings[random_res] )
    answer = raw_input("Input the new rating or quit:")

    while answer != 'q':
      restaurant_ratings[random_res] = int(answer)
      random_res = random.choice(restaurant_ratings.keys())
      print "{} : {}".format(random_res, restaurant_ratings[random_res] )
      answer = raw_input("Input the new rating or quit:")

    # Outputting a list of alphabatized keys from restaurant_ratings dictionary.
    for res_name, res_rating in sorted(restaurant_ratings.items()):
        print "{} : {}" .format(res_name, res_rating)


rate_restaurant()