
class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights_for_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result

    def search_flights_from_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city:
                result.append(flight)
        return result

    def search_flights_between_cities(self, city1, city2):
        result = []
        for flight in self.flights:
            if (flight.source == city1 and flight.destination == city2) or \
               (flight.source == city2 and flight.destination == city1):
                result.append(flight)
        return result
def main():
    flight_table = FlightTable()

    # Adding flight data
    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Select search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.search_flights_for_city(city)
    elif choice == 2:
        city = input("Enter the city: ")
        result = flight_table.search_flights_from_city(city)
    elif choice == 3:
        city1 = input("Enter the first city: ")
        city2 = input("Enter the second city: ")
        result = flight_table.search_flights_between_cities(city1, city2)
    else:
        print("Invalid choice")
        return

    if result:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")
    else:
        print("No flights found for the given criteria")

if __name__ == "__main__":
    main()