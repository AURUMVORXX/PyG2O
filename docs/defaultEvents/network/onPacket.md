# `event` onPacket
This event is triggered when new packet arrives from the client.

Original: [onPacket](https://gothicmultiplayerteam.gitlab.io/docs/0.3.0/script-reference/server-events/network/onPacket/)

## Parameters
* `dict` **kwargs**:
    * `int` **playerid**: the id of the player who sent the packet.
    * `Packet` **data**: data sended over network from client side.

## Usage
```python
import g2o
        
@g2o.event('onPacket')
def onPacketEvt(**kwargs):
    data = kwargs['data']
    message = data.readString()
    
    print(f'Got packet from {kwargs['playerid']} (bytes used {data.bytesUsed})')
    print(f'Packet says: {message}')
```