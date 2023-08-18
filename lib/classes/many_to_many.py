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
        else:
            return None
            # raise Exception("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and hometown and not hasattr(self, "hometown"):
            self._hometown = hometown
        else:
            return None
            # raise Exception("Hometown must be a non-empty string and it cannot be changed")

    def concerts(self):
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue, date):
        return Concert(date=date, band=self, venue=venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]

    
class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        type(self.all.append(self))

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str) and date:
            self._date = date
        else:
            return None
            # raise Exception("Date must be a non-empty string")
    

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if isinstance(band, Band):
            self._band = band
        else:
            return None
            # raise Exception("Band must be of type Band")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        if isinstance(venue, Venue):
            self._venue = venue
        else:
            return None
            # raise Exception("Venue must be of type Venue")

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

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
        else:
            return None
            # raise Exception("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str) and city:
            self._city = city
        else:
            return None
            # raise Exception("City must be a non-empty string")

    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

    def concert_on(self, date):
        return next(
            (concert for concert in self.concerts() if concert.date == date), None
        )
