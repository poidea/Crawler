# -*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
import requests
import sys

def handle_with_single_page(page):
    page = requests.post('http://srh.bankofchina.com/search/whpj/search.jsp', 
        data={
            'pjname': '1325',
            'page': str(page),
            'erectDate': '',
            'nothing': ''
        }
    )
    soup = BeautifulSoup(page.content)
    table = soup.findAll('table', width=640)[0]
    rows = table.findAll('tr')

    for i, row in enumerate(rows):
        if i == 0:
            continue
        row_output = []
        columns = row.findAll('td')
        for i, column in enumerate(columns):
            row_output.append(column.contents[0])
        if len(row_output) > 0:
            print ' '.join(row_output)

def main():
    page = 1
    while True:
        try:
            handle_with_single_page(page)
        except:
            break

        page = page + 1

reload(sys)
sys.setdefaultencoding('utf-8')
main()
