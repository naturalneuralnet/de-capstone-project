import streamlit as st
import plotly.express as px


def display_key_insights():
    st.subheader("Key Insights on UFO Sightings in the US:")
    st.write(" 👽 The majority of sightings are in the United States.")
    st.write(
        " 👽 The number of sightings dramatically increased after 2000.")
    st.write(
        " 👽 Sightings are highest in the summer months,"
        "do aliens like a bit of sun?")
    st.write(
        " 👽 The shape of the majority of sightings in the US is no shape at all, "
        "the next highest shape reported is triangle.")
    st.write(" 👽 Your best chance of seeing a UFO for yourself "
             "is in the state of California or the city of Seattle in July at 9pm.")


def create_state_filter(filtered_df):
    state_filters = st.multiselect("Select State",
                                   options=sorted(
                                       filtered_df['state'].unique()),
                                   default=sorted(filtered_df
                                                  ["state"].unique()))
    return state_filters


def get_total_sightings(filtered_df):
    return filtered_df['datetime'].count()


# number of sightings that are not hoaxes

def get_total_hoaxes(filtered_df):
    return filtered_df['is_hoax'].values.sum()


# def calculate_average_length_of_sighting(filtered_df):
#     return round(filtered_df['duration (seconds)'].mean(), 2)

def calculate_most_likely_hour(filtered_df):
    return filtered_df['hour'].mode()[0]


def calculate_most_likely_shape(filtered_df):
    return filtered_df['shape'].mode()[0]


def calculate_sightings_over_time(filtered_df):
    return filtered_df[['datetime', 'year', 'state', 'country']
                       ].groupby(['year']).count().reset_index()


def display_metrics(filtered_df):
    total_sightings = get_total_sightings(filtered_df)
    total_hoaxes = get_total_hoaxes(filtered_df)
    likeliest_hour = calculate_most_likely_hour(filtered_df)
    likeliest_shape = calculate_most_likely_shape(filtered_df)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Sightings:", value=total_sightings)
    with col2:
        st.metric(
            label="Total hoaxes:", value=total_hoaxes
        )
    with col3:
        st.metric(label="Likeliest Hour of sightings:",
                  value=f"{likeliest_hour}")
    with col4:
        st.metric(label="Likeliest Shape of Sighting", value=likeliest_shape)


# plot the number of sightings over time
def create_sightings_over_time_vis(filtered_df):
    sightings_over_time = calculate_sightings_over_time(filtered_df)
    fig = px.scatter(
        sightings_over_time,
        x='year',
        y='datetime',
        title='Sightings over time',
        color_continuous_scale='YlOrRd',
        labels={
            'year': 'Year',
            'datetime': 'Sightings'
        },
        color='datetime',
    )
    fig.update_layout(
        title_font=dict(size=23,),
        title_y=0.83,  # Title positioned near the top vertically
    )
    return fig


def create_sightings_map(filtered_df):
    us_data = filtered_df[filtered_df['country'] == 'us']
    us_data['state'] = filtered_df['state'].str.upper()
    sightings_per_state = us_data[['datetime', 'state']
                                  ].groupby(['state']).count().reset_index()

    fig = px.choropleth(sightings_per_state,
                        locations='state',
                        locationmode='USA-states',
                        color='datetime',
                        scope='usa')
    return fig


def create_global_sightings_map(filtered_df):
    fig = px.scatter_geo(filtered_df, lat='latitude', lon="longitude ",
                         hover_name='country', title="UFO Sightings Worldwide")
    return fig


def create_top_decades_for_sightings(filtered_df):

    top_3 = filtered_df[['datetime', 'year']].groupby(
        (filtered_df.year//10)*10)['datetime'].count().reset_index()

    fig = px.bar(
        top_3,
        x="year",
        y="datetime",
        title="Sightings by decade",
        color='year',
        color_continuous_scale='YlOrRd',
        labels={
            'year': 'Year',
            'datetime': 'Sightings'
        },
    )
    fig.update_layout(
        title_font=dict(size=23,),
        title_y=0.83,  # Title positioned near the top vertically
    )
    return fig


def create_category_filters():
    category_filters = st.selectbox(
        "Select a category to group and count sightings by:", ['city', 'hour', 'month_name', 'shape', 'state', 'season'])
    return category_filters


def top_category_for_sightings(filtered_df, category):

    top = filtered_df[['datetime', category]
                      ].groupby(
                          category).count().reset_index()
    top = top.sort_values(by='datetime', ascending=False)
    fig = px.bar(
        top.head(10),
        x=category,
        y="datetime",
        title=f"Top {category} for Sightings",
        color=category,
        labels={
            category: category,
            'datetime': 'sightings'
        },

    )

    fig.update_layout(
        title_font=dict(size=23,),
        title_y=0.83,  # Title positioned near the top vertically
    )
    return fig


def display_us_vis(filtered_df):
    # global_filters = create_global_filter(filtered_df)

    # fig1 = create_sightings_per_country_vis(filtered_df)
    # st.plotly_chart(fig1)
    display_metrics(filtered_df)
    display_key_insights()
    fig2 = create_sightings_over_time_vis(filtered_df)
    fig2.update_layout(
        title_font=dict(size=24,),
        title_y=0.83,
    )
    st.plotly_chart(fig2)

    fig5 = create_top_decades_for_sightings(filtered_df)
    st.plotly_chart(fig5)

    category = create_category_filters()
    fig9 = top_category_for_sightings(filtered_df, category)
    st.write(fig9)

    # state_filters = create_state_filter(filtered_df)
    # filtered_df = filtered_df[
    #     (filtered_df['state'].isin(state_filters))]

    # fig3 = create_sightings_map(filtered_df)
    # st.plotly_chart(fig3)
