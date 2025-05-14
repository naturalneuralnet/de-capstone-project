import streamlit as st
import plotly.express as px
from global_metrics_and_charts import (create_sightings_over_time_vis,
                                       create_category_filters,
                                       top_category_for_sightings,
                                       display_metrics)


def add_key_insights():
    st.subheader("Key Insights for sightings outside of the US:")
    st.write(
        " 👽 Most sightings outside the US occur in Canada, perhaps aliens really"
        " just like America?")
    st.write(" 👽 Once again, most sightings occur in summer months and the"
             " likeliest description is light, but this time circle is the"
             "next likeliest description!")
    st.write("👽 In Canada, Toronto is the city to go to find aliens but "
             "in Australia and Britian no one city is especially "
             "preferred by aliens.")


def add_country_filter(filtered_df):
    country_filters = st.multiselect(
        "Select Country", options=sorted(filtered_df['country'].unique()),
        default=sorted(filtered_df["country"].unique()))
    return country_filters


def calculate_sightings_per_country(filtered_df):
    return filtered_df[['datetime', 'country']
                       ].groupby(['country']).count().reset_index()


def create_sightings_per_country_vis(filtered_df):
    # plot number of sightings per country
    sightings_per_country = calculate_sightings_per_country(filtered_df)
    fig = px.bar(
        sightings_per_country,
        x="country",
        y="datetime",
        title="Sightings per Country",
        color='country',
        labels={
            'country': 'Country',
            'datetime': 'Sightings'
        },
    )
    fig.update_layout(
        title_font=dict(size=23,),
        title_y=0.83,  # Title positioned near the top vertically
    )
    return fig


def apply_filters(filtered_df):
    country_filters = add_country_filter(filtered_df)
    filtered_df = filtered_df[
        (filtered_df['country'].isin(country_filters))]
    return filtered_df


def display_non_us_vis(filtered_df):
    st.write(" ")
    filtered_df = apply_filters(filtered_df)
    st.write(" ")
    display_metrics(filtered_df)
    add_key_insights()

    fig1 = create_sightings_per_country_vis(filtered_df)
    st.write(fig1)

    fig2 = create_sightings_over_time_vis(filtered_df)
    st.write(fig2)

    category = create_category_filters()
    fig9 = top_category_for_sightings(filtered_df, category)
    st.write(fig9)
    # fig4 = top_category_for_sightings(filtered_df, category)
    # st.write(fig4)
    # fig3 = create_top_months_for_sightings(filtered_df)
    # st.write(fig3)
    # fig4 = create_sightings_per_hour()
