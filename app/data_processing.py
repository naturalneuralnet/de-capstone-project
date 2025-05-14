import pandas as pd


def load_data(filepath):
    df = pd.read_csv(filepath, engine='python')
    return df


def rename_columns(df):
    df.rename(columns={'duration (seconds)': 'duration_seconds',
              'longitude ': 'longitude'}, inplace=True)
    return df


def convert_to_correct_data_types(df):
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df['duration_seconds'] = pd.to_numeric(
        df['duration_seconds'], errors='coerce')
    df['comments'] = df['comments'].astype('str')
    return df


def clean_nulls(df):
    # remove null rows
    df = df.dropna(subset=['state', 'country'])
    df = df.dropna(subset=['datetime'])
    df = df.dropna(subset=['shape'])
    return df


def drop_unused_columns(df):
    df = df.drop(['date posted', 'duration (hours/min)'], axis='columns')
    return df


def create_season(month):
    if month in [3.0, 4.0, 5.0]:
        return "Spring"
    elif month in [6.0, 7.0, 8.0]:
        return "Summer"
    elif month in [9.0, 10.0, 11.0]:
        return "Autumn"
    else:
        return "Winter"


def is_hoax(comment):
    if 'hoax' in str(comment):
        return True
    else:
        return False


def is_us(country):
    if country == 'us':
        return 'us'
    else:
        return 'non-us'


def enrich_data(df):
    df['year'] = df['datetime'].dt.year
    df['month'] = df['datetime'].dt.month
    df['month_name'] = df['datetime'].dt.month_name()
    df['hour'] = df['datetime'].dt.hour
    df['season'] = df['month'].apply(create_season)
    df['is_hoax'] = df['comments'].apply(is_hoax)
    df['is_hoax'] = df['is_hoax'].astype('bool')
    df['is_us'] = df['country'].apply(is_us)
    return df


def export_data(df, export_filepath):
    df.to_csv(export_filepath)


def load_clean_and_export_data(filepath, export_filepath):
    df = load_data(filepath)
    df = rename_columns(df)
    df = convert_to_correct_data_types(df)
    df = clean_nulls(df)
    df = drop_unused_columns(df)
    df = enrich_data(df)

    export_data(df, export_filepath)
    return df
