def city_country_data(city, country, population=0):
    if population:
        data=(city+", "+country+":Population- "+str(population)).title()
    else:
        data=(city +", " + country).title()
    return data
