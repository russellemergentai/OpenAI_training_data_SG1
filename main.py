# https://platform.openai.com/docs/quickstart?context=python

import csv
import re

from openai import OpenAI
client = OpenAI(
   api_key="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",
 )

request = "Write me 50 single script lines by Stargate characters followed by the corresponding witty response from jack O'Neill \
from the Stargate SG1 series four scripts. You must only use format [Q: quote ; R: response] and no other."

# model="gpt-4",
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": request}
  ]
)
 
response = completion.choices[0].message.content

print(response)

# Extracting dialogues and responses using regular expression
dialogues = re.findall(r'\[Q: (.*?) ; R: (.*?)\]', response)

csv_file = "stargate_dialogue.csv"

with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = ['Q', 'R']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for dialogue, response in dialogues:
        writer.writerow({'Q': dialogue.strip(), 'R': response.strip()})

print(f"CSV file '{csv_file}' has been created.")
