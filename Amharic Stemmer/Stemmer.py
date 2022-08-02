# PROGRAM TO STEM AMHARIC WORDS TO THEIR ROOT FORM


# GROUP MEMBERS
# 1. Abiy Zebene
# 2. Dagemawi Yoseph
# 3. Elias Nuru
# 4. Emran Kasim
# 5. Eyosias Gezahegn

import codecs


#LIST OF SUFFIXES AND PREFIXES
suffix = [ 'iAäLäŜ','aWiW','aČäWaL','äČaT','äČaČHu','äČaČäW','aLäHu','aĞäT','aWoČ','aLäH','aLäŜ','aLäČHu','aLaLäČ','BaČäWS','BaČäW',
           'aČäWN','aLäČ','aLäN','aLaČHu','aČHuN','aČHu','aČHuT','WoČNNa','WoČN','aČäW','WoČuN','BWoT','aČNM','aSäWi','BäTä',
           'WoČu','äWNa', 'oČuN', 'äÑaNäTM', 'äÑaNa','äÑaNäT', 'äÑaN', 'äÑaWM','äÑaW','ÑaWa','BäTN','aČHuM','aČäW','oWa','äČW',
           'äČu', 'iču','NäW', 'NäT', 'aLu','aČN','aČW','KuM','KuT','KäW','äČN','äČM','äČH','äČŜ','äČN','äČW','YuŜN','YuŜ','äWi',
           'oČNNa','aWi','BäČ','oČ','oČu','WoN','äÑa','ÑaWN','ÑaW','oČN','äÑ','äM','ŜW','KM','äW','TM','Wo','WM','WN','NM','ŜN',
           'oČ','uT','iT','Ku','Wa','H','Ŝ','u','K','ä','äČ','uN','N','M','No','W','i']

prefix = ['SLäMaY','YäMaT','LaYa','ANDä','YäTä','BäMa','eNDä','AäL','SLä','MäS','AYä','AäS','AäT','AäY','YaL',
          'SaT','SaN','SaY','SaL','YaS','Yä','Bä','Lä','Kä','AN','AL','Y','T','ä']

#TEST WORDS

