# Star Wars API (SWAPI) - README

Welcome to the Star Wars API (SWAPI) documentation. SWAPI is a RESTful web service
that provides comprehensive data about the Star Wars universe, including information
about films, characters, starships, vehicles, species, and planets.
This README will guide you through the usage and capabilities of the SWAPI.

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
    - [Base URL](#base-url)
    - [Endpoints](#endpoints)
3. [Data Categories](#data-categories)
4. [Authentication](#authentication)
5. [Rate Limiting](#rate-limiting)
6. [Error Handling](#error-handling)
7. [Examples](#examples)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

SWAPI is a free and open API that aims to provide Star Wars enthusiasts with easily
accessible data from various aspects of the Star Wars universe. It allows developers
to fetch information about films, characters, starships, vehicles, species, and planets.
The data is provided in a machine-readable JSON format.

## Usage

### Base URL

The base URL for accessing SWAPI is: `https://swapi.dev/api/`

### Endpoints

SWAPI offers the following endpoints:

- `/films`: Information about Star Wars films.
- `/people`: Information about characters in the Star Wars universe.
- `/starships`: Information about starships in the Star Wars universe.
- `/vehicles`: Information about vehicles in the Star Wars universe.
- `/species`: Information about different species in the Star Wars universe.
- `/planets`: Information about planets in the Star Wars universe.

For detailed information on the available fields and data structure for each endpoint,
refer to the [SWAPI documentation](https://swapi.dev/documentation).

## Data Categories

SWAPI is organized into several data categories:

- Films: Information about individual films, including title, release date, director, and characters.
- People: Information about characters, including name, birth year, gender, and related films.
- Starships: Information about starships, including name, model, manufacturer, and pilots.
- Vehicles: Information about vehicles, including name, model, manufacturer, and pilots.
- Species: Information about species, including name, classification, language, and related characters.
- Planets: Information about planets, including name, climate, population, and related films.

## Authentication

SWAPI does not require authentication to access its data. It is an open API available for public use.

## Rate Limiting

SWAPI implements rate limiting to ensure fair usage of the API. By default, each IP
address is limited to **1000 requests per day**. This limit may change over time,
so please refer to the [SWAPI documentation](https://swapi.dev/documentation) for the most up-to-date information.

# [MIT License](LICENSE.md). Make sure to review and comply with the terms of the license when using the API.

---

Feel free to explore the vast Star Wars universe through the SWAPI.
May the Force be with you as you build amazing applications using this
API! If you have any questions, refer to the [official documentation]
(https://swapi.dev/documentation) or reach out to the SWAPI community.# Error Handling

SWAPI returns appropriate HTTP status codes and error messages for different scenarios
Make sure to handle errors gracefully in your applications by
checking the status codes and error responses from the API.

## Examples

Here are some examples of how to use SWAPI:

1. Get information about a specific film:
   ```
   GET https://swapi.dev/api/films/1/
   ```

2. Retrieve details about a character:
   ```
   GET https://swapi.dev/api/people/5/
   ```

3. Fetch data about a starship:
   ```
   GET https://swapi.dev/api/starships/9/
   ```
