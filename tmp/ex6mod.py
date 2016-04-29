
class Communicate:

    def __init__(self):
        self.msg_list=None
        self.prompt_count=0

    def get_message(self, prompt):

        self.prompt_count+=1
        prompt=prompt+" "+str(self.prompt_count)+":"

        self.msg_list[prompt]=input(prompt)
   
        return self.msg_list[prompt]

    def put_message(self, msg):
        print("you entered:", self.msg_list[list(self.msg_list)[len(self.msg_list)-1]])
        return msg


