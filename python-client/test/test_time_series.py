"""
    Bundesnetzagentur Strommarktdaten

    Bundesnetzagentur Strommarktdaten  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.smard.model.time_series_meta_data import TimeSeriesMetaData

from deutschland import smard

globals()["TimeSeriesMetaData"] = TimeSeriesMetaData
from deutschland.smard.model.time_series import TimeSeries


class TestTimeSeries(unittest.TestCase):
    """TimeSeries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeSeries(self):
        """Test TimeSeries"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeSeries()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
