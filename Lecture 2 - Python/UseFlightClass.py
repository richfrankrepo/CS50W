import FlightClass # iimport the FlightClass module

flight = FlightClass.Flight(3) # create instance of flightclass object
people =["Harry","Ron","Hermione","Ginny"]

for person in people:
    sucess = flight.add_passenger(person)
    if sucess:
        print(f"Added {person} to the flight succesfully")
    else:
        print(f"No available seat for {person}")

