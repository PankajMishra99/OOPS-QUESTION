class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.engines=[]
        self.features=[]
    
    def display_car_info(self):
        return f"Car Name {self.brand} and model {self.model} "
    
    class Engine:
        def __init__(self,engine_type,horse_power):
            self.engine_type=engine_type
            self.horse_power=horse_power
        
        def display_engine_info(self):
            return f"Engine type {self.engine_type} and engine power {self.horse_power}"
    class Feature:
        def __init__(self,feature_name,desc):
            self.feature_name=feature_name
            self.desc=desc
        
        def display_feature_info(self):
            return f"Feature {self.feature_name} and description {self.desc}"
    
    def add_engine_feature(self,engine,feature):
        self.engines.append(engine)
        self.features.append(feature)


car=Car('Maruti',2025)
engine1 = car.Engine('4 stroke','100hp')
engine2 = car.Engine('4 stroke','110hp')

feature1=  car.Feature('BS6','AI')
feature2=  car.Feature('BS6','AI camera')

car.add_engine_feature(engine=engine1,feature=feature1)
car.add_engine_feature(engine=engine2,feature=feature2)

for engine in car.engines:
    print(engine.engine_type,engine.horse_power)

print(car.display_car_info())
