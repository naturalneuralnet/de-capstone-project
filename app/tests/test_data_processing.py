import pytest
import pandas as pd
from data_processing import (rename_columns,
                             clean_nulls,
                             convert_to_correct_data_types,
                             drop_unused_columns,
                             enrich_data)


@pytest.fixture
def mock_data():
    data = {
        "datetime": ['10/10/1949 20:30', '10/10/1949 21:00', '10/10/1955 17:00', '10/10/1956 21:00'],
        "city": ['san marcos', 'lackland afb', 'chester(uk/england)', 'edna'],
        "state": ['tx', 'tx', None, 'tx'],
        "country": ['us', None, 'us', 'gb'],
        "shape": ['cylinder', 'None', 'circle', 'circle'],
        "duration (seconds)": [2700, 7200, 20, 20],
        "duration (hours/min)": ['45 minutes', '1-2 hrs', '20 seconds', '1/2 hour'],
        "comments": ["This event took place in early fall around 1949-50. It occurred after a Boy Scout meeting in the Baptist Church. The Baptist Church sit",
                     "1949 Lackland AFB&#44 TX.  Lights racing across the sky &amp; making 90 degree turns on a dime.",
                     "Green/Orange circular disc over Chester&#44 England",
                     "My older brother and twin sister were leaving the only Edna theater at about 9 PM&#44...we had our bikes and I took a different route home"],
        "date posted": ['4/27/2004', '12/16/2005', '1/21/2008', '1/17/2004'],
        "latitude": [29.8830556, 29.38421, 53.2, 28.9783333],
        "longitude ": [-97.9411111, -98.581082, -2.916667, -96.6458333]
    }
    return pd.DataFrame(data)


@pytest.fixture
def cleaned_column_names_data(mock_data):
    return rename_columns(mock_data.copy())


@pytest.fixture
def cleaned_nulls_data(mock_data):
    return clean_nulls(mock_data.copy())


@pytest.fixture
def cleaned_converted_data_types_data(mock_data):
    # renaming mock data columns here so as to not depend on the rename_columns function
    mock_data.rename(columns={'duration (seconds)': 'duration_seconds',
                              'longitude ': 'longitude'}, inplace=True)
    return (convert_to_correct_data_types(mock_data.copy()))


@pytest.fixture
def cleaned_dropped_columns_data(mock_data):
    return (drop_unused_columns(mock_data.copy()))


@pytest.fixture
def cleaned_enrich_dataset_data(mock_data):
    # renaming mock data columns here so as to not depend on the rename_columns function
    mock_data.rename(columns={'duration (seconds)': 'duration_seconds',
                              'longitude ': 'longitude'}, inplace=True)
    # converting datetime here so as to not depend on convert_to_correct_data_types
    mock_data['datetime'] = pd.to_datetime(
        mock_data['datetime'], errors='coerce')
    mock_data['duration_seconds'] = pd.to_numeric(
        mock_data['duration_seconds'], errors='coerce')
    mock_data['comments'] = mock_data['comments'].astype('str')
    return (enrich_data(mock_data.copy()))

# test columns are renamed


def test_rename_columns(cleaned_column_names_data):
    assert (list(cleaned_column_names_data.columns) == [
            "datetime", "city", "state", "country", "shape",
            "duration_seconds", "duration (hours/min)", "comments",
            "date posted", "latitude", "longitude"])

# test dropping nulls


def test_drop_nulls_state_column(cleaned_nulls_data):
    assert (cleaned_nulls_data['state'].isnull().sum() == 0)
    "State Column should have no missing values"


def test_drop_nulls_country_column(cleaned_nulls_data):
    assert (cleaned_nulls_data['country'].isnull().sum() == 0)
    "country Column should have no missing values"


def test_drop_nulls_datetime_column(cleaned_nulls_data):
    assert (cleaned_nulls_data['datetime'].isnull().sum() == 0)
    "datetime Column should have no missing values"


def test_drop_nulls_shape_column(cleaned_nulls_data):
    assert (cleaned_nulls_data['shape'].isnull().sum() == 0)
    "shape Column should have no missing values"


def test_datetime_type_converted(cleaned_converted_data_types_data):
    assert (
        cleaned_converted_data_types_data["datetime"].dtype.name == "datetime64[ns]")
    "datetime column should be of type datetime"


def test_duration_seconds_type_converted(cleaned_converted_data_types_data):
    assert pd.api.types.is_integer_dtype(
        cleaned_converted_data_types_data["duration_seconds"])
    "duration_second column should be of type numeric"


def test_comments_type_converted(cleaned_converted_data_types_data):
    assert pd.api.types.is_string_dtype(
        cleaned_converted_data_types_data["comments"])
    "comments column should be of type datetime"


def test_drop_date_posted_column(cleaned_dropped_columns_data):
    assert (
        'date_posted' not in cleaned_dropped_columns_data.columns
    )
    "date_posted column should not be in the dataframe "


def test_drop_duration_hour_column(cleaned_dropped_columns_data):
    assert (
        'duration (hours/min)' not in cleaned_dropped_columns_data.columns
    )
    "duration (hours/min) column should not be in the dataframe "


def test_enrich_data_create_year_column(cleaned_enrich_dataset_data):
    assert (
        'year' in cleaned_enrich_dataset_data.columns
    )
    "year should be in the dataframe"

# month


def test_enrich_data_create_month_column(cleaned_enrich_dataset_data):
    assert (
        'month' in cleaned_enrich_dataset_data.columns
    )
    "month should be in the dataframe"
# month_name


def test_enrich_data_create_month_name_column(cleaned_enrich_dataset_data):
    assert (
        'month_name' in cleaned_enrich_dataset_data.columns
    )
    "month_name should be in the dataframe"
# hour


def test_enrich_data_create_hour_column(cleaned_enrich_dataset_data):
    assert (
        'hour' in cleaned_enrich_dataset_data.columns
    )
    "hour should be in the dataframe"

# season


def test_enrich_data_create_season_column(cleaned_enrich_dataset_data):
    assert (
        'season' in cleaned_enrich_dataset_data.columns
    )
    "season should be in the dataframe"
# is hoax exists


def test_enrich_data_create_is_hoax_column(cleaned_enrich_dataset_data):
    assert (
        'is_hoax' in cleaned_enrich_dataset_data.columns
    )
    "is_hoax should be in the dataframe"

# is hoax type


def test_enrich_data_create_is_hoax_type_column(cleaned_enrich_dataset_data):
    assert pd.api.types.is_bool_dtype(
        cleaned_enrich_dataset_data['is_hoax']
    )
    "is_hoax should be in the dataframe"
# is_us


def test_enrich_data_create_is_us_column(cleaned_enrich_dataset_data):
    assert (
        'is_us' in cleaned_enrich_dataset_data.columns
    )
    "is_us should be in the dataframe"
