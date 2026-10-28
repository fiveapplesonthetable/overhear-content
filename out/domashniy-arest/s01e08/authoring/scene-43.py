# Authoring module for domashniy-arest-s01e08-scene-43.
ID = 'domashniy-arest-s01e08-scene-43'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 43
TITLE = 'Лёша пошёл  (Lyosha Walks)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'investigator': 'Следователь', 'lyosha': 'Лёша', 'marina': 'Марина'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "Meanwhile at the hospital, the police ask Marina to sign a paper confirming Arkady escaped house arrest to save her son, when young Lyosha suddenly stands up from his bed and starts walking on his own. Let's listen to the scene in Russian first."
OPENER = "Now let's walk through the lines as Lyosha takes his first steps without surgery."
TRANSITION = "Now let's listen to the whole heartwarming scene again from start to finish."
OUTRO = "Thanks to Dr. Tenenbaum's timely diagnosis, young Lyosha avoids dangerous joint surgery and takes his very first steps in the hospital corridor. See you next time!"
CLOSING = ('lyosha', 'Пока!')
STORY = [
    ('investigator', 'Вы подтверждаете слова Аникеева?', "Do you confirm Anikeyev's words?", [(989, 'Вы подтверждаете его слова')], "'его слова' -> 'слова Аникеева'"),
    ('marina', 'Да, он сбежал, чтобы спасти моего ребёнка.', 'Yes, he escaped custody to save my child.', [(992, 'Да, он сбежал из-под ареста, чтобы спасти моего ребенка')], "'из-под ареста' shortened"),
    ('investigator', 'Тогда подпишитесь здесь внизу.', 'Then sign here at the bottom.', [(994, 'Тогда подпишитесь здесь внизу')], ''),
    ('investigator', 'И на второй странице тоже.', 'And on the second page as well.', [(995, 'И на второй странице тоже')], ''),
    ('marina', 'Спасибо, я всё подписала.', 'Thank you, I have signed everything.', [(996, 'Спасибо')], "'я всё подписала' added"),
    ('lyosha', 'Мама, смотри на меня!', 'Mom, look at me!', [(997, 'Мам, смотри')], "'на меня' added"),
    ('lyosha', 'Я сам иду без палочек!', 'I am walking by myself without crutches!', [(999, 'Прихожу')], "'Прихожу' corrected to clean speech"),
    ('marina', 'Ты молодец, сынок! Так ты ходишь!', "Good boy, son! You're actually walking!", [(998, 'ты молодец'), (1001, 'Так ты ходишь')], "'А ты молодец' -> 'Ты молодец, сынок'"),
    ('marina', 'Ты только смотри, осторожно!', 'Just watch out, be careful!', [(1002, 'Ты смотри')], "'осторожно' added"),
    ('lyosha', 'Смотри, я могу стоять!', 'Look, I can stand!', [], 'context line'),
    ('marina', 'Молодец! Но доктор сказал ходить по чуть-чуть.', 'Good boy! But the doctor said to walk just a little at a time.', [(1003, 'Молодец'), (1004, 'доктор сказал, по чуть-чуть')], "'пузырь' omitted"),
    ('marina', 'Идём в палату, ложись спать.', "Let's go into the ward, go to bed.", [(1005, 'Идем'), (1007, 'Ложись спать')], "'в палату' added"),
    ('lyosha', 'Хорошо, мамочка. Я быстро лягу.', 'Alright, mommy. I will lie down quickly.', [(1009, 'А я сейчас')], 'A1 dialogue'),
]
WALK = [
    (0, None, "'Do you confirm Anikeyev's words?' The police investigator asks Marina to give an official statement about Arkady's escape."),
    (1, None, "'Yes, he escaped custody to save my child.' Marina confirms that Arkady broke house arrest solely to stop the unnecessary surgery."),
    (2, None, "'Then sign here at the bottom.' The officer points to the signature line on the official document."),
    (3, None, "'And on the second page as well.' The investigator flips the sheet over and points to a second spot that needs her signature."),
    (4, None, "'Thank you, I have signed everything.' Marina hands the clipboard back to the officers so they can leave."),
    (5, None, "'Mom, look at me!' Suddenly young Lyosha calls out happily from across the hospital corridor."),
    (6, None, "'I am walking by myself without crutches!' The boy steps forward without his forearm crutches for the first time in years."),
    (7, 'Ты молодец, сынок!', "'Good boy, son!' Marina gasps in joy as tears fill her eyes."),
    (7, 'Так ты ходишь!', "'You're actually walking!' The little word 'tak' at the start captures Marina's stunned disbelief: you're really walking!"),
    (8, None, "'Just watch out, be careful!' Marina rushes over to steady him in case he loses his balance."),
    (9, None, "'Look, I can stand!' Lyosha proudly balances on both feet without any support."),
    (10, None, "'Good boy! But the doctor said to walk just a little at a time.' The Moscow specialist Dr. Tenenbaum warned against overexerting his legs on the first day."),
    (11, None, "'Let's go into the ward, go to bed.' Marina gently leads her happy son back to his bed to rest."),
    (12, None, "'Alright, mommy. I will lie down quickly.' Lyosha smiles and settles under the warm blanket."),
]
