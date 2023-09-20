from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class for all command operations.
    """
    @abstractmethod
    def execute(self, stack):
        """
        Execute the command using the provided stack.
        """
        pass