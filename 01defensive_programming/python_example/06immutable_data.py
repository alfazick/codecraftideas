

# Immutable Data: Whenever possible, use immutable data structures that cannot 
# be modified after their creation. This approach reduces side effects and makes 
# the application's behavior more predictable. 

# Example 1 Easy: Use tuple

coordinates = (10,20)
print(f"Original coordinates: {coordinates}")

# Trying to change the value will cause an error
try:
    coordinates[0] = 15
except TypeError as e:
    print(e)


# Example 2 : Mediumd-Easy: Frozenset for Unique Collection of Items
    
# Immutable set of unique items using frozenset

inventory_items = frozenset(["apple","banana","orange"])
print(f"Original inventory items: {inventory_items}")

# Trying to add a new item will cause an error
try:
    inventory_items.add("pear")
except AttributeError as e:
    print(e)  # Frozensets are immutable

# Example 3: Medium: Immutable Class Using '@dataclass(frozen=True)'

from dataclasses import FrozenInstanceError, dataclass


@dataclass(frozen=True)
class Product:
    id: int
    name: str 
    price: float 


# Immutable product instance
product = Product(id=1, name="Laptop", price=999.99)
print(product)

# Trying to modify an attribute will cause an error
try:
    product.price = 1099.99
except FrozenInstanceError as e:
    print(e)  # Dataclass instances are immutable when frozen=True


# Scenario: System Configuration for a Web Server 
    
# Imagine you're writing a Python script to manage the configuration of a web server. 
# The server's configuration includes its port number, whether SSL is enabled, 
# and the root directory for the website it serves. 
# Once the server starts, changing these settings arbitrarily could 
# cause the server to become unreachable or introduce security issues. 
# Therefore, it's crucial to ensure that the configuration remains constant during runtime.

# Example #4
    
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class WebServerConfig:
    port: int 
    ssl_enabled: bool 
    root_dir: str 

# Immutable configuration instance
config = WebServerConfig(port=443, ssl_enabled=True, root_dir="/var/www/html")
print(config)

# The system attempts to modify the configuration after initialization
try:
    config.port = 8080  # Intentional or accidental modification attempt
except FrozenInstanceError as e:
    print(e)  # Ensures the configuration remains unchanged


# Example #5
    
# Hard: Async web_page parsing 

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup

# Define a tuple of real URLs for immutability
URLS = (
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com"
)

def fetch_and_parse_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the title of the web page 
            title = soup.find("title").text 
            return url, title
        else:
            return url, "Failed to fetch"
    except Exception as e:
        return url, f"Error: {str(e)}"
    

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_url = dict()

        for url in URLS:
            future = executor.submit(fetch_and_parse_title,url)
            future_to_url[future] = url 

        # poll features till complete
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                url, title = future.result()
                print(f"Title of {url}: {title}")
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")

main()
