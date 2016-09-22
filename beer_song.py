def beers(num_beers):

    while(num_beers > 0):
        print (str(num_beers) + " bottles of beer on the wall")
        print (str(num_beers) + " bottles of beer")
        print ("if one of those bottles should happen to fall")
        num_beers = num_beers - 1
        print (str(num_beers) + " bottles of beer of the wall\n")


beers(99)
