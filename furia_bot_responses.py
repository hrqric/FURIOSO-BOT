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
        
def requestRanking():
    url = 'https://www.hltv.org/team/8297/furia'
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')   
        rows = soup.find_all('div',{'flex-col','flex-col push-right'})
        auxiliar_variable = []
        count = 1

        for row in rows:
            ranking_hltv = row.select_one('div.flex span.value.h-rank').text.strip()
            ranking_valve = row.select_one('div.flex span.value.v-rank').text.strip()
            auxiliar_variable.append({
                'ID': count,
                'hltv': ranking_hltv,
                'valve': ranking_valve
            })
            count += 1

        result = 'INFORMAÇÕES RANKING - FURIA - LINEUP\n\n'
        for info in auxiliar_variable:
            if info['ID'] == 1:
                result += f'🎖️ Ranking atual HLTV: {info['hltv']}\n'
                result += f'🎖️ Ranking atual Valve: {info['valve']}\n'
            if info['ID'] == 2:
                result += f'🥇 Ranking mais alto HLTV da LINEUP: {info['hltv']}\n'
                result += f'🥇 Ranking mais alto Valve da LINEUP: {info['valve']}\n'
            if info['ID'] == 3:
                result += f'📅 Tempo no ranking mais alto HLTV da LINEUP: {info["hltv"]}\n'
                result += f'📅 Tempo no ranking mais alto Valve da LINEUP: {info["valve"]}\n\n'
            if info['ID'] == 4:
                result += 'INFORMAÇÕES RANKING - FURIA - ORGANIZAÇÃO\n\n'

            if info['ID'] == 5:
                result += f'🥇 Ranking mais alto HLTV do TIME: {info['hltv']}\n'
                result += f'🥇 Ranking mais alto Valve do TIME: {info['valve']}\n'
            if info['ID'] == 6:
                result += f'📅 Tempo no ranking mais alto HLTV do TIME: {info["hltv"]}\n'
                result += f'📅 Tempo no ranking mais alto Valve do TIME: {info["valve"]}\n\n'
        return result


    else:
        return(f"🔴Ih... Barrou 3 ! \n ‼️Error Code: {response.status_code}")


def requestNoticias():
    url = 'https://www.hltv.org/team/8297/furia#tab-newsBox'
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')   

def requestWinStreak():
    url = 'https://www.hltv.org/team/8297/furia#tab-matchesBox'
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    auxiliar_variable = []
    count = 1

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')   
        rows = soup.find_all('div', 'highlighted-stat')
        for row in rows:
            if count == 1:
                winstreak = row.select_one('div.stat').text.strip()
                count += 1
            elif count == 2:
                if row.select_one('div.description').text.strip() == "Win rate":                
                    winrate = row.select_one('div.stat').text.strip()
                    count+= 1
            else:
                auxiliar_variable.append({
                'winstreak': winstreak,
                'winrate': winrate
            })
                break


        result = 'WINSTREAK / WINRATE\n'
        for info in auxiliar_variable:
            result += f'🟨 WINSTREAK - {info['winstreak']} / WINRATE - {info['winrate']}'
        return result

def requestAllDetails():
    print('penis')