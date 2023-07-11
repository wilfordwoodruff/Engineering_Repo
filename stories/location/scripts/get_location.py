from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="zeonytang@gmail.com")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1) # at least 1 second delay between requests

def get_location_by_name(name):
    try:
        location = geocode(name)
        if location is not None:
            return location.latitude, location.longitude
    except GeocoderTimedOut:
        return get_location_by_name(name)
    return None, None
