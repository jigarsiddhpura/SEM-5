class Flight:
    def __init__(self, flight_number, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.passengers = []
    def display_flight_info(self):
        return f"Flight {self.flight_number} to {self.destination} at {self.departure_time}"
    def available_seats(self):
        return self.capacity - len(self.passengers)
    def book_ticket(self, passenger):
        if self.available_seats() > 0:
            self.passengers.append(passenger)
            return True
        else:
            return False
    def reschedule_flight(self, new_departure_time):
        self.departure_time = new_departure_time
    def cancel_reservation(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            return True
        else:
            return False
    def refund_ticket(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            return True
        else:
            return False
    def prioritize_reservations(self):
        # Sort passengers by a priority criterion (e.g., frequent flyer status)
        self.passengers.sort(key=lambda passenger: passenger.priority, reverse=True)

class Passenger:
    def __init__(self, name, age, priority=0):
        self.name = name
        self.age = age
        self.priority = priority
    def __str__(self):
        return f"{self.age}, Age: {self.age}, Priority: {self.priority}"
    
class Reservation:
    def __init__(self, flight, passenger):
        self.flight = flight
        self.passenger = passenger
    def display_reservation(self):
        return f"Reservation: {self.passenger.name} on {self.flight.display_flight_info()}"
    
# Usage example:
if __name__ == "__main__":
    # Create a Flight
    flight1 = Flight("F001", "New York", "12:00 PM", 150)
    # Create Passengers
    passenger1 = Passenger("Alice", 30, 5)
    passenger2 = Passenger("Bob", 25, 2)
    passenger3 = Passenger("Charlie", 45, 4)
    # Book Tickets
    flight1.book_ticket(passenger1)
    flight1.book_ticket(passenger2)
    flight1.book_ticket(passenger3)
    # Display Flight Info and Passengers
    print(flight1.display_flight_info())
    for passenger in flight1.passengers:
        print(passenger)
    # Reschedule Flight
    flight1.reschedule_flight("2:00 PM")
    print("Rescheduled to:", flight1.departure_time)
    # Cancel Reservation
    if flight1.cancel_reservation(passenger2):
        print(f"{passenger2.name}'s reservation has been canceled.")
    # Refund Ticket
    if flight1.refund_ticket(passenger3):
        print(f"Ticket refunded for {passenger3.name}.")
    # Display Passengers after changes
    print("Passengers after changes:")
    for passenger in flight1.passengers:
        print(passenger)
    # Prioritize Reservations
    flight1.prioritize_reservations()
    print("Passengers after prioritizing:")
    for passenger in flight1.passengers:
        print(passenger)
    # Create Reservation
    reservation = Reservation(flight1, passenger1)
    print(reservation.display_reservation())