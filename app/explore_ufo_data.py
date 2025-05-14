import pandas as pd
import streamlit as st
import io
import plotly.express as px


df = pd.read_csv("data/raw/UFO_sightings_raw.csv")
st.title("UFO Sightings")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()

st.write(s)
st.write(df.head())


# Calculate the percentage of nulls
st.write(df.isnull().sum() * 100 / len(df))

# Discover data that needs cleaning

df['shape'] = df['shape'].fillna(df['shape'].mode()[0])
# Discover rows without state or country
df = df.dropna(subset=['state', 'country'])


# Discover data that needs to be converted to a different datatype
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df = df.dropna(subset=['datetime'])
# convert duration to int
df['duration (seconds)'] = pd.to_numeric(
    df['duration (seconds)'], errors='coerce')
# Convert comments to string.
df['comments'] = df['comments'].astype('str')
# Maybe extract month and year into their own columns.
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
# Convert long and lat to floats.

# Standardisation (consistent formatting) lower or upper the comments
# Discover unneeded columns
# Drop the post and duration (hours/minutes) date
df = df.drop(['date posted', 'duration (hours/min)'], axis='columns')

# Enrichment (adding new features or calculated fields),
# Create the season it was seen


def create_season(month):
    if month in [3.0, 4.0, 5.0]:
        return "Spring"
    elif month in [6.0, 7.0, 8.0]:
        return "Summer"
    elif month in [9.0, 10.0, 11.0]:
        return "Autumn"
    else:
        return "Winter"

# Create a column for hoaxes


def is_hoax(comment):
    if 'hoax' in str(comment):
        return True
    else:
        return False


df['season'] = df['month'].apply(create_season)

# Add column stating if it's a hoax or not, Y or N boolean values
df['is_hoax'] = df['comments'].apply(is_hoax)
df['is_hoax'] = df['is_hoax'].astype('bool')


# Discover aggregations that can be made
# Sum of sightings

# st.write("Total sightings")
# st.write(df['datetime'].count())
# st.write("Total hoaxes")
# st.write(df['is_hoax'].values.sum())
# st.write("average length of sightings")
# st.write(df['duration (seconds)'].mean())
# st.write("likeliest shape of sighting")
# st.write(df['shape'].mode()[0])
st.write("Sightings per country")
st.write(df[['datetime', 'country']].groupby(['country']).count())
sightings_per_country = df[['datetime', 'country']
                           ].groupby(['country']).count().reset_index()

# Create a chart of sightings per country

st.write("Sightings over time")

sightings_over_time = df[['datetime', 'year', 'state', 'country']
                         ].groupby(['year']).count().reset_index()

fig1 = px.bar(
    sightings_per_country,
    x="country",
    y="datetime",
    title="Sightings per Country",
    labels={
        'country': 'country',
        'datetime': 'sightings'
    },
    color='country'
)
# fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")
st.write(fig1)
# Sightings over time plot
fig2 = px.scatter(
    sightings_over_time,
    x='year',
    y='datetime',
    title='Sightings over time',
    labels={
        'year': 'year',
        'datetime': 'sightings'
    },
    color='datetime'
)

st.write(fig2)
# Discover how to plot lat and long
fig3 = px.scatter_geo(df, lat='latitude', lon="longitude ",
                      hover_name='country', title="UFO Sightings over country")
st.write(fig3)
