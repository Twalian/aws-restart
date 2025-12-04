"""
Creare un dizionario config con le seguenti coppie:
"host": "192.168.1.1"
"port": 8080
"ssl": True
"timeout": 30
Stampare il valore di "host"
Modificare "port" in 443
Aggiungere una nuova chiave "protocol" con valore "https"
Stampare il dizionario completo

Output Atteso:
Host: 192.168.1.1
{'host': '192.168.1.1', 'port': 443, 'ssl': True, 'timeout': 30, 'protocol': 'https'}
"""

config : dict[str, str | int | bool] = {
    "host" : "192.168.1.1",
    "port" : 8080,
    "ssl" : True,
    "timeout" : 30
}

print(config["host"])

config["port"] = 443

config["protocol"] = "https"

print(config)