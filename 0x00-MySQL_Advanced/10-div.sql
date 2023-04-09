-- a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0
-- if the second number is equal to 0.

DELIMITER $$ ;

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
DECLARE float_div FLOAT;
IF b = 0
THEN
SET float_div = 0;
ELSE
SET float_div = a / b;
END IF;
RETURN float_div;
END $$
DELIMITER ; $$