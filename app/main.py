import streamlit as st
from data_processing import load_clean_and_export_data


def main():
    # Main function of the Streamlit application
    st.set_page_config(
        page_title="UFO Sighting Metrics",
        page_icon="🛸",
        layout="wide",
        initial_sidebar_state="auto"
    )

    st.title("UFO Sightings Dashboard")

    df = load_clean_and_export_data(
        "data/raw/UFO_sightings_raw.csv",
        "data/clean/UFO_sightings_clean.csv")


if __name__ == "__main__":
    main()
