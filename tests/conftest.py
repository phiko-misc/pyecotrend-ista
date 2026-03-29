"""Fixtures for Tests."""

from http import HTTPStatus
from pathlib import Path

import pytest
import requests_mock
from requests_mock.mocker import Mocker as RequestsMock

from pyecotrend_ista import PyEcotrendIsta, PyEcotrendIstaDK
from pyecotrend_ista.const import API_BASE_URL, DEMO_USER_ACCOUNT, PROVIDER_URL, API_BASE_URL_DK, GRAPHS_API_BASE_URL_DK

TEST_EMAIL = "max.istamann@test.com"
DEMO_EMAIL = DEMO_USER_ACCOUNT
TEST_PASSWORD = "password"

@pytest.fixture
def json_data(request) -> str:
    """Load json test data."""
    file = getattr(request, "param", "test_data")
    path = Path(__file__).parent / "data" / f"{file}.json"
    return path.read_text(encoding="utf-8")


@pytest.fixture
def ista_client(request) -> PyEcotrendIsta:
    """Create Bring instance."""
    ista = PyEcotrendIsta(
        email=getattr(request, "param", TEST_EMAIL),
        password=TEST_PASSWORD,
    )
    return ista


@pytest.fixture
def ista_client_dk() -> PyEcotrendIstaDK:
    """Create DK client instance."""
    return PyEcotrendIstaDK(
        email=TEST_EMAIL,
        password=TEST_PASSWORD,
    )

@pytest.fixture
def mock_requests_login(requests_mock: RequestsMock) -> RequestsMock:
    """Mock requests to Login Endpoints."""
    requests_mock.post(
        PROVIDER_URL + "token",
        json={
            "access_token": "ACCESS_TOKEN",
            "expires_in": 60,
            "refresh_expires_in": 5183999,
            "refresh_token": "REFRESH_TOKEN",
            "token_type": "Bearer",
            "id_token": "ID_TOKEN",
            "not-before-policy": 0,
            "session_state": "SESSION_STATE",
            "scope": "openid profile email",
        },
    )
    requests_mock.get(
        f"{API_BASE_URL}demo-user-token",
        json={
            "accessToken": "ACCESS_TOKEN",
            "accessTokenExpiresIn": 60,
            "refreshToken": "REFRESH_TOKEN",
            "refreshTokenExpiresIn": 5184000,
        },
    )
    requests_mock.get(
        PROVIDER_URL + "auth",
        text="""<form id="kc-form-login" onsubmit="return validateForm();"  action="https://keycloak.ista.com/realms/eed-prod/login-actions/authenticate?session_code=SESSION_CODE&amp;execution=EXECUTION&amp;client_id=ecotrend&amp;tab_id=TAB_ID" method="post">""",
        headers={
            "Set-Cookie": "AUTH_SESSION_ID=xxxxx.keycloak-xxxxxx; Version=1; Path=/realms/eed-prod/; SameSite=None; Secure; HttpOnly"
        },
    )
    requests_mock.post(
        "https://keycloak.ista.com/realms/eed-prod/login-actions/authenticate",
        headers={"Location": "https://ecotrend.ista.de/login-redirect#state=STATE&session_state=SESSION_STATE&code=AUTH_CODE"},
    )
    requests_mock.get(
        f"{API_BASE_URL}account",
        json={
            "firstName": "Max",
            "lastName": "Istamann",
            "email": "max.istamann@test.com",
            "keycloakId": None,
            "country": "DE",
            "locale": "de_DE",
            "authcode": None,
            "tos": "1.0",
            "tosUpdated": "01.01.1970",
            "privacy": None,
            "mobileNumber": "+49123456789",
            "transitionMobileNumber": "",
            "unconfirmedPhoneNumber": "",
            "password": None,
            "enabled": True,
            "consumptionUnitUuids": None,
            "residentTimeRangeUuids": None,
            "ads": False,
            "marketing": False,
            "fcmToken": "null",
            "betaPhase": None,
            "notificationMethod": "email",
            "emailConfirmed": False,
            "isDemo": False,
            "userGroup": "resident",
            "mobileLoginStatus": "non_initial",
            "residentAndConsumptionUuidsMap": {"17c4dff7-799f-4f16-badc-a9b3607a9383": "7a226e08-2a90-4db9-ae9b-8148901c6ec2"},
            "activeConsumptionUnit": "7a226e08-2a90-4db9-ae9b-8148901c6ec2",
            "supportCode": "XXXXXXXXX",
            "notificationMethodEmailConfirmed": True,
        },
    )
    requests_mock.post(PROVIDER_URL + "logout", status_code=HTTPStatus.NO_CONTENT)

    requests_mock.get(
        f"{API_BASE_URL}menu",
        json={
            "consumptionUnits": [
                {
                    "id": "7a226e08-2a90-4db9-ae9b-8148901c6ec2",
                    "address": {
                        "street": "Luxemburger Str.",
                        "houseNumber": "1",
                        "postalCode": "45131",
                        "city": "Essen",
                        "country": "DE",
                        "floor": "2. OG links",
                        "propertyNumber": "112233445",
                        "consumptionUnitNumber": "0001",
                        "idAtCustomerUser": "6234XB",
                    },
                    "booked": {"cost": True, "co2": False},
                    "propertyNumber": "57352474",
                }
            ],
            "coBranding": None,
        },
    )
    return requests_mock

