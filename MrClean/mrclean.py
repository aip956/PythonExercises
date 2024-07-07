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
# content of the pages. Returns the merged content.
def merge_contents(data):
    pages = data["query"]["pages"]
    content = ""
    for page in pages:
        content += page["revisions"][0]["content"]
    return content

# Tokenize the content by splitting it into words. The content is split
# by spaces and newline characters. Returns a list of tokens (words).
def tokenize(content):
    splitters = [" ", "\n"]
    regex_pattern = "|".join(map(re.escape, splitters))
    tokens = re.split(regex_pattern, content)
    return tokens

#Update the collection of words for them to be lower case
def lower_collection(collection):
    return [word.lower() for word in collection]

# Count the number of occurences of each word in the collection. Returns
# a dictionary where the keys are the words and the values are the counts.
def count_frequency(collection):
    frequency = {}
    for word in collection:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Filter out insignificant words from the frequency dictionary. The
# words to filter out are stored in the stopwords list. Returns a new
# dictionary with the insignificant words removed.
stop_words = ["the", "a", "an", "in", "on", "of", "and", "for", "to", "from", "with", "by", "as", "at", "that", "this", "these", "those", "then", "than", "thus", "so", "or", "but", "not", "is", "are", "was", "were", "be", "being", "been", "have", "has", "had", "do", "does", "did", "can", "could", "will", "would", "shall", "should", "may", "might", "must", "it", "its", "they", "their", "them", "he", "his", "him", "she", "her", "it", "its", "they", "their", "them", "he", "his", "him", "she", "her", "i", "me", "my", "mine", "you", "your", "yours", "we", "us", "our", "ours", "yourself", "yourselves", "myself", "ourselves", "himself", "herself", "itself", "themselves", "each", "every", "either", "neither", "some", "any", "all", "most", "several", "few", "many", "much", "more", "less", "least", "own", "other", "another", "such", "what", "which", "who", "whom", "whose", "where", "when", "why", "how", "if", "whether", "either", "or", "neither", "nor", "both", "and", "but", "however", "although", "though", "even", "just", "only", "unless", "until", "while", "because", "since", "so", "therefore", "thus", "hence", "accordingly", "consequently", "furthermore", "moreover", "meanwhile", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "one", "two", "three"]
def remove_stop_words(words, stop_words):
    return [word for word in words if word not in stop_words and word.strip() and word.isalpha()]


def print_most_frequent(frequency, n):
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(f"{sorted_frequency[i][0]}: {sorted_frequency[i][1]}")


# Fetch content from article "Ozone_layer"
data = get_content("Ozone_layer")
merge_content = merge_contents(data)
collection = tokenize(merge_content)
collection_lower = lower_collection(collection)
collection_filtered = remove_stop_words(collection_lower, stop_words)
frequency = count_frequency(collection_filtered)
# print(f"data: ", data)
# print(f"merge_content: ", merge_content)
# print(f"collection: ", collection)
# print(f"collection_lower: ", collection_lower)
# print(f"frequency: ", frequency)
print_most_frequent(frequency, 10)