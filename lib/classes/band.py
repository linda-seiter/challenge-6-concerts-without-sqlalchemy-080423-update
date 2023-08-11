class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name:
            self._name = name

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and hometown and not hasattr(self, "hometown"):
            self._hometown = hometown

    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue, date):
        return Concert(date=date, band=self, venue=venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


from classes.concert import Concert
