# Authoring module for domashniy-arest-s01e03-scene-30.
ID = 'domashniy-arest-s01e03-scene-30'
SHOW = 'domashniy-arest'
SEASON = 1
EPISODE = 3
SCENE = 30
TITLE = 'Жучок работает!  (The Bug Works!)'
LEVEL = 'A1 — Duolingo Section 2'
PAIR = 'ru-en'
LABELS = {'arkady': 'Аркадий', 'marina': 'Марина', 'zavarzin': 'Заварзин'}
SOURCE_NAME = 'Домашний арест (Domashniy Arest) S1.03'
SOURCE_FILE = 'sources/domashniy-arest/s01/e03.ru.dual.srt'
INTRO = "Back at the communal flat a couple of hours earlier. Last time, in court, Arkady's public defender Golovkin walked in as a surprise witness for the prosecution. Now the show flashes back to earlier that afternoon, while Arkady was still tied to the chair in his room before leaving for court. Marina slips into his room with the hidden microphone. Let's listen in Russian first."
OPENER = "Let's go through it line by line. Marina opens the door of Arkady's room and is surprised to find him tied up."
TRANSITION = "Now let's hear the whole scene once more, from start to finish."
OUTRO = 'So Marina managed to plant the bug while untying Arkady, and the listening post heard every word in the flat. Next we check in on Slavik and Lyolya at the party before returning to court. See you then. See you next time!'
CLOSING = ('zavarzin', 'Пока!')
STORY = [
    ('marina', 'Извините.', 'Excuse me.', [(1023, 'Извините')], "Marina enters Arkady's room and finds him tied to the chair"),
    ('arkady', 'Марина! Развяжите меня, пожалуйста.', 'Marina! Please untie me.', [(1024, 'меня, пожалуйста')], "'Марина!' added; 'Разведите' (subtitle typo) -> 'Развяжите'"),
    ('marina', 'Давайте я вас развяжу.', 'Let me untie you.', [(1025, 'Давайте я вас')], "'разовяжу' (subtitle typo) -> 'развяжу'"),
    ('arkady', 'Буду вам очень признателен. А то я устал сидеть.', "I'll be very grateful to you. Because I'm tired of sitting.", [(1026, 'Буду вам очень признателен'), (1027, 'А то')], "'затек совсем' -> 'я устал сидеть' (A1)"),
    ('marina', 'Да оставайтесь сзади лучше.', 'Just stay leaning back.', [(1029, 'Да оставайтесь сзади лучше')], ''),
    ('arkady', 'О, спасибо! И ноги, ноги.', 'Oh, thank you! And my legs, my legs.', [(1031, 'О, спасибо'), (1032, 'Ноги, ноги')], "'И' added; third 'ноги' dropped"),
    ('marina', 'Сейчас, сейчас.', 'Just a moment, just a moment.', [(1033, 'Сейчас, сейчас')], 'while bending down to untie his legs, she secretly sticks the bug in place'),
    ('arkady', 'Ой!', 'Ouch!', [(1034, 'Ой')], ''),
    ('marina', 'У вас упало это.', 'You dropped this.', [(1035, 'У вас упало это')], 'she hands him the empty foil wrapper as a cover'),
    ('arkady', 'Да? Ну, я понял.', 'Really? Well, I see.', [(1022, 'Да'), (1037, 'Ну, я понял')], ''),
    ('zavarzin', 'О, заработала!', "Oh, it's working!", [(1039, 'О, заработала')], 'at the listening post, the bug turns on when Klavdia walks into the room'),
    ('zavarzin', 'Ну вот! А ты говоришь — старушка!', 'There you go! And you called her an old lady!', [(1040, 'Ну вот, а ты говоришь')], "'бабка' -> 'старушка'; split into two short sentences"),
    ('zavarzin', 'Ладно, звони в свою пиццу. Заказывай!', 'All right, call your pizza place. Go ahead and order!', [(1041, 'Ладно, звони в свою пиццу'), (1042, 'Заказывай')], "Lavrov's reply folded into Zavarzin's role for the three-voice limit"),
]
WALK = [
    (0, None, "'Excuse me.' She uses the polite plural command form as she steps inside. Arkady is delighted to see anyone who can untie him."),
    (1, None, "'Marina! Please untie me.' He also uses the polite plural command form with his neighbour. Marina steps behind his chair."),
    (2, None, "'Let me untie you.' The first word, 'let's', followed by 'I will untie you' in the future form, is the natural Russian way to offer 'let me do that for you'."),
    (3, 'Буду вам очень признателен.', "'I'll be very grateful to you.' The word for 'grateful' is in the short masculine form, because Arkady is a man, and 'to you' is in the 'to/for' form."),
    (3, 'А то я устал сидеть.', "'Because I'm tired of sitting.' The two small words at the start mean 'otherwise' or 'because', and 'got tired' is masculine past form followed by the dictionary form 'to sit'. Marina needs him not to turn around while she takes out the microphone."),
    (4, None, "'Just stay leaning back.' Literally, 'stay behind better', telling him to keep his back to her. Once his hands are free, he points down."),
    (5, None, "'Oh, thank you! And my legs, my legs.' The word for 'legs' or 'feet' is plural here. Marina crouches down."),
    (6, None, "'Just a moment, just a moment.' Repeating the word for 'now' means 'one second, coming right up'. While she is down there, she sticks the tiny bug onto the furniture."),
    (7, None, "'Ouch!' A short exclamation as the rope comes off. Then Marina holds up the little foil packet she used to hide the microphone."),
    (8, None, "'You dropped this.' Literally, 'at you fell this', with the action word in the neuter past form to match 'this'."),
    (9, None, "'Really? Well, I see.' Literally, 'I understood', in the masculine past form. Arkady hurries off to court, old Klavdia wanders in talking to the little dog, and across the courtyard at the listening post, the microphone finally comes alive."),
    (10, None, "'Oh, it's working!' Literally, 'she started working', in the feminine past form for the piece of equipment."),
    (11, None, "'There you go! And you called her an old lady!' When Klavdia's voice comes through the headphones, the agents hear everything at last. And to celebrate, Major Lavrov finally gives in to Zavarzin's wish, heard here in Zavarzin's voice."),
    (12, None, "'All right, call your pizza place. Go ahead and order!' Both commands are informal singular: 'ring' and 'order'."),
]
