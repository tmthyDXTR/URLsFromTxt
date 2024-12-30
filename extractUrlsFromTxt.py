import re  # Importing the 're' module for regular expression operations

# List to store extracted URLs
result = []

# Open the specified .txt file in read mode
with open(r"\PathToFile") as file:
    # Process each line in the file
    for line in file:
        # Use a regex pattern to find all URLs in the current line
        urls = re.findall(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
            line
        )

        # Add each found URL to the result list if it's not empty
        for url in urls:
            if url:  # Avoid appending empty URLs
                result.append(url)

# Function to extract the top-level domain (TLD) from a URL
def tld(url):
    """
    Extracts the top-level domain (TLD) from a given URL.
    
    Parameters:
        url (str): The URL from which to extract the TLD.
        
    Returns:
        str: The TLD of the URL.
    """
    return url.split('.')[-1]  # Split the URL by '.' and return the last segment

# Sort the URLs in the result list based on their TLDs
Output = sorted(result, key=tld)

# Print each sorted URL to the console
for url in Output:
    print(url)
