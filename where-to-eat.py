import os

class Restauraunt:
    def __init__(self, name, *args):
        self.score = 1
        if (len(args) > 0):
            self.score = args[0]
        self.name = name

    def prompt(self, otherPlace):
        options = "\nOptions:\n - no\n - meh\n - yes \n - BIG YES\n\n >> "
        response = input(
            f"Would you prefer {self.name} over {otherPlace.name}?{options}")
        return response.lower().replace(" ", "")

    def __repr__(self):
        return f"We decided on {self.name}, we're going."


class Restauraunts:
    def __init__(self):
        self.places = [  # change these
            Restauraunt("Choice A"),
            Restauraunt("Choice B", 1.1),
            Restauraunt("Choice C", .7),
            Restauraunt("Choice D")
        ]
        self.winningScore = -100
        self.winner = None

    @staticmethod
    def clear():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def getPlaces(self, place):
        try:
            return place, self.places[self.places.index(place) + 1]
        except:
            return [place, Restauraunt("just stay at home", .5)]

    def displayProgress(self):
        if self.winner:
            print(f"leaning towards {self.winner.name} so far...\n\n")

    def decide(self, husband, wife):
        decision = "none"
        score = 0
        self.clear()
        for place in self.places:
            self.displayProgress()
            choices = self.getPlaces(place)
            decision = [husband.score(choices), wife.score(choices)]
            score = (decision[0] + decision[1])/2
            if score > self.winningScore:
                self.winningScore = score
                self.winner = place
            if score > 3:
                self.winner = place
                self.clear()
                print("happy wife, happy life")
                break
            self.clear()
        return self.winner


class Husband:

    def __init__(self):
        self.name = "John"  # change name here
        self.no = -1
        self.meh = .3
        self.yes = .5
        self.bigyes = .7

    def weigh(self, place, response):
        weight = getattr(self, response)
        return place.score * weight

    def score(self, options):
        place = options[0]
        otherPlace = options[1]
        print(f"\n\n/================= \n|  {self.name}:\n|\n")
        while True:
            response = place.prompt(otherPlace)
            if hasattr(self, response):
                return self.weigh(place, response)
            print("\n\nI'm not understanding you. Try again?\n\n")


class Wife(Husband):

    def __init__(self):
        super().__init__()
        self.name = "Jane"  # change name here
        self.yes = .7
        self.bigyes = 9000


if __name__ == '__main__':
    wife = Wife()
    husband = Husband()
    places = Restauraunts()
    result = places.decide(husband, wife)
    print(result)
