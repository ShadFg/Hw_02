class Human:

    def __init__(self, name, secondName, thirdName, birthday, phoneNumber, city, country, homeAddress):
        self.name = name
        self.secondName = secondName
        self.thirdName = thirdName
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        self.city = city
        self.country = country
        self.homeAddress = homeAddress

    def setHumanInfo(self, newName, newSecondName, newThirdName, newBirthday, newPhoneNumber, newCity, newCountry, newHomeAddress):
        self.name = newName
        self.secondName = newSecondName
        self.thirdName = newThirdName
        self.birthday = newBirthday
        self.phoneNumber = newPhoneNumber
        self.city = newCity
        self.country = newCountry
        self.homeAddress = newHomeAddress

    def showHumanInfo(self):
        print("\nname -", self.name)
        print("secondName -", self.secondName)
        print("thirdName -", self.thirdName)
        print("birthday -", self.birthday)
        print("phoneNumber -", self.phoneNumber)
        print("city -", self.city)
        print("country -", self.country)
        print("homeAddress -", self.homeAddress)

human = Human("name", "secondName", "thirdName", "birthday", "phoneNumber", "city", "country", "homeAddress")
human.setHumanInfo(
    input("new name - "),
    input("new secondName - "),
    input("new thirdName - "),
    input("new birthday - "),
    input("new phoneNumber - "),
    input("new city - "),
    input("new county - "),
    input("new homeAddress - ")
)

class City():

    def __init__(self, cityName, regionName, countryName, population, mailIndex, cityPhoneNumber):
        self.cityName = cityName
        self.regionName = regionName
        self.countryName = countryName
        self.population = population
        self.mailIndex = mailIndex
        self.cityPhoneNumber = cityPhoneNumber

    def setCityInfo(self, newCityName, newRegionName, newCountryName, newPopulation, newMailIndex, newCityPhoneNumber):
        self.cityName = newCityName
        self.regionName = newRegionName
        self.countryName = newCountryName
        self.population = newPopulation
        self.mailIndex = newMailIndex
        self.cityPhoneNumber = newCityPhoneNumber

    def showCityInfo(self):
        print("\ncityName -", self.cityName),
        print("regionName -", self.regionName),
        print("countryName -", self.countryName),
        print("population -", self.population),
        print("mailIndex -", self.mailIndex),
        print("cityPhoneNumber -", self.cityPhoneNumber)

city = City("cityName", "regionName", "countryName", "population", "mailIndex", "cityPhoneNumber")
city.setCityInfo(
    input("\nnew cityName - "),
    input("new regionName - "),
    input("new countryName - "),
    input("new population - "),
    input("new mailIndex - "),
    input("new cityPhoneNumber - ")
)

human.showHumanInfo()
city.showCityInfo()