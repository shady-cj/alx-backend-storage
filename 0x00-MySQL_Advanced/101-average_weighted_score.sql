--  SQL script that creates a stored procedure  ComputeAverageWeightedScoreForUsers that computes and store the average score for a student. 
-- Note: An average score can be a decimal


DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

DECLARE average FLOAT;
DECLARE user_id, b INT;
DECLARE users_cursor CURSOR FOR SELECT id FROM users;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET b = 1;
OPEN users_cursor;
REPEAT
FETCH users_cursor INTO user_id;
SELECT SUM(score * (SELECT weight FROM projects WHERE projects.id = project_id)) / SUM(1 * (SELECT weight FROM projects WHERE projects.id = project_id)) INTO average FROM corrections WHERE corrections.user_id = user_id;
UPDATE users SET average_score = average WHERE users.id = user_id;
UNTIL b = 1
END REPEAT;
CLOSE users_cursor;
END $$

DELIMITER ; $$