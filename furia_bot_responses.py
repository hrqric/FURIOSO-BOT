import cloudscraper
from bs4 import BeautifulSoup
from datetime import datetime
import locale

# def GET_DATA(url):
#     scraper = cloudscraper.create_scraper()
#     response = scraper.get(url)
#     return response


def requestDetailsMatches(qtd):
    scraper = cloudscraper.create_scraper()

    url = 'https://www.hltv.org/stats/teams/matches/8297/furia'
    response = scraper.get(url)


    if response.status_code == 200:
        i = 0
        soup = BeautifulSoup(response.text,'html.parser')

        rows = soup.select('table.stats-table tbody tr')
        partidas = []

        for row in rows:
            if i != qtd:
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
                i+=1
            else:
                break
        result = ''
        for p in partidas[:qtd]:
            result += f"🗓️ {p[ 'data']} - vs {p['oponente']}\n"
            result += f"🏆 Evento: {p['evento']} | 🗺️ Mapa: {p['mapa']}\n"
            result += f"📊 Resultado: {p['resultado']}\n"
            result += f"🔗 Link: {p['link']}\n\n"
        return result
    else:
        return(f"🔴Ih... Barrou 1 ! \n ‼️Error Code: {response.status_code}")

def requestLineUp():
    scraper = cloudscraper.create_scraper()

    url = 'https://www.hltv.org/team/8297/furia'

    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        
        count = 0
        lineup = [] 
        a_tags = soup.find_all('a', class_='col-custom')
        
        for a in a_tags:
            count += 1

            nome_jogador = a.select_one('div.overlayImageFrame div.text-ellipsis.nickname-container div.playerFlagName span.text-ellipsis.bold').text.strip()
            nacionalidade_jogador = a.select_one('div.overlayImageFrame div.text-ellipsis.nickname-container div.playerFlagName span.gtSmartphone-only img')['title']

            lineup.append({
                f'nickname': nome_jogador,
                'nacionalidade': nacionalidade_jogador
            })
        
        locale.setlocale(locale.LC_TIME, 'pt-BR.UTF-8')

        mes_atual_nome = datetime.now().strftime("%B")

        result = f'FURIA LINEUP {mes_atual_nome.upper()} \n\n'
        for player in lineup:
            result += f"🙎 {player['nickname']}\n"
            result += f"🏳️  {player[    'nacionalidade']}\n\n"
        return result
    else:
        return(f"🔴Ih... Barrou 2 ! \n ‼️Error Code: {response.status_code}")
        
# def requestRanking():
#     url = ''
#     scraper = cloudscraper.create_scraper()
#     response = scraper.get(url)

#     if response.status_code == 200:

#         print("fds")
#     else:
#         return(f"🔴Ih... Barrou 3 ! \n ‼️Error Code: {response.status_code}")

