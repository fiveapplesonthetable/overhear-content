# Authoring module for dix-pour-cent s01e03 scene 13 (cues 264-312; merged 12 cues 259-263 retold in INTRO).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e03/authoring/scene-13.py --out out/dix-pour-cent/s01e03/scene-13.json

ID = "dix-pour-cent-s01e03-scene-13"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 3
SCENE = 13
TITLE = "La fille de Christophe Lambert  (Christophe Lambert's Daughter)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie"}
LABELS = {"lea": "Camille", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E03"
SOURCE_FILE = "sources/dix-pour-cent/s01/e03.fr.dual.srt"

INTRO = ("While Andréa is striking her deal with Clément at the tax office, Camille catches Mathias in the corridor back at ASK. "
         "Calling him Dad under her breath, she thanks him for the César invitation, and he tells her it will let her meet people in the film business. "
         "But when Camille returns to her desk, Mathias's assistant Noémie is waiting for her, and she looks furious. "
         "Listen to the French first without worrying about catching every word.")

STORY = [
 ("lea", "Qu'est-ce qui ne va pas?", "What's wrong?",
  [(264, "Qu'est-ce qui ne va pas")], ""),
 ("noemie", "Je sais que tu mens. J'ai vu Mathias poser cette enveloppe sur ton bureau.", "I know you're lying. I saw Mathias put that envelope on your desk.",
  [(264, "Je sais que tu mens"), (266, "J'ai vu Mathias poser cette enveloppe sur ton bureau")], ""),
 ("lea", "Arrête, tu es pénible, Noémie!", "Stop it, you're annoying, Noémie!",
  [(268, "Tu es pénible, Noémie")], "omits 'couché avec lui' in 267"),
 ("noemie", "Pourquoi toi, alors?", "Why you, then?",
  [(268, "Pourquoi toi, alors")], ""),
 ("lea", "Parce que je suis nouvelle. Il a parlé à Andréa.", "Because I'm new. He talked to Andréa.",
  [(269, "Parce que"), (269, "il a parlé à Andréa"), (270, "je suis nouvelle")], ""),
 ("noemie", "Tu vois! Tu as regardé en haut à gauche! Ça veut dire que tu mens.", "You see! You looked up and to the left! That means you're lying.",
  [(271, "Tu vois"), (272, "Tu as regardé en haut à gauche"), (274, "Ça veut dire que tu mens")], ""),
 ("noemie", "Le premier jour, tu as vu Mathias avant Andréa. Donc tu le connais!", "On the first day, you saw Mathias before Andréa. So you know him!",
  [(278, "le jour"), (279, "tu as vu Mathias avant"), (280, "Donc tu le connais")], ""),
 ("noemie", "Tu travailles en secret pour Mathias?", "Are you working in secret for Mathias?",
  [(283, "pour Mathias")], "'tu espionnes pour Mathias' simplified to A1"),
 ("lea", "D'accord! En fait, il est un ami de mon père.", "Okay! In fact, he's a friend of my father's.",
  [(285, "D'accord"), (287, "En fait"), (288, "un ami de mon père")], ""),
 ("lea", "Je ne peux pas dire qui est mon père. Il est marié, avec des enfants.", "I can't say who my father is. He's married, with children.",
  [(291, "je ne peux pas dire qui est mon père"), (292, "Il est marié, avec"), (292, "des enfants")], ""),
 ("noemie", "Une des stars de l'agence? Un des clients de Mathias?", "One of the agency's stars? One of Mathias's clients?",
  [(294, "Une des stars de l'agence"), (296, "Un des clients de Mathias")], ""),
 ("lea", "Oui. Mais je ne peux pas te le dire.", "Yes. But I can't tell you.",
  [(297, "Je ne peux pas te le dire")], "'Ouais' -> 'Oui'"),
 ("noemie", "Qui? Dis-moi, ou je vais tout dire à Andréa!", "Who? Tell me, or I'll tell Andréa everything!",
  [(297, "Qui"), (298, "Je vais tout dire à Andréa")], "Camille glances at a film poster on the wall"),
 ("noemie", "Tu es la fille de Christophe Lambert?", "You're Christophe Lambert's daughter?",
  [(300, "Tu es la fille de Christophe Lambert")], ""),
 ("noemie", "Mais tu lui ressembles vraiment! Je suis vraiment désolée!", "But you really look like him! I'm really sorry!",
  [(304, "Mais tu lui ressembles vraiment"), (305, "Je suis vraiment"), (306, "désolé")], "omits 'Putain !' in 303; feminine 'désolée'"),
 ("lea", "N'en parle à personne.", "Don't talk about it to anyone.",
  [(308, "N'en parle à personne")], ""),
 ("noemie", "Bien sûr! Ça restera notre petit secret.", "Of course! It will stay our little secret.",
  [(309, "bien sûr"), (310, "Ça restera notre petit secret")], ""),
 ("noemie", "Les acteurs ont des vies peu ordinaires. Mais nous, on est juste leurs agents.", "Actors have unusual lives. But we are just their agents.",
  [(311, "Les acteurs ont des vies peu ordinaires"), (312, "Mais nous, on est juste leurs agents")], ""),
]

OPENER = "Let's break that down step by step. Camille sees right away that something is bothering Noémie."

WALK = [
 (0, None,
  "'What's wrong?' Literally 'what is it that doesn't go?', the natural way to ask what the matter is."),
 (1, "Je sais que tu mens.",
  "'I know you're lying.' The verb at the end is 'to lie' in the informal 'you' form."),
 (1, "J'ai vu Mathias poser cette enveloppe sur ton bureau.",
  "'I saw Mathias put that envelope on your desk.' Earlier, Camille told everyone the invitation came from Andréa."),
 (2, None,
  "'Stop it, you're annoying, Noémie!' A command followed by a useful everyday adjective for someone who won't let go."),
 (3, None,
  "'Why you, then?' Two short words and 'then' at the end."),
 (4, None,
  "'Because I'm new. He talked to Andréa.' Notice the feminine ending on 'new' because Camille is speaking."),
 (5, "Tu vois! Tu as regardé en haut à gauche!",
  "'You see! You looked up and to the left!' Literally 'in high to the left'. Noémie has been reading psychology books."),
 (5, "Ça veut dire que tu mens.",
  "'That means you're lying.' Literally 'that wants to say', the everyday French phrase for 'that means'."),
 (6, None,
  "'On the first day, you saw Mathias before Andréa. So you know him!' The little word for 'him' sits right before 'know'."),
 (7, None,
  "'Are you working in secret for Mathias?' Noémie thinks Camille is a spy planted in Andréa's office."),
 (8, None,
  "'Okay! In fact, he's a friend of my father's.' Cornered, Camille invents half a truth."),
 (9, None,
  "'I can't say who my father is. He's married, with children.' That part is completely true, though not the way Noémie thinks."),
 (10, None,
  "'One of the agency's stars? One of Mathias's clients?' Noémie's eyes light up at the thought of a famous name."),
 (11, None,
  "'Yes. But I can't tell you.' Two little object words sit side by side before 'tell': 'to you' and 'it'."),
 (12, None,
  "'Who? Tell me, or I'll tell Andréa everything!' Desperate, Camille glances at a film poster on the wall behind Noémie."),
 (13, None,
  "'You're Christophe Lambert's daughter?' Noémie follows her gaze to the poster and gasps. Camille just nods."),
 (14, None,
  "'But you really look like him! I'm really sorry!' In French you 'resemble to someone', so the word before the verb means 'to him'."),
 (15, None,
  "'Don't talk about it to anyone.' A negative command using the word for 'no one' instead of the usual negative word, plus the little word for 'about it'."),
 (16, None,
  "'Of course! It will stay our little secret.' Future tense of 'to stay'. Noémie is thrilled to share a secret with a star's daughter."),
 (17, None,
  "'Actors have unusual lives. But we are just their agents.' Literally 'lives little ordinary'. Noémie is already counting herself as an agent."),
]

TRANSITION = "Now let's listen to the whole conversation again."

OUTRO = ("Camille's real secret is safe, and Noémie now believes she works next to Christophe Lambert's daughter. "
         "Until next time!")
CLOSING = ("noemie", "Ça restera notre petit secret!")
