import sys
import re
from collections import defaultdict
from datetime import datetime

def citeste_fisier(cale_fisier):
    try:
        with open(cale_fisier, 'r') as fisier:
            linii = fisier.readlines()
        return linii
    except FileNotFoundError:
        print(f"Fisierul '{cale_fisier}' nu a fost gasit.")
        return []
    except Exception as e:
        print(f"Eroare la citirea fisierului: {e}")
        return []

def parseaza_linie(linie):
    pattern = re.compile(r'(?P<IP_ADDRESS>\d+\.\d+\.\d+\.\d+)\|(?P<PAGE_REQUEST>\/\w*)\|'r'(?P<RESPONSE_CODE>\d+)\|(?P<DATE_TIME>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    match = pattern.match(linie)
    if match:
        return match.groupdict()
    return None

def valideaza_linie(linie):
    if not linie['RESPONSE_CODE'].isdigit():
        return False
    try:
        datetime.strptime(linie['DATE_TIME'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False
    return True

def analizeaza_trafic(log_data):
    statistici_ip = defaultdict(list)
    pagini_vizitate = defaultdict(int)
    ore_aglomerate = defaultdict(int)

    for linie in log_data:
        linie_parsata = parseaza_linie(linie)
        if linie_parsata:
            if not valideaza_linie(linie_parsata):
                print(f"Linie invalida: {linie}")
                continue

            ip_address = linie_parsata['IP_ADDRESS']
            pagina = linie_parsata['PAGE_REQUEST']
            ora = datetime.strptime(linie_parsata['DATE_TIME'], '%Y-%m-%d %H:%M:%S').hour

            statistici_ip[ip_address].append({
                'PAGE_URL': pagina,
                'HTTP_STATUS_CODE': int(linie_parsata['RESPONSE_CODE']),
                'DATE_TIME': linie_parsata['DATE_TIME']
            })

            pagini_vizitate[pagina] += 1
            ore_aglomerate[ora] += 1

    return statistici_ip, pagini_vizitate, ore_aglomerate

def afiseaza_statistici(statistici_ip, pagini_vizitate, ore_aglomerate):
    print("\nStatistici IP:")
    for ip, statistici in statistici_ip.items():
        print(f"{ip}: {len(statistici)} requests")

    print("\nCele mai vizitate pagini:")
    for pagina, numar_vizite in sorted(pagini_vizitate.items(), key=lambda x: x[1], reverse=True):
        print(f"{pagina}: {numar_vizite} vizite")

    ora_maxima = max(ore_aglomerate, key=ore_aglomerate.get)
    print(f"\nOra cu cel mai mare trafic: {ora_maxima}:00 - {ora_maxima + 1}:00")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizare: python script.py cale/catre/fisier.txt")
        sys.exit(1)

    cale_fisier = sys.argv[1]
    log_data = citeste_fisier(cale_fisier)

    if not log_data:
        sys.exit(1)

    statistici_ip, pagini_vizitate, ore_aglomerate = analizeaza_trafic(log_data)
    afiseaza_statistici(statistici_ip, pagini_vizitate, ore_aglomerate)