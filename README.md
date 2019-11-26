# Python iGlo

## Unmaintained
The iGlo range of lights are based on ESP8266 chips and are
therefore compatible with a vast number of open source firmwares. 
As you can't retrieve the state from the stock firmware I advise you
flash an alternative.
 
 
----------



A library to control iGlo based RGB lights.

I am not sure if getting the current state from the light is supported,
so it is not in this library.

## Example usage

```python
>>> from iglo import Lamp
>>> lamp = Lamp('LAMP_ID','LAMP_IP_ADDRESS', 'LAMP_PORT')

>>> lamp.rgb(255,255,0)
>>> lamp.brightness(100)
>>> lamp.white(255)
>>> lamp.switch(False)
```

