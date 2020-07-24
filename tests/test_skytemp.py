import os
import numpy
from skytempy.skytemp import SkyTemp


def test_fileexists():
    file_name = "haslam408_ds_Remazeilles2014.fits"
    assert os.access(file_name, os.R_OK)


def test_skytemp_withfile():
    s = SkyTemp(0, 0, "haslam408_ds_Remazeilles2014.fits")
    assert type(s.temp408) is float
    assert round(s.temp408, 0) == 1804.
    assert type(s.get_temp(1400)) is float
    #print("Temp. at (0, 0) at 1400 MHz is {:.3f}".format(s.get_temp(1400)))
