#!/usr/bin/env python
from alchemyAPI import AlchemyAPI

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI('YOUR_KEY_HERE')

# Add two urls to compare
url1 = 'https://moz.com/beginners-guide-to-seo/keyword-research'
url2 = 'https://www.semrush.com/features/organic-research/'

print('Processing urls:\n' +  url2 + "\n" + url1)
print('')

# Get a keyword report
response1 = alchemyapi.keywords('url', url1, {'sentiment': 1, 'showSourceText': 1, 'sourceText' : 'raw'})
response2 = alchemyapi.keywords('url', url2, {'sentiment': 1, 'showSourceText': 1, 'sourceText' : 'raw'})

firstlist = []
secondlist = []

if response1['status'] == 'OK':
    for keyword in response1['keywords']:
        firstlist.append(keyword['text'])
else:
    print('Error in keyword extaction call: ', response1['statusInfo'])

if response2['status'] == 'OK':
    for keyword in response2['keywords']:
        secondlist.append(keyword['text'])
else:
    print('Error in keyword extaction call: ', response1['statusInfo'])

# Print the report
final_list = zip(firstlist, secondlist)

print("{:<30}     {:<30}".format(url1, url2))
counter = 0
for item in final_list:
    print("{}: {:<30}     {}: {:<30}".format(counter, ' '.join(item[0].split()), counter, ' '.join(item[1].split())))
    counter += 1

# Get a Concepts report
response1 = alchemyapi.concepts('url', url1)
response2 = alchemyapi.concepts('url', url2)

firstlist = []
secondlist = []

if response1['status'] == 'OK':
    for concept in response1['concepts']:
        firstlist.append((concept['text'], concept['relevance']))
else:
    print('Error in keyword extaction call: ', response1['statusInfo'])

if response2['status'] == 'OK':
    for concept in response2['concepts']:
        secondlist.append((concept['text'], concept['relevance']))
else:
    print('Error in keyword extaction call: ', response1['statusInfo'])

final_list = zip(firstlist, secondlist)

# Print Concepts report

print("{:<30}     {:<30}".format(url1, url2))
counter1 = 0
for item in final_list:
    print("{}: {:<30}     {}: {:<30}".format(counter1, str(item[0]), counter1, str(item[1])))
    counter1 += 1
