import mysql.connector
class db:
    def __init__(self):
        self.conn=mysql.connector.connect(host="us-cdbr-east-06.cleardb.net",user="be0d3365f89adf",password='8305a028',database="heroku_21e7d5b75b2b2ec")
        self.cursor=self.conn.cursor()
        print(self.conn)
        #cursor.execute('drop table chats')
        #cursor.execute("create table if NOT EXISTS chats ( chat_id int UNIQUE)")
    def insert(self,chats_id):
        cursor=self.conn.cursor()
        query="insert into chats (chat_id ) VALUES (%s);"
        print(chats_id)
        val=(chats_id,)
        try:
            self.cursor.execute(query,val)
        except Exception as e:
            print(e)
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
        self.conn.close()
    def get_chats(self):
        cursor=self.conn.cursor()
        query="select chat_id from chats;"
        cursor.execute(query)
        chat_ids=cursor.fetchall()
        print(chat_ids)
        self.conn.close()
        return chat_ids
