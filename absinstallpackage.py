from abc import ABC , abstractmethod
class ABCInstallPackage(ABC):
    
    @abstractmethod
    def install_packet(self, packet:str) -> None:
        pass