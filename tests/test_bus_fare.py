import unittest
from datetime import datetime
from src.bus_fare import bus_ticket_price

class TestBusFare(unittest.TestCase):

    def test_child_under_2_free(self):
        dt = datetime(2024, 5, 6, 10, 0)  # Weekday morning, off-peak
        fare = bus_ticket_price(age=1, ride_datetime=dt, ride_duration=10, is_public_holiday=False)
        self.assertEqual(fare, 0.0)

    # TODO: Complete the tests below based on rules

    def test_teenager_half_fare(self):
        ride_datetime = datetime(2025, 5, 6, 10, 0)  # Non-peak weekday
        price = bus_ticket_price(age=17, ride_datetime=ride_datetime, ride_duration=10, is_public_holiday=False)
        self.assertEqual(price, 1.5)  # Half of $3

    def test_adult_full_fare(self):
        ride_datetime = datetime(2025, 5, 6, 10, 0)  # Non-peak weekday
        price = bus_ticket_price(age=30, ride_datetime=ride_datetime, ride_duration=10, is_public_holiday=False)
        self.assertEqual(price, 3)  #$3

    def test_senior_half_fare(self):
        ride_datetime = datetime(2025, 5, 6, 10, 0)  # Non-peak weekday
        price = bus_ticket_price(age=70, ride_datetime=ride_datetime, ride_duration=10, is_public_holiday=False)
        self.assertEqual(price, 1.5)  # Half of $3

    def test_weekend_flat_rate(self):
        ride_datetime = datetime(2025, 5, 10, 10, 0)  # Weekend
        price = bus_ticket_price(age=17, ride_datetime=ride_datetime, ride_duration=10, is_public_holiday=False)
        self.assertEqual(price, 2)  # Flat weekend rate

    def test_public_holiday_surcharge(self):
        ride_datetime = datetime(2025, 5, 6, 10, 0)  # Non-weekend
        price = bus_ticket_price(age=30, ride_datetime=ride_datetime, ride_duration=10, is_public_holiday=True)
        self.assertEqual(price, 5)  # $3 + $2 holiday charge

    def test_short_trip_off_peak_free(self):
        ride_datetime = datetime(2025, 5, 6, 10, 0)  # Non-peak weekday
        price = bus_ticket_price(age=30, ride_datetime=ride_datetime, ride_duration=4, is_public_holiday=False)
        self.assertEqual(price, 0)  # Free for short off-peak rides

if __name__ == "__main__":
    unittest.main()
