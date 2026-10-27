# Authoring module for dix-pour-cent s01e05 scene 13 (cues 237-251).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-13.py --out out/dix-pour-cent/s01e05/scene-13.json

ID = "dix-pour-cent-s01e05-scene-13"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 13
TITLE = "La cible, c'est la femme chez le coiffeur  (The Target Is the Woman at the Hairdresser's)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "mathias": "marcel"}
LABELS = {"lea": "Camille", "herve": "Hervé", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 237-251. Spoken 'genre un avis de décès' is adapted to standard A1 'comme un avis de décès', "
               "and Mathias's stammered 'C'est... C'est... horrible' is joined into 'C'est horrible.'")

INTRO = ("Back in Paris at the ASK offices, Mathias is trying to stop the daytime soap opera from killing off his "
         "client Jonathan Joubert's character, Doctor Ryan. Camille suggests leaking the news to salon magazines so "
         "loyal viewers protest, and Hervé proudly unveils a mock death notice that goes way too far. Let's listen "
         "to the scene in French first.")

STORY = [
 ("lea", "La cible, c'est la femme qui bavarde avec ses amies chez le coiffeur.",
  "The target is the woman who chats with her friends at the hairdresser's.",
  [(237, "La cible"), (238, "c'est la femme qui bavarde avec ses amies chez le coiffeur")], ""),
 ("lea", "Le genre de femme qui adore Jonathan Joubert.",
  "The kind of woman who adores Jonathan Joubert.",
  [(239, "le genre de femme qui adore Jonathan Joubert")], ""),
 ("lea", "Ryan, je veux dire.",
  "Ryan, I mean.",
  [(240, "Ryan, je veux dire")], ""),
 ("lea", "Ce qu'il nous faut, c'est une fuite, pour que les fans commencent à protester.",
  "What we need is a leak, so that the fans start to protest.",
  [(241, "Ce qu'il nous faut, c'est une fuite, pour que les fans commencent à protester")], ""),
 ("mathias", "C'est quoi ton idée, comme un avis de décès?",
  "What is your idea, like a death notice?",
  [(242, "C'est quoi ton idée"), (242, "un avis de décès")], "'genre' -> 'comme'"),
 ("herve", "Exactement!",
  "Exactly!",
  [(243, "Exactement")], ""),
 ("herve", "Je me suis inspiré de cette affaire d'un enfant disparu en Corrèze.",
  "I took inspiration from that case of a missing child in Correze.",
  [(244, "Je me suis inspiré de cette affaire d'un enfant disparu en Corrèze")], ""),
 ("mathias", "C'est horrible.",
  "It's horrible.",
  [(246, "C'est"), (247, "horrible")], "Joined stammered cue"),
 ("mathias", "Écoute, laisse tomber.",
  "Listen, drop it.",
  [(248, "Écoute, laisse tomber")], ""),
 ("mathias", "Occupe-toi d'Audrey Fleurot.",
  "Take care of Audrey Fleurot.",
  [(249, "Occupe-toi d'Audrey Fleurot")], ""),
 ("mathias", "Elle a un problème d'emploi du temps avec ses enfants.",
  "She has a schedule problem with her children.",
  [(250, "Elle a un problème d'emploi du temps avec ses enfants")], ""),
 ("mathias", "Merci quand même.",
  "Thanks all the same.",
  [(251, "Merci quand même")], ""),
 ("herve", "De rien.",
  "You're welcome.",
  [(251, "De rien")], ""),
]

OPENER = "Now let's walk through the scene line by line and unpack the French expressions."

WALK = [
 (0, None,
  "'The target is the woman who chats with her friends at the hairdresser's.' The preposition before a profession means at their shop."),
 (1, None,
  "'The kind of woman who adores Jonathan Joubert.' Notice the noun for type or kind followed by the preposition 'of'."),
 (2, None,
  "'Ryan, I mean.' Literally 'I want to say', the standard everyday French way to say 'I mean'."),
 (3, None,
  "'What we need is a leak, so that the fans start to protest.' Notice how 'what we need' is built with the impersonal verb for needing."),
 (4, None,
  "'What is your idea, like a death notice?' In casual speech, placing the question word after the verb makes a quick, direct question."),
 (5, None,
  "'Exactly!' Hervé beams with pride and pulls out his printed mockup."),
 (6, None,
  "'I took inspiration from that case of a missing child in Corrèze.' The reflexive verb in the past tense takes the auxiliary 'to be'."),
 (7, None,
  "'It's horrible.' Mathias stares at the poster in total disbelief."),
 (8, None,
  "'Listen, drop it.' Literally 'let it fall', the universal French idiom for 'forget it' or 'drop it'."),
 (9, None,
  "'Take care of Audrey Fleurot.' Notice how the reflexive pronoun attaches to the end of a positive command."),
 (10, None,
  "'She has a schedule problem with her children.' The compound noun for a schedule literally means 'use of time'."),
 (11, None,
  "'Thanks all the same.' Mathias softens the blow before dismissing them."),
 (12, None,
  "'You're welcome.' Unbothered by the rejection, Hervé replies with the everyday phrase meaning 'of nothing'."),
]

TRANSITION = "Now listen to the entire office exchange one more time at natural speed."

OUTRO = ("Poor Hervé thought his missing-person poster was a stroke of genius, while Camille's salon rumor idea may "
         "actually work. Keep the phrase for drop it handy: listen and let it fall.")

CLOSING = ("mathias", "Écoute, laisse tomber.")
