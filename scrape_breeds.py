import requests
from bs4 import BeautifulSoup
import pandas as pd

'I scraped a table from the American Kennel Club webpage and store the results in a dataframe.'

url = "https://www.akc.org/expert-advice/nutrition/breed-weight-chart/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

breeds = []
male_weights = []
female_weights = []

for row in soup.find_all('tr')[1:]: 
    cols = row.find_all('td')
    if len(cols) >= 3:
        breed = cols[0].get_text()
        male = cols[1].get_text()
        female = cols[2].get_text()

        breeds.append(breed)
        male_weights.append(male)
        female_weights.append(female)

df = pd.DataFrame({
    'Breed': breeds,
    'Male Weight': male_weights,
    'Female Weight': female_weights
})

print(f'Total breeds scraped: {len(df)}\n')
print(df.head(6))

df.to_csv('dog_breeds.csv')