import requests
import re #For tokenizing the content


# Fetch content from Wikipedia by making an HTTP GET request to
# the Wikipedia API. The article_name parameter is the name of the
# article to fetch. It returns the JSON response from the API.
def get_content(article_name):
    url = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": article_name,
        "prop": "revisions",
        "rvprop": "content",
        "formatversion": 2
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# Clean the data; merge the contents of the pages into a single string
# and return it. Extracts the pages from the data and concatenates the

def merge_contents(data):
    pages = data["query"]["pages"]
    content = ""
    for page in pages:
        content += page["revisions"][0]["content"]
    return content

def tokenize(content):
    splitters = [" ", "\n"]
    regex_pattern = "|".join(map(re.escape, splitters))

# Fetch content from article "Ozone_layer"
data = get_content("Ozone_layer")
merge_content = merge_contents(data)
print(f"data: ", data)
# print(f"merge_content: ", merge_content)