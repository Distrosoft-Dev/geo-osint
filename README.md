# GeoOSINT Tool

**GeoOSINT** is a centralized Python geolocation tool designed for OSINT (Open Source Intelligence). It allows you to search for an address or coordinates and generate direct links to multiple popular mapping services.

---

## Features

- Search for coordinates from an address using the **Nominatim** API (OpenStreetMap).  
- Direct support for user-entered `(lat, lon)` coordinates.  
- Automatic generation of links for:  
  - Google Maps  
  - Yandex Maps  
  - OpenStreetMap  
  - Baidu Maps  
  - Bing Maps  
- Option to open all links directly in the browser.  
- Enhanced terminal interface using **Rich** for colorful and structured output.

---

## Requirements

- Python 3.13  
- Python modules:  
  - `requests`  
  - `rich`  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Distrosoft-Dev/geo-osint.git
cd geo-osint

