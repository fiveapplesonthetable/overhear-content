# Authoring module for dix-pour-cent-s01e04-scene-02.
ID = 'dix-pour-cent-s01e04-scene-02'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 4
SCENE = 2
TITLE = "Les photos de Sofia  (Sofia's Photos)"
LEVEL = "A1 — débutant"
PAIR = 'fr-en'
VOICES = {"narrator": "sky", "gabriel": "theo", "sofia": "emilie", "lea": "lucie"}
LABELS = {"gabriel": "Gabriel", "sofia": "Sofia", "lea": "Andréa"}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E04'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e04.fr.dual.srt'
INTRO = "Back at the agency, Gabriel is keeping the promise he made at the end of the last episode: he has taken on receptionist Sofia as a client. Between phone calls at the front desk, Sofia shows him her new professional headshots. We'll hear it in French first; just listen to the tone of their voices."
OPENER = "Let's go through it line by line. Sofia is answering the agency phone at the reception desk as Gabriel walks in."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = 'As they step out of the lift into the corridor, tax inspector Colette Brancillon politely reminds them about the documents she asked for, and Gabriel and Andréa worry that tax inspectors always find something wrong. See you next time.'
CLOSING = ("gabriel", "À demain!")
STORY = [
    ('sofia', 'ASK, bonjour. Oui, je vous la passe.', 'ASK, hello. Yes, I', [(49, 'ASK, bonjour'), (51, 'Oui, je vous la passe')], ''),
    ('sofia', 'Gabriel! Voilà mes nouvelles photos.', 'Gabriel! Here are my new photos.', [(52, 'Gabriel !'), (53, 'les photos')], ''),
    ('sofia', 'Elles sont en noir et blanc.', 'They', [(55, 'Elles sont en noir et blanc')], ''),
    ('sofia', "Tu crois qu'elles sont bien?", 'Do you think they', [(56, "Tu crois qu'elles sont bien ?")], ''),
    ('gabriel', 'Oui, très bien. Tes photos sont bonnes.', 'Yes, very good. Your photos are good.', [(61, 'Très bien'), (59, 'les photos'), (59, 'bonnes')], ''),
    ('sofia', 'Vraiment?', 'Really?', [(60, 'Vraiment ?')], ''),
    ('gabriel', 'Tu es photogénique.', 'You', [(64, 'Tu es photogénique')], ''),
    ('gabriel', "J'aime le regard dans les yeux, et le sourire aussi.", 'I like the look in your eyes, and the smile too.', [(68, 'Le regard dans les yeux'), (69, 'Le sourire aussi')], ''),
    ('gabriel', 'Enfin, vous êtes belle.', 'Well, you', [(70, 'Enfin, vous êtes belle')], ''),
    ('gabriel', "C'est simple et naturel.", 'It', [(72, "C'est simple"), (72, 'naturel')], ''),
    ('gabriel', "Vous avez de la grâce. Oui, c'est ça, de la grâce.", 'You have grace. Yes, that', [(77, "Vous avez de la grâce. Oui, c'est ça, de la grâce")], ''),
    ('sofia', 'Merci, Gabriel!', 'Thank you, Gabriel!', [(50, 'Merci'), (52, 'Gabriel !')], ''),
    ('gabriel', 'Bon, au travail!', 'Right, back to work!', [(79, 'Bon, au travail !')], ''),
    ('lea', 'Et après Sofia, tu prends aussi la fille de la boulangerie?', 'And after Sofia, are you taking on the girl from the bakery too?', [(81, 'la fille de la boulangerie')], ''),
    ('gabriel', "Elle fera la couverture d'un grand magazine!", 'She', [(82, 'Elle fera la couverture de')], ''),
    ('lea', "Tu es amoureux d'elle, non?", 'You', [(83, 'non ?')], ''),
    ('gabriel', 'Jamais avec mes clientes!', 'Never with my clients!', [(83, 'Jamais avec mes clientes')], ''),
]
WALK = [
    (0, None, "'ASK, hello. Yes, I'll put you through to her.' Literally 'I pass her to you', with both pronouns stacked before the verb."),
    (1, None, "'Gabriel! Here are my new photos.' The word for 'new' is in its feminine plural form to match 'photos', and stands before the noun."),
    (2, None, "'They're in black and white.' Literally 'in black and white', the same order as in English."),
    (3, None, "'Do you think they're good?' Sofia is nervous: she worries you can see her gums too much."),
    (4, None, "'Yes, very good. Your photos are good.' Gabriel reassures her right away."),
    (5, None, "'Really?' One word, asking if he truly means it."),
    (6, None, "'You're photogenic.' The camera loves her, just as he saw on stage at the theatre."),
    (7, None, "'I like the look in your eyes, and the smile too.' French uses 'the eyes' where English says 'your eyes'."),
    (8, None, "'Well, you're beautiful.' Notice how 'well' sets up the clause and leads naturally into 'beautiful'."),
    (9, None, "'It's simple and natural.' Both adjectives stay in the masculine singular after 'it is'."),
    (10, None, "'You have grace. Yes, that's it, grace.' The two words before 'grace' mean 'some', used before an abstract quality."),
    (11, None, "'Thank you, Gabriel!' Sofia is glowing as the lift doors open."),
    (12, None, "'Right, back to work!' Literally 'to the work'. Gabriel hurries into the lift, where Andréa is waiting."),
    (13, None, "'And after Sofia, are you taking on the girl from the bakery too?' Andréa mocks him for signing the agency's receptionist."),
    (14, None, "'She'll be on the cover of a big magazine!' Literally 'she will make the cover', using the future tense of 'to make'."),
    (15, None, "'You're in love with her, aren't you?' In the show Andréa puts it much more bluntly."),
    (16, None, "'Never with my clients!' Notice the feminine plural ending on 'clients': Gabriel has a strict rule. Let's listen to the whole scene once more."),
]
