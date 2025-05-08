from datetime import datetime

def bus_ticket_price(age: int, ride_datetime: datetime, ride_duration: int, is_public_holiday: bool) -> float:
    """
    Compute the price of a bus ride based on multiple rules:
    - Age-based pricing
    - Time-based surcharge (peak hours)
    - Weekend vs weekday flat rate
    - Public holiday override
    - Short trip during off-peak hours
    """
    # TODO: Public holiday overrides all
    if is_public_holiday:
        return 3.0 + 2.0 #charge holiday, full fare 3$ bcs holiday(2$ override other rules)

    # TODO: Free for children under 2
    if age < 2:
        return 0.0

    # TODO: Weekend flat rate
    weekday = ride_datetime.weekday()
    if weekday >= 5:  # Saturday or Sunday
        return 0.0 if age < 2 else 2.0

    # TODO: Short trip under 5 minutes during off-peak (non-weekend)
    if ride_duration < 5 and not is_peak_hour(ride_datetime):
        return 0.0

    # TODO: Base fare
    base_fare = 3.0
    if age < 18 or age > 65:
        base_fare = base_fare / 2

    # TODO: Add peak surcharge
    if is_peak_hour(ride_datetime):
        base_fare += 1.5

    return base_fare


def is_peak_hour(dt: datetime) -> bool:
    """
    Returns True if the datetime is within weekday peak hours:
    - Morning: 07:00–09:00
    - Evening: 16:00–18:00
    """
    hour = dt.hour
    return (7 <= hour < 9) or (16 <= hour < 18)
