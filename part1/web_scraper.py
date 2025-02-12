import requests
from bs4 import BeautifulSoup

response = requests.get("https://docs.python.org/3/")

soup = BeautifulSoup(response.text, "html.parser")
footers = soup.find_all("div", class_="footer")

for footer in footers:
    footer_part = print(footer.text.split("Copyright")[0].strip())