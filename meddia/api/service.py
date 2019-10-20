from abc import ABC, abstractmethod

class Service(ABC):

    @abstractmethod
    def getServiceFunctions():
        """Get the available calls to the service"""
        raise NotImplementedError

    @abstractmethod
    def getServiceStatus():
        """Get status of the service, very usefull when the service has external dependencies"""
        raise NotImplementedError

    @abstractmethod
    def start():
        """Initial function called to start the service."""
        pass

    @abstractmethod
    def stop():
        """Final function called to end the service."""
        pass

    @abstractmethod
    def reset():
        """Function called when restarting the service."""
        pass
