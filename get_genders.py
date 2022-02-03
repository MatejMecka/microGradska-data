"""
get_genders.py

This part attempts to guess a persons gender based on the name of the data.
"""
from genderize import Genderize, GenderizeException
from transliterate import translit
from alive_progress import alive_bar

def guessGenders(df):
    sexes = []
    probabilities = []

    # Loop Through 
    with alive_bar(len(df)) as bar:
        for dat in df["Име, име на родител и презиме"]:
            try:
                name = dat.split(" ")[0]
                name_data = Genderize().get([translit(name, reversed=True)])
                sexes.append(name_data[0]['gender'])
                probabilities.append(name_data[0]["probability"])
            except GenderizeException:
                print("Error fetching data from Gender API")
            bar()

    df["Пол"] = sexes
    df["ВеројатностЗаПол"] = probabilities

    return df