-- Always before an insert look for the data

CREATE TRIGGER t_date_registration
    BEFORE INSERT ON client
    FOR EACH ROW
    EXECUTE FUNCTION date_registration();