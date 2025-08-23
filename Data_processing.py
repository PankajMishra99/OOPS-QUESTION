from typing import Protocol,List
class DataTransformer(Protocol):
    def transform(self,data:str)->str:
        pass

class LowerCaseTransform:
    def transform(self,data:str)->str:
        return data.lower()

class RemoveSpaceTransform:
    def transform(self,data:str)->str:
        return data.replace(' ','')

class ReverseTextTransform:
    def transform(self,data:str)->str:
        return data[::-1]

class Pipeline:
    def __init__(self,transform:List[DataTransformer]):
        self.transform=transform
    
    def Transform(self,message):
        for trans in self.transform:
            print(trans.transform(message))

if __name__=="__main__":
    pipe=Pipeline([LowerCaseTransform(),RemoveSpaceTransform(),ReverseTextTransform()])
    pipe.Transform('Hello Python')