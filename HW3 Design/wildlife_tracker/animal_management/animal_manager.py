from typing import List, Any, Optional

from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat

class AnimalManager:

    def __init__(self) -> None:
        animals: dict[int, Animal] = {}

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

    def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
        pass
    
    def remove_animal(animal_id: int) -> None:
        pass
