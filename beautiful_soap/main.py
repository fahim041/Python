from textwrap import wrap
from bs4 import BeautifulSoup
import re
import csv

Funding_list = []
Funding_dict = {}
final_description = []
final_eligibility = []

count_num = []

'''
csv_file = open('data-2.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Status', 'Ministry',
                    'Deadline', 'Description', 'Eligibility', 'url'])
'''


def clear_text(text):
    temp_text = re.sub(r'[\ \n]{2,}', '', text)
    return temp_text


with open("test.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find("div", {"id": "pagebody"})

    for i in tags.find_all("h2"):
        if 'id' in i.attrs:

            if i.text == "Overview" or i.text == "Aboriginal Participation Fund" or i.text == "Contact us" or i.text == '''Regional Development Program: Eastern Ontario Development
            Fund and Southwestern Ontario Development Fun''':
                print()
            else:
                h3Tags = i

                if h3Tags.findNext('strong'):
                    statusTag = h3Tags.findNext('strong')
                else:
                    continue

                ministryTag = statusTag.findNext('p')

                deadLineTag = ministryTag.findNext('h3')

                if deadLineTag.text == "Deadline":
                    deadLineInfoTag = deadLineTag.findNext('p')

                print(h3Tags.text)
                # print(statusTag)
                # print(ministryTag)
                print(deadLineTag)
                print(deadLineInfoTag)

                count_num.append(h3Tags)

print(len(count_num))
'''
                csv_writer.writerow([h3tagTitles, status, ministry,
                                    deadline, final_format_description, eligibility_str, url['href']])
                                    '''
