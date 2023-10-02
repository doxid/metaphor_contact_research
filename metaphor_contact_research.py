from metaphor_python import Metaphor

# Initialize the Metaphor API client with your API key
api_key = 'b5101d09-53d3-4689-b372-a8c503a2c017'
metaphor = Metaphor(api_key)

# Define the starting URL for the assistant superintendent page
start_url = 'https://www.pausd.org/about-us/the-team'

# Find similar links to the starting URL
similar_links_response = metaphor.find_similar(url=start_url, num_results=10)

# Prepare a text file to write the results
output_file = 'assistant_superintendents.txt'


# Extract and write the results to the text file
with open(output_file, 'w') as file:
    # Write the school district name and the starting URL
    file.write(f'School District: Palo Alto Unified School District\n')
    file.write(f'Starting URL: {start_url}\n\n')

    # Write the details of the similar links
    for result in similar_links_response.results:
        title = result.title
        url = result.url
        file.write(f'School District: {title}\n')
        file.write(f'URL: {url}\n')
        file.write('\n')

print(f'Results written to {output_file}')
