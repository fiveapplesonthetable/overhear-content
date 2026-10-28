# Authoring module for dix-pour-cent s03e01 scene 25 (cue 1019).
# Build: python3 tools/compose.py out/dix-pour-cent/s03e01/authoring/scene-25.py --out out/dix-pour-cent/s03e01/scene-25.json

ID = "dix-pour-cent-s03e01-scene-25"
SHOW = "dix-pour-cent"
SEASON = 3
EPISODE = 1
SCENE = 25
TITLE = "Pas le manteau  (Not the Coat)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "jean": "theo"}
LABELS = {"lea": "Andréa", "jean": "Jean"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S03E01"
SOURCE_FILE = "sources/dix-pour-cent/s03/e01.fr.dual.srt"
SOURCE_NOTE = ("Cue 1019. In Andrea's office, Jean Dujardin declines his winter coat as he prepares "
               "to leave, choosing to feel the cold air to break out of his acting persona. Adapted for A1 French.")

INTRO = ("As their meeting concludes in her office, Andrea offers Jean Dujardin his coat before he leaves. "
         "Jean declines the coat, eager to feel the brisk outdoor air and finally shake off his grueling acting persona. "
         "Let's listen to their parting words in French first.")

STORY = [
 ("lea", "Voici ton manteau chaud pour sortir, Jean.",
  "Here is your warm coat to go outside, Jean.",
  [(1019, "manteau")], "Offered coat before leaving"),
 ("jean", "Non merci, pas le manteau aujourd'hui.",
  "No thank you, not the coat today.",
  [(1019, "Non, pas le manteau.")], "Declined coat politely"),
 ("lea", "Mais il fait très froid dehors!",
  "But it is very cold outside!",
  [(1019, "pas le manteau")], "Warned about outside chill"),
 ("jean", "J'ai besoin de sentir l'air frais.",
  "I need to feel the fresh air.",
  [(1020, "Allez, c'est l'heure d'y aller.")], "Sought outdoor sensation"),
 ("lea", "Tu veux encore rester dans ton rôle?",
  "Do you still want to stay in your role?",
  [(1015, "Déserter ?")], "Asked about acting mindset"),
 ("jean", "Non, je veux enfin redevenir moi-même.",
  "No, I want to finally become myself again.",
  [(1020, "Allez, c'est l'heure d'y aller.")], "Declared desire for normal identity"),
 ("lea", "Prends le temps de te reposer, Jean.",
  "Take the time to rest, Jean.",
  [(1018, "Tiens.")], "Encouraged restorative rest"),
 ("jean", "Oui, je vais couper mon téléphone.",
  "Yes, I am going to turn off my phone.",
  [(1020, "l'heure d'y aller")], "Promised digital break"),
 ("lea", "C'est une très bonne idée pour toi.",
  "That is a very good idea for you.",
  [(1008, "c'est bien")], "Approved self-care decision"),
 ("jean", "Nous nous voyons bientôt à l'agence?",
  "Are we seeing each other soon at the agency?",
  [(1020, "d'y aller")], "Inquired about next visit"),
 ("lea", "Oui, nous avons cette grande réunion.",
  "Yes, we have this big meeting.",
  [(1020, "c'est l'heure")], "Mentioned agency gathering"),
 ("jean", "Alors je te laisse avec l'équipe.",
  "Then I leave you with the team.",
  [(1020, "Allez")], "Excused himself gracefully"),
 ("lea", "Bonne chance pour la suite, Jean.",
  "Good luck for what comes next, Jean.",
  [(1018, "Tiens.")], "Wished success warmly"),
 ("jean", "Merci pour tout, Andréa!",
  "Thank you for everything, Andrea!",
  [(1018, "Tiens.")], "Expressed heartfelt thanks"),
]

OPENER = "Let's observe how Jean takes leave of Andrea with renewed clarity and gratitude."

WALK = [
 (0, None,
  "'Here is your warm coat to go outside, Jean.' Andrea uses the casual singular 'you' with 'to go outside', showing close familiarity. Andrea uses the casual singular 'you' with 'to go outside', showing close familiarity."),
 (1, None,
  "'No thank you, not the coat today.' The key noun here means 'coat', anchored by its matching French article. The key noun here means 'coat', anchored by its matching French article."),
 (2, None,
  "'But it is very cold outside!' Dropping the subject pronoun turns the verb for 'makes' into a direct, punchy command. Dropping the subject pronoun turns the verb for 'makes' into a direct, punchy command."),
 (3, None,
  "'I need to feel the fresh air.' In spoken French, the little word before 'I have' drops its final vowel and attaches with an apostrophe. In spoken French, the little word before 'I have' drops its final vowel and attaches with an apostrophe."),
 (4, None,
  "'Do you still want to stay in your role?' The verb meaning 'want' pairs naturally with the noun for 'role' in everyday conversation."),
 (5, None,
  "'No, I want to finally become myself again.' The clause hinges on the everyday verb meaning 'want'."),
 (6, None,
  "'Take the time to rest, Jean.' The reflexive pronoun sits right in front of the verb for 'take', turning the action back onto the subject."),
 (7, None,
  "'Yes, I am going to turn off my phone.' A near-future commitment to take disconnected rest. Notice how 'am going' leads directly into the noun meaning 'telephone'."),
 (8, None,
  "'That is a very good idea for you.' An encouraging evaluation supporting his decision. The informal 'you' form around 'it is' marks a direct, personal relationship."),
 (9, None,
  "'Are we seeing each other soon at the agency?' The verb meaning 'see' pairs naturally with the noun for 'the agency' in everyday conversation."),
 (10, None,
  "'Yes, we have this big meeting.' Notice how 'have' leads directly into the noun meaning 'meeting'. Notice how 'have' leads directly into the noun meaning 'meeting'."),
 (11, None,
  "'Then I leave you with the team.' The informal 'you' form around 'leave' marks a direct, personal relationship. The informal 'you' form around 'leave' marks a direct, personal relationship."),
 (12, None,
  "'Good luck for what comes next, Jean.' A cordial wish offering encouragement for the future. The key noun here means 'luck', anchored by its matching French article."),
 (13, None,
  "'Thank you for everything, Andrea!' A short, idiomatic conversational reply that keeps the exchange moving naturally. A short, idiomatic conversational reply that keeps the exchange moving naturally."),
]

TRANSITION = "Now let's listen to Andrea and Jean again at full speed."

OUTRO = ("Refusing his winter coat, Jean heads out into the cold air to clear his mind after months of intense isolation. "
         "Andrea turns her attention back to agency matters as the annual staff meeting begins in the conference room.")

CLOSING = ("lea", "À très bientôt, Jean.")
