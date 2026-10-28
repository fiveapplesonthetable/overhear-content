# Authoring module for dix-pour-cent-s01e02-scene-03.
ID = 'dix-pour-cent-s01e02-scene-03'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 2
SCENE = 3
TITLE = "La chaise de Samuel  (Samuel's Chair)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E02'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e02.fr.dual.srt'
INTRO = "The phones won't stop: the funeral is on Thursday at Père-Lachaise, and half of Paris wants to come, some to be seen. Then Mathias walks in and sits down in Samuel's chair. Andréa, who still has to tell everyone about her disastrous morning with Françoise Fabian, is not amused. First in French; don't try to catch everything."
OPENER = "Let's go through it. Mathias has settled into the chair at the head of the table, and Andréa says what everyone is thinking."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Two agents fighting over a chair and a client, all in the polite 'you'. Don't worry about every detail; you've got the shape of it. See you next time!"
CLOSING = ('andrea', 'Au revoir!')
STORY = [
    ('andrea', 'Ça me dérange de vous voir assis là.', 'It bothers me to see you sitting there.', [(97, 'Ça me dérange, de vous voir assis là')], ''),
    ('mathias', "C'est une chaise.", 'It', [(99, "C'est une chaise")], ''),
    ('andrea', "Non, c'est la place de Samuel. Il vient de mourir.", 'No, that is Samuel', [(100, "Non, c'est la place de Samuel. Il est mort il y a six jours")], ''),
    ('mathias', 'Ne perdons pas de temps sur les détails.', 'Let', [(106, 'Ne perdons pas de temps sur les détails')], ''),
    ('mathias', 'Nous avons des problèmes urgents. À commencer par les clients de Samuel.', "We have urgent problems. Starting with Samuel's clients.", [(107, 'Nous avons des problèmes urgents'), (108, 'À commencer par les clients de Samuel')], ''),
    ('mathias', 'Si ça se sait, ils vont partir.', 'If word gets out, they', [(119, 'Si ça se sait, ils vont partir')], ''),
    ('mathias', 'Voici ce que je propose.', 'Here', [(121, 'Voici ce que je propose')], ''),
    ('andrea', 'Un tableau Excel avec ce que gagne chaque personne?', 'A spreadsheet with what each person earns?', [(123, 'Un tableau Excel avec ce que gagne chaque personne ?')], ''),
    ('mathias', 'Exactement.', 'Exactly.', [(124, 'Exactement')], ''),
    ('andrea', "Vous voulez Françoise Fabian? Je l'ai vue ce matin.", 'You want Françoise Fabian? I saw her this morning.', [(129, "Vous voulez Françoise Fabian ? Je l'ai vue ce matin")], ''),
    ('mathias', "Vous l'avez approchée?", 'You approached her?', [(130, "Vous l'avez approchée")], ''),
    ('andrea', "Non! C'est elle qui a demandé à me voir.", 'No! She', [(131, 'Non'), (132, "C'est elle qui a demandé à me voir")], ''),
    ('mathias', 'Elle vous veut?', 'She wants you?', [(133, 'Elle vous veut ?')], ''),
    ('andrea', "Oui. Enfin, c'est compliqué.", 'Yes. Well, it', [(134, 'Oui'), (135, "Enfin, c'est compliqué")], ''),
    ('andrea', "Elle dit qu'elle ne veut pas faire le film de Gabor.", 'She says she doesn', [(136, "dit qu'elle ne veut pas faire le film de Gabor")], ''),
    ('mathias', "Je vais l'appeler.", 'I', [(137, "Je vais l'appeler")], ''),
    ('andrea', "Non, Mathias, c'est moi qui gère!", 'No, Mathias, I', [(138, "Non, Mathias, c'est moi qui gère")], ''),
    ('mathias', "Réglez ça en vingt-quatre heures ou j'interviens!", 'Sort it out in twenty-four hours or I step in!', [(144, "Réglez ça en 24 heures ou j'interviens")], ''),
]
WALK = [
    (0, None, "'It bothers me to see you sitting there.' The little word for 'me' comes before the verb 'to bother'. And here Andréa and Mathias use the polite 'you' with each other, a sign of how cold things are between them."),
    (1, None, "'It's a chair.' Mathias plays innocent."),
    (2, None, "'No, that is Samuel's spot. He just passed away.'s Samuel's place.' To say whose something is, French says 'the place of Samuel'."),
    (3, None, "'He died six days ago.' The phrase that usually means 'there is' also means 'ago' when it comes before a length of time. Someone suggests another seat; Mathias says that one is Camille's, isn't it, Camille? And Camille can only say yes."),
    (3, None, "'Let's not waste time on details.' A 'let's' command, made negative: the two negative words go around the verb."),
    (4, 'Nous avons des problèmes urgents.', "'We have urgent problems.' The adjective comes after the noun, as most French adjectives do."),
    (4, 'À commencer par les clients de Samuel.', "'Starting with Samuel's clients.' Here, Samuel's stars bring in a big share of the agency's money."),
    (5, None, "'If word gets out, they'll leave.' The first part literally means 'if it becomes known'. Then the near future: 'they are going to leave'."),
    (6, None, "'Here's what I suggest.' The first word is how you present something: 'here is'. He hands out a document."),
    (7, None, "'A spreadsheet with what each person earns?' Andréa can't believe it: he has divided up Samuel's clients in a table, with everyone's earnings in it."),
    (8, None, "'Exactly.' Same word as in English, said with complete calm."),
    (9, 'Vous voulez Françoise Fabian?', "'You want Françoise Fabian?' Andréa decides to tell them about her morning."),
    (9, "Je l'ai vue ce matin.", "'I saw her this morning.' The little word for 'her' sits before the verb, and loses its vowel. And because 'her' comes first, the past form of 'to see' takes an extra e on paper. You can't hear it."),
    (10, None, "'You approached her?' Mathias suspects her of stealing a client behind everyone's back."),
    (11, None, "'No! She's the one who asked to see me.' The pattern 'it's her who' puts the stress on 'her'. In the show Andréa also mocks him with a fake German army title."),
    (12, None, "'She wants you?' Mathias can't quite believe it."),
    (13, None, "'Yes. Well, it's complicated.' The second word here is a little hesitation, like 'well' or 'I mean'."),
    (14, None, "'She says she doesn't want to do Gabor's film.' Andréa leaves out the part where she insulted her."),
    (15, None, "'I'll call her.' The near future once more, with the little word for 'her' right before the action word."),
    (16, None, "'No, Mathias, I'm handling it!' Literally 'it's me who manages'. The same pattern as before, to say 'me, not you'."),
    (17, None, "'Sort it out in twenty-four hours or I step in!' A polite command, but a threat all the same. As the meeting breaks up, a colleague tells Andréa she's a legend for what she said to Françoise. A legend of embarrassment, she replies. Let's hear the meeting once more, all the way through."),
]
