"""
    Bundesnetzagentur Strommarktdaten

    Bundesnetzagentur Strommarktdaten  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.smard.api.default_api import DefaultApi  # noqa: E501

from deutschland import smard


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get(
        self,
    ):
        """Test case for chart_data_filter_region_filter_copy_region_copy_resolution_timestamp_json_get

        Zeitreihendaten  # noqa: E501
        """
        pass

    def test_chart_data_filter_region_index_resolution_json_get(self):
        """Test case for chart_data_filter_region_index_resolution_json_get

        Indizes  # noqa: E501
        """
        pass

    def test_table_data_filter_region_filter_copy_region_copy_quarterhour_timestamp_json_get(
        self,
    ):
        """Test case for table_data_filter_region_filter_copy_region_copy_quarterhour_timestamp_json_get

        Zeitreihendaten  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
