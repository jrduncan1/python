SELECT countries.name, languages.language, languages.percentage
FROM countries JOIN languages ON countries.id = languages.country_id
WHERE language = "Slovene"
ORDER BY languages.percentage DESC;

SELECT countries.name, count(*) AS num_of_cities
FROM cities
JOIN countries on cities.country_ID = countries.id
GROUP BY countries.name
ORDER BY num_of_cities DESC;

SELECT cities.name, cities.population FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = "mexico" AND cities.population > 500000
ORDER BY cities.population DESC;

SELECT languages.language, countries.name, languages.percentage
FROM languages LEFT JOIN countries ON languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT countries.name, countries.surface_area, countries.population FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = "constitutional monarchy" AND capital > 200 AND life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name = "Argentina" AND cities.district = "Buenos Aires";

SELECT countries.region, COUNT(countries.name) AS country_count FROM countries
GROUP BY countries.region
ORDER BY country_count DESC;