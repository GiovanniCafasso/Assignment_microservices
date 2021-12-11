import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
DB_BOOK = session.get("http://localhost:8000/books/").content
print(DB_BOOK)


#DB_BOOK = requests.get("http://localhost:8000/books/")
#print(DB_BOOK.json())
#for book in DB_BOOK.json():
#    print(book['id'])


#DB_CUSTOMER = requests.get("http://localhost:8001/customers")
#print(DB_CUSTOMER.json())
#for customer in DB_CUSTOMER.json():
#    print(customer['id'])