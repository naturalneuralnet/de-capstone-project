from unittest.mock import patch, MagicMock
import pytest
import app.main as main


@pytest.fixture
def setup_mocks():
    with patch("app.main.st.set_page_config") as mock_set_page_config, patch(
            "app.main.st.title") as mock_title:
        yield {
            "mock_set_page_config": mock_set_page_config,
            "mock_set_title": mock_title,
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
