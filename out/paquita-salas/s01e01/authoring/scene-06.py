ID = 'paquita-salas-s01e01-scene-06'
SHOW = 'paquita-salas'
SEASON = 1
EPISODE = 1
SCENE = 6
TITLE = 'Como bebo yo, bebemos todos  (If I Drink, Everyone Drinks)'
LEVEL = 'A1 — beginner'
PAIR = 'es-en'
LABELS = {'paquita': 'Paquita', 'lidia': 'Lidia'}
SOURCE_NAME = 'Paquita Salas S01E01: Casada con esto'
SOURCE_FILE = 'sources/paquita-salas/s01/e01.es.srt'
SOURCE_NOTE = 'Window 00:05:14,760–00:06:17,720.'
INTRO = ("Paquita boasts about her five-year marriage top Spanish film producer Paco Cerdeña and all the cinema figures who have dined at her flat. "
         "Seeing Magüi tense before the wedding, Paquita pours shots for everyone and refuses to let teetotaller Lidia sit out the toast. "
         "Listen to the Spanish first.")
OPENER = "Let's go through Paquita's stories and her toast."
TRANSITION = "Now let's listen to the whole scene again."
OUTRO = ("You heard all three singular and plural 'drink' forms side by side, plus casual commands for one listener and for a group. See you next time.")
CLOSING = ('paquita', '¡Hasta pronto!')

STORY = [
    ('paquita', 'Paco Cerdeña es mi ex, un productor muy importante del cine español.',
     'Paco Cerdeña is my ex, a very important Spanish film producer.',
     [(113, 'Paco Cerdeña es mi ex'), (113, 'Un productor muy importante'), (114, 'del cine español')], ''),
    ('paquita', 'Estuvimos casados cinco años.',
     'We were married for five years.',
     [(114, 'Estuvimos casados cinco años')], ''),
    ('paquita', 'Imagínate los contactos que tengo en el mundo del cine.',
     'Imagine the contacts I have in the film world.',
     [(115, 'Imagínate'), (115, 'contactos que tengo en el mundo del cine')],
     'Replaced colloquial la de with los for A1 clarity.'),
    ('paquita', 'Han cenado en mi casa y se quedaron a dormir.',
     "They've had dinner at my house and stayed over to sleep.",
     [(116, 'en mi casa'), (117, 'Han cenado y se quedaron a dormir')], ''),
    ('paquita', 'Dime un nombre y te digo una anécdota.',
     "Give me a name and I'll tell you a story.",
     [(118, 'Dime un nombre y te digo'), (118, 'anécdota')],
     'Added indefinite article una.'),
    ('paquita', 'Estás un poco tensa, ¿eh?',
     "You're a bit tense, aren't you?",
     [(127, 'estás un poco tensa, ¿eh?')], ''),
    ('paquita', 'Un chupito para soltarte. Venga, relaja.',
     'A shot to loosen you up. Come on, relax.',
     [(128, 'Un chupito para soltarte. Venga, relaja')], ''),
    ('paquita', '¿Quieres un chupito, Lidia?',
     'Do you want a shot, Lidia?',
     [(129, 'chupito'), (129, '¿Quieres'), (129, 'Lidia?')], ''),
    ('lidia', 'Yo paso. Yo no bebo, Paquita.',
     "I'll pass. I don't drink, Paquita.",
     [(130, 'Yo paso. Yo no bebo, Paquita')], ''),
    ('paquita', 'Tú sí bebes.',
     'You do drink.',
     [(131, 'Tú sí bebes')], ''),
    ('lidia', 'Yo no bebo.',
     "I don't drink.",
     [(131, 'Yo no bebo')], ''),
    ('paquita', 'Como bebo yo, bebemos todos.',
     "Since I'm drinking, we all drink.",
     [(132, 'Como bebo yo'), (133, 'bebemos todos')], ''),
    ('paquita', 'Pero brinda. Venga, sonreíd.',
     'At least toast. Come on, smile.',
     [(134, 'Pero brinda'), (135, 'Venga, sonreíd')], ''),
    ('paquita', 'Guapísimas. Me encanta.',
     'Gorgeous, all of you. I love it.',
     [(136, 'Guapísimas. Me encanta')], '')
]

WALK = [
    (0, None, "'Paco Cerdeña is my ex, a very important Spanish film producer.' Notice how Spanish reverses the English noun pile-up at the end: literally producer very important of the cinema Spanish, with nationality uncapitalised."),
    (1, None, "'We were married for five years.' Spanish needs no word for before the five years, and uses the completed past form because the marriage is firmly over."),
    (2, None, "'Imagine the contacts I have in the film world.' Casual you tacks onto imagine as one word. Unlike English, Spanish never drops the linking word for that between contacts and I have."),
    (3, None, "'They've had dinner at my house and stayed over to sleep.' Spanish has a dedicated single action word for eating dinner, rather than saying have dinner. In the second half, stayed adds a little word for themselves before to sleep."),
    (4, None, "'Give me a name and I'll tell you a story.' Literally, tell me a name and to you I tell an anecdote, using simple present forms for an immediate challenge."),
    (5, None, "'You're a bit tense, aren't you?' Because Paquita is speaking to Magüi, the word for tense ends in a feminine vowel. The little tag at the end works like right or aren't you."),
    (6, None, "'A shot to loosen you up. Come on, relax.' Spain's cute diminutive word for a small shot glass of spirits comes from sucking or sipping. After for, to loosen tacks you onto its end."),
    (7, None, "'Do you want a shot, Lidia?' Earlier we heard this same word mean loves when talking about a person; with a thing like a drink, it simply means want."),
    (8, None, "'I'll pass. I don't drink, Paquita.' Saying I pass works just like English I'll pass when turning down an offer. Repeating the word for I before don't drink makes Lidia's refusal firm and clear."),
    (9, None, "'You do drink.' Putting the word for yes right before you drink works just like stressing do in English when contradicting someone: yes you do drink."),
    (10, None, "'I don't drink.' Lidia mirrors Paquita's rhythm word for word, swapping casual you for I and replacing yes with no."),
    (11, None, "'Since I'm drinking, we all drink.' When that opening word leads a sentence, it means since or as rather than like. Putting I after drink adds bossy emphasis before switching to the we ending."),
    (12, None, "'At least toast. Come on, smile.' Look at the two casual command endings side by side: the first speaks to Lidia alone, while the final d ending addresses both women in the Castilian group command."),
    (13, None, "'Gorgeous, all of you. I love it.' The feminine plural ending on gorgeous praises both women at once. Then I love it literally says it enchants me.")
]
