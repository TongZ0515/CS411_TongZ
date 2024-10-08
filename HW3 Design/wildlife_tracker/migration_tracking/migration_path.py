from typing import Any, Optional

from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self, 
                 path_id: int, 
                 species: str, 
                 start_date: str, 
                 migration_path_id: int,
                 start_location: Habitat, 
                 destination: Habitat, 
                 duration: int = None) -> None:
        self.path_id = path_id
        self.species = species
        self.start_date = start_date
        self.migration_path_id = migration_path_id
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migration_path_details(path_id) -> dict:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass