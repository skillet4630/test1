import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        screenshots = soup.find_all('a', class_='screenshot')
        comp_addresses = []
        
        for screenshot in screenshots:
            comp_link = screenshot.get('href')
            comp_address = get_comp_address(comp_link)
            if comp_address:
                comp_addresses.append(comp_address)
            else:
                break  # Stop crawling if comp class is not found
        
        return comp_addresses
    else:
        print("Failed to fetch page:", response.status_code)
        return []

def get_comp_address(comp_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(comp_link, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        comp_element = soup.find('div', class_='comp')
        if comp_element:
            address = comp_element.text.strip()
            return address
        else:
            print("Comp class not found in:", comp_link)
            return None
    else:
        print("Failed to fetch comp page:", response.status_code)
        return None

def save_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(['Company Address'])
    for item in data:
        ws.append([item])
    wb.save(filename)

if __name__ == "__main__":
    starting_url = 'https://0xxx.me/index.php?s=publicagent+1080p'
    comp_addresses = crawl_website(starting_url)
    save_to_excel(comp_addresses, 'company_addresses.xlsx')
