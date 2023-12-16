
use world;

-- optimize
select Name from city where Population > (select AVG(Population) from city) and CountryCode in (select Code from country where Population > (select AVG(Population) from country));
select * from city join country on city.CountryCode in  (select code from country where Name ="India");
optimize table city,country;

-- indexing
create index Name_index on country(Name);
drop index Name_index on country;
select * from country where Name = "India";
select * from city join country on city.CountryCode in  (select code from country where Name ="India");

SELECT * FROM country WHERE Continent = 'Asia' ORDER BY Population DESC;