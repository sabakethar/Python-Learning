#! /usr/bin/python

class Communicate:

    def __init__(self):
        self.msg_list={}
        self.prompt_count=0

    def get_message(self, prompt):

        self.prompt_count+=1
        prompt=prompt+" "+str(self.prompt_count)+":"

        self.msg_list[prompt]=input(prompt)
   
        return self.msg_list[prompt]

    def put_message(self, msg):
        print("you entered:", self.msg_list[list(self.msg_list)[len(self.msg_list)-1]])
        return msg

def main():

    c=Communicate()

    from os import system
 
    while True:
        system("clear")

        print("prompt:", end=' ')
        if c.put_message(c.get_message(input())) == "xxx":
            break        

    system("clear")
    for key in sorted(c.msg_list.keys()):
        print(key, c.msg_list[key])

main()




