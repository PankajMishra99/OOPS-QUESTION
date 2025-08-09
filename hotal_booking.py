class Room:
    def __init__(self,room_no,price_per_night):
        self.room_no=room_no
        self.price=price_per_night
        self.is_book=False
        self.customer_id =None
        self.rooms={}

    def book_room(self,customer_id):
        if not self.is_book:
            self.rooms[customer_id]={
                'room_no': self.room_no,
                'price':self.price
            }
            self.is_book=True
            print(f"{self.room_no} booked successfully for {customer_id}")
        else:
            print('Already Booked')
    
    # def show_avialble_room(self):
    #     if self.rooms:

    def cancil_book(self,customer_id):
        if self.is_book:
            for id in self.rooms:
                if id==customer_id:
                    print(f"Booking for {customer_id} is cancelled..")
                    self.is_book=False
                    self.customer_id=None
                else:
                    raise f"{customer_id} is not avialble in the list.."
        else:
            print('already avilable')

    def calculate_bill(self,night):
        return self.price * night
    
    def __str__(self):
        status = 'booked' if self.is_book else 'Available'
        return f"{self.customer_id} with per night charge {self.price}/night -{status} "

class Single_room(Room):
    def __init__(self,room_no):
        super().__init__(room_no,1500)

class Double_room(Room):
    def __init__(self,room):
        super().__init__(room,2000)

class Tripple_room(Room):
    def __init__(self,room):
        super().__init__(room,2500)

if __name__=="__main__":
    room =[Single_room(101),Double_room(201),Tripple_room(401)]
    for room in room:
        print(room.calculate_bill(2))
    


            
