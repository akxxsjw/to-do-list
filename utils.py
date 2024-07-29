import psycopg2
from models import User

def con_db(fun):
    def wrap(*args, **kwargs):
        with psycopg2.connect("dbname=to_do_list user=postgres password = 20072604sh host=localhost port=5432") as conn:
            cur = conn.cursor()
            answer = fun(cur, *args, **kwargs)
            conn.commit()
        return answer
    return wrap

@con_db
def register(cur):
    username = input('Username - ')
    email = input('Email - ')
    password = input('Password - ')
    password2 = input('Password2 - ')
    if password == password2:
        cur.execute('insert into users (username, email, password) values (%s,%s,%s)', (username, email, password))
    else:
        print('Passwords are not same')
        
@con_db
def login(cur):
    username = input('Username - ')
    password = input('Password - ')
    cur.execute('select * from users where username = %s and password = %s', (username,password))
    user = cur.fetchone()
    user = User(*user)
    return user


@con_db
def add_tasks(cur, user):
    title = input('Title - ')
    description = input('Description - ')
    date = input('Date - ')
    cur.execute('insert into tasks (title, description, date_at, user_id) values (%s, %s, %s, %s)', (title, description,date, user.id))

    
def delete_tasks(cur, user):
    task_id = input('Введите идентификатор задачи: ')
    cur.execute('SELECT user_id FROM tasks WHERE id = %s', (task_id,))
    task_owner_id = cur.fetchone()
    if task_owner_id and task_owner_id[0] == user.id:
        cur.execute('DELETE FROM tasks WHERE id = %s AND user_id = %s', (task_id, user.id))
        cur.execute('UPDATE users SET falled_task = falled_task + 1 WHERE id = %s', (user.id,))
        print('Операция успешно выполнена.')
    else:
        print('Эта задача не принадлежит вам.')

@con_db
def done_tasks(cur, user):
    task_id = input('Введите идентификатор задачи: ')
    cur.execute('DELETE FROM tasks WHERE id = %s AND user_id = %s', (task_id, user.id))
    cur.execute('UPDATE users SET dane_task = dane_task + 1 WHERE id = %s', (user.id,))
    print('Задача успешно завершена.')
    