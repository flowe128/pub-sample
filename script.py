import requests
import hashlib

data = requests.get('http://localhost:5000/data').text

file_name = hashlib.sha256(data.encode()).hexdigest()
file_content = data

with open(f'files/{file_name}.txt', 'w') as file:
    file.write(file_content)
