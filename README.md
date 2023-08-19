# Login and Register Window

This repository contains test code for creating a login and registration window. This code also establishes communication with a database to store all the records and to be able to verify the access credentials of the clients.

For this project it is recommended to use ``pgAdmin4`` as database manager.

## Explanation

First of all, a table called ``client`` was created to store the information about the client's login. These dice are used to validate the login.

![Captura de Ecrã (2393)](https://github.com/AguilaDavid/login_register_window/assets/125582704/2fea8502-a099-4659-b4cb-12610817655f)

* This table contains a unique id for each client automatically generated using ``SERIAL``. This method is advantageous in an environment with recurrence because the database manager itself generates and processes the ID.

* The password is encrypted using a plsql extension called ``pgcrypto``

* The ``registration_dat`` is completed by a trigger during a table insert

In the python code, two windows are created, one with the login and the other with the registration form. Whenever one window is open the other remains hidden.

### Login window
![Captura de Ecrã (2391)](https://github.com/AguilaDavid/login_register_window/assets/125582704/2c67048a-936f-4f80-b0c5-b8d0e2a72e82)

### Registration window
![Captura de Ecrã (2390)](https://github.com/AguilaDavid/login_register_window/assets/125582704/880cf9df-8de3-48e4-81b1-f77c60f7f006)

The table is protected i.e. when a user registers but an error occurs, all the dice entered is ignored and the last safe commit is returned.

```python
# Transition: Either all data is sent correctly or none is sent
try:
    cur.execute("QUERY")
    conn.commit()
except Exception:
    conn.rollback()
```
