# Authoring module for dix-pour-cent s03e04 scene 06 (cues 257-287).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e04/authoring/scene-06.py --out out/dix-pour-cent/s03e04/scene-06.json

ID = "dix-pour-cent-s03e04-scene-06"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 4
SCENE = 6
TITLE = "Appel à la maternité  (Call at the Maternity Ward)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "colette": "emilie"}
LABELS = {"lea": "Andréa", "colette": "Colette"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E04"
SOURCE_FILE = "sources/dix-pour-cent/s03/e04.fr.dual.srt"
SOURCE_NOTE = ("Cues 257-287. At the maternity clinic, Andrea takes an urgent call from star client "
               "Fabrice Luchini while Colette urges her to rest and focus on their new baby. Adapted for A1 French.")

INTRO = ("At the maternity clinic, Andrea Martel has just given birth to her baby daughter with her partner Colette by her side. "
         "When prominent client Fabrice Luchini calls her phone, Andrea answers immediately despite the hospital setting. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("colette", "Tu n'es pas obligée de répondre.",
     "You do not have to answer.",
     [(259, "T'es pas obligée de répondre")], "Colette advises Andrea to rest"),
    ("lea", "Je ne veux pas disparaître du jour au lendemain.",
     "I do not want to disappear overnight.",
     [(260, "disparaître du jour au lendemain.")], "Andrea fears losing her agency relevance"),
    ("colette", "Mais si, tu es à la maternité!",
     "Oh yes, you are in the maternity ward!",
     [(261, "Mais si.")], "Colette points out the obvious reality"),
    ("lea", "Je ne peux pas perdre Fabrice!",
     "I cannot afford to lose Fabrice!",
     [(262, "perdre le Kini.")], "Andrea protects her marquee client"),
    ("lea", "Allô Fabrice? Tu vas bien?",
     "Hello Fabrice? Are you doing well?",
     [(263, "Tu vas bien ?")], "Andrea answers her mobile phone"),
    ("lea", "Merci, c'est vraiment très gentil.",
     "Thank you, that is truly very kind.",
     [(264, "c'est gentil.")], "Andrea accepts warm congratulations"),
    ("lea", "Écoute, tout se passe super bien.",
     "Listen, everything is going super well.",
     [(265, "c'est super.")], "Andrea downplays any hospital disruption"),
    ("lea", "La petite fille est vraiment magnifique.",
     "The little girl is truly magnificent.",
     [(266, "La petite est vraiment")], "Andrea praises the newborn daughter"),
    ("lea", "Ne t'inquiète pas du tout.",
     "Do not worry at all.",
     [(272, "t'inquiète pas.")], "Andrea reassures Fabrice regarding work"),
    ("colette", "Andréa, s'il te plaît, raccroche maintenant.",
     "Andrea, please hang up right now.",
     [(258, "je te laisse finir")], "Colette urges her to prioritize family"),
    ("lea", "Fabrice, je peux te rappeler?",
     "Fabrice, can I call you back?",
     [(284, "je peux te rappeler ?")], "Andrea yields to Colette's plea"),
    ("lea", "J'ai un imprévu en ce moment.",
     "I have an unexpected situation right now.",
     [(285, "j'ai un imprévu.")], "Andrea makes up an urgent hospital excuse"),
    ("colette", "Merci, pensons enfin à notre bébé.",
     "Thank you, let's finally think about our baby.",
     [(287, "Non.")], "Colette sighs with deep relief"),
]

OPENER = "Let's explore how Andrea balances client demands with new motherhood line by line."

WALK = [
    (0, None,
     "'You do not have to answer.' Colette gently tells Andrea to ignore her ringing mobile phone. This conversational past tense combines a helper verb with the past participle for 'obliged'."),
    (1, None,
     "'I do not want to disappear overnight.' Andrea insists that she must remain available for top talent. Notice the classic French sandwich negation wrapping right around 'want'."),
    (2, None,
     "'Oh yes, you are in the maternity ward!' Colette reminds her that she just delivered their daughter. The key noun here means 'maternity clinic!', anchored by its matching French article."),
    (3, None,
     "'I cannot afford to lose Fabrice!' Andrea refuses to risk her relationship with star actor Fabrice Luchini. The two-part French negation brackets the verb for 'can' on both sides."),
    (4, None,
     "'Hello Fabrice? Are you doing well?' Andrea answers her client with energetic professional cheer. In everyday spoken French, rising intonation on 'are going' at the end is enough to turn the sentence into a question."),
    (5, None,
     "'Thank you, that is truly very kind.' Andrea warmly receives Fabrice's congratulations on the newborn baby. In spoken French, the little word before 'it is' drops its final vowel and attaches with an apostrophe."),
    (6, None,
     "'Listen, everything is going super well.' Andrea assures him that motherhood will not disrupt their work. The reflexive pronoun sits right in front of the verb for 'listen', turning the action back onto the subject."),
    (7, None,
     "'The little girl is truly magnificent.' Andrea shares a tender description of their newborn infant. The key noun here means 'girl', anchored by its matching French article."),
    (8, None,
     "'Do not worry at all.' Andrea comforts Fabrice about his upcoming movie schedule and costume concerns. The reflexive pronoun sits right in front of the verb for 'worry', turning the action back onto the subject."),
    (9, None,
     "'Andrea, please hang up right now.' Colette tries to steer Andrea's attention back to family time. The informal 'you' form around 'pleases' marks a direct, personal relationship."),
    (10, None,
     "'Fabrice, can I call you back?' Andrea finally concedes and prepares to pause the conversation. In everyday spoken French, rising intonation on 'can' at the end is enough to turn the sentence into a question."),
    (11, None,
     "'I have an unexpected situation right now.' Andrea invents an urgent excuse to end the work call. Notice how 'I have' leads directly into the noun meaning 'unexpected event'."),
    (12, None,
     "'Thank you, let's finally think about our baby.' Colette welcomes Andrea back into their peaceful hospital room. The verb meaning 'let's think' pairs naturally with the noun for 'baby.' in everyday conversation."),
]

TRANSITION = "Now let's listen to the maternity clinic conversation once more to solidify what you have learned."

OUTRO = ("Andrea struggles to set aside her agency duties even in the maternity clinic, while Colette brings her back to the moment. "
         "Let's review the essential vocabulary from this hospital scene.")

CLOSING = ("colette", "Merci, pensons enfin à notre bébé.")
