# Logger System (Protocol for Logging)
# Requirement:
# Define a Logger protocol with method log(message: str).
# Implement ConsoleLogger, FileLogger, and DatabaseLogger.
# A SystemMonitor should accept any logger.

from typing import Protocol,List
class Logger(Protocol):
    def log(self,message:str):
        pass

class ConsoleLogger:
    def log(self,message:str):
        print(f"[Console] {message}")

class FileLogger:
    def log(self,message:str):
        print(f"[File Logger] {message}")

class DataLogger:
    def log(self,message:str):
        print(f"[DataLogger ] {message}")


def SystemMonitor(logger:List[Logger],message):
    for logs in logger:
        logs.log(message)
if __name__=="__main__":
    system=SystemMonitor([ConsoleLogger(),FileLogger(),DataLogger()],'..Logging successfull..')