wordList = []
with codecs.open('TestCorpus.txt', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    wordList.append(line)

#wordList = ['ብረቶች','ሰዋሰው','ቤቶቹ','የቤቶቹ','መንፈሳዊ','ምክንያትህ','እንደምንኖር','በተያዘው','ሀገራቸው','ብርጭቆውን','መነጽርዎቹን',
#            'ኩባያዋ', 'መጽሀፉ', 'አበላል', 'ጫማዎቹ', 'በመሠላል', 'ከደነው', 'አንብብ', 'ጥፋቶች', 'አደረጃጀት', 'ቀጣፊ',
#            'ሽቦዎች', 'የኤሌክትሪክ','በውሃ','የዳቦ','ከጤፍ','ከልጃችንም','ባሪያውን','ላያፈርሳቸው','በባልደረባነት','የደገፈኝ','የመጀመሪያው'                                        
#            ,'ኃይማኖታዊ','የከተማዋን','ከመፈልፈልዎ','አለብዎት','ወረዳዎች','የበቆሎ','አስናቀው','እንቁላሎቹ','ይስማው']



#FUNCTION TO CONVERT TEST WORDS TO CONSONANT VOWEL(CV) OR PHONETIC FORM
def convert(s):
 
    # initialization of string to ""
    new = ""
 
    # traverse in the string
    for x in s:
        if x == 'ሀ':
            new += "Hä"
        if x == 'ሁ':
            new += "Hu"
        if x == 'ሂ':
            new += "Hi"
        if x == 'ሃ':
            new += "Ha"
        if x == 'ሄ':
            new += "He"
        if x == 'ህ':
            new += 'H'
        if x == 'ሆ':
            new += 'Ho'

        if x == 'ለ':
            new += "Lä"
        if x == 'ሉ':
            new += "Lu"
        if x == 'ሊ':
            new += "Li"
        if x == 'ላ':
            new += "La"
        if x == 'ሌ':
            new += "Le"
        if x == 'ል':
            new += "L"
        if x == 'ሎ':
            new +="Lo"

        if x == 'ሐ':
            new += "Hä"
        if x == 'ሑ':
            new += "Hu"
        if x == 'ሒ':
            new += "Hi"
        if x == 'ሓ':
            new += "Hā"
        if x == 'ሔ':
            new += "He"
        if x == 'ሕ':
            new += "H"
        if x == 'ሖ':
            new += "Ho"

        if x == 'መ':
            new += "Mä"
        if x == 'ሙ':
            new += 'Mu'
        if x == 'ሚ':
            new += "Mi"
        if x == 'ማ':
            new+= "Ma"
        if x == 'ሜ':
            new += "Me"
        if x == 'ም':
            new += "M"
        if x == 'ሞ':
            new += 'Mo'

        if x == 'ሠ':
            new += "Sä"
        if x == 'ሡ':
            new += "Su"
        if x == 'ሢ':
            new += "Si"
        if x == 'ሣ':
            new += 'Sa'
        if x == 'ሤ':
            new += "Se"
        if x == 'ሥ':
            new += "S"
        if x == 'ሦ':
            new += "So"

        if x == 'ረ':
            new += "Rä"
        if x == 'ሩ':
            new += "Ru"
        if x == 'ሪ':
            new += "Ri"
        if x == 'ራ':
            new += "Ra"
        if x == 'ሬ':
            new += "Re"
        if x == 'ር':
            new += "R"
        if x == 'ሮ':
            new += "Ro"

        if x == 'ሰ':
            new += "Sä"
        if x == 'ሱ':
            new += "Su"
        if x == 'ሲ':
            new += "Si"
        if x == 'ሳ':
             new += "Sa"
        if x == 'ሴ':
            new += "Se"
        if x == 'ስ':
            new = "S"
        if x == 'ሶ':
            new += "So"

        if x == 'ሸ':
            new += "Ŝä"
        if x == 'ሹ':
            new += "Ŝu"
        if x == 'ሺ':
            new += "Ŝi"
        if x == 'ሻ':
            new += "Ŝa"
        if x == 'ሼ':
            new += "Ŝe"
        if x == 'ሽ':
            new += "Ŝ"
        if x == 'ሾ':
            new += "Ŝo"

        if x == 'ቀ':
            new += "Qä"
        if x == 'ቁ':
            new += "Qu"
        if x == 'ቂ':
            new += "Qi"
        if x == 'ቃ':
            new += "Qa"
        if x == 'ቄ':
            new += "Qe"
        if x == 'ቅ':
            new += "Q"
        if x == 'ቆ':
            new += "Qo"
            
        if x == 'በ':
            new += "Bä"
        if x == 'ቡ':
            new += "Bu"
        if x == 'ቢ':
            new += "Bi"
        if x == 'ባ':
            new += "Ba"
        if x == 'ቤ':
            new += 'Be'
        if x == 'ብ':
            new +="B"
        if x == 'ቦ':
            new += 'Bo'

        if x == 'ተ':
            new += "Tä"
        if x == 'ቱ':
            new += "Tu"
        if x == 'ቲ':
            new += 'Ti'
        if x == 'ታ':
            new += "Ta"
        if x == 'ቴ':
            new += "Te"
        if x == 'ት':
            new += "T"
        if x == 'ቶ':
            new += "To"
            
        if x == 'ቸ':
            new += "Čä"
        if x == 'ቹ':
            new += "Ču"
        if x == 'ቺ':
            new += "Či"
        if x == 'ቻ':
            new += "Ča"
        if x == 'ቼ':
            new += "Če"
        if x == 'ች':
            new += "Č"
        if x == 'ቾ':
            new += "Čo"

        if x == 'ኀ':
            new += "Hä"
        if x == 'ኁ':
            new += "Hu"
        if x == 'ኂ':
            new += "hi"
        if x == 'ኃ':
            new += 'Ha'
        if x == 'ኄ':
            new += "He"
        if x == 'ኅ':
            new += "H"
        if x == 'ኆ':
            new += "ho"

        if x == 'ነ':
            new += "Nä"
        if x == 'ኑ':
            new += "Nu"
        if x == 'ኒ':
            new += "Ni"
        if x == 'ና':
            new += "Na"
        if x == 'ኔ':
            new += "Ne"
        if x == 'ን':
            new += 'N'
        if x == 'ኖ':
            new += "No"

        if x == 'ኘ':
            new += "Ñä"
        if x == 'ኙ':
            new += "Ñu"
        if x == 'ኚ':
            new += "Ñi"
        if x == 'ኛ':
            new += "Ña"
        if x == 'ኜ':
            new += "Ñe"
        if x == 'ኝ':
            new += "Ñ"
        if x == 'ኞ':
            new += "Ño"
            
        if x == 'አ':
            new += "ä"
        if x == 'ኡ':
            new += "u"
        if x == 'ኢ':
            new += "i"
        if x == 'ኣ':
            new += "a"
        if x == 'ኤ':
            new += "é"
        if x == 'እ':
            new += "e"
        if x == 'ኦ':
            new += "o"
            
        if x == 'ከ':
            new += "Kä"
        if x == 'ኩ':
            new += "Ku"
        if x == 'ኪ':
            new += "Ki"
        if x == 'ካ':
            new += "Ka"
        if x == 'ኬ':
            new += "Ke"
        if x == 'ክ':
            new += "K"
        if x == 'ኮ':
            new += "Ko"

        if x == 'ኸ':
            new += "Xä"
        if x == 'ኹ':
            new += "Xu"
        if x == 'ኺ':
            new += "Xi"
        if x == 'ኻ':
            new += "Xa"
        if x == 'ኼ':
            new += 'Xe'
        if x == 'ኽ':
            new += 'X'
        if x == 'ኾ':
            new += "Xo"
        
        if x == 'ወ':
            new += "Wä"
        if x == 'ዉ':
            new += "Wu"
        if x == 'ዊ':
            new += "Wi"
        if x == 'ዋ':
            new += "Wa"
        if x == 'ዌ':
            new += 'We'
        if x == "ው":
            new += 'W'
        if x == 'ዎ':
            new += "Wo"
            
        if x == 'ዐ':
            new += "Aä"
        if x == 'ዑ':
            new += "Au"
        if x == 'ዒ':
            new += "Ai"
        if x == 'ዓ':
            new += "Aā"
        if x == 'ዔ':
            new +="Aé"
        if x == 'ዕ':
            new += "A"
        if x == 'ዖ':
            new += "Ao"


        if x == 'ዘ':
            new += "Zä"
        if x == 'ዙ':
            new += "Zu"
        if x == 'ዚ':
            new += "Zi"
        if x == 'ዛ':
            new += "Za"
        if x == 'ዜ':
            new += "Ze"
        if x == 'ዝ':
            new += "Z"
        if x == 'ዞ':
            new += "Zo"

        if x == 'ዠ':
            new += "Žä"
        if x == 'ዡ':
            new += "Žu"
        if x == 'ዢ':
            new += "Ži"
        if x == 'ዣ':
            new += 'Ža'
        if x == 'ዤ':
            new += "Žw"
        if x == 'ዥ':
            new += "Ž"
        if x == 'ዦ':
            new += "Žo"

        if x == 'የ':
            new += "Yä"
        if x == 'ዩ':
            new += "Yu"
        if x == 'ዪ':
            new += "Yi"
        if x == 'ያ':
            new += "Ya"
        if x == 'ዬ':
            new += "Ye"
        if x == 'ይ':
            new += "Y"
        if x == 'ዮ':
            new += "Yo"

        if x == 'ደ':
            new += "Dä"
        if x == 'ዱ':
            new += "Du"
        if x == 'ዲ':
            new += "Di"
        if x == 'ዳ':
            new += "Da"
        if x == 'ዴ':
            new += "De"
        if x == 'ድ':
            new += "D"
        if x == 'ዶ':
            new += "Do"

        if x == 'ጀ':
            new += "Ğä"
        if x == 'ጁ':
            new += "Ğu"
        if x == 'ጂ':
            new += "Ği"
        if x == 'ጃ':
            new += "Ğa"
        if x == 'ጄ':
            new += "Ğe"
        if x == 'ጅ':
            new += "Ğ"
        if x == 'ጆ':
            new += "Ğo"
            
        if x == 'ገ':
            new += "Gä"
        if x == 'ጉ':
            new += "Gu"
        if x == 'ጊ':
            new += "Gi"
        if x == 'ጋ':
            new += "Ga"
        if x == 'ጌ':
            new += "Ge"
        if x == 'ግ':
            new += "G"
        if x == 'ጎ':
            new += "Go"

        if x == 'ጠ':
            new += "Ṭä"
        if x == 'ጡ':
            new += "Ṭu"
        if x == 'ጢ':
            new += "Ṭi"
        if x == 'ጣ':
            new += "Ṭa"
        if x == 'ጤ':
            new += "Ṭe"
        if x == 'ጥ':
            new += "Ṭ"
        if x == 'ጦ':
            new += "Ṭo"

        if x == 'ጨ':
            new += "Ċä"
        if x == 'ጩ':
            new += "Ċu"
        if x == 'ጪ':
            new += "Ċi"
        if x == 'ጫ':
            new += "Ċa"
        if x == 'ጬ':
            new += "Ċe"
        if x == 'ጭ':
            new += "Ċ"
        if x == 'ጮ':
            new += "Ċo"

        if x =='ጰ':
            new += "P̣ä"
        if x =='ጱ':
            new += "P̣u"
        if x == 'ጲ':
             new += "P̣i"
        if x == 'ጳ':
             new += "P̣a"
        if x == 'ጴ':
             new += "P̣a"
        if x == 'ጵ':
             new += "P̣"
        if x == "ጶ":
             new += "P̣o"

        if x == 'ጸ':
            new += "Ṣä"
        if x == 'ጹ':
            new += "Ṣu"
        if x == 'ጺ':
            new += "Ṣi"
        if x == 'ጻ':
            new += "Ṣa"
        if x == 'ጼ':
            new += "Ṣe"
        if x == 'ጽ':
            new += "Ṣ"
        if x == 'ጾ':
            new += "Ṣo"

        if x == 'ፀ':
            new +="Ṡä"
        if x == 'ፁ':
            new +="Ṡu"
        if x == 'ፂ':
            new +="Ṡi"
        if x == 'ፃ':
            new +="Ṡa"
        if x == 'ፄ':
            new += "Ṡe"
        if x == 'ፅ':
            new += "Ṡ"
        if x == 'ፆ':
            new += "Ṡo"

        if x == 'ፈ':
            new += "Fä"
        if x == 'ፉ':
            new += "Fu"
        if x == 'ፊ':
            new += "Fi"
        if x == 'ፋ':
            new += 'Fa'
        if x == 'ፌ':
            new += "Fe"
        if x == 'ፍ':
            new += "F"
        if x == 'ፎ':
            new += "Fo"

        if x == 'ፐ':
            new += "Pä"
        if x == 'ፑ':
            new += "Pu"
        if x == 'ፒ':
            new += "Pi"
        if x == 'ፓ':
            new += "Pa"
        if x == 'ፔ':
            new += "Pe"
        if x == 'ፕ':
            new += "P"
        if x == 'ፖ':
            new += "Po"

        if x == 'ቨ':
            new += "Vä"
        if x == 'ቩ':
            new += "Vu"
        if x == 'ቪ':
            new += "Vi"
        if x == 'ቫ':
            new += "Va"
        if x == 'ቬ':
            new += 'Ve'
        if x == 'ቭ':
            new += "V"
        if x == 'ቮ':
            new += "Vo"    
 
    # return string
    return new

#FUNCTION TO CONVERT BACK FROM CV FROM TO ROOT/STEM FORM
def convertBack(x):
 
    # initialization of string to ""
    new = ""

    if x == 'Hä':
        new = "ሀ"
    if x == 'Hu':
        new = "ሁ"
    if x == 'Hi':
        new = "ሂ"
    if x == 'ሃ':
        new = "Ha"
    if x == 'He':
        new = "ሄ"
    if x == 'H':
        new = 'ህ'
    if x == 'Ho':
        new = 'ሆ'

    if x == 'Lä':
        new = "ለ"
    if x == 'Lu':
        new = "ሉ"
    if x == 'Li':
        new = "ሊ"
    if x == 'La':
        new = "ላ"
    if x == 'Le':
        new = "ሌ"
    if x == 'L':
        new = "ል"
    if x == 'Lo':
        new ="ሎ"

    if x == 'Hä':
        new = "ሐ"
    if x == 'Hu':
        new = "ሑ"
    if x == 'Hi':
        new = "ሒ"
    if x == 'Hā':
        new = "ሓ"
    if x == 'He':
        new = "ሔ"
    if x == 'H':
        new = "ሕ"
    if x == 'Ho':
        new = "ሖ"

    if x == 'Mä':
        new = "መ"
    if x == 'Mu':
        new = 'ሙ'
    if x == 'Mi':
        new = "ሚ"
    if x == 'Ma':
        new= "ማ"
    if x == 'Me':
        new = "ሜ"
    if x == 'M':
        new = "ም"
    if x == 'Mo':
        new = 'ሞ'

    if x == 'Sä':
        new = "ሠ"
    if x == 'Su':
        new = "ሡ"
    if x == 'Si':
        new = "ሢ"
    if x == 'Sa':
        new = 'ሣ'
    if x == 'Se':
        new = "ሤ"
    if x == 'S':
        new = "ሥ"
    if x == 'So':
        new = "ሦ"

    if x == 'Rä':
        new = "ረ"
    if x == 'Ru':
        new = "ሩ"
    if x == 'Ri':
        new = "ሪ"
    if x == 'Ra':
        new = "ራ"
    if x == 'Re':
        new = "ሬ"
    if x == 'R':
        new = "ር"
    if x == 'Ro':
        new = "ሮ"

    if x == 'Sä':
        new = "ሰ"
    if x == 'Su':
        new = "ሱ"
    if x == 'Si':
        new = "ሲ"
    if x == 'Sa':
        new = "ሳ"
    if x == 'Se':
        new = "ሴ"
    if x == 'S':
        new = "ስ"
    if x == 'So':
        new = "ሶ"

    if x == 'Ŝä':
        new = "ሸ"
    if x == 'Ŝu':
        new = "ሹ"
    if x == 'Ŝi':
        new = "ሺ"
    if x == 'Ŝa':
        new = "ሻ"
    if x == 'Ŝe':
        new = "ሼ"
    if x == 'Ŝ':
        new = "ሽ"
    if x == 'Ŝo':
        new = "ሾ"

    if x == 'Qä':
        new = "ቀ"
    if x == 'Qu':
        new = "ቁ"
    if x == 'Qi':
        new = "ቂ"
    if x == 'Qa':
        new = "ቃ"
    if x == 'Qe':
        new = "ቄ"
    if x == 'Q':
        new = "ቅ"
    if x == 'Qo':
        new = "ቆ"
            
    if x == 'Bä':
        new = "በ"
    if x == 'Bu':
        new = "ቡ"
    if x == 'Bi':
        new = "ቢ"
    if x == 'Ba':
        new = "ባ"
    if x == 'Be':
        new = 'ቤ'
    if x == 'B':
        new ="ብ"
    if x == 'Bo':
        new = 'ቦ'

    if x == 'Tä':
        new = "ተ"
    if x == 'Tu':
        new = "ቱ"
    if x == 'Ti':
        new = 'ቲ'
    if x == 'Ta':
        new = "ታ"
    if x == 'Te':
        new = "ቴ"
    if x == 'T':
        new = "ት"
    if x == 'To':
        new = "ቶ"
            
    if x == 'Čä':
        new = "ቸ"
    if x == 'Ču':
        new = "ቹ"
    if x == 'Či':
        new = "ቺ"
    if x == 'Ča':
        new = "ቻ"
    if x == 'Če':
        new = "ቼ"
    if x == 'Č':
        new = "ች"
    if x == 'Čo':
        new = "ቾ"

    if x == 'Hä':
        new = "ኀ"
    if x == 'Hu':
        new = "ኁ"
    if x == 'Hi':
        new = "ኂ"
    if x == 'Ha':
        new = 'ኃ'
    if x == 'He':
        new = "ኄ"
    if x == 'H':
        new = "ኅ"
    if x == 'Ho':
        new = "ኆ"

    if x == 'Nä':
        new = "ነ"
    if x == 'Nu':
        new = "ኑ"
    if x == 'Ni':
        new = "ኒ"
    if x == 'Na':
        new = "ና"
    if x == 'Ne':
        new = "ኔ"
    if x == 'N':
        new = "ን"
    if x == 'No':
        new = "ኖ"

    if x == 'Ñä':
        new = "ኘ"
    if x == 'Ñu':
        new = "ኙ"
    if x == 'Ñi':
        new = "ኚ"
    if x == 'Ña':
        new = "ኛ"
    if x == 'Ñe':
        new = "ኜ"
    if x == 'Ñ':
        new = "ኝ"
    if x == 'Ño':
        new = "ኞ"
            
    if x == 'ä':
        new = "አ"
    if x == 'u':
        new = "ኡ"
    if x == 'i':
        new = "ኢ"
    if x == 'a':
        new = "ኣ"
    if x == 'é':
        new = "ኤ"
    if x == 'e':
        new = "እ"
    if x == 'o':
        new = "ኦ"
            
    if x == 'Kä':
        new = "ከ"
    if x == 'Ku':
        new = "ኩ"
    if x == 'Ki':
        new = "ኪ"
    if x == 'Ka':
        new = "ካ"
    if x == 'Ke':
        new = "ኬ"
    if x == 'K':
        new = "ክ"
    if x == 'Ko':
        new = "ኮ"

    if x == 'Xä':
        new = "ኸ"
    if x == 'Xu':
        new = "ኹ"
    if x == 'Xi':
        new = "ኺ"
    if x == 'Xa':
        new = "ኻ"
    if x == 'Xe':
        new = 'ኼ'
    if x == 'X':
        new = 'ኽ'
    if x == 'Xo':
        new = "ኾ"
       
    if x == 'Wä':
        new = "ወ"
    if x == 'Wu':
        new = "ዉ"
    if x == 'Wi':
        new = "ዊ"
    if x == 'Wa':
        new = "ዋ"
    if x == 'We':
        new = 'ዌ'
    if x == "W":
        new = 'ው'
    if x == 'Wo':
        new = "ዎ"
            
    if x == 'Aä':
        new = "ዐ"
    if x == 'Au':
        new = "ዑ"
    if x == 'Ai':
        new = "ዒ"
    if x == 'Aā':
        new = "ዓ"
    if x == 'Aé':
        new ="ዔ"
    if x == 'A':
        new = "ዕ"
    if x == 'Ao':
        new = "ዖ"


    if x == 'Zä':
        new = "ዘ"
    if x == 'Zu':
        new = "ዙ"
    if x == 'Zi':
        new = "ዚ"
    if x == 'Za':
        new = "ዛ"
    if x == 'Ze':
        new = "ዜ"
    if x == 'Z':
        new = "ዝ"
    if x == 'Zo':
        new = "ዞ"

    if x == 'Žä':
        new = "ዠ"
    if x == 'Žu':
        new = "ዡ"
    if x == 'Ži':
        new = "ዢ"
    if x == 'Ža':
        new = 'ዣ'
    if x == 'Žw':
        new = "ዤ"
    if x == 'Ž':
        new = "ዥ"
    if x == 'Žo':
        new = "ዦ"

    if x == 'Yä':
        new = "የ"
    if x == 'Yu':
        new = "ዩ"
    if x == 'Yi':
        new = "ዪ"
    if x == 'Ya':
        new = "ያ"
    if x == 'Ye':
        new = "ዬ"
    if x == 'Y':
        new = "ይ"
    if x == 'Yo':
        new = "ዮ"

    if x == 'Dä':
        new = "ደ"
    if x == 'Du':
        new = "ዱ"
    if x == 'Di':
        new = "ዲ"
    if x == 'Da':
        new = "ዳ"
    if x == 'De':
        new = "ዴ"
    if x == 'D':
        new = "ድ"
    if x == 'Do':
        new = "ዶ"

    if x == 'Ğä':
        new = "ጀ"
    if x == 'Ğu':
        new = "ጁ"
    if x == 'Ği':
        new = "ጂ"
    if x == 'Ğa':
        new = "ጃ"
    if x == 'Ğe':
        new = "ጄ"
    if x == 'Ğ':
        new = "ጅ"
    if x == 'Ğo':
        new = "ጆ"
            
    if x == 'Gä':
        new = "ገ"
    if x == 'Gu':
        new = "ጉ"
    if x == 'Gi':
        new = "ጊ"
    if x == 'Ga':
        new = "ጋ"
    if x == 'Ge':
        new = "ጌ"
    if x == 'G':
        new = "ግ"
    if x == 'Go':
        new = "ጎ"
    
    if x == 'Ṭä':
        new = "ጠ"
    if x == 'Ṭu':
        new = "ጡ"
    if x == 'Ṭi':
        new = "ጢ"
    if x == 'Ṭa':
        new = "ጣ"
    if x == 'Ṭe':
        new = "ጤ"
    if x == 'Ṭ':
        new = "ጥ"
    if x == 'Ṭo':
        new = "ጦ"

    if x == 'Ċä':
        new = "ጨ"
    if x == 'Ċu':
        new = "ጩ"
    if x == 'Ċi':
        new = "ጪ"
    if x == 'Ċa':
        new = "ጫ"
    if x == 'Ċe':
        new = "ጬ"
    if x == 'Ċ':
        new = "ጭ"
    if x == 'Ċo':
        new = "ጮ"

    if x =='Ṗä':
        new = "ጰ"
    if x =='Ṗu':
        new = "ጱ"
    if x == 'Ṗi':
        new = "ጲ"
    if x == 'Ṗa':
        new = "ጳ"
    if x == 'Ṗa':
        new = "ጴ"
    if x == 'Ṗ':
        new = "ጵ"
    if x == "Ṗo":
        new = "ጶ"

    if x == 'Ṣä':
        new = "ጸ"
    if x == 'Ṣu':
        new = "ጹ"
    if x == 'Ṣi':
        new = "ጺ"
    if x == 'Ṣa':
        new = "ጻ"
    if x == 'Ṣe':
        new = "ጼ"
    if x == 'Ṣ':
        new = "ጽ"
    if x == 'Ṣo':
        new = "ጾ"

    if x == 'Ṡä':
        new ="ፀ"
    if x == 'Ṡu':
        new ="ፁ"
    if x == 'Ṡi':
        new ="ፂ"
    if x == 'Ṡa':
        new ="ፃ"
    if x == 'Ṡe':
        new = "ፄ"
    if x == 'Ṡ':
        new = "ፅ"
    if x == 'Ṡo':
        new = "ፆ"

    if x == 'Fä':
        new = "ፈ"
    if x == 'Fu':
        new = "ፉ"
    if x == 'Fi':
        new = "ፊ"
    if x == 'Fa':
        new = 'ፋ'
    if x == 'Fe':
        new = "ፌ"
    if x == 'F':
        new = "ፍ"
    if x == 'Fo':
        new = "ፎ"

    if x == 'Pä':
        new = "ፐ"
    if x == 'Pu':
        new = "ፑ"
    if x == 'Pi':
        new = "ፒ"
    if x == 'Pa':
        new = "ፓ"
    if x == 'Pe':
        new = "ፔ"
    if x == 'P':
        new = "ፕ"
    if x == 'Po':
        new = "ፖ"
    
    if x == 'Vä':
        new = "ቨ"
    if x == 'Vu':
        new = "ቩ"
    if x == 'Vi':
        new = "ቪ"
    if x == 'Va':
        new = "ቫ"
    if x == 'Ve':
        new = 'ቬ'
    if x == 'V':
        new = "ቭ"
    if x == 'Vo':
        new = "ቮ"    

    return new


#STEMMER FUNCTION - NORMALIZE AND REMOVES PREFIXES AND SUFFIXES FROM THE TEST WORD
def stemmer(s):
    finalstr = s
    if 'AeNDa' in s:
        finalstr = s.replace("AeNDa","Ao")
    if 'ĊaL' in s:
        finalstr = s.replace("ĊaL","ṬaL")
    if ('eäS' in s) and ('Ñ' == s[len(s)-1]):
        finalstr = s.replace("eäS","S")
    if ('äLa' in s) and len(s)>2: 
        finalstr = s.replace('äLa','ä')
        finalstr = finalstr.strip(finalstr[0:2])
        
    if len(finalstr) > 3:
        su = list(suffix)
        pre = list(prefix)

        for s in su:
            if finalstr.endswith(s):
                finalstr = finalstr.replace(s,'')

        for p in pre:
            if finalstr.startswith(p):
                finalstr = finalstr.replace(p,"")
    return finalstr

#FUNCTION TO CHECK IF THE STEMMED WORD CONTAINS VOWELS 
def containsVowel(s):
    if ('ä' in s) or ('u' in s) or ('i' in s) or ('a' in s) or ('e' in s) or ('o' in s):
        return True
    else:
        return False
    
def main():
    for x in wordList:

        #CONVERT WORD TO CV FORM  
        st = convert(x)
        print(x , end= ' | ')
        
        print(st + ' | stemmed to ',end = ' | ')

        #STEM WORD
        print(stemmer(st),end = ' | ')

        #CONVERT WORD BACK TO ROOT/STEM FORM BY CHECKING IT A PAIR OF WORDS CONTAIN VOWELS
        string = ' '
        i = 0
        while i<=len(stemmer(st))-1:
            if containsVowel(stemmer(st)[i:i+2]):
                if not containsVowel(stemmer(st)[i]): 
                    print(stemmer(st)[i:i+2],end = '-')
                    string += convertBack(stemmer(st)[i:i+2])
                    i = i + 2
                else:
                    print(stemmer(st)[i],end = '-')
                    string += convertBack(stemmer(st)[i])
                    i = i + 1
            else:
                print(stemmer(st)[i],end = '-')
                string += convertBack(stemmer(st)[i])
                i = i + 1
                    
        print(string)
        

main()

