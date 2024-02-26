```SQL
--Using EVregistry, Write a query to select the ModelYear, Make, and Model off all of the vehicles in the registry.
SELECT ModelYear, Make, Model
FROM evRegistry
```
```SQL
--Using the EVRegistry table, Write a query that lists all of the unique types of EV's. your reult set should have one column, ElectricVehicleType.
SELECT DISTINCT ElectricVehicleType
FROM evRegistry
```
```SQL
--Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry.
SELECT *
FROM EVRegistry
WHERE ElectricVehicleType = 'Battery Electric Vehicle (BEV)'
```
```SQL
--Using the EVRegistry, wirte a query that returns the Make and Model of all of the EV's that have a BaseMSRP between 20000 and 35000?
SELECT Make, Model 
FROM EVRegistry
WHERE BaseMSRP >= 20000 AND BaseMSRP <= 35000
```
```SQL
--Using EVRegistry, write a query to find a record where the City attribute is NULL. Return all of the available columns.
SELECT *
FROM EVRegistry
WHERE City = NULL
```
```SQL
--Write a query to find the make, model, and ElectricVehicleType where the VIN number has that ends in '3E1EA1J'.
SELECT Make, Model, ElectricVehicleType
FROM EVRegistry
WHERE VIN LIKE '%3E1EA1J'
```
```SQL
--Select the ModelYear, make, model, ElectricVehicleType, and range of the Tesla vehicles or cheverolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest.
SELECT ModelYear, Make, Model, ElectricVehicleType, ElectricRange
FROM EVRegistry 
WHERE Make IN ('TESLA', 'CHEVROLET') 
ORDER BY Make, ModelYear DESC
```
```SQL
--Using EVCharging, Write a query to find out how many many times those stations were used. Order them by the most used to the least used and limit the output to 5 records.
SELECT StationID, Count(*) as numUses
FROM evCharge
GROUP BY StationID 
ORDER BY COUNT(*) DESC
LIMIT 5
```
```SQL
--Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be userid, minTime, and maxTime. Order this result set by the last two columns respectively.
SELECT userId, MIN(chargeTimeHrs) as 'minhours', MAX(chargeTimeHrs) as 'maxHours'
FROM evCharge
WHERE chargeTimeHrs > 0.5
GROUP BY userId
ORDER BY 2,3
```
```SQL
--Using EVCharging, Which day of the week has the highest average charging time? Round the answer to 2 decimal points.
SELECT ROUND(AVG(chargeTimeHrs),2), weekday
FROM EVCharging
```
```SQL
--Using, EV charging, Find the total power consumed from charging EV's by each User. Return the userId and name the calculated column, totalPower. Round the answer to 2 deciaml points and list the out put in highest to lowest order. Limit the order to the top 15 users.
SELECT UserId, ROUND(SUM(kwhTotal),2) as 'totalPower'
FROM EVcharging
GROUP BY UserID
ORDER BY totalPower DESC
LIMIT 15
```
```SQL
--Using dimfacility and factCharge, write a query to find out which type of facility (GROUP BY) has the most amount of charging stations. Return type Facility and name the calculated column numStation. Order the result set from highest to lowest number of charging stations.
SELECT d.typeFacility, COUNT(f.facilityID) AS numStations
FROM dimFacility AS d
JOIN factCharge AS f ON f.facilityID = d.typeFacility
GROUP BY d.typeFacility
ORDER BY numStations DESC
```
<!---
In your own words, Briefly explain Primary Keys and Foreign Keys.
--->
### A primary key is a identifier for values in a database table. The foreign key is reference from one table to the primary values of another table. Primary and foreign keys can establish a relationship between database tables through connected values. 
```SQL
--Using EV Charging, For the folks who charged longer than one hour, show the min and max of the charging time for each user. Your output columns should be userid, minTime, and maxTime. Order this result set by the last two columns respectively. HINT: USE HAVING
SELECT UserID, MIN(chargeTimeHrs) AS minTime, MAX(chargeTimeHrs) AS maxTime
FROM EVCharging
GROUP BY UserID  
HAVING MAX(chargeTimeHrs) > 1
ORDER BY 2,3 
```