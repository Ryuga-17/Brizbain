import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Function to fetch location details
def get_location(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True, timeout=10)
        if location:
            address = location.raw.get('address', {})
            town = address.get('town', '')
            city = address.get('city', address.get('municipality', ''))
            state = address.get('state', '')
            country = address.get('country', '')
            return town, city, state, country
    except GeocoderTimedOut:
        time.sleep(1)
        return get_location(lat, lon)
    except Exception as e:
        return '', '', '', ''

# Load the data file
def process_file(input_path, output_path):
    # Load the file
    data = pd.read_excel(input_path)

    # Initialize the geolocator
    global geolocator
    geolocator = Nominatim(user_agent="geo_locator")

    # Add new columns for the location details
    data[['Town', 'City', 'State', 'Country']] = data.apply(
        lambda row: pd.Series(get_location(row['Lat'], row['Long_'])), axis=1
    )

    # Save the updated data to a new file
    data.to_excel(output_path, index=False)
    print(f"Processed file saved to: {output_path}")

# Example usage
# Replace 'input_path' and 'output_path' with the actual file paths
input_path = "path_to_your_input_file.xlsx"
output_path = "path_to_your_output_file.xlsx"
process_file(input_path, output_path)
