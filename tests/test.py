from skytempy.skytemp import SkyTemp

s = SkyTemp(0, 0, 'haslam408_ds_Remazeilles2014.fits')
print(s.get_temp(1400))
