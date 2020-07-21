class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():
            return False # return the value False and do not execute any further lines in this function.
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)