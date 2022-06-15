-- Coffee Farmer's Almanac
-- Joshua Harris
-- Database Manipulation queries for the Coffee Farmer's Almanac Web Application

-- Varieties Table
    -- Display genetic varieties of coffee plants (and get information for dropdowns)
SELECT plant_id, plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, Organizations.name, Types.name FROM Varieties 
LEFT JOIN Organizations ON Varieties.organization_id = Organizations.organization_id 
INNER JOIN Types ON Varieties.type_id = Types.type_id
ORDER BY plant_id
    -- Get information for dropdowns
    -- Organization info
SELECT organization_id, name FROM Organizations
    -- Types info
SELECT type_id, name FROM Types

    -- Add genetic varieties of coffee plants
    -- No organization has rights to genetic variety 
INSERT INTO Varieties (plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, type_id) 
VALUES (:name, :rust, :nematode, :opt_alt, :opt_rain, :opt_temp, :type_id)
    -- Has organization info
INSERT INTO Varieties (plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, organization_id, type_id) 
VALUES (:name, :rust, :nematode, :opt_alt, :opt_rain, :opt_temp, :org_id, :type_id)

    -- Update the data for a genetic variety of coffee (allow 1:M relationship with Organizations to be NULLable)
    -- Retrieve info for one variety
SELECT plant_id, plant_name, rust_resist, nematode_resist, optimal_altitude, optimal_rainfall, optimal_temp, Organizations.name, Types.name FROM Varieties 
LEFT JOIN Organizations ON Varieties.organization_id = Organizations.organization_id 
INNER JOIN Types ON Varieties.type_id = Types.type_id 
WHERE plant_id = :plant_id
    -- Update data
    -- No organization
UPDATE Varietes
SET Varieties.plant_name = :name, Varieties.rust_resist = :rust, Varieties.nematode_resist = :nematode, Varieties.optimal_altitude = :opt_alt, Varieties.optimal_rainfall = :opt_rain, Varieties.optimal_temp = :opt_temp, Varieties.organization_id = NULL, Varieties.type_id = :type_id  
WHERE Varieties.plant_id = :plant_id 
    -- With organization
UPDATE Varietes
SET Varieties.plant_name = :name, Varieties.rust_resist = :rust, Varieties.nematode_resist = :nematode, Varieties.optimal_altitude = :opt_alt, Varieties.optimal_rainfall = :opt_rain, Varieties.optimal_temp = :opt_temp, Varieties.organization_id = :org_id, Varieties.type_id = :type_id  
WHERE Varieties.plant_id = :plant_id 

    -- Delete a variety
DELETE FROM Varieties WHERE plant_id = :plant_id

-- Regions Table
    -- Display coffee growing regions (and get information for dropdowns)
SELECT region_id, region, altitude, soil_type, rainfall, temp, Countries.country FROM Regions INNER JOIN Countries ON Regions.country_id = Countries.country_id ORDER BY region_id
    -- Add a coffee growing region
INSERT INTO Regions (region, altitude, soil_type, rainfall, temp, country_id) VALUES (:name, :altitude, :soil, :rain, :temp, :country_id)
    -- Get information for dropdowns
    -- Countries info
SELECT country_id, country FROM Countries

    -- Delete a Region
DELETE FROM Regions WHERE region_id = :region_id

-- Regions & Varieties Table
    -- Display Regions & Varieties Intersection Table (suitable varieties of coffee by region)
SELECT region_plant_id, Varieties.plant_name, Varieties.rust_resist, Varieties.nematode_resist, Regions.altitude, Regions.rainfall, Regions.temp, Regions.region FROM Regions_Varieties
INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id
INNER JOIN Varieties ON Varieties.plant_id = Regions_Varieties.plant_id
ORDER BY region_plant_id ASC
    -- get information for dropdowns
SELECT DISTINCT Regions.region_id, Regions.region FROM Regions_Varieties INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id ORDER BY Regions_Varieties.region_id

    -- Search for suitable varieties of coffee by region
SELECT region_plant_id, Varieties.plant_name, Varieties.rust_resist, Varieties.nematode_resist, Regions.altitude, Regions.rainfall, Regions.temp, Regions.region FROM Regions_Varieties
INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id
INNER JOIN Varieties ON Varieties.plant_id = Regions_Varieties.plant_id
WHERE Regions.region_id = :region_id

    -- Add a suitable variety of coffee for a region
INSERT INTO Regions_Varieties (region_id, plant_id) VALUES (:region_id, :plant_id)
        -- get information for dropdowns
        -- Regions
SELECT region_id, region FROM Regions
        -- Varieties
SELECT plant_id, plant_name FROM Varieties       

    -- Update a suitable variety of coffee for a region (M-to-M relationship update)
    -- Retrieve info for update
SELECT Regions_Varieties.region_plant_id, Varieties.plant_id, Varieties.plant_name, Regions.region_id, Regions.region FROM Regions_Varieties
INNER JOIN Regions ON Regions.region_id = Regions_Varieties.region_id
INNER JOIN Varieties ON Varieties.plant_id = Regions_Varieties.plant_id 
WHERE region_plant_id = :region_plant_id
    -- Update
UPDATE Regions_Varieties SET Regions_Varieties.region_id = :region_id, Regions_Varieties.plant_id = :plant_id WHERE Regions_Varieties.region_plant_id = :region_plant_id
    -- Remove a suitable variety of coffee for a region (M-to-M relationship deletion)
DELETE FROM Regions_Varieties WHERE region_plant_id = :region_plant_id

-- Types Table
    -- Display main types of coffee plants
SELECT * FROM Types
    -- Add a type of coffee plant
INSERT INTO Types (`name`, `description`) VALUES (:name, :desc)

-- Countries Table
    -- Display countries
SELECT * FROM Countries
    -- Add a country
INSERT INTO Countries (country, export_quantity, export_usd, cultivated_area) VALUES (:country, :exportqty, :exportusd, :area)

-- Organizations Table
    -- Display organizations (and get information for dropdowns)
SELECT * FROM Organizations
    -- Add an organization
INSERT INTO Organizations (`name`, `type`) VALUES (:name, :type)
