-- Common Table Expressions (CTEs)

-- CTE for airports in Fiftyville
WITH FiftyvilleAirports AS (
  SELECT id
    FROM airports
   WHERE city = 'Fiftyville'
)

-- CTE for common conditions for ATM transactions
, CommonATMConditions AS (
  SELECT year, month, day, atm_location, transaction_type
    FROM atm_transactions
   WHERE year = 2023
     AND month = 7
     AND day = 28
     AND atm_location = 'Leggett Street'
     AND transaction_type = 'withdraw'
)

-- Main Query

-- Crime scene reports
SELECT description
  FROM crime_scene_reports
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND street = 'Humphrey Street';

-- Interviews on a specific day
SELECT name, transcript
  FROM interviews
 WHERE year = 2023
   AND month = 7
   AND day = 28;

-- Interviews with transcript containing 'bakery'
SELECT name, transcript
  FROM interviews
 WHERE year = 2023
   AND month = 7
   AND day = 28
   AND transcript LIKE '%bakery%'
 ORDER BY name;

-- ATM transactions with common conditions
SELECT account_number, amount
  FROM CommonATMConditions;

-- People with ATM transactions (withdraw) and common conditions
SELECT name, atm_transactions.amount
  FROM people
  JOIN bank_accounts ON people.id = bank_accounts.person_id
  JOIN CommonATMConditions ON bank_accounts.account_number = CommonATMConditions.account_number;

-- Airports in Fiftyville
SELECT abbreviation, full_name, city
  FROM airports
 WHERE id IN (SELECT id FROM FiftyvilleAirports);

-- Flights from airports in Fiftyville on a specific day
SELECT flights.id, full_name, city, flights.hour, flights.minute
  FROM airports
  JOIN flights ON airports.id = flights.destination_airport_id
 WHERE flights.origin_airport_id IN (SELECT id FROM FiftyvilleAirports)
   AND flights.year = 2023
   AND flights.month = 7
   AND flights.day = 29
 ORDER BY flights.hour, flights.minute;

-- People on a specific flight at a specific time
SELECT passengers.flight_id, name, passengers.passport_number, passengers.seat
  FROM people
  JOIN passengers ON people.passport_number = passengers.passport_number
  JOIN flights ON passengers.flight_id = flights.id
 WHERE flights.year = 2023
   AND flights.month = 7
   AND flights.day = 29
   AND flights.hour = 8
   AND flights.minute = 20
 ORDER BY passengers.passport_number;

-- People involved in phone calls with a duration less than or equal to 60
WITH PhoneCallPeople AS (
  SELECT people.name, phone_calls.duration
    FROM people
    JOIN phone_calls ON people.phone_number = phone_calls.caller
   WHERE phone_calls.year = 2023
     AND phone_calls.month = 7
     AND phone_calls.day = 28
     AND phone_calls.duration <= 60
  UNION
  SELECT people.name, phone_calls.duration
    FROM people
    JOIN phone_calls ON people.phone_number = phone_calls.receiver
   WHERE phone_calls.year = 2023
     AND phone_calls.month = 7
     AND phone_calls.day = 28
     AND phone_calls.duration <= 60
)
SELECT * FROM PhoneCallPeople
ORDER BY duration;

-- People involved in bakery security logs with specific conditions
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
  FROM people
  JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
 WHERE bakery_security_logs.year = 2023
   AND bakery_security_logs.month = 7
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.activity = 'exit'
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute >= 15
   AND bakery_security_logs.minute <= 25
 ORDER BY bakery_security_logs.minute;
