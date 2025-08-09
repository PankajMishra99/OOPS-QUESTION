class Parking:
    parking_slot = 0
    def __init__(self,slot_no,vehicle_type):
        self.vehicle_type=vehicle_type
        self.slot_no=slot_no
        self.is_accuipied= False
        Parking.parking_slot += 1

    
    def park_vehicle(self):
        if not self.is_accuipied:
            self.is_accuipied=True
            print(f"Parking slot {self.slot_no} is accoupied")

        else:
            print(f"{self.slot_no} is already accuipied..")
    
    def parking_remove(self):
        if self.is_accuipied:
            self.is_accuipied=False
            print(f"Parking slot {self.slot_no} is free for parking")
        else:
            print(f"Parking slot {self.slot_no} is already avialble..")
    
    def __str__(self):
        status = 'Accuipied' if self.is_accuipied else 'Free'
        return f"{self.vehicle_type} - slot no : {self.slot_no} with {status}"

if __name__=="__main__":
    system = Parking(1,'car')
    system.park_vehicle()
    # system.parking_remove()
    print(system)