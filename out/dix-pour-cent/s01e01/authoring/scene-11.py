# Authoring module for dix-pour-cent s01e01 scene 11 (cues 323-399, with merged scenes 09-10 in the bridge).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e01/authoring/scene-11.py --out out/dix-pour-cent/s01e01/scene-11.json

ID = "dix-pour-cent-s01e01-scene-11"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 11
TITLE = "La visite de l'agence  (A Tour of the Agency)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "noemie": "emilie"}
LABELS = {"lea": "Camille", "herve": "Hervé", "noemie": "Noémie"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Back at the agency, a lot has happened in a few minutes. "
         "Gabriel told Samuel he couldn't lie to Cécile, and Samuel's advice was simple: you don't have to lie, "
         "just don't tell her the truth. Then the boss put on his hat and left for the airport and his holiday in Rio. "
         "A little later Cécile rang, Gabriel panicked, pressed the wrong button and rejected her call, "
         "and the whole office laughed at him. "
         "Now it's Camille's first hour as Andréa's assistant. Andréa gave her the rules at top speed: "
         "each agent looks after about eighty actors, the agency takes ten percent of their pay, "
         "answer every call, write everything down, always say Andréa is in a meeting, "
         "and never promise that she'll call back. Then she left Camille with two assistants, Hervé and Noémie, "
         "who give her the tour, and a lot of gossip with it. "
         "Here's the story in French first. Don't worry about catching every word.")

STORY = [
 ("lea", "Vous êtes l'assistante de Mathias Barneville?", "Are you Mathias Barneville's assistant?",
  [(335, "Vous êtes l'assistante de Mathias Barneville")], ""),
 ("noemie", "Oui. Il est très sympa.", "Yes. He's very nice.",
  [(336, "Oui"), (337, "Très sympa")], "'Il est' added"),
 ("herve", "Tout le monde le trouve horrible.", "Everyone thinks he's horrible.",
  [(338, "Tout le monde le trouve horrible")], "the second half (Noémie's ideal man) left out"),
 ("herve", "C'est la comptabilité. Ils sont adorables.", "This is Accounts. They're lovely.",
  [(345, "C'est la Comptabilité"), (346, "ils sont adorables")], ""),
 ("lea", "Bonjour, je suis Camille!", "Hello, I'm Camille!",
  [(348, "Je suis Camille")], "'Bonjour' added"),
 ("herve", "Maintenant, je vous montre le service juridique.", "Now I'll show you the Legal Department.",
  [(353, "Maintenant je vous montre le service juridique")], "speaker not certain in the source; given to Hervé"),
 ("noemie", "Voici les scripts. Sans scénario, pas de film!", "Here are the scripts. No script, no film!",
  [(358, "Voici les scripts"), (360, "Sans scénario, pas de film")], "shortened"),
 ("lea", "Et ici, c'est qui, Arlette?", "And here, who's Arlette?",
  [(362, "C'est qui, Arlette")], "'Et ici' added (she is looking at the agents' script shelves)"),
 ("herve", "Arlette, c'est la doyenne des agents à Paris.", "Arlette is the most senior agent in Paris.",
  [(363, "la doyenne des agents à Paris")], ""),
 ("herve", "Elle dit imprésario, pas agent.", "She says impresario, not agent.",
  [(364, "Elle dit")], "guillemets of the subtitle dropped"),
 ("lea", "Et Andréa ne lit pas?", "And Andréa doesn't read?",
  [(366, "Andréa ne lit pas")], ""),
 ("noemie", "Tu plaisantes? Andréa lit tout.", "Are you kidding? Andréa reads everything.",
  [(367, "Tu plaisantes ? Andréa lit tout")], "speaker not certain in the source; given to Noémie"),
 ("noemie", "Elle a peur de rater quelque chose.", "She's scared of missing something.",
  [(369, "Elle a peur de rater quelque chose")], "'d'important' dropped"),
 ("herve", "Et voilà la salle de presse. On appelle ça la boutique.", "And here's the press room. We call it the shop.",
  [(375, "la salle de presse"), (376, "On appelle ça")], "'Et voilà' added"),
 ("herve", "Cécile de France? Refusée, à cause de son âge.", "Cécile de France? Turned down, because of her age.",
  [(387, "à cause de son âge")], "the gossip question of cue 387 retold as a short remark"),
 ("noemie", "Regardez! Cécile est là!", "Look! Cécile's here!",
  [(389, "Regardez"), (391, "Cécile est là")], ""),
 ("lea", "Cécile de France? Ici?", "Cécile de France? Here?", [], "new: Camille's reaction"),
]

