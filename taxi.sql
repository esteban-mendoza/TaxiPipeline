CREATE DATABASE taxi;

CREATE TABLE trips (
    vendorid VARCHAR(1),
    tpep_pickup_datetime DATETIME,
    tpep_dropoff_datetime DATETIME,
    passenger_count SMALLINT,
    trip_distance DECIMAL(5,2),
    pulocationid INTEGER,
    dolocationid INTEGER,
    ratecodeid SMALLINT,
    store_and_fwd_flag VARCHAR(1),
    payment_type SMALLINT,
    fare_amount DECIMAL(5,2),
    extra DECIMAL(5,2),
    mta_tax DECIMAL(5,2),
    improvement_surcharge DECIMAL(5,2),
    tip_amount DECIMAL(5,2),
    tolls_amount DECIMAL(5,2),
    total_amount DECIMAL(5,2)
);

## Queries

# Count trips per hour
SELECT HOUR(tpep_pickup_datetime), COUNT(*) 
FROM trips
GROUP BY HOUR(tpep_pickup_datetime);

# Mean revenue per hour
SELECT HOUR(tpep_pickup_datetime) as hour, AVG(total_amount - tolls_amount) AS revenue_avg
FROM trips
WHERE total_amount >= 0
GROUP BY hour;

# Variance of revenue per hour
SELECT HOUR(tpep_pickup_datetime) as hour, Variance(total_amount - tolls_amount) AS revenue_var
FROM trips
WHERE total_amount >= 0
GROUP BY hour;

