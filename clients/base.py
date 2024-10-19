class ChatClient():
    """Base class for all chat clients."""
    async def join(self,*args,**kwargs):
        #TODO:Join a channel(group) with given arguments.
        raise NotImplemented()
    async def chat(self,*args,**kwargs):
        #TODO:Send a chat message
        raise NotImplemented()
    async def whisper(self,*args,**kwargs):
        #TODO:Send a whisper to given user
        raise NotImplemented()
    async def recv(self,*args,**kwargs):
        #TODO:Recvive a raw message from current channel.
        raise NotImplemented()
    