import sys
from typing import Any
from unittest.mock import MagicMock

import pytest
import httpx

from weather_refactor import WeatherService


@pytest.mark.parametrize(
    "city,expected_temp",
    [
        ("London", 15),
        ("Berlin", 20),
        ("Rome", 18),
    ],
)
def test_parametrized_temperatures_refactor(city: str, expected_temp: float) -> None:
    mock_http_client = MagicMock()
    mock_http_client.get.return_value = MagicMock(
        **{
            "raise_for_status": lambda: None,
            "json": lambda: {"current": {"temp_c": expected_temp}},
        }
    )

    service = WeatherService(client=mock_http_client, api_key="fake-key")
    assert service.get_temperature(city) == expected_temp


def test_temperature_raises_error_refactor(monkeypatch: pytest.MonkeyPatch) -> None:
    mock_http_client = MagicMock()
    mock_http_client.get.return_value = MagicMock(
        **{
            "raise_for_status": MagicMock(
                  side_effect=httpx.HTTPStatusError("Error", request=None, response=None)
              ),
            "json": lambda: {"current": {"temp_c": 19}},
        }
    )

    service = WeatherService(client=mock_http_client, api_key="fake-key")

    with pytest.raises(Exception):
        service.get_temperature("Oslo")


@pytest.mark.skip(reason="Temporarily skipping for demo purposes")
def test_skipped_refactor() -> None:
    assert False


@pytest.mark.skipif(sys.platform == "win32", reason="Fails on Windows")
def test_non_windows_behavior_refactor() -> None:
    assert True


@pytest.mark.xfail(reason="Intentional failure due to API bug")
def test_expected_failure_refactor() -> None:
    assert 1 + 1 == 3