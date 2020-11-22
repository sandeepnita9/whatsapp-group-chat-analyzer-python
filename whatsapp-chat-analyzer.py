import pandas as pd
import numpy as np
import re
import dateparser
from collections import Counter
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def read_chat_file(chatFile):
    #Function that will read Whatsapp chat file and do chat data manipulation
    filex = open(chatFile,'r', encoding = 'utf-8')
    chatContent = filex.read().splitlines()
    #chatContent = filey.splitlines() #The splitline method converts the chunk of string into a list of strings
    return chatContent

def Merge_multiple_chat_lines(whatsappChatFile):
    #Merge messages that belongs are part of continuation messages from same sender
    msgs = [] #message container
    pos = 0 #counter for position of msgs in the container

    for line in WhatsappChat:
        if re.findall("\A\d+[/]", line):
            msgs.append(line)
            pos += 1
        else:
            take = msgs[pos-1] + ". " + line
            msgs.append(take)
            msgs.pop(pos-1)
    return msgs

def Create_Columns_with_Data_for_Dataframe(CleanedChatData):
#make arrays of different parts of the messages
    Date = []
    Time = []
    Number_Author = []
    msg = []
    counter = 0
    for temp in CleanedChatData:
    
        #enable below lines if your chat date format is like 1/07/2020 and NOT like 01/07/2020 we are adding padding of 0 in this case
        '''paddingZero = temp.find("/")
        if paddingZero == 1:
            temp = '0'+temp'''
            
        #enable below lines if your chat date format is like 01/07/20 and NOT like 01/07/2020 we are making YY to YYYY
        '''temp = temp.replace('/20,', '/2020,',1)'''
        
        # Below code works fine for sample chat string as 01/07/2020, 22:04 - User Name: Chat Message
        mydate = temp[0:10]
        Date.append(mydate)
            
        mytime = temp[12:17]
        Time.append(mytime)
            
        hyphenposition = temp.find(': ')
        myname = temp[20:hyphenposition]
        Number_Author.append(myname)
            
        myMessage = temp[hyphenposition:]
        msg.append(myMessage)
            
    #print(len(Date), len(Time), len(Number_Author), len(msg))
            
    #Create DataFrame
    ChatData_df = pd.DataFrame()
    ChatData_df["Date"] = Date
    ChatData_df["Time"] = Time
    ChatData_df["Number_Author"] = Number_Author
    ChatData_df["msg"] = msg
        
    Generate_Most_Active_User_Graph(ChatData_df)


def Generate_Most_Active_User_Graph(ChatData_DataFrame):
    top10ActiveMember = ChatData_DataFrame.Number_Author.value_counts(ascending=False).head(8)
    print(top10ActiveMember)
    ax = top10ActiveMember.plot.barh(color='Darkblue')
    ax.set_xlabel ('Number of sent message')
    ax.set_ylabel("Users")
    ax.set_title("Most Active Users of Group - Based on No. of messages sent")

'''def Generate_Most_Engagement_Time(ChatData_DataFrame):
toptimeengaged = ChatData_DataFrame.Time.value_counts(ascending=False).head(4)
ax = toptimeengaged.plot(kind="bar", color='Darkblue')
ax.set_xlabel ('Time')
ax.set_ylabel ('Frequency')
ax.set_title("Top 10 Time of Engagement")''' 

if __name__ == "__main__": 
    
    # calling function that will read chat data and do first level of line spliting
    WhatsappChat = read_chat_file('D:\py-scripts\whatsapp-chat-analyzer\Chat.txt')
    
    #Below line will help you to know if your chat data have user joined notification messages. You can remove these lines.
    joined_Line_Messgae = [joinedLineMessgae for joinedLineMessgae in WhatsappChat if  "joined using this" in joinedLineMessgae]
    
    #Below line will help you to know if your chat data have user left group notification messages. You can remove these lines.
    Group_Left_Line_Messgae = [GroupLeftLineMessgae for GroupLeftLineMessgae in WhatsappChat if GroupLeftLineMessgae.endswith("left,")]
    
    #Merge messages that belongs to same sender and in continuation
    CleanedChatData = Merge_multiple_chat_lines(WhatsappChat)

    Create_Columns_with_Data_for_Dataframe(CleanedChatData)
