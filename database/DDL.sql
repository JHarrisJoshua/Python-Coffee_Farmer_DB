-- Coffee Farmer's Almanac
-- Joshua Harris
-- Table structure for Coffee Database
--

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

CREATE OR REPLACE TABLE `Countries` (
  `country_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `country` varchar(255) NOT NULL,
  `export_quantity` int(11) NOT NULL,
  `export_usd` int(11) NOT NULL,
  `cultivated_area` int(11) NOT NULL
);

CREATE OR REPLACE TABLE `Regions` (
  `region_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `region` varchar(255) NOT NULL,
  `altitude` enum('high','med','low') NOT NULL DEFAULT 'med',
  `soil_type` enum('andosol','red latosol','red-yellow latosol') NOT NULL DEFAULT 'andosol',
  `rainfall` enum('high','med','low') NOT NULL DEFAULT 'med',
  `temp` enum('high','med','low') NOT NULL DEFAULT 'med',
  `country_id` int(11) NOT NULL,
  FOREIGN KEY(country_id) REFERENCES Countries(country_id) ON DELETE CASCADE
);

CREATE OR REPLACE TABLE `Organizations` (
  `organization_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `type` enum('Breeder','Rights Holder') NOT NULL
); 

CREATE OR REPLACE TABLE `Types` (
  `type_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL
);

CREATE OR REPLACE TABLE `Varieties` (
  `plant_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `plant_name` varchar(255) NOT NULL,
  `rust_resist` enum('high','med','low') NOT NULL DEFAULT 'med',
  `nematode_resist` enum('high','med','low') NOT NULL DEFAULT 'med',
  `optimal_altitude` enum('high','med','low') NOT NULL DEFAULT 'med',
  `optimal_rainfall` enum('high','med','low') NOT NULL DEFAULT 'med',
  `optimal_temp` enum('high','med','low') NOT NULL DEFAULT 'med',
  `organization_id` int(11) DEFAULT NULL,
  `type_id` int(11) NOT NULL,
  FOREIGN KEY(type_id) REFERENCES Types(type_id) ON DELETE CASCADE,
  FOREIGN KEY(organization_id) REFERENCES Organizations(organization_id) 
  ON DELETE SET NULL
);

CREATE OR REPLACE TABLE `Regions_Varieties` (
  `region_plant_id` int(11) AUTO_INCREMENT NOT NULL PRIMARY KEY,
  `region_id` int(11) NOT NULL,
  `plant_id` int(11) NOT NULL,
   FOREIGN KEY(region_id) REFERENCES Regions(region_id) ON DELETE CASCADE,
   FOREIGN KEY(plant_id) REFERENCES Varieties(plant_id) ON DELETE CASCADE
);

INSERT into Countries (country, export_quantity, export_usd, cultivated_area)
VALUES('Brazil', 56300000, 3810000, 2480000),
('Vietnam',30500000, 2240000 ,605000),
('Colombia', 12900000, 2540000, 860000),
('Indonesia',10630000, 842540 , 1200000);

INSERT into Types (name, description)
VALUES ('arabica', "Considered the first type of coffee cultivated, this species makes up a majority of the world's production"),
('robusta', "Robusta is known to have a higher yield and be less susceptible than Arabica"),
('excelsa', "Resistant to many common diseases and pests. Unlike other types, it grows taller and resembles a tree more than a shrub"),
('liberica',"Has lower caffeine content than other types, but commands a higher price due to limited supply");

INSERT into Regions(region, altitude, soil_type, rainfall, temp, country_id)
VALUES ("Minas Gerais", 'low', 'red-yellow latosol', 'med', 'med', 1),
("Cerrado", 'med', 'red latosol', 'low', 'med', 1),
("Mogiana", 'med', 'red latosol', 'low', 'med', 1),
("Bahia", 'med', 'andosol', 'low', 'high', 1),
("Rondonia", 'low', 'red latosol', 'med', 'med',1),
("Da Lat", 'high', 'red latosol', 'med', 'low', 2),
("Dak Lak", 'low', 'red-yellow latosol', 'med', 'high', 2),
("Gia Lai", 'low', 'red-yellow latosol', 'med', 'high', 2),
("Dak Nong", 'low', 'andosol', 'med', 'high', 2),
("Lam Dong", 'low', 'andosol', 'low', 'high',  2),
("Narino", 'high', 'andosol', 'low', 'high', 3),
("Cauca", 'high', 'andosol', 'low', 'high', 3),
("Meta", 'high', 'andosol', 'med', 'low',  3),
("Huila", 'high', 'andosol', 'med', 'low', 3),
("Tolima", 'high', 'andosol', 'med', 'low',  3),
("Sumatra", 'low', 'andosol', 'high', 'high',  4),
("Java", 'low', 'andosol', 'med', 'med', 4),
("Sulawesi", 'med', 'red latosol', 'low', 'high', 4 ),
("Flores", 'low', 'red latosol', 'low', 'high', 4),
("Bali", 'low', 'red latosol', 'low', 'high', 4);

INSERT into Organizations(name, type)
VALUES("International Union for the Protection of New Varieties of Plants", "Rights Holder" ),
("Central Highlands Agroforestry", "Breeder"),
("Indonesian Coffee and Cocoa Research Institute", "Breeder"),
("Brazilian Coffee Institute", "Rights Holder");

INSERT into Varieties(plant_name, rust_resist, nematode_resist, optimal_altitude,optimal_rainfall, optimal_temp, organization_id, type_id)
VALUES ("bourbon-typica", 'low', 'low', 'low', 'med', 'med', NULL, 1),
("typica", 'low', 'low', 'high', 'med', 'low', NULL, 1),
("TR4", 'high', 'med', 'low', 'med', 'high', 2, 2),
("BP961", 'med', 'high', 'low', 'med', 'high', 3, 2),
("Conilon", 'med', 'med', 'med', 'low', 'high', 4, 1),
("johor", 'high', 'high', 'low', 'high', 'high', NULL ,4),
("luwak", 'med', 'high', 'med', 'low', 'med', 3,4),
("mooleh manay", 'med', 'med', 'low', 'med', 'high', 2,  3),
("suntikoopa", 'high', 'high' , 'low', 'low', 'high', 1, 3);

INSERT into Regions_Varieties(region_id, plant_id)
VALUES (1, 1), (5, 1), (17, 1), (6, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (8, 3), (9, 3), (8, 4), (9, 4),
(4, 5), (18, 5), (16, 6), (2, 7), (3, 7), (8, 8), (9, 8), (7, 9), (10, 9), (19, 9), (20, 9); 

SET FOREIGN_KEY_CHECKS=1;
COMMIT;