import streamlit as st


def add_year_filter(df):
    st.sidebar.header("Date and Time Filters")
    select_year_range = reversed(sorted(df['year'].unique()))
    yearmax = df['year'].max()
    yearmin = df['year'].min()
    select_year_slider = st.sidebar.select_slider(
        'Use slider to select year range:', options=select_year_range, value=(yearmax, yearmin))
    startyear, endyear = list(select_year_slider)[
        0], list(select_year_slider)[1]

    return {'start': startyear, 'end': endyear}


def add_month_filter(df):
    month_filters = st.sidebar.multiselect(
        "Select Month", options=sorted(df['month'].unique()),
        default=sorted(df["month"].unique()))
    return month_filters


def add_season_filter(df):
    season_filters = st.sidebar.multiselect(
        "Select Season", options=sorted(df['season'].unique()),
        default=sorted(df["season"].unique()))
    return season_filters


# def create_global_filter(filtered_df):
#     global_filters = st.sidebar.multiselect("Select Region",
#                                             options=sorted(
#                                                 filtered_df['is_us'].unique()),
#                                             default=sorted(filtered_df["is_us"].unique()))
#     return global_filters


def filter_dataframe(df, year_filters):
    startyear = year_filters.get('start')
    endyear = year_filters.get('end')
    filtered_df = df[
        ((df.year <= startyear) & (df.year >= endyear))]
    return filtered_df


def apply_filters(df):
    year_filters = add_year_filter(df)
    # month_filters = add_month_filter(df)
    # season_filters = add_season_filter(df)
    # global_filters = create_global_filter(df)

    df = filter_dataframe(df, year_filters)
    return df
