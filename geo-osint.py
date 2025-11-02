# geo_osint_tool.py
import webbrowser
import requests
import urllib.parse

from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel

console = Console()

def geocode_address(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "GeoOSINTTool/1.0"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        return float(data[0]['lat']), float(data[0]['lon'])
    return None, None

def generate_links(lat, lon):
    return {
        "Google Maps": f"https://www.google.com/maps?q={lat},{lon}",
        "Yandex Maps": f"https://yandex.com/maps/?ll={lon}%2C{lat}&z=16",
        "OpenStreetMap": f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=18/{lat}/{lon}",
        "Baidu Maps": f"http://api.map.baidu.com/marker?location={lat},{lon}&output=html",
        "Bing Maps": f"https://www.bing.com/maps?cp={lat}~{lon}&lvl=16"
    }

def main():
    console.print(Panel("[bold cyan]GeoOSINT - Outil de recherche de géolocalisation \nby Distrosoft[/bold cyan]", width=60))
    query = Prompt.ask("[bold green]Entrez une adresse ou des coordonnées (lat,lon)[/bold green]")

    if "," in query and all(part.replace(".", "", 1).replace("-", "", 1).isdigit() for part in query.split(",")):
        lat, lon = map(float, query.split(","))
    else:
        lat, lon = geocode_address(query)
        if lat is None:
            console.print("[red]Adresse introuvable. Veuillez réessayer.[/red]")
            return

    links = generate_links(lat, lon)
    console.print(f"\n[bold yellow]Résultats pour:[/bold yellow] [italic]{query}[/italic] ({lat}, {lon})\n")

    for name, url in links.items():
        console.print(f"[cyan]{name}[/cyan]: {url}")

    if Prompt.ask("\n[bold green]Ouvrir tous les liens dans le navigateur ?[/bold green] (y/n)").lower() == 'y':
        for url in links.values():
            webbrowser.open_new_tab(url)

if __name__ == "__main__":
    main()

