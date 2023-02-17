# ============================================================================ #
# Final Project for Introduction to Python, Spring 2021
# 
# Names
#     Soufiane El kabil
import random
import os

class Entry:

    def __init__(self, deutsch, englisch): #Function for determine the languages and filename and self
        self.deutsch = deutsch
        self.englisch= englisch
        
    def toString(self):
        return self.deutsch + '-' + self.englisch


#check file.txt exists or not
if not os.path.exists('file.txt'):
    open('file.txt','w') # it will create new 'file.txt' if there is no file.txt

eintraege=[]  
deutsch_worte=[]
#read file
with open('file.txt','r') as file:
    for line in file:
        if len(line.split('='))==2: # making sure that this line is on our standard.
            du_en=line.replace('\n','').split('=')
            du=du_en[0].strip() #deutsch words
            en=du_en[1].strip() #englisch words
            eintraege.append(Entry(du,en))
            deutsch_worte.append(du)

def eingabe():
    while True :
        deutsch= input('Deutsches Wort :')
        if deutsch =='fertig':
            break
        englisch= input('Englishes Wort :')
        if englisch =='fertig':
            break
        
        # input corrections
        deutsch=deutsch.strip()
        englisch=englisch.strip().lower()
        
        # write and append
        if deutsch not in deutsch_worte: # it checks not to add repeated words
            entry=Entry(deutsch,englisch)
            
            with open('file.txt' , 'a') as file:
                file.write(f'{entry.deutsch}={entry.englisch}\n')
            
            eintraege.append(entry)
            deutsch_worte.append(deutsch)
        else:
            print('Diese Wörter existieren bereits !')
     
def abfrage():
    if len(eintraege)>0: 
        flag=True
    else:
        flag=False # if 'eintraege' is empty , it will not run the loop
        print('es gibt nichts zu fragen') 
    
    not_asked=eintraege.copy() # to be able to remove an item without affecting on "eintraege"
    
    while flag:
        if len(not_asked) != 0:
            rand_choice=random.choice(not_asked)
        else: # if all questions are answered , it will stop the loop
            print('gut erledigt')
            break 
        
        englisch = input('Englische Ubersetzung von ' + rand_choice.deutsch + ':')
        if (englisch.strip().lower() =='fertig'):
            break 
        elif (rand_choice . englisch) == englisch:
            not_asked.remove(rand_choice) # it will remove an item that aswered correct not to ask again
            print('korrekt')
        
        elif englisch in (rand_choice . englisch).split('/') : # there are some german word with more than one meaning
                                                               # if one of those meaning is answered, that will be accepted
                                                               
            not_asked.remove(rand_choice) # it will remove an item that aswered correct not to ask again
            print('korrekt')
        
        else :
            print('falsch ' + rand_choice . englisch)
            
def print_all():
    for eintrag in eintraege:
        print(eintrag.toString())

###########################################################################
def change(du,en):
    replacement=''
    with open('file.txt','r') as file:
        for line in file:
            if (line.split('=')[0]==du) and line!=f'{du}={en}\n':
                replacement+=f'{du}={en}\n'
                print('Done !')
            else:
                replacement+=line

    with open('file.txt','w') as file:
        file.write(replacement)

def remove_repeated_words():
    replacement=''
    with open('file.txt','r') as file:
        for line in file:
            if line not in replacement:
                replacement+=line
            else:
                continue
            
    with open('file.txt','w') as file:
        file.write(replacement)
############################################################################


while True :
    befehl = input('Befehl:')
    if befehl == 'eingabe':
        eingabe()
    elif befehl =='abfrage':
        abfrage()    
    elif befehl == 'ausgabe':
        print_all()
    elif befehl =='beenden':
        break      
    else :
        print('Diese Befehl gibt nicht, sorry gebe andere Befehl bitte ')