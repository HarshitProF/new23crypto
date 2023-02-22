class text_func:
    def __init__(self):
        pass
    def get_chats(self):
        chat_ids=[]
        with open("chats.text") as t:
            chats=t.readlines()
            for chat in chats:
                chat_ids.append(str(chat).strip())
        t.close()
        return chat_ids


    def insert(self,chat_id):
        if str(chat_id) in self.get_chats():
            return "alredy exists"
        if not chat_id in self.get_chats():
            with open('chats.text','a') as file:
                file.writelines(str(chat_id))
                file.writelines('\n')
                file.close()
            return "inserted"