--  SQL script that creates a stored procedure  ComputeAverageWeightedScoreForUser that computes and store the average score for a student. 
-- Note: An average score can be a decimal


DELIMITER $$ ;

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN

DECLARE average FLOAT;

SELECT SUM(score * (SELECT weight FROM projects WHERE projects.id = project_id)) / SUM(1 * (SELECT weight FROM projects WHERE projects.id = project_id)) INTO average FROM corrections WHERE corrections.user_id = 2;
UPDATE users SET average_score = average WHERE users.id = user_id;

END $$

DELIMITER ; $$