# domashniy-arest/s01e03/scene-35.py
ID = "domashniy-arest-s01e03-scene-35"
SHOW = "domashniy-arest"
SEASON = 1
EPISODE = 3
SCENE = 35
TITLE = "Собака нашлась  (The Dog Is Found)"
LEVEL = "A1 — Duolingo Section 2"
PAIR = "ru-en"
SOURCE_NAME = "Домашний арест (Domashniy Arest) S1.03"
SOURCE_FILE = "sources/domashniy-arest/s01/e03.ru.dual.srt"
VOICES = {"narrator": "sky", "judge": "anja", "anya": "alisa"}
LABELS = {"judge": "Илья Олегович", "anya": "Аркадий"}
INTRO = "Still in the communal flat, a moment later. Now the door opens, and Judge Berg bursts in with his daughter Polina, who points straight at Slavik as the boy who stole her dog Lyutik. Let's listen in Russian first."
STORY = [
    ("judge", "Собака где? Где наш Лютик?", "Where's the dog? Where is our Lyutik?", [(1123, 'Собака где'), (1132, 'Лютик')], ""),
    ("judge", "Так, Славик, это кто? Что случилось?", "Right, Slavik, who is this? What happened?", [(1126, 'Так, Славик, это кто? Что случилось')], ""),
    ("judge", "Это ваш сын? Он украл нашу собаку!", "Is this your son? He stole our dog!", [(1127, 'Это ваш сын'), (1128, 'Он украл нашу собаку')], "'с целью шантажа' dropped for A1 length; explained by the narrator"),
    ("judge", "Собаку? Ты зачем украл собаку?", "A dog? Why did you steal a dog?", [(1129, 'Собаку')], "'Ты зачем украл собаку?' added as Samson turns to Slavik"),
    ("judge", "Дядя Аркаша попросил?! Отдай собаку!", "Uncle Arkasha asked you?! Give back the dog!", [(1130, 'дядя Аркаша попросил'), (1134, 'Отдай собаку')], "Samson repeats Slavik's excuse (cue 1130) in disbelief; 'дебил' (1131) dropped"),
    ("judge", "Между прочим, я председатель суда.", "For your information, I am the chairman of the court.", [(1133, 'Между прочим, я председатель суда')], ""),
    ("judge", "Скажите спасибо, что собака нашлась.", "Say thank you that the dog was found.", [(1138, 'скажите спасибо, что собака нашлась')], ""),
    ("judge", "А то бы он попал в колонию!", "Otherwise he would have ended up in a colony!", [(1139, 'А то бы'), (1139, 'в колонию')], "'ты мигом загремел в колонию для несовершеннолетних' -> 'он попал в колонию'"),
    ("judge", "А вообще-то я ещё не решил. Пошли!", "Actually, I haven't decided yet. Let's go!", [(1140, 'А вообще-то я еще не решил'), (1142, 'пошли')], ""),
    ("anya", "Что, Ваня?", "What's up, Vanya?", [(1143, 'Вань')], "'Че, Вань?' -> 'Что, Ваня?'"),
    ("judge", "Ты решил из моего сына уголовника сделать?", "Did you decide to make my son a criminal?", [(1144, 'решил из моего сына уголовника сделать')], "'Ты че' -> 'Ты'"),
    ("anya", "Не понял.", "I don't understand.", [(1145, 'Не понял')], ""),
    ("judge", "Что ты не понял? Что ты делал?!", "What did you not understand? What were you doing?!", [(1146, 'ты не понял'), (1148, 'делал')], "'Че' -> 'Что'"),
    ("anya", "Ваня, послушай! Послушай меня!", "Vanya, listen! Listen to me!", [(1149, 'Послушай'), (1150, 'Послушай')], "'Ваня' and 'меня' added around cues 1149-1150"),
]
OPENER = "Let's walk through it slowly. Polina has just pointed at Slavik, and Judge Berg demands his dog."
WALK = [
    (0, None, "'Where's the dog? Where is our Lyutik?' Putting the word for 'where' after 'dog' makes the question sound sharp and urgent. Samson has no idea why this stranger is in their corridor."),
    (1, None, "'Right, Slavik, who is this? What happened?' The verb 'happened' has the neuter past ending because 'what' is grammatically neuter. Judge Berg answers for the boy."),
    (2, 'Это ваш сын?', "'Is this your son?' He uses the polite plural 'your' with the parents."),
    (2, 'Он украл нашу собаку!', "'He stole our dog!' The noun for 'dog' and the word for 'our' both change their '-a' ending to '-u' as the direct object. In the show Berg adds that it was for blackmail. Samson stares at his son."),
    (3, None, "'A dog? Why did you steal a dog?' Repeating 'dog' in the object case means 'what do you mean, a dog?'. Frightened Slavik blurts out that Uncle Arkasha asked him to, and he didn't do it on purpose. Samson can hardly believe his ears."),
    (4, 'Дядя Аркаша попросил?!', "'Uncle Arkasha asked you?!' Children in Russia call grown-up family friends 'Uncle' or 'Aunt' plus their short first name."),
    (4, 'Отдай собаку!', "'Give back the dog!' Samson gives Slavik a cuff on the head and tells him to hand the little dog over right now. Polina hugs her beloved Lyutik, and Judge Berg draws himself up."),
    (5, None, "'For your information, I am the chairman of the court.' The first two words literally mean 'between other things', the everyday idiom for 'by the way' or 'for your information'. After 'chairman', 'court' takes the 'of' ending. And he gives them a warning."),
    (6, None, "'Say thank you that the dog was found.' The verb 'was found' is literally 'found itself', with the self-action verb form at the back. Otherwise, things would have been much worse for Slavik."),
    (7, None, "'Otherwise he would have ended up in a colony!' The two little words at the start mean 'or else', and the particle after them makes it 'would have'. By a 'colony', he means a juvenile detention colony."),
    (8, None, "'Actually, I haven't decided yet. Let's go!' The last word is literally 'went' in the plural past, which Russians use as a brisk 'let's go!'. Berg and Polina leave with Lyutik, and Samson slowly walks into Arkady's room."),
    (9, None, "'What's up, Vanya?' Arkady is still sitting at the table, not yet realising what just happened in the hall. Samson's voice is dangerously quiet."),
    (10, None, "'Did you decide to make my son a criminal?' Literally, 'to make a criminal out of my son'. Both 'my son' after 'out of' and 'criminal' as the animate object take the '-a' ending. Arkady blinks."),
    (11, None, "'I don't understand.' Literally, 'I didn't understand', in the masculine past tense. That is the last straw for Samson."),
    (12, None, "'What did you not understand? What were you doing?!' He steps right up to Arkady, furious that Arkady dragged little Slavik into stealing a judge's dog. Arkady backs away."),
    (13, None, "'Vanya, listen! Listen to me!' Two urgent commands from the single-action form 'to listen'. But Samson doesn't listen."),
]
TRANSITION = "Let's hear the whole scene once more, from the beginning."
OUTRO = "Samson swings a punch, and everything goes black. A moment later, a paramedic is bending over Arkady on the floor, asking if he can hear and telling him not to move. That cliffhanger ends Episode 3, followed by the closing song about how much money it takes to be happy. Great work, and see you in Episode 4. See you next time!"
CLOSING = ("anya", "Пока!")
