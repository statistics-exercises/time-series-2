import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        self.assertTrue( np.abs( expectation - 1/lamd ) < 1e-7, "the value you have set for the expectation is incorrect"  )
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "you have plotted the wrong number of coordinates in your graph" )
        for i in range(len(this_y)) :
             self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x coordinates in your graph are not correct" )
             bar = np.sqrt(1/(lamd*lamd)/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
             self.assertTrue( np.fabs( this_y[i] - 1/lamd )<bar, "the y coordiants of your graph appear to be incorrect" )
