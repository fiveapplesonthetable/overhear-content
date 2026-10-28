# Authoring module for dix-pour-cent-s01e01-scene-03.
ID = 'dix-pour-cent-s01e01-scene-03'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 3
TITLE = 'Je veux juste voir Mathias  (I Just Want to See Mathias)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'sofia': 'Sofia'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "Now a stranger walks in. Camille is in her early twenties, new to Paris from the south of France, and she goes straight to the reception desk, where Sofia is juggling the phones. She wants to see Mathias, and she has no appointment. First the whole thing in French; you don't need to catch every word."
OPENER = "Let's walk through it. When Camille arrives, Sofia is still on the phone, offering somebody two possible meeting times."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "You've just learned how to ask for someone at a front desk, and how to say you only want one thing. See you next time!"
CLOSING = ('camille', 'Merci, au revoir!')
STORY = [
    ('sofia', 'Soit jeudi à quatorze heures, soit vendredi à onze heures.', 'Either Thursday at two, or Friday at eleven.', [(106, 'Soit jeudi à quatorze heures'), (107, 'soit vendredi à onze heures')], ''),
    ('camille', 'Bonjour.', 'Hello.', [(108, 'Bonjour')], ''),
    ('sofia', 'Bonjour. Je peux vous aider?', 'Hello. Can I help you?', [(108, 'Bonjour')], ''),
    ('camille', 'Je suis là pour voir Mathias Barneville.', 'I', [(109, 'Je suis là pour voir Mathias Barneville')], ''),
    ('sofia', 'Il vous attend?', 'Is he expecting you?', [(110, 'Il vous attend ?')], ''),
    ('camille', "Non, mais c'est important.", 'No, but it', [(111, "Non, mais c'est important")], ''),
    ('sofia', 'Laissez vos photos et votre CV ici.', 'Leave your photos and your CV here.', [(112, 'Laissez vos photos et votre CV ici')], ''),
    ('sofia', 'Cette agence ne représente que des stars.', 'This agency only represents stars.', [(113, 'cette agence ne représente que des stars')], ''),
    ('camille', 'Je ne suis pas actrice. Je veux juste voir Mathias.', "I'm not an actress. I just want to see Mathias.", [(115, 'Je ne suis pas actrice. Je veux juste voir Mathias')], ''),
    ('sofia', 'Votre nom?', 'Your name?', [(116, 'Votre nom ?')], ''),
    ('camille', 'Camille Valentini. Il me connaît.', 'Camille Valentini. He knows me.', [(117, 'Camille Valentini'), (118, 'Il me connaît')], ''),
    ('sofia', 'Sans rendez-vous? Je ne promets rien.', 'Without an appointment? I', [(119, 'sans rendez-vous'), (120, 'Je ne promets rien')], ''),
    ('sofia', 'Asseyez-vous.', 'Have a seat.', [(120, 'Asseyez-vous')], ''),
    ('camille', 'Merci.', 'Thank you.', [], ''),
    ('sofia', 'Mathias, Camille Valentini est là. Désolée de vous déranger.', 'Mathias, Camille Valentini is here. Sorry to bother you.', [(121, 'Mathias, Camille Valentini est là'), (122, 'Désolée de vous déranger')], ''),
]
WALK = [
    (0, None, "'Either Thursday at two, or Friday at eleven.' The same little word, said twice, gives you 'either, or'. And two in the afternoon is fourteen hours again, office style."),
    (1, None, "'Hello.' Camille waits politely for her turn."),
    (2, 'Je peux vous aider?', "'Can I help you?' Sofia uses the formal 'you', the right choice with a stranger at a front desk."),
    (3, None, "'I'm here to see Mathias Barneville.' The little word meaning 'to' or 'in order to' links 'here' to the plain verb 'to see'. Camille uses his full name, like a visitor would."),
    (4, None, "'Is he expecting you?' Literally 'he waits for you'. The formal 'you' sits before the verb."),
    (5, None, "'No, but it's important.' Short and firm. Sofia has seen this many times before."),
    (6, None, "'Leave your photos and your CV here.' A polite command, with the formal ending. She is sure Camille is one more young actress hoping to be discovered."),
    (7, None, "'This agency only represents stars.' Here's a neat trick: the negative pair is used with a different second word, and the meaning becomes 'only'. Nothing but stars."),
    (8, 'Je ne suis pas actrice.', "'I'm not an actress.' The ordinary negative this time, wrapped around the verb 'to be'. And with jobs, French drops the word for 'a'."),
    (8, 'Je veux juste voir Mathias.', "'I just want to see Mathias.' Now she uses only his first name, which tells Sofia something."),
    (9, None, "'Your name?' Half a question, all business."),
    (10, 'Il me connaît.', "'He knows me.' The word for 'me' comes before the verb. Sofia is not convinced."),
    (11, None, "'Without an appointment? I'm not promising anything.' The negative again, this time with the word for 'nothing'."),
    (12, None, "'Have a seat.' Literally 'sit yourself down', a polite command you'll hear in any waiting room."),
    (13, None, "'Thank you.' Camille sits down and waits."),
    (14, 'Mathias, Camille Valentini est là.', "'Mathias, Camille Valentini is here.' Sofia rings through to his office."),
    (14, 'Désolée de vous déranger.', "'Sorry to bother you.' Sofia apologises to her boss, so she uses the formal 'you' with him too. And the name works: Mathias agrees to see this young woman with no appointment. Here's the whole scene again. Now listen to the whole conversation one more time."),
]
