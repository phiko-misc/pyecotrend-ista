"""Tests for DK implementation."""

from __future__ import annotations

from http import HTTPStatus
import json
from pathlib import Path

import pytest
import requests
from requests_mock.mocker import Mocker as RequestsMock
from syrupy.assertion import SnapshotAssertion

from pyecotrend_ista import LoginError, ParserError, PyEcotrendIstaDK, ServerError
from pyecotrend_ista.const import API_BASE_URL_DK, GRAPHS_API_BASE_URL_DK

_DK_TOKEN_PAYLOAD = {
    "access_token": "ACCESS_TOKEN",
    "token_type": "bearer",
    "expires_in": "3600",
    ".issued": "9999-12-24 00:00:00Z",
    ".expires": "9999-12-24 00:00:00Z",
    "Email": "",
    "Phone": "",
    "FirstName": "Max Istamann",
    "InstanceId": "0",
    "Language": "da-DK",
    "Username": "0000000000000",
    "PortalAdminId": "0",
    "ConsId": "00000000000",
    "isTenant": "true",
    "InstId": "000000000",
    "isAdmin": "false",
    "Key": "Value",
}

_INTERVAL_TO_VALUE = {
    "day": "1",
    "week": "2",
    "month": "3",
    "year": "4",
    "billing": "5",
}


def _load_dk_graph_data(meter_type: str, data_type: str, interval: str) -> str:
    """Load DK graph JSON fixture payload."""
    path = Path(__file__).parent / "data" / "DK" / meter_type / data_type / f"{interval}.json"
    return path.read_text(encoding="utf-8")


def _mock_dk_token(requests_mock: RequestsMock) -> None:
    """Mock DK token endpoint with a shared payload."""
    requests_mock.post(API_BASE_URL_DK + "token", json=_DK_TOKEN_PAYLOAD)