OPENER = ("Let's take it slowly. Camille starts by asking Noémie a question, and she uses the polite form, "
          "because they have only just met.")

WALK = [
 (0, None,
  "'Are you Mathias Barneville's assistant?' Notice how it's built: you are, the assistant, of Mathias. "
  "French has no apostrophe-s for owners; it uses a little word meaning 'of'. Noémie answers at once."),
 (1, "Il est très sympa.",
  "'He's very nice.' The last word is a short, friendly way of saying 'nice' or 'likeable'. "
  "Hervé doesn't agree at all."),
 (2, None,
  "'Everyone thinks he's horrible.' Word for word: all the world finds him horrible. "
  "The tiny word for 'him' sits in front of the verb, not after it, which is normal in French."),
 (3, None,
  "'This is Accounts. They're lovely.' Hervé points at the accountants, and Camille, being Camille, says hello to them."),
 (4, None,
  "'Hello, I'm Camille!' The verb 'to be', first person: I am. Short and warm."),
 (5, None,
  "'Now I'll show you the Legal Department.' Here Hervé still uses the formal 'you' with the new girl. "
  "Then come the scripts."),
 (6, "Voici les scripts.",
  "'Here are the scripts.' This little word is how you present something: here is, here are."),
 (6, "Sans scénario, pas de film!",
  "'No script, no film!' Literally 'without a script, not of film'. In quick speech the French often keep only "
  "the second half of the 'not' and drop the verb completely. Camille spots a name on a shelf."),
 (7, None,
  "'And here, who's Arlette?' A casual question: it is who, Arlette? Hervé explains with some pride."),
 (8, None,
  "'Arlette is the most senior agent in Paris.' The word he uses means the oldest member of a group, "
  "the one who has been there longest, and it ends in a feminine way because Arlette is a woman."),
 (9, None,
  "'She says impresario, not agent.' The old-fashioned word, very Arlette. Then Camille notices that one shelf is almost empty."),
 (10, None,
  "'And Andréa doesn't read?' Here is the full negative: one little word before the verb and one after it, "
  "wrapped around 'reads' like two slices of bread. Noémie switches to the casual 'you'."),
 (11, "Tu plaisantes?",
  "'Are you kidding?' The casual 'you', between assistants of the same age. Compare it with the polite form at the start."),
 (11, "Andréa lit tout.",
  "'Andréa reads everything.' The same verb as before, now without the negative around it."),
 (12, None,
  "'She's scared of missing something.' Literally 'she has fear': in French you have fear, you don't 'are' scared. "
  "Next stop, the press room."),
 (13, "Et voilà la salle de presse.",
  "'And here's the press room.' This is the cousin of the word we heard with the scripts, and it often means 'there you go'."),
 (13, "On appelle ça la boutique.",
  "'We call it the shop.' Free gifts for the stars end up there. The first little word means 'we' or 'people' in everyday speech. "
  "And then the gossip turns to the star of the day."),
 (14, None,
  "'Cécile de France? Turned down, because of her age.' Camille remembers this. It will matter very soon. "
  "At that moment Noémie looks out of the window."),
 (15, None,
  "'Look! Cécile's here!' The first word is a polite command, 'look', and the second sentence uses a word meaning 'there' "
  "that really means 'here, now'. The whole office starts shouting."),
 (16, None,
  "'Cécile de France? Here?' Camille can hardly believe it: on her very first morning, the star walks in."),
]

TRANSITION = "Good. Now let's hear the tour once more, from the top."

OUTRO = ("Well done, that was a busy tour. When you watch, listen for the polite and the casual 'you', "
         "and for that little word that means 'here is'. Until next time.")
CLOSING = ("lea", "À plus!")
