from typing import Any, Optional

class Animal:

    def __init__(self, 
                animal_id: int,
                species: str,
                age: Optional[int] = None,
                health_status: Optional[str] = None) -> None:
        self.age = age
        self.animal_id = animal_id
        self.species = species
        self.health_status = health_status

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(self, Animal) -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass
                

