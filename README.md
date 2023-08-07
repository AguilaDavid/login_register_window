# Login and Register Window

This repository contains test code for creating a login and registration window. This code also establishes communication with a database to store all the records and to be able to verify the access credentials of the clients.

For this project it is recommended to use ``pgAdmin4`` as database manager.

## Explication

First of all, a table called ``client`` was created to store the information about the client's login. These dice are used to validate the login.

![Captura de Ecrã (2393)](https://github.com/AguilaDavid/login_register_window/assets/125582704/3bfac159-8154-41cc-82be-d3d6a69bc790)

* This table contains a unique id for each client automatically generated using ``SERIAL``. This method is advantageous in an environment with recurrence because the database manager itself generates and processes the ID.

* The password is encrypted using a plsql extension called ``pgcrypto``

* The ``registration_dat`` is completed by a trigger during a table insert

In the python code, two windows are created, one with the longin and the other with the registration form. Whenever one window is open the other remains hidden.

### Login window
![Captura de Ecrã (2391)](https://github.com/AguilaDavid/login_register_window/assets/125582704/0b9fe80e-aee6-4c64-83ca-560dcd5bddec)

### Registration window
![Captura de Ecrã (2390)](https://github.com/AguilaDavid/login_register_window/assets/125582704/8c57c361-0e13-4886-8c8e-628447cb6784)

The table is protected. Ou seja, when a user registers but an error occurs, all the dice entered are ignored and the last safe commit is returned.

```python
# Transition: Either all data is sent correctly or none is sent
try:
    cur.execute("QUERY")
    conn.commit()
except Exception:
    conn.rollback()
```
