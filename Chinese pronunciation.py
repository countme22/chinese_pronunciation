# Requirement:
# pip3 install requests
# pip3 install beautifulsoup4
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

def query_data_from_moe(vocabulary):
    url_add = f'https://crptransfer.moe.gov.tw/index.jsp?SN={vocabulary}&sound=1#res'
    print(f"Download {vocabulary}...")
    response = requests.get(url_add, headers=headers)
    response_text = response.text
    soup = BeautifulSoup(response_text, 'lxml')
    query_sections = soup.find_all(target="new")
    try:
        if len(query_sections) > 0:
            word_id = query_sections[0].attrs["href"].split("=")[-1]
            download = requests.get(f'https://crptransfer.moe.gov.tw/getSound.jsp?ID={word_id}',headers=headers)
        if download.status_code == 200:
            with open('hello.mp3', 'wb') as f:
                f.write(download.content)
    except:
        pass
vocabulary = '海邊'
query_data_from_moe(vocabulary)