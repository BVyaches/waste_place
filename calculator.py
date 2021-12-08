import datetime as dt


class Calculator:

    def __init__(self, limit: int):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_stats(self, days):
        today = dt.date.today()
        days_before = today - dt.timedelta(days=days)
        total = sum(r.amount for r in self.records
                    if days_before <= r.date <= today)
        return total

    def get_today_stats(self):
        return self.get_stats(0)

    def get_week_stats(self):
        return self.get_stats(6)

    def get_remained(self):
        return self.limit - self.get_today_stats()


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            date_format = '%d.%m.%Y'
            self.date = dt.datetime.strptime(date, date_format).date()


class CashCalculator(Calculator):
    USD_RATE = 74.45
    EURO_RATE = 89.51

    def get_today_cash_remained(self, currency='rub'):
        currency_dict = {
            'rub': ('руб.', 1),
            'usd': ('USD', self.USD_RATE),
            'eur': ('EURO', self.EURO_RATE)
        }
        remained = self.get_remained()
        if remained == 0:
            return 'Денег нет'
        currency, rate = currency_dict[currency]
        remained /= rate
        if remained < 0:
            remained = -remained
            return f'Денег нет, долг {remained:.2f} {currency}'
        return f'на сегодня осталось {remained:.2f} {currency}'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remained = self.get_remained()
        if remained > 0:
            return f'Можно съесть что-то с {remained} кКал'
        else:
            return 'Хватит есть'
