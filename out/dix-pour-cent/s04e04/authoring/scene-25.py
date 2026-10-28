# Authoring module for dix-pour-cent s04e04 scene 25 (cues 1214).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e04/authoring/scene-25.py --out out/dix-pour-cent/s04e04/scene-25.json

ID = "dix-pour-cent-s04e04-scene-25"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 4
SCENE = 25
TITLE = "Une chanson sincère  (A Sincere Song)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sandrine", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E04"
SOURCE_FILE = "sources/dix-pour-cent/s04/e04.fr.dual.srt"
SOURCE_NOTE = (
    "Cue 1214. Backstage and on stage at a Parisian cabaret, Sandrine Kiberlain sings an emotional melody about "
    "childhood memories and freedom, choosing her true love for singing over stand-up comedy."
)

INTRO = (
    "At a Parisian music club, Sandrine Kiberlain steps onto the stage under warm stage lights to perform a tender song. "
    "Leaving comedy behind, she embraces her true passion for music as Gabriel cheers her on from the wings. "
    "Let's listen to the scene in French first."
)

OPENER = "Let's look at Sandrine's heartfelt musical performance step by step."

STORY = [
    ("gabriel", "Sandrine, vous êtes prête à chanter?",
     "Sandrine, are you ready to sing?",
     [(1214, "du passé")], "Gabriel encourages her from the wings"),
    ("lea", "Oui, je monte sur scène maintenant.",
     "Yes, I am going on stage now.",
     [(1214, "du passé")], "Sandrine smiles with quiet confidence"),
    ("gabriel", "Chantez avec tout votre cœur.",
     "Sing with all your heart.",
     [(1214, "du passé")], "Gabriel offers warm support"),
    ("lea", "Souviens-toi du passé avec tendresse.",
     "Remember the past with tenderness.",
     [(1214, "Souviens-toi du passé")], "Begins her lyrical song on stage"),
    ("lea", "Garde toujours tes souvenirs d'enfance.",
     "Always keep your childhood memories.",
     [(1214, "souvenirs d'enfance")], "Sings with deep emotion"),
    ("gabriel", "Votre voix est magnifique ce soir.",
     "Your voice is magnificent tonight.",
     [(1214, "souvenirs d'enfance")], "Gabriel listens in awe"),
    ("lea", "La musique m'apporte une grande joie.",
     "Music brings me great joy.",
     [(1214, "du passé")], "Expresses her artistic fulfillment"),
    ("gabriel", "Le public vous écoute en silence.",
     "The audience is listening to you in silence.",
     [(1214, "du passé")], "Notices the captivated crowd"),
    ("lea", "Je me sens enfin libre ici.",
     "I finally feel free here.",
     [(1214, "du passé")], "Rejoices in the moment"),
    ("gabriel", "Vous êtes une artiste extraordinaire.",
     "You are an extraordinary artist.",
     [(1214, "du passé")], "Praises her unique talent"),
    ("lea", "Je n'ai plus peur du trac.",
     "I am no longer afraid of stage fright.",
     [(1214, "du passé")], "Overcomes her earlier anxiety"),
    ("gabriel", "La scène vous appartient, Sandrine.",
     "The stage belongs to you, Sandrine.",
     [(1214, "du passé")], "Applauds her performance"),
    ("lea", "Merci pour votre soutien précieux, Gabriel.",
     "Thank you for your precious support, Gabriel.",
     [(1214, "du passé")], "Thanks her loyal agent"),
    ("gabriel", "Bravo pour cette très belle chanson!",
     "Congratulations on this very beautiful song!",
     [(1214, "du passé")], "Congratulates her warmly"),
]

WALK = [
    (0, None,
     "'Sandrine, are you ready to sing?' Gabriel asks if she is prepared to take the stage. Gabriel uses the polite 'you' form alongside 'sing' to keep a respectful professional tone."),
    (1, None,
     "'Yes, I am going on stage now.' Sandrine confirms that she is stepping out to perform. The verb meaning 'go up' pairs naturally with the noun for 'stage' in everyday conversation."),
    (2, None,
     "'Sing with all your heart.' Gabriel encourages her to express herself freely. Notice how 'sing' leads directly into the noun meaning 'heart'."),
    (3, None,
     "'Remember the past with tenderness.' Sandrine opens her lyrical melody with nostalgic warmth. The verb meaning 'remember' pairs naturally with the noun for 'past' in everyday conversation."),
    (4, None,
     "'Always keep your childhood memories.' Sandrine sings of holding on to youthful innocence. The informal 'you' form around 'keep' marks a direct, personal relationship."),
    (5, None,
     "'Your voice is magnificent tonight.' Gabriel marvels at her expressive musical tone. Gabriel uses the polite 'you' form alongside 'voice' to keep a respectful professional tone."),
    (6, None,
     "'Music brings me great joy.' Sandrine explains that singing brings her great joy in the moment. The verb meaning 'brings' pairs naturally with the noun for 'music' in everyday conversation."),
    (7, None,
     "'The audience is listening to you in silence.' Gabriel observes the spellbound crowd. The verb meaning 'listens to' pairs naturally with the noun for 'audience' in everyday conversation."),
    (8, None,
     "'I finally feel free here.' Sandrine describes the liberation she finds in song. The reflexive pronoun sits right in front of the verb for 'feel', turning the action back onto the subject."),
    (9, None,
     "'You are an extraordinary artist.' Gabriel praises her distinctive emotional depth. Gabriel uses the polite 'you' form alongside 'artist' to keep a respectful professional tone."),
    (10, None,
     "'I am no longer afraid of stage fright.' Sandrine celebrates conquering her anxiety. Notice how 'have' leads directly into the noun meaning 'fear'."),
    (11, None,
     "'The stage belongs to you, Sandrine.' Gabriel reassures her of her rightful place. The verb meaning 'belongs' pairs naturally with the noun for 'stage' in everyday conversation."),
    (12, None,
     "'Thank you for your precious support, Gabriel.' Sandrine expresses gratitude to her dedicated agent. The formal 'you' pronoun sets a courteous, professional distance around 'thank you'."),
    (13, None,
     "'Congratulations on this very beautiful song!' Gabriel celebrates her triumphant musical performance."),
]

TRANSITION = "Now listen to the whole scene again at normal speed, and see how much more you catch."
OUTRO = "After struggling with stand-up comedy, Sandrine finds her true artistic voice in music, performing a moving song about childhood memories while Gabriel cheers her on. When you watch the episode, listen out for the expressions meaning 'ready' and 'sing'. You'll catch them now. See you next time."
CLOSING = ("lea", "La musique m'apporte une grande joie.")
