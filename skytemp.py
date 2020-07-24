from __future__ import print_function, division, absolute_import

import numpy as np, argparse as ap
from scipy.interpolate import CubicSpline
from astropy.table import Table


def proc_args():
    pars = ap.ArgumentParser()
    pars.add_argument('fits')
    pars.add_argument('gl', type=float)
    pars.add_argument('gb', type=float)
    pars.add_argument('-f', '--freq', default=408, type=float)
    pars.add_argument('-s', '--spind', default=-2.9, type=float)

    return(vars(pars.parse_args()))


class SkyTemp:
    def __init__(self, gl, gb, table):
        self.gl = gl
        self.gb = gb
        self.table = table
        self.temp408 = self.interp()
        
    def get_pix(self):
        ylen, xlen = self.table.shape 
        xval = np.floor(xlen*self.gl/360) 
        yval = np.floor(ylen*(90-self.gb)/180) 
        return(int(xval), int(yval))
        
    def get_glgb(self, xval, yval):
        ylen, xlen = self.table.shape 
        gl = 360*xval/xlen 
        gb = 90 - (180*yval/ylen) 
        return(gl, gb)
        
    def interp(self):
        gl = self.gl
        gb = self.gb
        xcen, ycen = self.get_pix()
        xvals = np.array([xcen-1, xcen, xcen+1])
        yvals = np.array([ycen-1, ycen, ycen+1])
        xwrap = None 
        ywrap = None 
        if xcen - 1 < 0 or xcen + 1 > self.table.shape[1]: 
            xwrap = True 
            xvals = xvals % self.table.shape[1] 
             
        x_fory = np.array([xcen, xcen, xcen]) 
        if ycen - 1 < 0: 
            ywrap = 'neg' 
            yvals[0] = ycen 
            x_fory[0] = (xcen+self.table.shape[1])%self.table.shape[1] 
        elif ycen + 1 > self.table.shape[0]: 
            ywrap = 'pos' 
            yvals[-1] = ycen 
            x_fory[-1] = (xcen+self.table.shape[1])%self.table.shape[1] 
       
        temps_l = np.array([self.table[ycen, xv] for xv in xvals]) 
        temps_b = np.array([self.table[yv, xv] for xv, yv in zip(x_fory, yvals)]) 
        if ywrap == 'neg': 
            yvals[0] -= 1 
        elif ywrap == 'pos': 
            yvals[-1] += 1 
            
        lvals = np.zeros(3) 
        bvals = np.zeros(3) 
        for i, x, y in zip(np.arange(3), xvals, yvals): 
            lvals[i], bvals[i] = self.get_glgb(x, y)
      
        if xwrap: 
            lvals = ((lvals + 180) % 360) + 180 
            gl = ((gl + 180) % 360) + 180 
        
        temps_l = temps_l[np.argsort(lvals)] 
        lvals = lvals[np.argsort(lvals)] 
        temps_b = temps_b[np.argsort(bvals)] 
        bvals = bvals[np.argsort(bvals)] 
        cs_l = CubicSpline(lvals, temps_l) 
        cs_b = CubicSpline(bvals, temps_b) 
        return(np.mean([cs_l(gl), cs_b(gb)]))
        
    def get_temp(self, freq, spec_ind=-2.9):
        return(self.temp408*(freq/408)**spec_ind)


def read_fits(fits_file):
    t = Table.read(fits_file)
    return(t['TEMPERATURE'])


def main(fits, gl, gb, freq=408, spind=-2.9):
    table = read_fits(fits)
    print("gl  gb  freq  temp")
    print("{} {} {} {:.3f}".format(gl, gb, freq, SkyTemp(gl, gb, table).get_temp(freq, spind)))
        

if __name__ == "__main__":
    main(**proc_args())
