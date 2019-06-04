
from unittest import TestCase

import voyager
import pandas

class TestVoyager(TestCase):
    def test_json(self):
        df = pandas.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
        voyager(df)