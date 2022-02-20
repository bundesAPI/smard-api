# SMARD API

SMARD ist die Informationsplattform der Bundesnetzagentur über den deutschen Strommarkt. Unter www.smard.de stehen allen Nutzer\*innen die visuell und tabellarisch aufbereiteten Daten zur Verfügung. Die hier dokumentierte API bietet Zugriff auf die Strommarktdaten der Bundesnetzagentur.

## Anfragen

Über die API lassen sich Timestamps und Zeitreihendaten über einfache GET-requests ohne Query-String anfragen. Ergebnisse werden über Pfad-Parameter (im Folgenden in geschweiften Klammern) gefiltert.


**Zeitstempel-URL:** https://www.smard.de/app/chart_data/{filter}/{region}/index_{resolution}.json

Anfrage gibt verfügbare Timestamps für Filter, Region und Auflösung aus.


**Zeitreihen-URL:** https://www.smard.de/app/chart_data/{filter}/{region}/{filterCopy}_{regionCopy}_{resolution}_{timestamp}.json

Anfrage gibt Zeitreihendaten nach Filter, Region und zeitlicher Auflösung ab dem spezifizierten Timestamp aus. 


### Filter

**Parameter:** *resolution* 

Zeitliche Auflösung der Daten:
- 'hour' - Stündlich
- 'quarterhour' - Viertelstündlich
- 'day' - Täglich
- 'week' - Wöchentlich
- 'month' - Monatlich
- 'year' - Jährlich


**Parameter:** *filter* 

Mögliche Filter:
- '1223' - Stromerzeugung: Braunkohle
- '1224' - Stromerzeugung: Kernenergie
- '1225' - Stromerzeugung: Wind Offshore
- '1226' - Stromerzeugung: Wasserkraft
- '1227' - Stromerzeugung: Sonstige Konventionelle
- '1228' - Stromerzeugung: Sonstige Erneuerbare
- '4066' - Stromerzeugung: Biomasse
- '4067' - Stromerzeugung: Wind Onshore
- '4068' - Stromerzeugung: Photovoltaik
- '4069' - Stromerzeugung: Steinkohle
- '4070' - Stromerzeugung: Pumpspeicher
- '4071' - Stromerzeugung: Erdgas
- '410' - Stromverbrauch: Gesamt (Netzlast)
- '4359' - Stromverbrauch: Residuallast
- '4387' - Stromverbrauch: Pumpspeicher


**Parameter:** *filterCopy* 

Muss dem Wert von "filter" entsprechen (wegen kaputtem API-Design).


**Parameter:** *region* 

Land / Regelzone / Marktgebiet:
- 'DE' - Land: Deutschland
- 'AT' - Land: Österreich
- 'LU' - Land: Luxemburg
- 'DE-LU' - Marktgebiet: DE/LU (ab 01.10.2018)
- 'DE-AT-LU' - Marktgebiet: DE/AT/LU (bis 30.09.2018)
- '50Hertz' - Regelzone (DE): 50Hertz
- 'Amprion'- Regelzone (DE): Amprion
- 'TenneT' - Regelzone (DE): TenneT
- 'TransnetBW' - Regelzone (DE): TransnetBW
- 'APG' - Regelzone (AT): APG
- 'Creos' - Regelzone (LU): Creos



**Parameter:** *regionCopy* 

Muss dem Wert von "region" entsprechen (wegen kaputtem API-Design).


### Beispiel:

```bash
timestamps=$(curl -m 60 'https://www.smard.de/app/chart_data/1223/DE/index_hour.json')
timeseries=$(curl -m 60 'https://www.smard.de/app/chart_data/1223/DE/1223_DE_hour_1627855200000.json')
```