@pytest.fixture
def mock_requests_login_dk(requests_mock: RequestsMock) -> RequestsMock:
    """Mock requests to Login Endpoints."""
    requests_mock.post(
        API_BASE_URL_DK + "token",
        json={
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
            "Key": "Value"
        },
    )
    requests_mock.get(
        f"{API_BASE_URL_DK}api/GetUserInfo",
        json={
            "Username": "00000000000",
            "Name": "Max Istamann",
            "Phone": "max.istamann@example.com",
            "Email": "max.istamann@example.com",
            "Language": "da-DK",
            "Address": "Nørrebrogade 56",
            "ZipCity": "København N",
            "ShowEconomy": True,
            "ShowClimate": False
        },
    )

    requests_mock.get(
        f"{API_BASE_URL_DK}api/GetUserSettings",
        json={
            "Mail": "max.istamann@example.com",
            "Phone": "max.istamann@example.com",
            "UseDayValues": True,
            "UseHourValues": True,
            "TenantCount": 1,
            "PreferredProgram": 1,
            "receiveNotification": True,
            "receiveNotificationByMail": True,
            "receiveNotificationByPhone": True
        },
    )

    requests_mock.get(
        f"{API_BASE_URL_DK}api/Meters",
        json={
            "errorMessage": {
                "ErrorType": "",
                "UserMessage": "",
                "InternalMessage": ""
            },
            "Meters": {
                "Value": [
                    {
                        "Message": " ",
                        "Headline": "Varme",
                        "MeterText": "Varme",
                        "MeterType": "HCA",
                        "Unit": "Delinger",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 8151,
                        "Reading_date": "03-02-2026",
                        "Last_Meter_Consumption": 15,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "Bathroom",
                        "METER_NO": "000000000",
                        "METCAT_LABEL": "Doprimo 3 SoC",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2018-04-06T00:00:00"
                    },
                    {
                        "Message": " ",
                        "Headline": "Varme",
                        "MeterText": "Varme",
                        "MeterType": "HCA",
                        "Unit": "Delinger",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 4485,
                        "Reading_date": "03-02-2026",
                        "Last_Meter_Consumption": 16,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "Family kitchen",
                        "METER_NO": "000000000",
                        "METCAT_LABEL": "Doprimo 3 SoC/fj",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2018-04-06T00:00:00"
                    },
                    {
                        "Message": " ",
                        "Headline": "El",
                        "MeterText": "El",
                        "MeterType": "EL",
                        "Unit": "kWh",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 0,
                        "Reading_date": None,
                        "Last_Meter_Consumption": 0,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "",
                        "METER_NO": "000000",
                        "METCAT_LABEL": "ABB",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2018-04-06T13:12:32"
                    },
                    {
                        "Message": None,
                        "Headline": None,
                        "MeterText": "Røg",
                        "MeterType": "SMOKE",
                        "Unit": " ",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 0,
                        "Reading_date": None,
                        "Last_Meter_Consumption": 0,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "",
                        "METER_NO": "0000000",
                        "METCAT_LABEL": "Fumonic",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2020-02-25T00:00:00"
                    }
                ]
            }
        },
    )

    requests_mock.get(
        f"{GRAPHS_API_BASE_URL_DK}MeterType/GetMeterTypes",
        json={
            "electricity": {
                "unit": "kWh",
                "useEcoData": True,
                "interval": {
                    "hour": False,
                    "day": True,
                    "week": True,
                    "month": True,
                    "year": True
                },
                "compare": {
                    "comparePeriode": True,
                    "property": True,
                    "installation": False,
                    "national": False,
                    "outsideTemperature": False,
                    "aconto": False
                }
            },
            "heat": {
                "unit": "Delinger",
                "useEcoData": True,
                "interval": {
                    "hour": False,
                    "day": True,
                    "week": True,
                    "month": True,
                    "year": True
                },
                "compare": {
                    "comparePeriode": True,
                    "property": True,
                    "installation": False,
                    "national": False,
                    "outsideTemperature": False,
                    "aconto": False
                }
            },
            "waterCold": None,
            "waterHot": None,
            "energy": None,
            "co2": None,
            "humidity": None,
            "noise": None,
            "temperature": None,
            "temperatureOut": None,
            "humonic": None
        },
    )
    
    return requests_mock
