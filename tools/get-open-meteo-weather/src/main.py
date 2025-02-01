import time
import requests

def get_open_meteo_weather(latitude: float, longitude: float, timezone: str, temperature_unit: str = "fahrenheit") -> dict[str, any]:
    """Tool to get weather information based on location.
    
    Parameters:
        latitude (float): Latitude of the location, e.g., 34.0549
        longitude (float): Longitude of the location, e.g., -118.2426
        timezone (str): Timezone of the location, e.g., America/Los_Angeles
        temperature_unit (str): Unit for temperature, e.g., fahrenheit
        
    Returns:
        dict[str, Any]: Dictionary containing weather data including:
            - weather_code: Daily weather code
            - apparent_temperature_max: Maximum apparent temperature
            - apparent_temperature_min: Minimum apparent temperature
            - sunrise: Time of sunrise
            - rain_sum: Total rainfall
            - snowfall_sum: Total snowfall
            
    Raises:
        ValueError: If API request fails, times out, or returns invalid response
    """

    # For more options:
    # https://open-meteo.com/en/docs

    daily_features = [
        'weather_code',
        'apparent_temperature_max', 
        'apparent_temperature_min',
        'sunrise',
        'rain_sum',
        'snowfall_sum'
    ]

    base_url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': ','.join(daily_features),
        'timezone': timezone,
        'forecast_days': 1,
        'temperature_unit': temperature_unit
    }
    weather_forecast_url = f'{base_url}?' + '&'.join(f'{k}={v}' for k, v in params.items())

    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = requests.get(weather_forecast_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                raise ValueError('Weather API request timed out after multiple retries')
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise ValueError(f'Failed to fetch weather data: {str(e)}')
        except ValueError as e:
            raise ValueError(f'Invalid JSON response from weather API: {str(e)}')
            
        time.sleep(retry_delay)