# Air Quality Comparison — Polish Cities

Which Polish city has the worst air quality right now?

A Python script that fetches live PM2.5 air quality data for several Polish cities using the Open-Meteo Air Quality API (no API key required), compares them, and identifies the city with the worst current air quality.

## Example

Current PM2.5 values: {'Wrocław': 8.2, 'Warszawa': 10.9, 'Kraków': 13.3, 'Gdańsk': 5.0, 'Poznań': 9.2}
Highest PM2.5 level: Kraków (13.3 μg/m³)



## How to Run

```bash
pip install requests
python main.py
Tech Stack
Python — requests
Open-Meteo Air Quality API — free, no authentication required
Portfolio project by Wiktoria Gocałek · Data Engineering · 2026


