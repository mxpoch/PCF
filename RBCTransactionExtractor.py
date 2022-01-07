from bs4 import BeautifulSoup
import pandas as pd
import re

filename = input("Name of File: ")
output = input("Name of Exported CSV: ")

with open(filename+'.html', 'r') as webpage:
    soup = BeautifulSoup(webpage, 'html.parser')
    tranlib = {}
    
    for row in soup.find_all('tr'):
        current = row.find_all(attrs={"class" : re.compile('withdraw|deposit')})
        if len(current) > 0: 
            amount = current[0].find('span').text.replace("$","")
            rawdate = str(current[0]['headers'][0]).split("-")
            date = " "
            for c in reversed(rawdate): date += c
            tranlib[hash(date+amount)] = [date, amount]

    df = pd.DataFrame(tranlib.values(), columns=["Date","$CAD"])
    df.to_csv(output+'.csv', index=False)
