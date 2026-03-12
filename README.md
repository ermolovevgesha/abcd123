# Overview
A Django-based web application that displays an interactive map using Leaflet.js. Users can click on the map to save geographic coordinates (latitude/longitude) to a PostgreSQL/PostGIS database. All saved points are listed on a separate page.

# Technology Stack and Features
- **Django**
- **PostgreSQL** with **PostGIS**
- **GDAL** 
- **Leaflet.js** 
- **Docker** & **Docker Compose**
# Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/ermolovevgesha/abcd123

```

Run the following in the terminal from the project root folder:
```bash
docker compose up -d
```

# Usage
##  Displays a Leaflet map.

```
GET /map/
```
Click anywhere on the map to save the coordinates. A marker will appear indicating a successful save

```bash
curl -X 'GET' \
  'http://localhost:8000/map' \
  -H 'accept: application/json'
```

## Save a clicked point
```
POST /points
```
Saves a point with the given latitude and longitude. Expects a JSON payload:

```bash
curl -X 'POST' \
  'http://localhost:8000/points' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "lat": 55.75,
  "lng": 37.62
}'

```

## List all saved points

```
GET /points
```

Returns an HTML page listing all stored coordinates with their creation timestamps.

```bash
curl -X 'GET' \
  'http://localhost:8000/points' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
```

# Structure
```text
.
├── docker-compose.yaml          # Docker services configuration
├── Dockerfile                   # App container definition
├── manage.py
├── pyproject.toml               # Python dependencies
├── mapproject/                  # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── asgi.py
│   ├── urls.py                  # Main URL router
│   └── wsgi.py
└── mapapp/                      # Main Django application
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py                 # Location model with PointField
    ├── urls.py                   # App routes
    ├── views.py                  # MapView and PointsView
    ├── templates/
    │   └── app/
    │       ├── map.html          # Leaflet map template
    │       └── point_list.html   # Points list template
    └── migrations/
        └── ...                   # Database migrations
```
