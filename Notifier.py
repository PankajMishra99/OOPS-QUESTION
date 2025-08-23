from typing import Protocol,List
class Notifier(Protocol):
    def send(self,message:str)->None:
        pass

class Email_notifier:
    def send(self,message:str)->None:
        print(f"Email sent : {message}")

class SMSNotifier:
    def send(self,message:str)->None:
        print(f"SMS Send : {message}")

class PushNotifier:
    def send(self,message:str)->None:
        print(f"Push Notifier : {message}")

class Alert_Call:
    def send(self,notifiers:List[Notifier],message:str)->None:
        for notifier in notifiers:
            notifier.send(message)


if __name__=="__main__":

    notifier_list = [Email_notifier(),SMSNotifier(),PushNotifier()]
    alert = Alert_Call()
    alert.send(notifier_list,'Hello world')
        

