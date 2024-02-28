from .api import api

routes = [
    ("/api", api),
]

__all__ = ["routes"]
