import unittest
import Essential_Functions

class MyTestCase(unittest.TestCase):

    def test_temp_avg(self):
        self.assertEqual(Essential_Functions.Essentials.TempAvg(), 55.88)

    def test_wind_max(self):
        self.assertEqual(Essential_Functions.Essentials.WindMax(), 19)

    def test_precip_sum(self):
        self.assertEqual(Essential_Functions.Essentials.PrecipSum(), 0.73)


if __name__ == '__main__':
    unittest.main()
