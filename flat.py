class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period, unit="£"):
        self.amount = amount
        self.period = period
        self.unit = unit


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, flatmate_list, bill):
        total_days = sum(flatmate.days_in_house for flatmate in flatmate_list)
        weight = self.days_in_house / total_days
        return bill.amount * weight
