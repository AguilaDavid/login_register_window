__version__ = 1

import psycopg2
import PySimpleGUI as sg
import sys

layout_login = [
    [sg.Text('User')],
    [sg.Input(key='user')],
    [sg.Text('Password')],
    [sg.Input(key='password')],
    [sg.Button('login'),sg.Button('registration')],
    [sg.Text(key='message')],
]

''' window = Login window
_______________________________
|User			       |
|[			      ]|
|Password		       |
|[			      ]|
|[Login] [registration]	       |
|______________________________|

'''

layout_registration = [
    [sg.Text('Name')],
    [sg.Input(key='name')],
    [sg.Text('Password')],
    [sg.Input(key='password')],
    [sg.Text('Email')],
    [sg.Input(key='email')],
    [sg.Button('send')],
]

''' windowR = Registration window
_______________________________
|Name			       |
|[			      ]|
|Password		       |
|[			      ]|
|Email			       |
|[			      ]|
|[send]			       |
|______________________________|

'''

window = sg.Window('Login',layout=layout_login)
windowR = sg.Window('Login',layout=layout_registration)

def exitHandler():
    '''
        #### Purpose: 
        Free the resources that the program took during the execution\n
        #### Param: 
        None\n
        #### Return: 
        None\n
    '''
    window.close() # destroy the login window
    windowR.close() # destroy the registration window
    cur.close() # close cursor
    conn.close() # close connection
    sys.exit("Interrupted Program")

if __name__ == "__main__":

    conn = psycopg2.connect("host=localhost dbname=[YOUR DATA BASE'S NAME] user=postgres password=[YOUR DATA BASE'S PASSWORD]") # connect
    cur = conn.cursor() # cursor start

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            exitHandler()
            break
        
        elif event == 'login':
            
            cur.execute("SELECT id, nome FROM client WHERE email = %s AND password = crypt(%s, password);",(values['user'],values['password'],))
            line, = cur.fetchall()
            
            if line is not None:
                window['message'].update('Login successful. User. {0}'.format(line[1]))
            else:
                window['message'].update('Login unsuccessful')

        elif event == 'registration':
            
            window.hide() # hide login window
            
            while True:

                event, values = windowR.read()

                if event == sg.WIN_CLOSED:
                    exitHandler()
                    break

                elif event == 'send':
                    
                    # Transition: Either all data is sent correctly or none is sent
                    try:
                        cur.execute("INSERT INTO client (nome, email, password) VALUES (%s, %s, crypt(%s, 'bf$$a_x@@Q«1^2»'));",(values['name'],values['email'],values['password'],))
                        conn.commit()
                    except Exception:
                        conn.rollback()
                    
                    windowR.hide() # hide the registration window
                    window.un_hide() # make the login window visible again
                    break

    exitHandler()