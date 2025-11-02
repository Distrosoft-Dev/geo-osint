# GeoOSINT Tool

**GeoOSINT** est un outil Python de géolocalisation centralisée destiné à l'OSINT (Open Source Intelligence). Il permet de rechercher une adresse ou des coordonnées et de générer des liens directs vers plusieurs services de cartographie populaires.

---

## Fonctionnalités

- Recherche de coordonnées à partir d'une adresse via l'API **Nominatim** (OpenStreetMap).
- Prise en charge directe des coordonnées `(lat, lon)` saisies par l'utilisateur.
- Génération automatique de liens pour :
  - Google Maps
  - Yandex Maps
  - OpenStreetMap
  - Baidu Maps
  - Bing Maps
- Option pour ouvrir tous les liens directement dans le navigateur.
- Interface terminal améliorée grâce à **Rich** pour un affichage coloré et structuré.

---

## Prérequis

- Python 3.13
- Modules Python :
  - `requests`
  - `rich`

```bash
pip install -r requirements.txt
