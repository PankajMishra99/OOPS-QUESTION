class Passenger:
    def __init__(self,name,passport_number):
        self.name=name
        self.passport_number=passport_number
    
    def __str__(self):
        return f"Passenger name {self.name} with passport number {self.passport_number}"
class Flight:
    def __init__(self,flight_no,capacity):
        self.flight_no=flight_no
        self.capacity = capacity
        self.passengers=[]
    
    def book_passengers(self,passenger):
        if len(self.passengers)<=self.capacity:
            self.passengers.append(passenger)
            print(f"{passenger.name} with passport {passenger.passport_number} has been added successfully")
        else:
            print('seat full')
    
    def show_passengers(self):
        if self.passengers:
            for passenger in self.passengers:
                print("passenger name :",passenger)
        print ("No passenger avilable in the Passenger list")
    
    def __str__(self):
        return f"{self.flight_no} with capacity {self.capacity}"
    
class Airline:
    def __init__(self):
        self.flights=[]
    
    def add_flight(self,flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_no} has been added successfully..")
    
    def find_flight(self,flight_no):
        if self.flights:
            for flight in self.flights:
                if flight.flight_no==flight_no:
                    return flight
            # return None
        else:
            print('No any flight avilable..')
if __name__=="__main__":
    airline = Airline()
    # ----------------------------------------
    flight= Flight('A011',200)
    flight.book_passengers(Passenger('Mr.A','P011'))
    flight.book_passengers(Passenger('Mr.B','P012'))

    flight1= Flight('A012',250)
    flight1.book_passengers(Passenger('Mr.A','P021'))
    flight1.book_passengers(Passenger('Mr.B','P022'))
    # -----------------------------------------
    airline.add_flight(flight)
    airline.add_flight(flight1)

    print(airline.find_flight('A011'))


            
