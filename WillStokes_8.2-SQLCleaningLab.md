```SQL
--Write a query to look at all the records in the Topspeed column.
SELECT TopSpeed
FROM EvCars
```
```SQL
--Choose the appropriate string function from the string function list. There may be more then one way to accomplish this task.
UPDATE EvCars
SET TopSpeed =RTRIM(TopSpeed,' km/h')
```
```SQL
--Use a select statement to visualize the original column, TopSpeed and the changes that are made by the string function side by side in the result set.
SELECT TopSpeed
FROM EvCars
```
```SQL
--Write the update statement to set TopSpeed to equal the return value of the string function you chose in 2.2
UPDATE EvCars
SET TopSpeed =RTRIM(TopSpeed,' km/h')
```
```SQL
--Write a select statement to look at the column again. (you can reuse the code you wrote above in 2.1)
SELECT TopSpeed
FROM EvCars
```
```SQL
--Write a select statement to multiply the speed by 0.621371. Return original Topspeed and calculated TopspeedMPH. Round the answer to 1 decimal place .
SELECT TopSpeed, ROUND(TopSpeed * 0.621371, 1) AS TopSpeedMPH
FROM EvCars
```
```SQL
--Turn this query into an UPDATE statement
UPDATE EvCars
SET TopSpeed = ROUND(TopSpeed * 0.621371, 1)
```
```SQL
--Rename the TopSpeed column to topSpeedMPH
ALTER TABLE EvCars
RENAME TopSpeed to TopSpeedMPH
```
```SQL
--Select All of the records to get a look at the whole table with your recent changes
SELECT*
FROM EvCars
```
```SQL
--Review the column that you are looking to change
SELECT Range
FROM EvCars
```
```SQL
--We would like to remove 'km' from each value in the column Range.
SELECT Range, rtrim(Range,' km') 
FROM EvCars
```
```SQL
--Use a select statement to visualize the original column, Range and the changes that are made by the string function side by side in the result set.
SELECT Range, rtrim(Range,' km') 
FROM EvCars
```
```SQL
--Write the update statement to set Range to equal the return value of the string function you chose in 3.2
UPDATE EvCars
SET Range =rtrim(Range,' km')
```
```SQL
--Write a select statement to look at the column again. (you can reuse the code you wrote above)
SELECT Range
FROM EvCars
```
```SQL
--Write a select statement to multiply the distance by 0.621371. Return original Range and calculated RangeMiles. Round the answer to 1 decimal place.
SELECT Range, ROUND(Range * 0.621371, 1) AS RangeMiles
FROM EvCars
```
```SQL
--Turn this query into an UPDATE statement.
UPDATE EvCars
SET Range = ROUND(Range * 0.621371, 1)
```
```SQL
--Rename the Range column to rangeMiles
ALTER TABLE EvCars
RENAME Range to RangeMiles
```
```SQL
--Select All of the records to get a look at the whole table with your recent changes
SELECT *
FROM EvCars
```
```SQL
--Write a select statement to review both of the columns that you are looking to change
SELECT Efficiency, FastCharge
FROM EvCars
```
```SQL
--Choose the appropriate string function from the string function list. There may be more then one way to accomplish this task.
SELECT Efficiency, rtrim(Efficiency,'Wh/km')
FROM EvCars
SELECT FastCharge, rtrim(FastCharge,'km/h')
FROM EvCars
```
```SQL
--Use a select statement to visualize the original column efficiency, the string function removing ' Wh/km', original column Fastcharge, and the string function removing ' km/h'
SELECT Efficiency, rtrim(Efficiency,'Wh/km')
FROM EvCars
SELECT FastCharge, rtrim(FastCharge,'km/h')
FROM EvCars
```
```SQL
--Write the update statement to set Efficiency/FastCharge to equal the return value of the string function you chose in 4.2
UPDATE EvCars
SET Efficiency =rtrim(Efficiency,' Wh/km')
UPDATE EvCars
SET FastCharge =rtrim(FastCharge,' km/h')
```
```SQL
--Write a select statement to look at all of the columns again. (you can reuse the code you wrote above in section4.3)
SELECT Efficiency, FastCharge
FROM EvCars
```
```SQL
--Write a select statement to multiply the distance by 0.621371. Return original FastCharge and calculated OneHourFastChargeMiles. Round the answer to 1 decimal place.
SELECT FastCharge, ROUND(FastCharge * 0.621371, 1) AS OneHourFastChargeMiles
FROM EvCars
```
```SQL
--Turn this query into an UPDATE statement.
UPDATE EvCars 
SET FastCharge = ROUND(FastCharge * 0.621371, 1) 
```
```SQL
--Rename the FastCharge column to OneHourFastChargeMiles
--Rename the efficiency column to efficiencyWHperKM
ALTER TABLE EvCars
RENAME Efficiency to EfficiencyWHperKM
ALTER TABLE EvCars
RENAME FastCharge to OneHourFastChargeMiles
```
```SQL
--Select All of the records to get a look at the whole table with your recent changes
SELECT *
FROM EvCars
```
```SQL
--Write a query that selects RapidCharge and counts all the records based on that attribute. (HINT: Remember GROUP BY from SQL Lesson 7.2)
SELECT RapidCharge, count(*)
FROM EvCars
GROUP by RapidCharge
```
### For the purpose of this exercise, if the car's RapidCharge value equals 'yes' then I want you to change the value to 'Yes'
### If the RapidCharge value equals 'no' then I want you to change the value to 'No'.
```SQL
--use this syntax reminder to help guide your update statement writing
UPDATE EvCars
SET RapidCharge = 'yes'
WHERE RapidCharge = 'Rapid charging possible'
UPDATE EvCars
SET RapidCharge = 'no'
WHERE RapidCharge = 'Rapid charging not possible'
```
```SQL
--Write a query that selects PowerTrain and counts all the records.
SELECT PowerTrain, count(*)
FROM EvCars
GROUP by PowerTrain
```
### look at the three DISTINCT values from the query you wrote in 6.1 and fill in the blanks.
### If the PowerTrain equals All Wheel Drive then I want you to change the value to 'AWD'
### If the PowerTrain equals Rear Wheel Drive then I want you to change the value to 'RWD'
### If the PowerTrain equals Front Wheel Drive then I want you to change the value to 'FWD'

```SQL
UPDATE EvCars
SET PowerTrain = 'AWD'
WHERE PowerTrain = 'All Wheel Drive'
UPDATE EvCars
SET PowerTrain = 'RWD'
WHERE PowerTrain = 'Rear Wheel Drive'
UPDATE EvCars
SET PowerTrain = 'FWD'
WHERE PowerTrain = 'Front Wheel Drive'
```
```SQL
SELECT *
FROM EvCars
```
```SQL
--Write a select statement to multiply the PriceEuro by 1.09 and Return PriceEuro and calculated column. Round the calculated column to 2 decimal places.
SELECT PriceEuro, ROUND(PriceEuro * 1.09, 2) 
FROM EvCars
```
```SQL
--Turn this query into an UPDATE statement. Remember to round the calculation to two decimal points.
UPDATE EvCars 
SET PriceEuro = ROUND(PriceEuro * 1.09, 2) 
```
```SQL
--Rename PriceEuro to PriceUSD
ALTER TABLE EvCars
RENAME PriceEuro to PriceUSD
```


