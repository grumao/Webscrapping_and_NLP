import requests

def web_scrape():

    resp2 = requests.get("http://3.85.131.173:8000/random_company")
    company_website = resp2.text.split("\n")
    for line in company_website:
        if 'Name:' in line:
            s1 = line
        if 'Purpose:' in line:
            s2 = line

    in1 = s1.find('Name:')
    in2 = s1.find('</li>')
    company_name = s1[(in1+6):in2]
    inp1 = s2.find('<li>Purpose:')
    inp2 = s2.find('</li>')
    company_purpose = s2[(inp1+13):inp2]

    return (company_name,company_purpose)

L = list()

for i in range(50):
    l = list(web_scrape())
    L.append(l)

import csv
fields = ['Name', 'Purpose']
with open('webscrapenames', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(L)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(L)

