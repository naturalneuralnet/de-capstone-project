import streamlit as st


def main():
    # Main function of the Streamlit application
    st.set_page_config(
        page_title="UFO Sighting Metrics",
        page_icon="🛸",
        layout="wide",
        initial_sidebar_state="auto"
    )

    st.title("UFO Sightings Dashboard")


if __name__ == "__main__":
    main()
