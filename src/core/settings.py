import os
from dataclasses import dataclass


@dataclass
class Settings:
    db_url: str = os.getenv('DB_URL') or 'sqlite+aiosqlite:///db.db'
