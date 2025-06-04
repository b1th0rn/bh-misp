# MISP instance to-do list and tasks

## Core Configuration

- Enrichment
    - Enable the feature
    - Write a user guide

- TAXII

## Integration

- Get IoCs based on the 'last seen' condition
    - Create a JSON file with IoCs, last seen date, and expiration date
    - Create a CSV file with IoCs, last seen date, and expiration date

Note -- The expiration date is determined by the sightings linked to each attribute. You can access these sightings using the /sightings/index/*event_id* API endpoint.
``` bash
curl -k -X GET https://misp.bithorn.org/sightings/index/*event_id* -H "Authorization: *api_key*" -H "Accept: application/json" -H "Content-Type: application/json"
```