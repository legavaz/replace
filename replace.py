import os

m_dir =   os.path.abspath(os.path.dirname(__file__))
print('Поиск файлов *.txt в :{0}'.format(m_dir))

massif_file =   []
for file in os.listdir(m_dir):
    if file.endswith(".txt"):
        massif_file.append(os.path.join(m_dir, file))
        

def save_new_txt_file(file_name,some_text):
    new_name       =   os.path.splitext(item_file)[0]+'_2.txt'
    f = open(new_name,'w',encoding="utf-8")
    f.write(some_text)
    f.close()

def replace_text(file_name,text_serch,text_replace):
    f = open(file_name,'rt',encoding="utf-8")
    m_text          =   ''
    m_text_old      =   ''
    m_replace       =   False
    while True:        
        line        = f.readline();   
        line_rep    = line.replace(text_serch,text_replace)  
        m_replace   = line!=line_rep or m_replace  
        m_text      = m_text + line_rep
        m_text_old  = m_text_old+line
        if len(line)==0:
            break
    f.close() 
    if m_replace:
        print('было:')
        print(m_text_old)
        print('стало:')
        print(m_text)
        save_new_txt_file(file_name,m_text)
    else:
        print('не обработан')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()


text_serch  =input('Укажите текст поиска:')
text_replace=input('Укажите текст замены:')

if text_serch   ==  '' or text_replace   ==  '':
    print('Указаны не все параметры. ')
else:
    for item_file in massif_file:
        print('*'*25)
        print('обработка',item_file)
        replace_text(item_file,text_serch,text_replace)
        


#input(' для продолжени нажмите Enter')