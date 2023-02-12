#!/usr/bin/python3
"""magic method for models directory; ensures it's a package"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
