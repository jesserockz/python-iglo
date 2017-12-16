# Python iGlo

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

