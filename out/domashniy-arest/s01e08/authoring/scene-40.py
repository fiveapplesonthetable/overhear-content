# Authoring module for domashniy-arest-s01e08-scene-40.
ID = 'domashniy-arest-s01e08-scene-40'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 8
SCENE = 40
TITLE = 'Срыв дебатов  (Debate Interruption)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'pasha': 'Паша', 'samson': 'Самсон', 'veteran': 'Ветеран'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.08'
SOURCE_FILE = 'sources/domashniy-arest/s01/e08.ru.dual.srt'
INTRO = "At the Sineozersk municipal television studios that evening. The live mayoral debate begins with Samsonov absent, allowing acting mayor Osipenko to address voters alone and denounce Ivan as a coward. Suddenly, Ivan bursts through the stage doors to defend his family, provoking an uproar until an elderly war veteran in the audience stands up. Let's listen to the scene in Russian first."
OPENER = "Let's go through the scene line by line. First, Osipenko addresses the live television cameras."
TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = "Next time, Uncle Mitya takes us back to 1942 to reveal how Ivan's grandfather performed a heroic feat under enemy fire. Superb work following this dramatic debate confrontation. See you next time!"
CLOSING = ('veteran', 'Пока!')
STORY = [
    ('pasha', 'Иван Самсонов испугался и не пришёл.', 'Ivan Samsonov was scared and did not come.', [(892, 'не явился на теледебаты'), (899, 'Он просто струсил')], ''),
    ('pasha', 'Он струсил, как его дед в войну!', 'He lost his nerve, like his grandfather during the war!', [(899, 'как и его родственник в далеком 1942 году')], ''),
    ('samson', 'Пустите меня! Я кандидат в мэры!', 'Let me in! I am a mayoral candidate!', [(901, 'Пусти, я сказал'), (902, 'я кандидат')], ''),
    ('pasha', 'Посмотрите на него, граждане! Это же фашист!', 'Look at him, citizens! This man is a fascist!', [(903, 'кто к нам пожаловал'), (905, 'Здравствуй, полицай'), (913, 'это фашист')], ''),
    ('samson', 'Не трогай моих детей! Они честные люди!', "Don't touch my children! They are honest people!", [(907, 'Ты что, детей моих припутываешь'), (909, 'Какие они тебе враги народа')], ''),
    ('pasha', 'Охрана, немедленно уберите этого хулигана отсюда!', 'Security, remove this hooligan from here immediately!', [(918, 'Уберите это отсюда')], ''),
    ('samson', 'Ты врёшь про меня и мою семью!', 'You are lying about me and my family!', [(911, 'Ты обо мне говоришь, что хочешь')], ''),
    ('veteran', 'А ну-ка, уберите руки от парня!', 'Hey now, take your hands off the young man!', [(930, 'Ну-ка, руки убрали от него')], ''),
    ('pasha', 'Уважаемый ветеран, перед вами внук предателя!', 'Esteemed veteran, before you is the grandson of a traitor!', [(932, 'вот это вот внук полицая')], ''),
    ('veteran', 'Какая разница, кем был его дед?', 'What difference does it make who his grandfather was?', [(935, 'Какая разница, кто у него дед')], ''),
    ('veteran', 'Только фашисты судили людей по крови!', 'Only fascists judged people by their blood!', [(935, 'Это ж фашисты так делали'), (936, 'кровь брали')], ''),
    ('veteran', 'Я воевал с тринадцати лет ради справедливости!', 'I fought from age thirteen for the sake of justice!', [(937, 'Я в 13 лет в партизаны пошел и воевал до 45-го')], ''),
    ('veteran', 'А теперь послушайте правду про его деда.', 'And now listen to the truth about his grandfather.', [(940, 'А теперь о его деде')], ''),
]
WALK = [
    (0, None, "'Ivan Samsonov was scared and did not come.' Osipenko smugly announces to the television cameras that his rival has forfeited."),
    (1, None, "'He lost his nerve, like his grandfather during the war!' The incumbent mayor continues his vicious public character assassination."),
    (2, None, "'Let me in! I am a mayoral candidate!' Ivan bursts through studio security guards, demanding his rightful time on air."),
    (3, None, "'Look at him, citizens! This man is a fascist!' Osipenko points dramatically at Ivan to provoke the live audience."),
    (4, None, "'Don't touch my children! They are honest people!' Ivan is furious that his opponent slandered his family on live television."),
    (5, None, "'Security, remove this hooligan from here immediately!' Osipenko panics and orders the station guards to drag Ivan away."),
    (6, None, "'You are lying about me and my family!' Ivan resists the guards and shouts directly into the television microphones."),
    (7, None, "'Hey now, take your hands off the young man!' An elderly wartime veteran rises from the audience with authority."),
    (8, None, "'Esteemed veteran, before you is the grandson of a traitor!' Osipenko attempts to justify his hostility to the decorated elder."),
    (9, None, "'What difference does it make who his grandfather was?' The veteran sternly rejects holding children accountable for ancestors."),
    (10, None, "'Only fascists judged people by their blood!' The old partisan draws a sharp moral parallel to wartime Nazi persecution."),
    (11, None, "'I fought from age thirteen for the sake of justice!' Uncle Mitya reminds the audience of his genuine sacrifices in the war."),
    (12, None, "'And now listen to the truth about his grandfather.' The veteran prepares to share a crucial wartime secret with the public."),
]
