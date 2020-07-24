# SkyTemp

Calculate the Sky Temperature at a given Galactic Latitude and Longitude and frequency, based on the Remazeilles et al. 2014 reprocessing of the Haslam 408 MHz map. 

Example command line usage:
```
python skytempy/skytemp.py haslam408_ds_Remazeilles2014.fits 10 -35 1284
```

Example python code:
```python
import numpy as np
from skytempy import SkyTemp

gl, gb = (0, 0)
s = SkyTemp(0, 0, path_to_fits)
freqs = np.linspace(856, 1712, 12)
temps = s.get_temp(freqs)
print("Temperature of sky at position ({}, {}):".format(gl, gb))
for f, t in zip(freqs, temps):
    print("{} at {} MHz".format(t, f))

```
