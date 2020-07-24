from skytempy.skytemp import SkyTemp

s = SkyTemp(0, 0, 'haslam408_ds_Remazeilles2014.fits')
assert round(s.temp408, 0) == 1804.
print("Temp. at (0, 0) at 1400 MHz is {:.3f}".format(s.get_temp(1400)))
