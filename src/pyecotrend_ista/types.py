# numpydoc ignore=EX01
"""
Types for PyEcotrendIsta.

This module defines various TypedDicts used in the PyEcotrendIsta client to represent
responses and data structures from the ista EcoTrend API.

See Also
--------
PyEcotrendIsta : The main client class for interacting with the ista EcoTrend API.
"""

from typing import Any, Literal, TypeAlias, TypedDict


class GetTokenResponse(TypedDict):  # numpydoc ignore=ES01,SA01,EX01,GL01,GL02,GL03
    """A TypedDict for the response returned by the getToken function.

    Attributes
    ----------
    access_token : str
        The access token issued by the authentication provider.
    expires_in : int
        The number of seconds until the access token expires.
    refresh_token : str
        The refresh token that can be used to obtain new access tokens.
    refresh_expires_in : int
        The number of seconds until the refresh token expires.

    """

    access_token: str
    expires_in: int
    refresh_token: str
    refresh_expires_in: int


class AccountResponseDE(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the response for an account in the ista EcoTrend API.

    Attributes
    ----------
    firstName : str
        The first name of the account holder.
    lastName : str
        The last name of the account holder.
    email : str
        The email address of the account holder.
    keycloakId : str
        The Keycloak ID associated with the account.
    country : str
        The country associated with the account.
    locale : str
        The locale setting for the account.
    authcode : str
        The authentication code for the account.
    tos : str
        The terms of service agreed to by the account holder.
    tosUpdated : str
        The date the terms of service were last updated.
    privacy : str
        The privacy setting for the account.
    mobileNumber : str
        The mobile phone number associated with the account.
    transitionMobileNumber : str
        The mobile number used during the transition period.
    unconfirmedPhoneNumber : str
        The unconfirmed phone number associated with the account.
    password : str
        The password for the account.
    enabled : bool
        Indicates whether the account is enabled.
    consumptionUnitUuids : list of str
        List of UUIDs for the consumption units.
    residentTimeRangeUuids : list of str
        List of UUIDs for the resident time ranges.
    ads : bool
        Indicates whether advertisements are enabled.
    marketing : bool
        Indicates whether the account holder has opted into marketing communications.
    fcmToken : str
        The FCM (Firebase Cloud Messaging) token for push notifications.
    betaPhase : str
        Indicates if the account is in the beta phase.
    notificationMethod : str
        The method of notification preferred by the account holder.
    emailConfirmed : bool
        Indicates whether the email address is confirmed.
    isDemo : bool
        Indicates whether the account is a demo account.
    userGroup : str
        The user group the account belongs to.
    mobileLoginStatus : str
        The status of mobile login for the account.
    residentAndConsumptionUuidsMap : dict of str to str
        A map of resident UUIDs to consumption unit UUIDs.
    activeConsumptionUnit : str
        The UUID of the active consumption unit.
    supportCode : str
        The support code for the account.
    notificationMethodEmailConfirmed : bool
        Indicates whether the email for notification method is confirmed.
    """

    firstName: str
    lastName: str
    email: str
    keycloakId: str
    country: str
    locale: str
    authcode: str
    tos: str
    tosUpdated: str
    privacy: str
    mobileNumber: str
    transitionMobileNumber: str
    unconfirmedPhoneNumber: str
    password: str
    enabled: bool
    consumptionUnitUuids: list[str]
    residentTimeRangeUuids: list[str]
    ads: bool
    marketing: bool
    fcmToken: str
    betaPhase: str
    notificationMethod: str
    emailConfirmed: bool
    isDemo: bool
    userGroup: str
    mobileLoginStatus: str
    residentAndConsumptionUuidsMap: dict[str, str]
    activeConsumptionUnit: str
    supportCode: str
    notificationMethodEmailConfirmed: bool

class TokenResponse(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the Token response in the ista EcoTrend DK API.

    Attributes
    ----------
    access_token : str
        The access token for the API.
    token_type : str
        The type of token.
    expires_in : str
        The number of seconds until the token expires.
    ".issued" : str
        The timestamp when the token was issued.
    ".expires" : str
        The timestamp when the token expires.
    Email : str
        The email address associated with the token.
    Phone : str
        The phone number associated with the token.
    FirstName : str
        The first name associated with the token.
    InstanceId : str
        The instance ID associated with the token.
    Language : str
        The language associated with the token.
    Username : str
        The username associated with the token.
    PortalAdminId : str
        The portal admin ID associated with the token.
    ConsId : str
        The consumer ID associated with the token.
    isTenant : str
        Indicates whether the token is for a tenant.
    InstId : str
        The installation ID associated with the token.
    isAdmin : str
        Indicates whether the token is for an admin user.
    Key : str
        The key associated with the token.
    """

    access_token: str
    token_type: str
    expires_in: str
    issued: str
    expires: str
    Email: str
    Phone: str
    FirstName: str
    InstanceId: str
    Language: str
    Username: str
    PortalAdminId: str
    ConsId: str
    isTenant: str
    InstId: str
    isAdmin: str
    Key: str

class UserInfo(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the response for an user info in the ista EcoTrend DK API.

    Attributes
    ----------
    Username : str
        The username of the account holder.
    Name : str
        The full name of the account holder.
    Phone : str
        The phone number of the account holder.
    Email : str
        The email address of the account holder.
    Language : str
        The language preference of the account holder.
    Address : str
        The address of the account holder.
    ZipCity : str
        The zip code and city of the account holder.
    ShowEconomy : bool
        Indicates whether to show economy information.
    ShowClimate : bool
        Indicates whether to show climate information.
    """

    Username: str
    Name: str
    Phone: str
    Email: str
    Language: str
    Address: str
    ZipCity: str
    ShowEconomy: bool
    ShowClimate: bool

class UserSettings(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the response for an user settings in the ista EcoTrend DK API.

    Attributes
    ----------
    Mail : str
        The email address of the account holder.
    Phone : str
        The phone number of the account holder.
    UseDayValues : bool
        Indicates whether to use day values.
    UseHourValues : bool
        Indicates whether to use hour values.
    TenantCount : int
        The number of tenants in the account.
    PreferredProgram : int
        The preferred program for the account holder.
    receiveNotification : bool
        Indicates whether to receive notifications.
    receiveNotificationByMail : bool
        Indicates whether to receive notifications by mail.
    receiveNotificationByPhone : bool
        Indicates whether to receive notifications by phone.
    """

    Mail: str
    Phone: str
    UseDayValues: bool
    UseHourValues: bool
    TenantCount: int
    PreferredProgram: int
    receiveNotification: bool
    receiveNotificationByMail: bool
    receiveNotificationByPhone: bool

class MetersErrorMessage(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the Meters error response in the ista EcoTrend DK API.

    Attributes
    ----------
    ErrorType : str
        The type of error.
    UserMessage : str
        The user-friendly error message.
    InternalMessage : str
        The internal error message.
    """

    ErrorType: str
    UserMessage: str
    InternalMessage: str

class MetersValue(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the Meters value in the ista EcoTrend DK API.

    Attributes
    ----------
    Message : str | None
        The message associated with the meter value.
    Headline : str | None
        The headline associated with the meter value.
    MeterText : str
        The text associated with the meter.
    MeterType : str
        The type of meter.
    Unit : str
        The unit of measurement for the meter value.
    INST_NO : int
        The installation number of the meter.
    Last_Meter_Reading : int
        The last reading of the meter.
    Reading_date : str | None
        The date of the last reading of the meter.
    Last_Meter_Consumption : int
        The last consumption value of the meter.
    METER_ID : int
        The ID of the meter.
    ROOM_DESCR : str
        The description of the room where the meter is installed.
    METER_NO : str
        The number of the meter.
    METCAT_LABEL : str
        The label of the meter category.
    METTYPE_CODE : str | None
        The code of the meter type.
    Deactivation_date : str
        The deactivation date of the meter.
    Activation_date : str
        The activation date of the meter.
    """

    Message: None | str
    Headline: None | str
    MeterText: str
    MeterType: str
    Unit: str
    INST_NO: int
    Last_Meter_Reading: int
    Reading_date: None | str
    Last_Meter_Consumption: int
    METER_ID: int
    ROOM_DESCR: str
    METER_NO: str
    METCAT_LABEL: str
    METTYPE_CODE: None | str
    Deactivation_date: str
    Activation_date: str

class MetersValues(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    TypedDict represents the Meters Values in the ista EcoTrend DK API.

    Attributes
    ----------
    value : list[MetersValue]
        The list of meter values.
    """

    value: list[MetersValue]

class MetersResponse(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the Meters response in the ista EcoTrend DK API.

    Attributes
    ----------
    errorMessage : MetersErrorMessage
        The error message associated with the meter response.
    Meters : MetersValues
        The list of meter values associated with the meter response.
    """

    errorMessage: MetersErrorMessage
    Meters: MetersValues

class MeterTypesCompare(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing the Meter Types Compare in the ista EcoTrend DK graphs API.

    Attributes
    ----------
    comparePeriode : bool
        Indicates whether the comparison is for a period.
    property : bool
        Indicates whether the comparison is for a property.
    installation : bool
        Indicates whether the comparison is for an installation.
    national : bool
        Indicates whether the comparison is national.
    outsideTemperature : bool
        Indicates whether the comparison includes outside temperature.
    aconto : bool
        Indicates whether the comparison includes aconto (advance payment).
    """

    comparePeriode: bool
    property: bool
    installation: bool
    national: bool
    outsideTemperature: bool
    aconto: bool

class MeterTypesInterval(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing the Meter Types interval in the ista EcoTrend DK graphs API.

    Attributes
    ----------
    hour : bool
        Indicates whether the interval is hourly.
    day : bool
        Indicates whether the interval is daily.
    week : bool
        Indicates whether the interval is weekly.
    month : bool
        Indicates whether the interval is monthly.
    year : bool
        Indicates whether the interval is yearly.
    """

    hour: bool
    day: bool
    week: bool
    month: bool
    year: bool

class MeterTypesElement(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing the Meter Types interval in the ista EcoTrend DK graphs API.

    Attributes
    ----------
    unit : str
        The unit of measurement for the meter type element.
    useEcoData : bool
        Indicates whether eco data is used for the meter type element.
    interval : MeterTypesInterval
        The interval settings for the meter type element.
    compare : MeterTypesCompare
        The comparison settings for the meter type element.
    """

    unit: str
    useEcoData: bool
    interval: MeterTypesInterval
    compare: MeterTypesCompare

class MeterTypesResponse(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the Meter Types response in the ista EcoTrend DK graphsAPI.

    Attributes
    ----------
    electricity : MeterTypesElement | None
        The meter type element for electricity, or None if not available.
    heat : MeterTypesElement | None
        The meter type element for heat, or None if not available.
    waterCold : MeterTypesElement | None
        The meter type element for cold water, or None if not available.
    waterHot : MeterTypesElement | None
        The meter type element for hot water, or None if not available.
    energy : MeterTypesElement | None
        The meter type element for energy, or None if not available.
    co2 : MeterTypesElement | None
        The meter type element for CO2, or None if not available.
    humidity : MeterTypesElement | None
        The meter type element for humidity, or None if not available.
    noise : MeterTypesElement | None
        The meter type element for noise, or None if not available.
    temperature : MeterTypesElement | None
        The meter type element for temperature, or None if not available.
    temperatureOut : MeterTypesElement | None
        The meter type element for outside temperature, or None if not available.
    humonic : MeterTypesElement | None
        The meter type element for humonic, or None if not available.
    """

    electricity: MeterTypesElement | None
    heat: MeterTypesElement | None
    waterCold: MeterTypesElement | None
    waterHot: MeterTypesElement | None
    energy: MeterTypesElement | None
    co2: MeterTypesElement | None
    humidity: MeterTypesElement | None
    noise: MeterTypesElement | None
    temperature: MeterTypesElement | None
    temperatureOut: MeterTypesElement | None
    humonic: MeterTypesElement | None

class IstaMonthYear(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing a month and year.

    Attributes
    ----------
    month : int
        The month value.
    year : int
        The year value.
    """

    month: int
    year: int


class IstaAverageConsumption(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing average consumption values.

    Attributes
    ----------
    additionalAverageConsumptionPercentage : int
        Percentage of additional average consumption.
    additionalAverageConsumptionValue : str
        Value of additional average consumption.
    additionalResidentConsumptionPercentage : int
        Percentage of additional resident consumption.
    additionalResidentConsumptionValue : str
        Value of additional resident consumption.
    averageConsumptionPercentage : int
        Percentage of average consumption.
    averageConsumptionValue : str
        Value of average consumption.
    residentConsumptionPercentage : int
        Percentage of resident consumption.
    residentConsumptionValue : str
        Value of resident consumption.
    """

    additionalAverageConsumptionPercentage: int
    additionalAverageConsumptionValue: str
    additionalResidentConsumptionPercentage: int
    additionalResidentConsumptionValue: str
    averageConsumptionPercentage: int
    averageConsumptionValue: str
    residentConsumptionPercentage: int
    residentConsumptionValue: str


class IstaCompared(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing compared values.

    Attributes
    ----------
    comparedPercentage : int
        Percentage comparison value.
    comparedValue : str
        Compared value.
    lastYearValue : float
        Value from the last year.
    period : IstaMonthYear
        Period associated with the comparison.
    smiley : str
        Smiley associated with the comparison.
    """

    comparedPercentage: int
    comparedValue: str
    lastYearValue: float
    period: IstaMonthYear
    smiley: str


class IstaReading(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing a reading.

    Attributes
    ----------
    additionalUnit : str
        Additional unit associated with the reading.
    additionalValue : str
        Additional value associated with the reading.
    averageConsumption : IstaAverageConsumption
        Average consumption details.
    comparedConsumption : dict
        Compared consumption details.
    comparedCost : IstaCompared
        Compared cost details.
    estimated : bool
        Indicates if the reading is estimated.
    type : Literal["heating", "warmwater", "water"]
        Type of the reading (heating, warmwater, water).
    unit : str
        Unit of measurement for the reading.
    value : str
        Value of the reading.
    """

    additionalUnit: str
    additionalValue: str
    averageConsumption: IstaAverageConsumption
    comparedConsumption: dict
    comparedCost: IstaCompared
    estimated: bool
    type: Literal["heating", "warmwater", "water"]
    unit: str
    value: str


class IstaTimeRange(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing a time range.

    Attributes
    ----------
    end : IstaMonthYear
        The end of the time range.
    start : IstaMonthYear
        The start of the time range.
    """

    end: IstaMonthYear
    start: IstaMonthYear


class IstaBillingPeriod(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing a billing period.

    Attributes
    ----------
    exception : Any, optional
        Any exceptions related to this billing period. (data type unknown)
    readings : list[IstaReading]
        List of readings associated with this billing period.
    timeRange : IstaTimeRange
        The time range for this billing period.
    """

    exception: Any
    readings: list[IstaReading]
    timeRange: IstaTimeRange


class IstaBillingPeriods(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing the billing periods.

    Attributes
    ----------
    currentBillingPeriod : IstaBillingPeriod
        The details of the current billing period.
    previousBillingPeriod : IstaBillingPeriod
        The details of the previous billing period.
    """

    currentBillingPeriod: IstaBillingPeriod
    previousBillingPeriod: IstaBillingPeriod


class IstaCostsByEnergyType(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing the costs associated with a specific energy type.

    Attributes
    ----------
    comparedCost : IstaCompared
        The cost comparison data for the energy type.
    estimated : bool
        Indicates whether the cost is estimated.
    type : Literal["heating", "warmwater", "water"]
        The type of energy (heating, warm water, or water).
    unit : str
        The unit of measurement for the cost.
    value : int
        The cost value.
    """

    comparedCost: IstaCompared
    estimated: bool
    type: Literal["heating", "warmwater", "water"]
    unit: str
    value: int


class IstaPeriods(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing data for a specific period.

    Attributes
    ----------
    date : IstaMonthYear
        The month and year for the period.
    documentNumber : str | None
        The document number associated with the period, if any.
    exception : Any
        An exception associated with the period (data type unspecified).
    isSCEedBasic : bool
        Indicates if the SCEed basic plan is active for the period.
    readings : list[IstaReading]
        A list of readings recorded during the period.
    costsByEnergyType : list[IstaCostsByEnergyType]
        A list of costs categorized by energy type for the period.
    """

    date: IstaMonthYear
    documentNumber: str | None
    exception: Any
    isSCEedBasic: bool
    readings: list[IstaReading]
    costsByEnergyType: list[IstaCostsByEnergyType]


class ConsumptionsResponse(TypedDict, total=False):  # numpydoc ignore=ES01,SA01,EX01
    """
    A TypedDict representing the response structure for consumption data.

    Attributes
    ----------
    co2Emissions : list[IstaPeriods]
        A list of CO2 emission data over different periods.
    co2EmissionsBillingPeriods : list[IstaBillingPeriods]
        A list of CO2 emission data over different billing periods.
    consumptionUnitId : str
        The unique identifier for the consumption unit.
    consumptions : list[IstaPeriods]
        A list of consumption data over different periods.
    consumptionsBillingPeriods : IstaBillingPeriods
        The consumption data over different billing periods.
    costs : list[IstaPeriods]
        A list of cost data over different periods.
    costsBillingPeriods : IstaBillingPeriods
        The cost data over different billing periods.
    isSCEedBasicForCurrentMonth : bool
        Indicates if the SCEed basic plan is active for the current month.
    nonEEDBasicStartDate : Any
        The start date for non-EED basic plan (data type unknown).
    resident : dict[str, Any]
        A dictionary containing resident information.
    """

    co2Emissions: list[IstaPeriods]
    co2EmissionsBillingPeriods: list[IstaBillingPeriods]
    consumptionUnitId: str
    consumptions: list[IstaPeriods]
    consumptionsBillingPeriods: IstaBillingPeriods
    costs: list[IstaPeriods]
    costsBillingPeriods: IstaBillingPeriods
    isSCEedBasicForCurrentMonth: bool
    nonEEDBasicStartDate: Any
    resident: dict[str, Any]


class IstaConsumptionUnitAddress(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the address of a consumption unit.

    Attributes
    ----------
    street : str
        The street name of the address.
    houseNumber : str
        The house number of the address.
    postalCode : str
        The postal code of the address.
    city : str
        The city of the address.
    country : str
        The country code of the address.
    floor : str
        The floor number of the address.
    propertyNumber : str
        The property number of the address.
    consumptionUnitNumber : str
        The consumption unit number associated with the address.
    idAtCustomerUser : str
        The ID assigned to the address at the customer user's end.
    """

    street: str
    houseNumber: str
    postalCode: str
    city: str
    country: str  # country code
    floor: str
    propertyNumber: str
    consumptionUnitNumber: str
    idAtCustomerUser: str


class IstaConsumptionUnitBookedServices(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the booked extra services for an Ista consumption unit.

    Attributes
    ----------
    cost : bool
        Indicates if cost service is booked.
    co2 : bool
        Indicates if CO2 service is booked.
    """

    cost: bool
    co2: bool


class IstaConsumptionUnit(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents a consumption unit.

    Attributes
    ----------
    id : str
        The UUID of the consumption unit.
    address : IstaConsumptionUnitAddress
        The address details of the consumption unit.
    booked : IstaConsumptionUnitBookedServices
        The booked services for the consumption unit.
    propertyNumber : str
        The property number associated with the consumption unit.
    """

    id: str  # UUID
    address: IstaConsumptionUnitAddress
    booked: IstaConsumptionUnitBookedServices
    propertyNumber: str


class ConsumptionUnitDetailsResponse(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    Represents the response details for consumption units.

    Attributes
    ----------
    consumptionUnits : list[IstaConsumptionUnit]
        The list of consumption units.
    coBranding : Any
        Co-branding information (data type unknown).
    """

    consumptionUnits: list[IstaConsumptionUnit]
    coBranding: Any  # #unknown

class ElectricityConsumptionElement(TypedDict):  # numpydoc ignore=ES01,SA01,EX01
    """
    TypedDict representing the electricity and consumption element in the ista EcoTrend DK Graphs API.

    Attributes
    ----------
    when : str
        The time period for the consumption element.
    value : int | None
        The consumption value for the specified time period, or None if not available.
    formerPeriode : float | None
        The consumption value for the former period, or None if not available.
    minValue : int | None
        The minimum consumption value for the specified time period, or None if not available.
    maxValue : float | None
        The maximum consumption value for the specified time period, or None if not available.
    percent : float | None
        The percentage change in consumption compared to the former period, or None if not available.
    property : float | None
        The property value associated with the consumption, or None if not available.
    propertyProcentage : float | None
        The percentage change in property value compared to the former period, or None if not available.
    national : float | None
        The national average consumption value, or None if not available.
    nationalProcentage : float | None
        The percentage change in national average consumption compared to the former period, or None if not available.
    corresponding : float | None
        The corresponding consumption value for the same period in the previous year, or None if not available.
    price : float | None
        The price associated with the consumption, or None if not available.
    cumulativePrice : float
        The cumulative price for the consumption up to the specified time period.
    aconto : float | None
        The aconto (advance payment) amount associated with the consumption, or None if not available.
    date : str
        The date associated with the consumption element.
    stopDate : str | None
        The stop date for the consumption element, or None if not available.
    interval : int
        The interval for the consumption element (e.g., hourly, daily).
    outsideTemperature : float | None
        The outside temperature associated with the consumption element, or None if not available.
    headline : str
        The headline or title for the consumption element.
    dateValueTemplate : str
        The template for displaying the date and value of the consumption element.
    message : str
        The message or description associated with the consumption element.
    seriesSetup : str | None
        The series setup information for the consumption element, or None if not available.
    periodeFrom : str | None
        The start date of the period for the consumption element, or None if not available.
    periodeTo : str | None
        The end date of the period for the consumption element, or None if not available.
    priceValue : int | None
        The price value associated with the consumption, or None if not available.
    """

    when: str
    value: int | None
    formerPeriode: float | None
    minValue: int | None
    maxValue: float | None
    percent: float | None
    property: float | None
    propertyProcentage: float | None
    national: float | None
    nationalProcentage: float | None
    corresponding: float | None
    price: float | None
    cumulativePrice: float
    aconto: float | None
    date: str
    stopDate: str | None
    interval: int
    outsideTemperature: float | None
    headline: str
    dateValueTemplate: str
    message: str
    seriesSetup: str | None
    periodeFrom: str | None
    periodeTo: str | None
    priceValue: int | None

ElectricityConsumptionResponse: TypeAlias = list[ElectricityConsumptionElement]  # numpydoc ignore=ES01,SA01,EX01
"""Represent the response for economy and consumption elements from the ista EcoTrend DK Graphs API."""