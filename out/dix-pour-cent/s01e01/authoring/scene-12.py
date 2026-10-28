# Authoring module for dix-pour-cent-s01e01-scene-12.
ID = 'dix-pour-cent-s01e01-scene-12'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "J'ai encore un agent?  (Do I Still Have an Agent?)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "cecile": "emilie", "gabriel": "theo", "herve": "marcel"}
LABELS = {"cecile": "Cécile", "gabriel": "Gabriel", "herve": "Hervé"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = "He has been dodging her calls all morning. So Cécile has decided to come in person. She walks onto the agents' floor, looks for Gabriel's assistant Hervé, and asks a rather awkward question. Gabriel, meanwhile, would love to be anywhere else. First the French version. Don't try to catch everything; the shape of it is enough. Let's listen to the scene in French first."
OPENER = "Let's walk through it. Cécile arrives and tells the room why she's here, with a handy way of saying what you've come for."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = "Nicely done. Next time someone tells you they have to take an urgent call, you'll know exactly what to think. See you soon for what happens next."
CLOSING = ("cecile", "À tout à l'heure!")
STORY = [
    ('cecile', 'Bonjour. Je suis là pour voir Gabriel.', "Hello. I'm here to see Gabriel.", [(400, 'Je suis là pour voir')], ''),
    ('herve', 'Pas maintenant!', 'Not now!', [(402, 'Pas maintenant')], ''),
    ('cecile', 'Hervé! Hervé!', 'Hervé! Hervé! (she calls him, louder)', [(403, 'Hervé'), (404, 'Hervé')], ''),
    ('herve', 'Oh! Bonjour, Cécile.', 'Oh! Hello, Cécile.', [(405, 'Bonjour, Cécile')], ''),
    ('cecile', "J'ai encore un agent ici?", 'Do I still have an agent here?', [(406, "J'ai encore un agent ici")], ''),
    ('herve', 'Oui, pourquoi?', 'Yes, why?', [(406, 'Oui, pourquoi')], ''),
    ('cecile', "C'est peut-être dans ma tête.", 'Maybe it', [(407, "C'est peut-être dans ma tête")], ''),
    ('cecile', "Mais j'ai l'impression que Gabriel m'évite.", 'But I have the feeling Gabriel is avoiding me.', [(407, "mais j'ai l'impression que Gabriel m'évite")], ''),
    ('gabriel', 'Il est une heure. Je vais déjeuner.', "It's one o'clock. I'm going to lunch.", [(409, 'Il est une heure, je vais déjeuner')], ''),
    ('gabriel', 'Sofia, tu veux venir avec moi?', 'Sofia, do you want to come with me?', [(410, 'Tu veux')], ''),
    ('cecile', "Gabriel? Qu'est-ce qui se passe ici?", 'Gabriel? What', [(413, "Qu'est-ce qui se passe ici")], ''),
    ('gabriel', "Je suis désolé. Je dois répondre, c'est urgent.", "I'm sorry. I have to answer, it's urgent.", [(414, 'Je suis désolé'), (415, "Je dois répondre, c'est urgent")], ''),
    ('gabriel', "Oui, allô? Ça fait des mois que j'attends ton appel!", "Yes, hello? I've been waiting for your call for months!", [(416, 'Oui, allô'), (419, "Ça fait des mois que j'attends ton appel")], ''),
    ('cecile', 'Un appel urgent? Vraiment?', 'An urgent call? Really?', [], ''),
    ('herve', 'Il a beaucoup de travail, Cécile.', 'He has a lot of work, Cécile.', [], ''),
    ('cecile', 'Bon. Alors, je vais attendre.', 'Fine. Then I', [], ''),
]
WALK = [
    (0, None, "'I'm here to see Gabriel.' Word for word: I am there, to see Gabriel. The French often say 'there' when they mean 'here'. Hervé is buried in his work and doesn't even look up."),
    (1, None, "'Not now!' Two words, and no verb at all. He has no idea who he's talking to. So she calls him again."),
    (2, None, "'Hervé! Hervé! (she calls him, louder)' Just his name, twice, a little louder. And this time he looks up."),
    (3, None, "'Oh! Hello, Cécile.' He uses her first name: in this world, agents and stars are on first-name terms. Then comes her question."),
    (4, None, "'Do I still have an agent here?' The word in the middle means 'still', and it's what makes the question sting. Notice the question is just a statement with a rising voice; no special word order needed."),
    (5, None, "'Yes, why?' Hervé plays innocent, as if he had no idea. So Cécile explains, carefully."),
    (6, None, "'Maybe it's all in my head.' Literally 'it's perhaps in my head'. The word for 'maybe' sits right after the verb."),
    (7, None, "'But I have the feeling Gabriel is avoiding me.' French says 'I have the impression that' for 'I feel that'. And just then Gabriel walks past, very busy all of a sudden."),
    (8, None, "'It's one o'clock.' For the time, French says 'it is one hour'."),
    (9, None, "'I'm going to lunch.' Here's a pattern you'll use every day: the verb 'to go' plus another verb in its basic form talks about what you're about to do. I'm going to eat lunch."),
    (10, None, "'Sofia, do you want to come with me?' He asks Sofia, the receptionist, using the casual 'you'. She happily accepts, and the two of them head for the door. But Cécile isn't fooled."),
    (11, None, "'Gabriel? What's going on here?' A very useful question whenever something feels odd. Gabriel grabs his phone."),
    (12, None, "'I'm sorry.' He's a man, so the word for 'sorry' is in its masculine form. A woman writes it with an extra letter at the end."),
    (13, None, "'I have to answer, it's urgent.' Another verb plus a basic-form verb: I must, then 'answer'. And he starts talking to someone, or perhaps to no one."),
    (14, None, "'Yes, hello?' This greeting is only used on the phone."),
    (15, None, "'I've been waiting for your call for months!' Literally 'it makes months that I wait for your call'. A bit much, for a call that may not exist."),
    (16, None, "'An urgent call? Really?' Cécile has seen this act before."),
    (17, None, "'He has a lot of work, Cécile.' Loyal Hervé covers for his boss. The phrase for 'a lot of' is followed by a small word meaning 'of', just like in English."),
    (18, None, "'Fine. Then I'll wait.' The 'go plus verb' pattern once more: I'm going to wait. Cécile isn't going anywhere. Right, here's the whole scene again, a little faster. Now let's hear the full exchange again from beginning to end."),
]