def _build_dk_graph_path(meter_type: str, data_type: str, interval: str) -> str:
    """Build graph path exactly as defined in the Postman Ista collection."""
    interval_value = _INTERVAL_TO_VALUE[interval]
    if meter_type == "Heat" and data_type == "Economy":
        return f"Overview/Economy_Heat_Data?inverval={interval_value}"
    if meter_type == "Heat" and data_type == "Consumption":
        return f"Overview/Usage_Heat_Data?inverval={interval_value}"
    if meter_type == "Electricity" and data_type == "Economy":
        return f"Overview/Economy_Electricity_Data?inverval={interval_value}"
    return f"Overview/Usage_Electricity_Data?interval={interval_value}"


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_login(ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK login method."""
    assert ista_client_dk.login() == "ACCESS_TOKEN"


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_user_info(ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK user info endpoint."""
    assert ista_client_dk.get_user_info()["Email"] == "max.istamann@example.com"


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_user_settings(ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK user settings endpoint."""
    assert ista_client_dk.get_user_settings()["UseDayValues"] is True


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_meters(ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK meters endpoint."""
    assert len(ista_client_dk.get_meters()["Meters"]["Value"]) == 4


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_meter_types(ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK meter types endpoint."""
    meter_types = ista_client_dk.get_meter_types()
    assert meter_types["electricity"] is not None
    assert meter_types["heat"] is not None


def test_dk_currency_code_is_iso_4217(ista_client_dk: PyEcotrendIstaDK) -> None:
    """DK client should expose ISO 4217 currency code for economy values."""
    assert ista_client_dk.get_currency_code() == "DKK"


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_user_info_snapshot(ista_client_dk: PyEcotrendIstaDK, snapshot: SnapshotAssertion) -> None:
    """Snapshot test for DK user info response."""
    assert ista_client_dk.get_user_info() == snapshot


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_user_settings_snapshot(ista_client_dk: PyEcotrendIstaDK, snapshot: SnapshotAssertion) -> None:
    """Snapshot test for DK user settings response."""
    assert ista_client_dk.get_user_settings() == snapshot


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_meters_snapshot(ista_client_dk: PyEcotrendIstaDK, snapshot: SnapshotAssertion) -> None:
    """Snapshot test for DK meters response."""
    assert ista_client_dk.get_meters() == snapshot


@pytest.mark.usefixtures("mock_requests_login_dk")
def test_dk_get_meter_types_snapshot(ista_client_dk: PyEcotrendIstaDK, snapshot: SnapshotAssertion) -> None:
    """Snapshot test for DK meter types response."""
    assert ista_client_dk.get_meter_types() == snapshot


@pytest.mark.parametrize(
    ("meter_type", "data_type", "interval"),
    [
        ("Electricity", "Consumption", "day"),
        ("Electricity", "Economy", "day"),
        ("Heat", "Consumption", "day"),
        ("Heat", "Economy", "day"),
    ],
)
def test_dk_get_graph_data_snapshot(
    requests_mock: RequestsMock,
    ista_client_dk: PyEcotrendIstaDK,
    snapshot: SnapshotAssertion,
    meter_type: str,
    data_type: str,
    interval: str,
) -> None:
    """Snapshot test for representative DK graph endpoint responses."""
    payload = _load_dk_graph_data(meter_type, data_type, interval)
    graph_path = _build_dk_graph_path(meter_type, data_type, interval)

    _mock_dk_token(requests_mock)
    requests_mock.get(
        f"{GRAPHS_API_BASE_URL_DK}{graph_path}",
        text=payload,
    )

    assert ista_client_dk.get_graph_data(meter_type, data_type, interval) == snapshot


@pytest.mark.parametrize("meter_type", ["Electricity", "Heat"])
@pytest.mark.parametrize("data_type", ["Consumption", "Economy"])
@pytest.mark.parametrize("interval", ["billing", "day", "week", "month", "year"])
def test_dk_get_graph_data(
    requests_mock: RequestsMock,
    ista_client_dk: PyEcotrendIstaDK,
    meter_type: str,
    data_type: str,
    interval: str,
) -> None:
    """Test DK graph endpoint for all supported meter/data/interval combinations."""
    payload = _load_dk_graph_data(meter_type, data_type, interval)
    graph_path = _build_dk_graph_path(meter_type, data_type, interval)

    _mock_dk_token(requests_mock)
    requests_mock.get(
        f"{GRAPHS_API_BASE_URL_DK}{graph_path}",
        text=payload,
    )

    assert ista_client_dk.get_graph_data(meter_type, data_type, interval) == json.loads(payload)


def test_dk_get_user_info_http_error(requests_mock: RequestsMock, ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK unauthorized error mapping."""
    _mock_dk_token(requests_mock)
    requests_mock.get(f"{API_BASE_URL_DK}api/GetUserInfo", status_code=HTTPStatus.UNAUTHORIZED)

    with pytest.raises(expected_exception=LoginError):
        ista_client_dk.get_user_info()


def test_dk_get_user_info_parse_error(requests_mock: RequestsMock, ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK parser error mapping."""
    _mock_dk_token(requests_mock)
    requests_mock.get(f"{API_BASE_URL_DK}api/GetUserInfo", text="not-json")

    with pytest.raises(expected_exception=ParserError):
        ista_client_dk.get_user_info()


def test_dk_get_user_info_request_error(requests_mock: RequestsMock, ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test DK request exception mapping."""
    _mock_dk_token(requests_mock)
    requests_mock.get(f"{API_BASE_URL_DK}api/GetUserInfo", exc=requests.RequestException)

    with pytest.raises(expected_exception=ServerError):
        ista_client_dk.get_user_info()


@pytest.mark.parametrize(
    ("method_name", "meter_type", "data_type", "interval"),
    [
        ("get_electricity_consumption_billing", "Electricity", "Consumption", "billing"),
        ("get_electricity_consumption_day", "Electricity", "Consumption", "day"),
        ("get_electricity_consumption_week", "Electricity", "Consumption", "week"),
        ("get_electricity_consumption_month", "Electricity", "Consumption", "month"),
        ("get_electricity_consumption_year", "Electricity", "Consumption", "year"),
        ("get_electricity_economy_billing", "Electricity", "Economy", "billing"),
        ("get_electricity_economy_day", "Electricity", "Economy", "day"),
        ("get_electricity_economy_week", "Electricity", "Economy", "week"),
        ("get_electricity_economy_month", "Electricity", "Economy", "month"),
        ("get_electricity_economy_year", "Electricity", "Economy", "year"),
        ("get_heat_consumption_billing", "Heat", "Consumption", "billing"),
        ("get_heat_consumption_day", "Heat", "Consumption", "day"),
        ("get_heat_consumption_week", "Heat", "Consumption", "week"),
        ("get_heat_consumption_month", "Heat", "Consumption", "month"),
        ("get_heat_consumption_year", "Heat", "Consumption", "year"),
        ("get_heat_economy_billing", "Heat", "Economy", "billing"),
        ("get_heat_economy_day", "Heat", "Economy", "day"),
        ("get_heat_economy_week", "Heat", "Economy", "week"),
        ("get_heat_economy_month", "Heat", "Economy", "month"),
        ("get_heat_economy_year", "Heat", "Economy", "year"),
    ],
)
def test_dk_interval_convenience_methods(
    requests_mock: RequestsMock,
    ista_client_dk: PyEcotrendIstaDK,
    method_name: str,
    meter_type: str,
    data_type: str,
    interval: str,
) -> None:
    """Test DK convenience methods for interval-specific graph endpoints."""
    payload = _load_dk_graph_data(meter_type, data_type, interval)
    graph_path = _build_dk_graph_path(meter_type, data_type, interval)

    _mock_dk_token(requests_mock)
    requests_mock.get(
        f"{GRAPHS_API_BASE_URL_DK}{graph_path}",
        text=payload,
    )

    method = getattr(ista_client_dk, method_name)
    assert method() == json.loads(payload)


def test_dk_get_graph_data_validation(ista_client_dk: PyEcotrendIstaDK) -> None:
    """Test strict runtime validation of graph data arguments."""
    with pytest.raises(expected_exception=ValueError):
        ista_client_dk.get_graph_data("Water", "Consumption", "day")  # type: ignore[arg-type]

    with pytest.raises(expected_exception=ValueError):
        ista_client_dk.get_graph_data("Electricity", "Cost", "day")  # type: ignore[arg-type]

    with pytest.raises(expected_exception=ValueError):
        ista_client_dk.get_graph_data("Electricity", "Consumption", "hour")  # type: ignore[arg-type]
