import time
import requests

def get_bitcoin_exchange_rate(currency: str) -> dict[str, float]:
    """Tool to get Bitcoin's exchange rate from currency.
    
    Parameters:
    currency (str): Currency code to get Bitcoin exchange rate for, e.g., USD

    Returns:
        dict[str, float]: Dictionary containing the exchange rate
    
    Raises:
        ValueError: If API request fails or returns invalid response
    """
    base_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            if attempt == max_retries - 1:
                raise ValueError('Bitcoin API request timed out after multiple retries')
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise ValueError(f'Failed to fetch Bitcoin data: {str(e)}')
        except ValueError as e:
            raise ValueError(f'Invalid JSON response from Bitcoin API: {str(e)}')
            
        time.sleep(retry_delay)