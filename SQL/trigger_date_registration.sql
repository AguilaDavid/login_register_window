--Store at registration date

CREATE OR REPLACE FUNCTION date_registration()
RETURNS TRIGGER AS 
$$
BEGIN
	NEW.registration_date = CURRENT_DATE;
	RETURN NEW;
END;
$$ language 'plpgsql';