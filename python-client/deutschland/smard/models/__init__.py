# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.smard.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.smard.model.indices import Indices
from deutschland.smard.model.time_series import TimeSeries
from deutschland.smard.model.time_series2 import TimeSeries2
from deutschland.smard.model.time_series2_series_inner import TimeSeries2SeriesInner
from deutschland.smard.model.time_series2_series_inner_values_inner import (
    TimeSeries2SeriesInnerValuesInner,
)
from deutschland.smard.model.time_series2_series_inner_values_inner_versions_inner import (
    TimeSeries2SeriesInnerValuesInnerVersionsInner,
)
from deutschland.smard.model.time_series_meta_data import TimeSeriesMetaData
