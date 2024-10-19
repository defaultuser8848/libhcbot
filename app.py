from .clients.base import ChatClient
from .handler import Handler
import asyncio
__all__=["ChatApp"]
class ChatApp():
    def __init__(self):
        self.handlers=[]
        self._event=asyncio.Event()
    def add_handler(self,handler:Handler):
        """Add a handler to this app."""
        self.handlers.append(handler)
    async def stop(self):
        """Stop running."""
        self._event.set()
    async def run(self,cli:ChatClient):
        """Run app via a **joined** client object."""
        while not self._event.is_set():
            pass
    