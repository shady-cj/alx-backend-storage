--  a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.

DELIMITER $$ ;
CREATE TRIGGER decrement_item AFTER INSERT ON orders FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - 1 WHERE name = NEW.item_name;
END$$
DELIMITER ; $$