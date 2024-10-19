import websockets
import json
class HCClient():
    def __init__(self,ws_url:str="wss://hack.chat/chat-ws"):
        pass
    async def join(self,chann:str,nick:str,pws:str|None=None):
        "(re-)Connect websocket and join a channel."
        pass
    async def chat(self,msg:str):
        "Send a message to current channel."
        pass
    async def whisper(self,text:str,target:str):
        "Send a whisper to given user."
        pass
    async def recv(self):
        "Recvive a raw message from current channel."
        pass

    
