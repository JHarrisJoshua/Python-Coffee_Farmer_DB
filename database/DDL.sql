-- Coffee Farmer's Almanac
-- Joshua Harris
-- Table structure for Coffee Database
--

begin;
set transaction read write;

DROP TABLE IF EXISTS varieties, regions, types, organizations, countries;

DROP TYPE IF EXISTS soil, ranges, orgs;

CREATE TABLE Countries (
  country_id SERIAL PRIMARY KEY,
  country varchar(255) NOT NULL,
  export_quantity int NOT NULL,
  export_usd int NOT NULL,
  cultivated_area int NOT NULL
);

CREATE TYPE soil AS ENUM('Andosol','Red Latosol','Red-yellow Latosol');
CREATE TYPE ranges AS ENUM('High','Medium','Low');
CREATE TYPE orgs AS ENUM('Breeder','Rights Holder');

CREATE TABLE Regions (
  region_id SERIAL PRIMARY KEY,
  region varchar(255) NOT NULL,
  soil_type soil NOT NULL DEFAULT 'Andosol',
  altitude ranges NOT NULL DEFAULT 'Medium',
  rainfall ranges NOT NULL DEFAULT 'Medium',
  temp ranges NOT NULL DEFAULT 'Medium',
  country_id int NOT NULL,
  FOREIGN KEY(country_id) REFERENCES Countries(country_id) ON DELETE CASCADE
);

CREATE TABLE Organizations (
  organization_id SERIAL PRIMARY KEY,
  org_name varchar(255) NOT NULL,
  org_type orgs NOT NULL
);

CREATE TABLE Types (
  type_id SERIAL PRIMARY KEY,
  type_name varchar(255) NOT NULL,
  description varchar(255) NOT NULL
);

CREATE TABLE Varieties (
  plant_id SERIAL PRIMARY KEY,
  plant_name varchar(255) NOT NULL,
  rust_resist ranges NOT NULL DEFAULT 'Medium',
  nematode_resist ranges NOT NULL DEFAULT 'Medium',
  optimal_altitude ranges NOT NULL DEFAULT 'Medium',
  optimal_rainfall ranges NOT NULL DEFAULT 'Medium',
  optimal_temp ranges NOT NULL DEFAULT 'Medium',
  organization_id int DEFAULT NULL,
  type_id int NOT NULL,
  FOREIGN KEY(type_id) REFERENCES Types(type_id) ON DELETE CASCADE,
  FOREIGN KEY(organization_id) REFERENCES Organizations(organization_id)
  ON DELETE SET NULL
);

INSERT into Countries (country, export_quantity, export_usd, cultivated_area)
VALUES('Brazil', 56300000, 3810000, 2480000),
('Vietnam',30500000, 2240000 ,605000),
('Colombia', 12900000, 2540000, 860000),
('Indonesia',10630000, 842540 , 1200000);

INSERT into Types (type_name, description)
VALUES ('Arabica', 'Considered the first type of coffee cultivated, this species makes up a majority of global production'),
('Robusta', 'Robusta is known to have a higher yield and be less susceptible than Arabica'),
('Excelsa', 'Resistant to many common diseases and pests. Unlike other types, it grows taller and resembles a tree more than a shrub'),
('Liberica','Has lower caffeine content than other types, but commands a higher price due to limited supply');

INSERT into Regions(region, soil_type, altitude, rainfall, temp, country_id)
VALUES ('Minas Gerais', 'Red-yellow Latosol', 'Low', 'Medium', 'Medium', 1),
('Cerrado', 'Red Latosol', 'Medium', 'Low', 'Medium', 1),
('Mogiana', 'Red Latosol', 'Medium', 'Low', 'Medium', 1),
('Bahia', 'Andosol', 'Medium', 'Low', 'High', 1),
('Rondonia', 'Red Latosol', 'Low', 'Medium', 'Medium',1),
('Da Lat', 'Red Latosol', 'High', 'Medium', 'Low', 2),
('Dak Lak', 'Red-yellow Latosol', 'Low', 'Medium', 'High', 2),
('Gia Lai', 'Red-yellow Latosol', 'Low', 'Medium', 'High', 2),
('Dak Nong', 'Andosol', 'Low', 'Medium', 'High', 2),
('Lam Dong', 'Andosol', 'Low', 'Low', 'High',  2),
('Narino', 'Andosol', 'Medium', 'Low', 'High', 3),
('Cauca', 'Andosol', 'Medium', 'Low', 'High', 3),
('Meta', 'Andosol', 'High', 'Medium', 'Low',  3),
('Huila', 'Andosol', 'High', 'Medium', 'Low', 3),
('Tolima', 'Andosol', 'High', 'Medium', 'Low',  3),
('Sumatra', 'Andosol', 'Low', 'High', 'High',  4),
('Java', 'Andosol', 'Low', 'Medium', 'Medium', 4),
('Sulawesi', 'Red Latosol', 'Medium', 'Low', 'High', 4),
('Flores', 'Red Latosol', 'Low', 'Low', 'High', 4),
('Bali', 'Red Latosol', 'Low', 'Low', 'High', 4);

INSERT into Organizations(org_name, org_type)
VALUES('International Union for the Protection of New Varieties of Plants', 'Rights Holder' ),
('Central Highlands Agroforestry', 'Breeder'),
('Indonesian Coffee and Cocoa Research Institute', 'Breeder'),
('Brazilian Coffee Institute', 'Rights Holder');

INSERT into Varieties(plant_name, rust_resist, nematode_resist, optimal_altitude,optimal_rainfall, optimal_temp, organization_id, type_id)
VALUES ('Bourbon-Typica', 'Low', 'Low', 'Low', 'Medium', 'Medium', NULL, 1),
('Typica', 'Low', 'Low', 'High', 'Medium', 'Low', NULL, 1),
('TR4', 'High', 'Medium', 'Low', 'Medium', 'High', 2, 2),
('BP961', 'Medium', 'High', 'Low', 'Medium', 'High', 3, 2),
('Conilon', 'Medium', 'Medium', 'Medium', 'Low', 'High', 4, 1),
('Johor', 'High', 'High', 'Low', 'High', 'High', NULL ,4),
('Luwak', 'Medium', 'High', 'Medium', 'Low', 'Medium', 3,4),
('Mooleh Manay', 'Medium', 'Medium', 'Low', 'Medium', 'High', 2,  3),
('Suntikoopa', 'High', 'High' , 'Low', 'Low', 'High', 1, 3);

commit;
