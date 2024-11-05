import unittest
import math
from scientific_calculator import sin , cos, tan, sqrt, log, exp

class test_scientific_calculator(unittest.TestCase):
    def test_sinpositive(self):
        self.assertAlmostEqual(sin(math.pi/2), 1.0)
    
    def test_sinnegative(self):
        self.assertAlmostEqual(sin(-math.pi/2), -1.0)
    
    def test_sinzero(self):
        self.assertAlmostEqual(sin(0), 0.0)
    
    def test_sinnumeric(self):
        with self.assertRaises(TypeError):
            sin("pass")

    def test_cospositive(self):
        self.assertAlmostEqual(cos(math.pi/2), 0)
    
    def test_cosnegative(self):
        self.assertAlmostEqual(cos(-math.pi/2), 0)
    def test_coszero(self):
        self.assertAlmostEqual(cos(0), 1)
    
    def test_cosnumeric(self):
        with self.assertRaises(TypeError):
            cos("pass")

    def test_tanpositive(self):
        self.assertAlmostEqual(tan(math.pi/4), 1.0)
    
    def test_tannegative(self):
        self.assertAlmostEqual(tan(-math.pi/4), -1.0)
    def test_tanzero(self):
        self.assertAlmostEqual(tan(0), 0)
    
    def test_tannumeric(self):
        with self.assertRaises(TypeError):
            tan("pass")

    def test_sqrtpositive(self):
        self.assertAlmostEqual(sqrt(4), 2.0)
    
    def test_sqrtzero(self):
        self.assertAlmostEqual(sqrt(0), 0.0)
    
    def test_sqrtnegative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
    
    def test_sqrtnumeric(self):
        with self.assertRaises(TypeError):
            sqrt("pass")

    def test_logpositive(self):
        self.assertAlmostEqual(log(math.e), 1.0)
    
    def test_lognegative(self):
        with self.assertRaises(ValueError):
            log(-1)
    
    def test_logzero(self):
        with self.assertRaises(ValueError):
            log(0)
    
    def test_lognumeric(self):
        with self.assertRaises(TypeError):
            log("pass")

    def test_exppositive(self):
        self.assertAlmostEqual(exp(1), math.e)
    
    def test_expnegative(self):
        self.assertAlmostEqual(exp(-1), 1/math.e)
    
    def test_expzero(self):
        self.assertAlmostEqual(exp(0), 1.0)
    
    def test_expnumeric(self):
        with self.assertRaises(TypeError):
            exp("pass")

if __name__ == '__main__':
    unittest.main()

