import cloudscraper
from bs4 import BeautifulSoup
import datetime

def requestDetailsMatches(qtd):
    url = 'https://www.hltv.org/stats/teams/matches/8297/furia'
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)


    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')

        rows = soup.select('table.stats-table tbody tr')
        partidas = []

        for row in rows:


            date = row.select_one('td.time a').text.strip()
            opponent = row.select_one('td:not([class]) a').text.strip()
            event = row.select_one('td.gtSmartphone-only a span').text.strip()
            result = row.select_one('td.gtSmartphone-only.text-center span.statsDetail').text.strip()
            map_played = row.select_one('td.statsMapPlayed span').text.strip()
            match_link = 'https://www.hltv.org' + row.select_one('td.time a')['href']

            partidas.append({
                'data': date,
                'oponente': opponent, 
                'evento': event,
                'resultado': result,
                'mapa': map_played,
                'link': match_link
            })
        result = ''
        for p in partidas[:qtd]:
            result += f"🗓️ {p[ 'data']} - vs {p['oponente']}\n"
            result += f"🏆 Evento: {p['evento']} | 🗺️ Mapa: {p['mapa']}\n"
            result += f"📊 Resultado: {p['resultado']}\n"
            result += f"🔗 Link: {p['link']}\n\n"
        return result
    else:
        return("Ih... Barrou !")


