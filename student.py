from datetime import date, timedelta

class Student:
    """A student class as a base for method testing"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)
        return self.end_date + days
    
    def alert_santa(self):
        self.naughty_list = True






