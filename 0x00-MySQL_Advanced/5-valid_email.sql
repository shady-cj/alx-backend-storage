-- a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed

DELIMITER $$ ;
CREATE TRIGGER validate_email BEFORE UPDATE ON users FOR EACH ROW
BEGIN
IF NEW.email NOT LIKE '%_@__%.__%' AND PATINDEX('%[^a-z,0-9,@,.,_,\-]%', NEW.email) <> 0
THEN
SET NEW.valid_email = 0;
ELSE
SET NEW.valid_email = 1;
END IF;
END $$
DELIMITER ; $$