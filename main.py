import re
#
# Extracts all URLs from a .txt File
#
result = list()

with open(r"\PathToFile") as file:
    for line in file:
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)

        for url in urls:
            if url is not []:
                result.append(url)

# Function to sort in tld order
def tld(result):
    return result.split('.')[-1]


# Using sorted and calling function
Output = sorted(result, key=tld)

for url in Output:
    print (url)