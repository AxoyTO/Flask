import json
import psycopg2
import random
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        return cur, conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def import_users(curr, conn):
    curr.execute('SELECT * FROM users')
    db = curr.fetchone()
    print(db)
    with open('../users.json') as users_json:
        data = json.load(users_json)

        for i, row in enumerate(data, start=1):
            username = row['username']
            password = row['password']
            email = row['email']
            expert = row['expert']
            admin = row['admin']
            curr.execute('INSERT INTO users (id,username, password, email, expert, admin) VALUES (%s, %s, %s, %s, %s, %s);',
                         (i, username, password, email, expert, admin,))

            conn.commit()


def import_questions(curr, conn):
    with open("../questions.json") as questions_json:
        data = json.load(questions_json)

        curr.execute('SELECT * FROM users')
        all_users_ids = [i[0] for i in curr.fetchall()]
        curr.execute('SELECT * from users WHERE expert=True')
        expert_ids = [i[0] for i in curr.fetchall()]

        for i, row in enumerate(data, start=1):
            id = i
            question = row['question_text']
            answer = row['answer_text']

            real_asker_id = row['asked_by_id']
            asked_by_id = real_asker_id if real_asker_id in all_users_ids else random.choice(
                all_users_ids)

            real_expert_id = row['expert_id']
            expert_id = real_expert_id if real_expert_id in expert_ids else random.choice(
                expert_ids)

            time = row['time']

            curr.execute('INSERT INTO questions (id, question_text, answer_text, asked_by_id, expert_id, time) VALUES (%s, %s, %s, %s, %s, %s);',
                         (id, question, answer, asked_by_id, expert_id, time,))

            conn.commit()


if __name__ == '__main__':
    try:
        curr, conn = connect()
        #import_users(curr, conn)
        #import_questions(curr, conn)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if curr is not None:
            curr.close()
        if conn is not None:
            conn.close()
            print('Database connection closed.')
