import re  # Importing the 're' module for regular expression operations

# List to store extracted URLs
result = []

# Prompt the user to input the file path
file_path = input("Please enter the path to the .txt file: ")

# Open the specified .txt file in read mode
try:
    with open(file_path, 'r') as file:
        # Process each line in the file
        for line in file:
            # Use a regex pattern to find all URLs (with or without schemes)
            urls = re.findall(
                r'(?:http[s]?://)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?', 
                line
            )

            # Add each found URL to the result list if it's not empty
            for url in urls:
                if url:  # Avoid appending empty URLs
                    # Add "http://" if the URL doesn't have a scheme
                    if not url.startswith(('http://', 'https://')):
                        url = 'http://' + url
                    result.append(url)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please check the path and try again.")
    exit()

# Function to extract the top-level domain (TLD) from a URL
def tld(url):
    """
    Extracts the top-level domain (TLD) from a given URL.
    
    Parameters:
        url (str): The URL from which to extract the TLD.
        
    Returns:
        str: The TLD of the URL.
    """
    return url.split('.')[-1].split('/')[0]  # Extract the TLD from the URL

# Sort the URLs in the result list based on their TLDs
Output = sorted(result, key=tld)

# Print each sorted URL to the console
print("\nSorted URLs:")
for url in Output:
    print(url)
