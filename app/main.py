import streamlit as st
from data_processing import load_clean_and_export_data
from data_filtering import apply_filters
from global_metrics_and_charts import display_us_vis
from non_us_metrics_and_charts import display_non_us_vis

image_path = "https://cdn.pixabay.com/photo/2016/11/02/14/19/ufo-1791706_1280.png"


def main():
    # Main function of the Streamlit application
    st.set_page_config(
        page_title="UFO Sighting Metrics",
        page_icon="🛸",
        layout="wide",
        initial_sidebar_state="auto"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.title("UFO Sightings Dashboard")
    with col2:
        st.image(image_path, width=100, output_format="JPEG")

    df = load_clean_and_export_data(
        "data/raw/UFO_sightings_raw.csv",
        "data/clean/UFO_sightings_clean.csv")

    filtered_df = apply_filters(df)

    # add navigation
    with st.sidebar:
        st.header("Navigation")
        section = st.radio("Display section:", [
            "United States", "Outside of the United States"])
    if section == "United States":
        filtered_df = filtered_df[filtered_df['is_us'] == 'us']
        display_us_vis(filtered_df)
    elif section == "Outside of the United States":
        filtered_df = filtered_df[filtered_df['is_us'] == 'non-us']
        display_non_us_vis(filtered_df)


if __name__ == "__main__":
    main()
