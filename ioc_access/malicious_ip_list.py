#!/usr/bin/env python3

import requests, urllib3, time
from datetime import datetime, timedelta

#### Input interattivo 
misp_url = input("Inserisci l'URL di MISP (es: https://misp.bithorn.org): ").strip()
api_key = input("Inserisci la MISP API key: ").strip()
last_seen = input("Inserisci i giorni da cui parture (es: 2025-06-01): ").strip()

try:
    max_iocs = int(input("Quanti IoC vuoi estrarre? (default: 100): ") or "100")
except ValueError:
    print("Numero non valido, uso default = 100")
    max_iocs = 100

#### Parametri
verify_cert = True        # imposta a False se il certificato non è valido
timeout = 10              # timeout per la richiesta

#### Disattiva warning SSL se necessario 
if not verify_cert:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#### Calcolo timestamp 
## timestamp = int(time.mktime((datetime.now() - timedelta(days=last_days)).timetuple()))

#### Costruzione richiesta 
data = {
    "controller": "attributes",
    "type": ["ip-src"],
    "to_ids": True,
    "deleted": False,
    ## "timestamp": timestamp,
    "last_seen": last_seen,
    "order": "timestamp desc",
    "limit": max_iocs,
}

headers = {
    "Authorization": api_key,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

#### Chiamata API 
print("\n📡 Richiesta in corso a MISP...")

response = requests.post(
    f"{misp_url}/attributes/restSearch",
    json=data,
    headers=headers,
    verify=verify_cert,
    timeout=timeout
)

response.raise_for_status()
attributes = response.json().get("response", {}).get("Attribute", [])


'''
#### Estrai IP unici 
ip_list = list({attr["value"] for attr in attributes})

#### Output 
print(f"\n✅ Trovati {len(ip_list)} IP di tipo ip-src:\n")
for ip in ip_list:
    print(ip)
'''

print(f"\n✅ Trovati {len(attributes)} IP di tipo ip-src:\n")
for ip in attributes:
    print(f"IP: {ip['value']}, First Seen: {ip['first_seen']}, Last Seen: {ip['last_seen']}, Expiration: {ip['expiration_date']}")
