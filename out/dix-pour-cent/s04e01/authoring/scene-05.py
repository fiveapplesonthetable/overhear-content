# Authoring module for dix-pour-cent s04e01 scene 05 (cues 276-359).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e01/authoring/scene-05.py --out out/dix-pour-cent/s04e01/scene-05.json

ID = "dix-pour-cent-s04e01-scene-05"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 1
SCENE = 5
TITLE = "Le projet d'Oscar  (Oscar's Project)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "charlotte": "emilie", "oscar": "theo"}
LABELS = {"lea": "Andréa", "charlotte": "Charlotte", "oscar": "Oscar"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E01"
SOURCE_FILE = "sources/dix-pour-cent/s04/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 276-359. Charlotte Gainsbourg rehearses a bizarre science-fiction script with her friend Oscar, "
               "begging Andrea to find an excuse to extract her from the project without hurting his feelings.")

INTRO = ("Charlotte Gainsbourg reads lines from a bizarre science-fiction script with her childhood friend Oscar. "
         "Horrified by the dialogue, she turns to Andrea for help backing out of the project. "
         "Let's listen to their conversation in French first.")

STORY = [
    ("charlotte", "Si ça continue, l'humanité va s'éteindre!",
     "If this continues, humanity will go extinct!",
     [(276, "Si ça continue, toute la race humaine va s'éteindre.")], "Charlotte reads dramatic dialogue from the script"),
    ("oscar", "Charlotte, parle plus fort s'il te plaît!",
     "Charlotte, speak louder please!",
     [(278, "Charlotte, excuse-moi, parle plus fort.")], "Oscar directs Charlotte during the rehearsal"),
    ("charlotte", "Je croyais que nous étions amoureux.",
     "I thought that we were in love.",
     [(291, "Pourquoi ? On est amoureux.")], "Charlotte questions the romantic relationship between characters"),
    ("oscar", "Pas du tout, c'est ton petit-fils!",
     "Not at all, he is your grandson!",
     [(292, "Pas du tout, c'est ton petit-fils !")], "Oscar corrects her regarding the characters' family ties"),
    ("oscar", "Il vient du futur dans le passé!",
     "He comes from the future into the past!",
     [(294, "Il est venu du futur pour te rencontrer dans le passé.")], "Oscar explains the convoluted time travel plot"),
    ("charlotte", "C'est ça que vous appelez un scénario?",
     "Is that what you call a script?",
     [(332, "C'est ça que vous appelez un bon scénario ?")], "Charlotte privately expresses dismay to Andrea"),
    ("lea", "Je n'ai pas eu le temps de lire.",
     "I did not have time to read.",
     [(334, "Je n'ai pas eu le temps de le lire.")], "Andrea confesses she did not read the script in advance"),
    ("charlotte", "Certains virent leur agent pour moins que ça!",
     "Some people fire their agent for less than that!",
     [(340, "Certains virent leur agent pour moins que ça.")], "Charlotte warns Andrea about professional negligence"),
    ("lea", "On va te sortir de ce film.",
     "We will get you out of this movie.",
     [(345, "On va te sortir de là.")], "Andrea promises to find an escape route"),
    ("lea", "Je dirai que tu exiges une réécriture.",
     "I will say that you demand a rewrite.",
     [(349, "Et que tu ne feras pas le rôle sans une réécriture complète.")], "Andrea proposes a professional excuse"),
    ("charlotte", "Je ne veux pas blesser mon vieil ami.",
     "I do not want to hurt my old friend.",
     [(350, "Il est hors de question que je me brouille avec Oscar.")], "Charlotte refuses to hurt Oscar's fragile feelings"),
    ("charlotte", "Officiellement, j'adore ça, mais sauve-moi!",
     "Officially, I love this, but save me!",
     [(354, "Donc officiellement, j'adore le scénario."), (357, "Il n'est pas question que je le fasse.")], "Charlotte demands a silent rescue"),
    ("lea", "Je vais demander le double de ton cachet!",
     "I am going to ask double your fee!",
     [(360, "Je vais jouer la carte du double cachet.")], "Andrea devises a pricing strategy to repel the producers"),
]

OPENER = "Let's explore Charlotte and Andrea's discussion line by line."

WALK = [
    (0, None,
     "'If this continues, humanity will go extinct!' Charlotte reads an overly dramatic science-fiction line from the draft. In spoken French, the little word before 'continues' drops its final vowel and attaches with an apostrophe."),
    (1, None,
     "'Charlotte, speak louder please!' Oscar interrupts the reading to ask for a stronger delivery. Oscar uses the casual singular 'you' with 'speak', showing close familiarity."),
    (2, None,
     "'I thought that we were in love.' Charlotte questions whether the characters are supposed to be lovers. The descriptive adjective for 'in love.' agrees in gender and number with its noun."),
    (3, None,
     "'Not at all, he is your grandson!' Oscar clarifies that the male hero is actually her grandson. Oscar uses the casual singular 'you' with 'he is', showing close familiarity."),
    (4, None,
     "'He comes from the future into the past!' Oscar explains the bizarre timeline of his story. Notice how 'comes' leads directly into the noun meaning 'future'."),
    (5, None,
     "'Is that what you call a script?' Charlotte steps aside to voice her shock to Andrea. Charlotte uses the polite 'you' form alongside 'is it' to keep a respectful professional tone."),
    (6, None,
     "'I did not have time to read.' Andrea admits she neglected to review the pages beforehand. The two-part French negation brackets the verb for 'have' on both sides."),
    (7, None,
     "'Some people fire their agent for less than that!' Charlotte scolds Andrea for letting her walk into this meeting. Dropping the subject pronoun turns the verb for 'fire' into a direct, punchy command."),
    (8, None,
     "'We will get you out of this movie.' Andrea reassures her client that she will resolve the dilemma. The informal 'you' form around 'are going' marks a direct, personal relationship."),
    (9, None,
     "'I will say that you demand a rewrite.' Andrea suggests claiming the script needs major editorial changes. The verb meaning 'will say' pairs naturally with the noun for 'rewrite.' in everyday conversation."),
    (10, None,
     "'I do not want to hurt my old friend.' Charlotte insists that their lifelong friendship must be protected. The two-part French negation brackets the verb for 'want' on both sides."),
    (11, None,
     "'Officially, I love this, but save me!' Charlotte orders Andrea to find a quiet exit behind the scenes. This conversational past tense combines a helper verb with the past participle for 'save me!'."),
    (12, None,
     "'I am going to ask double your fee!' Andrea proposes setting an impossibly high salary to scare the financiers away. Notice how 'am going' leads directly into the noun meaning 'double'."),
]

TRANSITION = "Now let's listen to Charlotte and Andrea's exchange once more from start to finish."

OUTRO = ("Charlotte and Andrea search for a diplomatic way to exit a disastrous film production. "
         "Let's review the key vocabulary from this scene.")

CLOSING = ("lea", "Je vais demander le double de ton cachet!")
