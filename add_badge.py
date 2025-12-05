from pathlib import Path
from bs4 import BeautifulSoup
path=Path('index.html')
soup=BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
for card in soup.select('.ops-gallery article.ops-card'):
    header = card.find('div', class_='ops-card-header')
    if header and not card.find('div', class_='badge-ops-status'):
        badge = soup.new_tag('div', attrs={'class':'badge-ops-status'})
        badge.string = 'Upcoming Content'
        header.insert_before(badge)
path.write_text(str(soup), encoding='utf-8')
