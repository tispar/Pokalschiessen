# Pokalschiessen
Software zur live-Ansicht von Ranglisten während Pokalschießen des Schützenverein Rönneburg und Umgegend von 1897 e.V.

## Anforderungen
* ausführbare exe-Datei
* JSON-File auslesen und anhand von Wettbewerbsbedingungen kategoriesieren und ordnen
* Anzeige der Top-10 in den einzelnen Wettbewerben
* Such-Funktion für Teilnehmer bzw. Teams
* ggfs eine Admin-Ebene zur Implementierung weiterer Wettbewerbe 

## Aufbau der Daten 

Die Daten werden in Form einer log-Datei mit einzelnen JSON-Elementen übermittelt. In diesen JSON-Elementen ist das Element 'Objects' eingebunden, welche alle für uns relevanten Informationen beinhaltet. 

'Objects' hat folgende Struktur:
| # |  Column              |    Non-Null Count | Dtype |
|---|---|---|---|
| 0  | ShotDateTime     |       77 non-null |    object |
| 1  | TLStatus    |            77 non-null |    object | 
| 2  | LastTLChange |           77 non-null |    int64  |
| 3  | Source |           77 non-null    | object |
| 4  | Range   |                77 non-null |    int64  |
| 5  | Competition |             0 non-null |     object |
| 6  | DiscType  |              77 non-null |    object |
| 7  | DiscTypeRaw |             0 non-null |     object |
| 8  | X            |           77 non-null |    int64  |
| 9  | Y            |           77 non-null |    int64  |
| 10 | Distance     |           77 non-null |    float64 |
| 11 | Count        |           77 non-null |    int64  |
| 12 | FullValue    |           77 non-null |    int64  |
| 13 | DecValue     |           77 non-null |    float64 |
| 14 | Run          |           77 non-null |    int64 | 
| 15 | IsValid      |           77 non-null |    bool  | 
| 16 | IsWarmup     |           77 non-null |    bool  | 
| 17 | IsHot        |           77 non-null |    bool  |
| 18 | IsDummy      |           77 non-null |    bool  |
| 19 | IsInnerten   |           77 non-null |    bool  | 
| 20 | IsShootoff   |           77 non-null |    bool  | 
| 21 | Remark       |           77 non-null |    object |
| 22 | UUID         |           77 non-null |    object |
| 23 | Shooter.Firstname |       77 non-null |    object |
| 24 | Shooter.Lastname  |      77 non-null  |   object |
| 25 | Shooter.Birthyear |      77 non-null  |   int64  |
| 26 | Shooter.InternalID |     77 non-null  |   object |
| 27 | Shooter.Identification |  77 non-null |    object |
| 28 | Shooter.Team |           0 non-null   |   object |
| 29 | Shooter.Club |           0 non-null   |   object |
| 30 | MenuItem.MenuID |         77 non-null  |   object |
| 31 | MenuItem.MenuPointName | 77 non-null  |   object |
| 32 | MenuItem.MenuItemName  | 0 non-null   |   object |
| 33 | MenuItem.UUID |          77 non-null  |   object |

Die Anzahl der Non-Null Counts sind aus dem übergebenen Testdatensatz übernommen worden.

Für den endgültigen Output wird ein DataFrame mit (mindestens) folgenden Spalten benötigt

| Position | Vorname | Nachname | Punktzahl |
| --- | --- | --- | --- |
| 1 | Hans | Peter |  42 |

Je nach Wettbewerb werden unterschiedliche Kriterien zumn Filtern der Schützinnen und Schützen sowie der Erstellung der Rangfolge benutzt.

Die entsprechenden Funktionen zum Datenauslesen, der Datenaufbereitung und Erstellung der Ausgabe-Daten werden im Notebook 'backend' erstellt und getestet.

## GUI

Die grafische Nutzeroberfläche wird mit Hilfe des Python Pakets tkinter erstellt.