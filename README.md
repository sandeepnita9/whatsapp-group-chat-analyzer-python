I am new to Python and Data exploration world. At the time of writing this program, I was exploring and implementing small code snippets. As part of fun activity, I though to implement WhatsApp Group Chat Analyzer which can generate some interesting graph.
How I have done this?
Export WhatsApp Group Chat 
•	Open the individual or group chat. 
•	Tap More options > More > Export chat. 
•	Choose whether to export with media or without media.

In order to run this program, you must have below Python library on your machine 
•	Pandas 
•	Numpy 
•	Dateparser 
•	Matplotlib

Steps that I followed in code
•	Read Chat file Split chat data into separate lines. 
•	Merge chat lines if that are part of continuation messages from same sender. 
•	Loop through chat rows and separate out 'Date', 'Time', User' & 'Messages'. 
•	Put all these items into four different Lists object. 
•	Prepare Data Frame using these four Lists. 

Then Generate Graph (I have created single graph of Most Active user of the Group).
You can create more graph similarly based on your need.
Inspiration Credit - https://github.com/iamreechi/Whatsapp-chat-Analysis

