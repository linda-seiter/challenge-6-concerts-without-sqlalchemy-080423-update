class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str) and city:
            self._city = city

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

    def concert_on(self, date):
        return next(
            (concert for concert in self.concerts() if concert.date == date), None
        )


from classes.concert import Concert
