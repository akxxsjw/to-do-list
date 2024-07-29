
# conn = psycopg2.connect("dbname=to_do_list user=postgres password = 20072604sh host=localhost port=5432")
# cur = conn.cursor()
# cur.execute
# name = input()
# email = input()
# password = input() # ; drop table users;
# 'select * from users where  name = name and password = pasword'
# cur.execute(f"insert into users (username, email, dane_task, falled_task) values (%s, %s, 0, 0)", (name,email))
# conn.commit()
# conn.close()

# conn = psycopg2.connect("dbname=to_do_list user=postgres password = 20072604sh host=localhost port=5432")
# cur = conn.cursor()
# cur.execute('Select * from users')
# records = cur.fetchall()
# for i in records:
#     print(i)
# name = input()
# email = input()
# password = input() # ; drop table users;
# 'select * from users where  name = name and password = pasword'
# cur.execute(f"insert into users (username, email, dane_task, falled_task) values (%s, %s, 0, 0)", (name,email))
# conn.commit()
# conn.close()
# from utils import register, login
# conn = psycopg2.connect("dbname=to_do_list user=postgres password = 20072604sh host=localhost port=5432")
# cur = conn.cursor()
# cur.execute('Select * from users')
# records = cur.fetchall()
# for i in records:
#     print(i)
# name = input()
# email = input()
# password = input() # ; drop table users;
# 'select * from users where  name = name and password = pasword'
# cur.execute(f"insert into users (username, email, dane_task, falled_task) values (%s, %s, 0, 0)", (name,email))
# conn.commit()
# conn.close()
import psycopg2
from utils import register, login
# conn = psycopg2.connect("dbname=to_do_list user=postgres password = 20072604sh host=localhost port=5432")
# cur = conn.cursor()
# cur.execute('Select * from users')
# records = cur.fetchall()
# for i in records:
#     print(i)
# name = input()
# email = input()
# password = input() # ; drop table users;
# 'select * from users where  name = name and password = pasword'
# cur.execute(f"insert into users (username, email, dane_task, falled_task) values (%s, %s, 0, 0)", (name,email))
# conn.commit()
# conn.close()
from utils import register, login, add_tasks,delete_tasks,done_tasks
class App():
    
    def __init__(self) -> None:
        self.run_app = True
        self.is_auth = False
    
    def run(self):
        while self.run_app:
            if self.is_auth:
                print('Add tasks - 1, Delete tasks - 2, Done tasks - 3')
                com = input('Input command - ')
                if com == '1':
                    add_tasks(self.user)
                elif com == '2':
                    delete_tasks(self.user)
                    print('You deleted tasks')
                elif com == '3':
                    done_tasks(self.user)
                    print('You done tasks')
                    
                    
            else:
                print('Register - 1, Login - 2, Exit - 3')
                com = input('Input command - ')
                if com == '1':
                    register()
                    print('Вы зарегистрированы')
                elif com == '2':
                    self.user = login()
                    self.is_auth = True
                elif com == '3':
                    self.run_app = False



if __name__ == '__main__':
    app = App()
    app.run()
