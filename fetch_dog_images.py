import pandas as pd
import requests

# Read the breeds from the csv file Ramsil got
df1 = pd.read_csv('dog_breeds.csv')
breeds = df1['Breed'].tolist()

image_urls = []

for breed in breeds:
    breed_formatted = breed.lower().replace(' ', '-')
    url = f"https://dog.ceo/api/breed/{breed_formatted}/images/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            image_urls.append(data['message'])
        else:
            print(f"Breed not found on Dog CEO API: {breed}")
            image_urls.append('Breed Not Found')
    else:
        print(f"API Error for breed: {breed}")
        image_urls.append('API Error')

df2 = pd.DataFrame({
    'Breed Name': breeds,
    'Image URL': image_urls
})

df2.to_csv('dog_images.csv', index=False)

print("Done fetching the dog images!")


