text = '''Ах, если бы 'Биму' сейчас несколько/ глотков воды! А так, наверно, (он не встал бы никогда), если бы... Подошла женщина. Она была в ватном пиджаке и ватных же брюках, голова повязана платком. Сильная, большая женщина. Видимо, она сперва подумала, что Бим уже мертв, - наклонилась над ним, став на колени, и прислушалась: Бим/ еще дышал. Он настолько ослабел со времени прощания с другом, что ему, конечно, нельзя было устраивать такой прогон, какой он совершил за поездом, - это безрассудно. Но разве имеет значение в таких случаях разум, даже у человека!
Женщина* взяла в ладони голову; "Бима" и приподняла:
- Что с тобой, собачка? Ты что, Черное Ухо? За кем же ты так бежал, горемыка?'''
print(text, end='\n\n')

punctuation = '.,:;!?-\'\"()*/'

words = []
for word in text.split():
    if len(word) > 1:
        words += [''.join(word.strip(punctuation))]
print(*words)

# Ах если бы Биму сейчас несколько глотков воды
# так наверно он не встал бы никогда если бы Подошла
# женщина Она была ватном пиджаке ватных же брюках
# голова повязана платком Сильная большая женщина
# Видимо она сперва подумала что Бим уже мертв наклонилась
# над ним став на колени прислушалась Бим еще дышал
# Он настолько ослабел со времени прощания другом что ему
# конечно нельзя было устраивать такой прогон какой он совершил
# за поездом это безрассудно Но разве имеет значение таких случаях 
# разум даже человека Женщина взяла ладони голову Бима приподняла 
# Что тобой собачка Ты что Черное Ухо За кем же ты так бежал горемыка