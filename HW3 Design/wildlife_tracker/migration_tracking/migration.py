from typing import Any, Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class Migration:

     def __init__(self, 
                 migration_id: int, 
                 status: str = "Scheduled", 
                 current_location: Optional[int] = None, 
                 current_date: Optional[str] = None) -> None:
        self.migration_id = migration_id
        self.status = status
        self.current_location = current_location
        self.current_date = current_date
    
