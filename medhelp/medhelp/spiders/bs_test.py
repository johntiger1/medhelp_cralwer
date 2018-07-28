# import requests


from bs4 import BeautifulSoup

html_doc = '''
<div id="subject_msg" class="trunc_subj_msg" itemprop="text">
                I have a lot of health problems both physical and mental, and because of that, I have tried to catch and monitor my symptoms daily. I wanted to know if other people experience this. 
<br>
<br>It happens most often when I am sitting down reading or such, or just getting down to sleep. Like 2 mins ago I just did it, sitting at my desk, typing. It doesn't happen when I'm out and about, doing things.&nbsp;&nbsp;
<br>
<br>I will just be sitting there and then randomly I will take in a deep breath of air. I'm not too concerned about it but I want to know your option. I do notice that normally I breathe very softly almost shallow but I'm not uncomfortable or anything. One time when my sister was sleeping in the same room as me. She actually called my name because she said she was worried because she couldn't hear me breathing, though I was awake still and I was. 
<br>
<br>I have been tested for sleep apnea and been told I do not have it, rather, that my brain keeps waking me up in the night without my knowledge leading to me being chronically tired and unable to think during the day. 
<br>
<br>What are your thoughts?
          </div>
          '''
# Also, try the XPATH stuff!
soup=BeautifulSoup(html_doc)

print(soup.div.string) #WOW OK....
