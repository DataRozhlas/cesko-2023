import csv
import json

csv_data = '''pivo1,"PIVO - Budou v roce 2023 Češi stále první na světě v množství vypitého piva na osobu?",
0,ANO,
1,NE,
,,
pivo2,"PIVO - Jaká bude v roce 2023 průměrná cena lahvové desítky?",
0,"Více než 15 Kč",
1,"11–15 Kč",
2,"Přibližně 10 Kč (jako nyní)",
3,"5–9 Kč",
4,"méně než 5 Kč",
,,
styl1,"ŽIVOTNÍ STYL - Bude v roce 2023 platit úplný zákaz kouření v restauracích?",
0,ANO,
1,NE,
,,
styl2,"ŽIVOTNÍ STYL - Jakého věku se budou Češi v roce 2023 průměrně dožívat?",
0,"O 5 let a více než nyní",
1,"O 3-4 roky více než nyní",
2,"O 1-2 roky více než nyní",
3,"Stejného věku jako nyní (78 let)",
4,"O 1-2 roky méně než nyní",
5,"O 3-4 roky méně než nyní",
6,"O 5 let a méně než nyní",
,,
media1,"MÉDIA - Jak se do roku 2023 změní počet posluchačů Českého rozhlasu?",
0,"Vzroste o víc než 2 miliony",
1,"Vzroste maximálně o 2 miliony",
2,"Vzroste maximálně o 1 milion",
3,"Zůstane stejný jako nyní (2,5 milionů týdně)",
4,"Klesne maximálně o 1 milion",
5,"Klesne maximálně o 2 miliony",
6,"Klesne o víc než 2 miliony",
,,
media2,"MÉDIA - Kolik bude mít Česká televize v roce 2023 kanálů?",
0,"10 a více",
1,7-9,
2,"6 (jako nyní)",
3,3-5,
4,0-2,
,,
prezident1,"PREZIDENT - Změní se do roku 2023 ústavní pravomoci hlavy státu?",
0,"Změní se, budou větší",
1,"Změní se, budou menší",
2,"Změní se bez jednoznačného zvětšení nebo zmenšení",
3,"Nezmění se",
,,
prezident2,"PREZIDENT - Kdo bude v roce 2023 hlavou státu?","Napište jméno a příjmení"
,,
doprava1,"DOPRAVA - Bude v roce 2023 nejpoužívanějším dopravním prostředkem auto?",
0,ANO,
1,NE,
,,
doprava2,"DOPRAVA - Jaké bude v roce 2023 nejpoužívanější palivo?",
0,"Benzín nebo nafta",
1,Elektřina,
2,"Plyn (LPG nebo CNG)",
3,Vodík,
4,"Stlačený vzduch",
5,Jiné:,
,,
penize1,"PENÍZE - Budeme v roce 2023 platit eurem?",
0,ANO,
1,NE,
,,
penize2,"PENÍZE - Budeme v roce 2023 ještě používat kovové mince?",
0,ANO,
1,NE,
,,
technologie1,"TECHNOLOGIE - Budeme v roce 2023 ještě platit za připojení k internetu?",
0,ANO,
1,NE,
,,
technologie2,"TECHNOLOGIE - Jak bude v roce 2023 vypadat nejprodávanější mobilní telefon?",
0,"Podobně jako dotykový telefon z roku 2013",
1,"Jako hodinky",
2,"Jako brýle",
3,Jinak:,
,,
sport1,"SPORT - Podaří se někomu do roku 2023 překonat světový rekord Jarmily Kratochvílové v běhu na 800 metrů z roku 1983?","Rekord má hodnotu 1 minuta 53,28 vteřin"
0,ANO,
1,NE,
,,
sport2,"SPORT - Kolikrát do roku 2023 získá Česko zlatou medaili na mistrovství světa v hokeji?","MS v hokeji by mělo být celkem 10x"
0,"ani jednou",
1,1x,
2,2x,
3,3x,
4,4x,
5,"5x a vícekrát",
,,
kultura1,"KULTURA - Bude v příštích deseti letech nějaký český film oceněn soškou Oscara?",
0,ANO,
1,NE,
,,
kultura2,"KULTURA - Kdo se v následujících deseti letech stane nejčastěji absolutním vítězem Slavíka?",
0,"Lucie Bílá (jako v uplynulých deseti letech)",
1,"Aneta Langerová",
2,"Karel Gott",
3,"Tomáš Klus",
4,"Skupina Kabát",
5,"Skupina Nightwork",
6,"Někdo jiný:",
,,
mimozemstane1,"MIMOZEMŠŤANÉ - Přiletí do roku 2023 na Zemi oficiálně návštěvníci z jiné planety?",
0,ANO,
1,NE,
,,
mimozemstane2,"MIMOZEMŠŤANÉ - Pokud přiletí, tak s jakými úmysly?",
0,"Spřátelit se",
1,"Požádat o pomoc",
2,"Zkoumat floru a faunu",
3,"Válčit a podrobit si lidstvo",
4,"Přiletí na dovolenou",
5,"S jinými úmysly:",
,,
0,"Osobní část",
,,
partner,"Můj partnerský život v roce 2023",
0,"Zůstanu se současným partnerem",
1,"Najdu si nového partnera",
2,"Budu sám/sama",
,,
deti,"Mé děti do roku 2023",
0,"Žádné nové děti mít nebudu",
1,"Narodí se mi 1 dítě",
2,"Narodí se mi 2 děti",
3,"Narodí se mi 3 nebo více dětí",
,,
bydleni,"Mé bydlení do roku 2023",
0,"Zůstanu ve stejném bytě/domě",
1,"Přestěhuji se v rámci města/obce",
2,"Přestěhuji se do jiného města/obce",
3,"Budu žít v jiné zemi",
,,
vzdelani,"Mé vzdělání do roku 2023",
0,"Nic se nezmění",
1,Odmaturuji,
2,"Získám vysokoškolský diplom",
3,Jiné:,
,,
vaha,"Má váha do roku 2023",
0,"Zhubnu více než 10 kilo",
1,"Zhubnu 6-10 kilo",
2,"Zhubnu 1-5 kilo",
3,"Budu vážit stejně",
4,"Ztloustnu 1-5 kilo",
5,"Ztloustnu 6-10 kilo",
6,"Ztloustnu více než 10 kilo",
,,
koureni,"Já a kouření do roku 2023",
0,"Přestanu kouřit",
1,"Začnu kouřit",
2,"Zůstanu nekuřákem",
3,"Zůstanu kuřákem",
,,
zamestnani,"Mé zaměstnání do roku 2023",
0,"Najdu si práci",
1,"Najdu si jinou práci",
2,"Budu ve stejném zaměstnání a povýším",
3,"Budu ve stejném zaměstnání na stejné pozici",
4,"Budu ve stejném zaměstnání na nižší pozici",
5,"Budu v důchodu",
6,"Budu bez práce",
,,
mzda,"Má hrubá mzda do roku 2023",
0,"Polepším si o 30 tisíc korun měsíčně nebo více",
1,"Polepším si o 20-29 tisíc korun měsíčně",
2,"Polepším si o 10-19 tisíc korun měsíčně",
3,"Polepším si o 1-9 tisíc korun měsíčně",
4,"Budu mít stejný plat jako dnes",
5,"Pohorším si o 1-9 tisíc korun měsíčně",
6,"Pohorším si o 10-19 tisíc korun měsíčně",
7,"Pohorším si o 20-29 tisíc korun měsíčně",
8,"Pohorším si o 30 tisíc korun měsíčně nebo více",
,,
zivot,"Můj život v roce 2023",
0,"Bude se mi žít lépe než v roce 2013",
1,"Bude se mi žít hůře než v roce 2013",
,,
chci-byt,"V roce 2023 bych chtěl být ...",
0,Miliardářem,
1,"Slavnou celebritou",
2,"Úspěšným sportovcem",
3,"Princeznou nebo modelkou",
4,"Kosmonautem nebo popelářem",
5,Bezdomovcem,
6,"Alespoň naživu",
,,
vzkaz-pro-mne,"Vzkaz do roku 2023 pro mě",
,,
vzkaz-posluchacum,"Vzkaz do roku 2023 pro posluchače Českého rozhlasu",
,,
pocet-navstev,"Jaký byl včera počet návštěv na webu www.cesko2023.cz?","Odpověď rozhoduje o tom, kdo dostane dnešní odměnu (princip odměňování naleznete v <a href=""http://www.rozhlas.cz/cesko2023/oprojektu/_zprava/pravidla-souteze-cesko-2023--1272603"" target=""_blank"">pravidlech</a>)."
,,
mail1,"Váš e-mail, prostřednictvím kterého Vás budeme informovat o případné odměně:",
,,
mail2,"E-mail nebo e-maily, na kterých budete za 10 let k zastižení (Vaše odpovědi Vám v roce 2023 připomeneme).",
0,"Stejný jako současný e-mail",
1,Jiný:,
,,
jmeno,"Vaše jméno","Je nezbytné pro předání odměny"
,,
prijmeni,"Vaše příjmení","Je nezbytné pro předání odměny"
,,
pohlavi,"Vaše pohlaví","Bude použito ke statistickým účelům"
0,Muž,
1,Žena,
,,
souhlas,Souhlasím,"Účastí v tipování (v soutěži) dává účastník souhlas podle zákona č. 101/2000 Sb., o ochraně osobních údajů, se zpracováním svých osobních údajů v rozsahu jméno, příjmení, e-mailová adresa (či adresy) a pohlaví. Souhlas se zpracováním osobních údajů se uděluje na dobu 10 let, případně do odvolání tohoto souhlasu subjektem údajů. Osobní údaje budou zpracovávány výlučně správcem osobních údajů Českým rozhlasem, se sídlem Vinohradská 12, 120 99 Praha 2 a pouze za výše uvedeným účelem. Udělení souhlasu je dobrovolné. Osobní údaje nebudou předávány třetím osobám. Subjekt údajů má právo kdykoliv souhlas odvolat, právo na opravu a přístup ke svým osobním údajům, jakož i ostatní práva uvedená v § 21 z. č. 101/2000 Sb., o ochraně osobních údajů."
,,
novinky,"Mám zájem o zasílání informačních e-mailů týkajících se novinek v programu Českého rozhlasu.",
,,
captcha,"Opište následující číslo, abychom měli jistotu, že nejste robot: 569",
,,
'''

# Split the CSV data into lines
lines = csv_data.split('\n')

# Initialize variables
questions = []
current_question = None

# Iterate through the lines
for line in lines:
    # Skip empty lines
    if not line.strip():
        continue

    # Split the line into fields
    fields = list(csv.reader([line]))[0]

    # If the line contains only two commas, it marks the end of the current question
    if len(fields) == 3 and fields[1] == '':
        if current_question is not None:
            questions.append(current_question)
        current_question = None
        continue

    # If there is no current question, create one
    if current_question is None:
        current_question = {
            'question_id': fields[0],
            'question_text': fields[1],
            'answers': []
        }
    else:
        # Add an answer to the current question
        answer = {
            'answer_id': int(fields[0]),
            'answer_text': fields[1]
        }
        current_question['answers'].append(answer)

# Add the last question
if current_question is not None:
    questions.append(current_question)

# Write the questions to a JSON file
with open('../src/assets/questions.json', 'w', encoding='utf-8') as json_file:
    json.dump(questions, json_file, ensure_ascii=False, indent=2)
