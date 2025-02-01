import random
import xml.etree.ElementTree as ET
import requests

def get_arxiv_paper(topic: str) -> dict[str, str]:
    """Get a random arXiv paper related to the given topic.
    
    Args:
        topic: The scientific topic to search for
        
    Returns:
        dict[str, str]: Paper details containing title and abstract
        
    Raises:
        ValueError: If API request fails or returns invalid response
    """
    # Randomize which paper to get from first 100 results
    start = random.randint(1, 100)
    
    base_url = "https://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{topic}",
        "start": start,
        "max_results": 1
    }
    arxiv_url = f"{base_url}?" + "&".join(f"{k}={v}" for k, v in params.items())
    
    try:
        response = requests.get(arxiv_url, timeout=10)
        response.raise_for_status()
        
        # Parse XML response
        root = ET.fromstring(response.content)
        entry = root.find("{http://www.w3.org/2005/Atom}entry")
        
        if entry is None:
            raise ValueError("No papers found for the given topic")
            
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        abstract = entry.find("{http://www.w3.org/2005/Atom}summary").text
        
        return {
            "title": title.strip(),
            "abstract": abstract.strip()
        }
        
    except (requests.exceptions.RequestException, ET.ParseError) as e:
        raise ValueError(f"Failed to fetch arXiv paper: {str(e)}")