import nltk
from nltk.chat.util import Chat, reflections
print(Chat)


self_pairs=[
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is (.*) name ?",
        ["My name is Inovatee and I'm a chatbot ",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*) created ?",
        ["Harsha created me using Python Library's",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, Telangana',]
    ],
    [
        r"name (.*) team members",
        ["shanmuka he is the leader,nivas the one who execute's the code and visvulize the data,Harsha the one who make users to see the output"]
    ],
    [
        r"(.*) you know| heard| about current situation?",
        ["yes corona in all over the world and now showings its power to india"]
    ],
    [
               r"do you have (.*) updates on current pandamic on (.*) decisions that have taken by the government",
               [
                   "%1 yeh the team who created me had made a small research on how,what and why the demanded situation have "
                   "taken the government to take the correct decisions about what should be taken care and what not"]
    ],
    [
        r"show me some (.*) words",
        ["ok!! there are 34334 %1 words.top %1 words are:  technical,draw,cp delhi..."]
    ],

    [
        r"iam a (.*) in (.*)",
        ["%2 is an awsome university, I have heard about it."]
    ],

    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy iam not effected with corona don't worry :)"]
    ],
    [
        r"what about some positive words",
        ["ok!! there are 88 positive words.top positive words are: great,love,best..."]
    ],
    [
        r"what about some negitive words",
        ["yeh sure!! there are 48 negitive words.top negitive words are:dead,killer,shithead"]
    ],

    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you.Stay home stay safe"]
],
]
def chatbot():
    print("Hi, I'm Inovatee")
chatbot()

chat=Chat(self_pairs, reflections)
chat.converse()



