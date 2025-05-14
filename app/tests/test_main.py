from unittest.mock import patch, MagicMock
import pytest
import app.main as main


@pytest.fixture
def setup_mocks():
    with patch("app.main.st.set_page_config") as mock_set_page_config, patch(
            "app.main.st.title") as mock_title, patch(
            "app.main.load_clean_and_export_data") as mock_load_clean_and_export_data:

        mock_load_clean_and_export_data.return_value = MagicMock()

        yield {
            "mock_set_page_config": mock_set_page_config,
            "mock_set_title": mock_title,
            "mock_load_clean_and_export_data": mock_load_clean_and_export_data
        }


def test_set_config(setup_mocks):
    main.main()
    setup_mocks["mock_set_page_config"].assert_called_once_with(
        page_title="UFO Sighting Metrics",
        page_icon="🛸",
        layout="wide",
        initial_sidebar_state="auto"
    )


def test_set_title(setup_mocks):
    main.main()
    setup_mocks["mock_set_title"].assert_called_once_with(
        "UFO Sightings Dashboard"
    )


def test_load_clean_and_export_data(setup_mocks):
    main.main()
    setup_mocks["mock_load_clean_and_export_data"].assert_called_once_with(
        "data/raw/UFO_sightings_raw.csv",
        "data/clean/UFO_sightings_clean.csv"
    )
