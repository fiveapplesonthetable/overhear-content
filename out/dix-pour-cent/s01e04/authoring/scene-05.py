# Authoring module for dix-pour-cent s01e04 scene 05 (cues 126-159).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-05.py --out out/dix-pour-cent/s01e04/scene-05.json

ID = "dix-pour-cent-s01e04-scene-05"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 5
TITLE = "Un week-end d'escalade  (A Climbing Weekend)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "noemie": "emilie", "herve": "theo"}
LABELS = {"lea": "Camille", "noemie": "Noémie", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("In Mathias's office, Mathias has just talked the young Internet comedy star Augustin into considering "
         "Audrey Fleurot for his first film, swearing that Audrey loves his online videos. "
         "Meanwhile, out at the assistants' desks, Noémie is rummaging through a drawer in pain after a very "
         "unusual weekend, while Camille and Hervé are hard at work. "
         "We'll hear the scene in French first; don't worry about catching every word.")

STORY = [
 ("lea", "Vous cherchez quelque chose?", "Are you looking for something?",
  [(126, "Vous cherchez quelque chose ?")], ""),
 ("noemie", "Oui, un médicament. J'ai mal au dos.", "Yes, some medicine. My back hurts.",
  [(127, "Oui"), (128, "mal"), (128, "dos")], "'des analgésiques... Samuel les a pris pour son mal de dos' simplified"),
 ("noemie", "J'ai fait un stage d'escalade ce week-end.", "I did a rock-climbing course this weekend.",
  [(129, "J'ai fait un stage d'escalade ce week-end.")], ""),
 ("herve", "Tu as aimé?", "Did you like it?",
  [(131, "Tu as aimé ?")], ""),
 ("noemie", "Oui, beaucoup! Mais je suis une fille de la ville.", "Yes, a lot! But I'm a city girl.",
  [(132, "Oui, beaucoup !"), (133, "je suis une fille de la ville")], ""),
 ("noemie", "Et la corde fait très mal!", "And the rope really hurts!",
  [(137, "la corde"), (138, "fait mal")], "double-entendre about climbing harness in cues 134-142 simplified cleanly"),
 ("lea", "Hervé, sur Internet, cette actrice a dix ans de plus. Je fais quoi?",
  "Hervé, on the Internet, this actress is ten years older. What do I do?",
  [(146, "dix ans"), (146, "cette actrice"), (146, "Je fais quoi ?")],
  "'On a rajouté dix ans à l'âge de cette actrice sur Wikipedia' simplified"),
 ("herve", "Corrige l'âge, tout simplement.", "Just correct the age.",
  [(147, "corrige")], "'Crée un compte et corrige-le' simplified"),
 ("lea", "Je peux enlever encore cinq ans!", "I can take off another five years!",
  [(148, "enlever encore cinq ans")], "'Je pourrais' -> 'Je peux'"),
 ("lea", "Allô? Oui, merci! Bisou-bisou!", "Hello? Yes, thank you! Kiss-kiss!",
  [(151, "Allô."), (152, "Bisou-bisou !")], ""),
 ("noemie", "Vous dites bisou-bisou à une grande star?", "Do you say kiss-kiss to a big star?",
  [(154, "Vous"), (154, "bisou-bisou"), (154, "stars ?")], "'Vous venez de dire bisou-bisou à l'une de nos stars?' simplified"),
 ("lea", "Non!", "No!",
  [(155, "Non.")], ""),
 ("noemie", "Si!", "Yes, you did!",
  [(155, "Si.")], ""),
 ("lea", "C'est juste une habitude.", "It's just a habit.",
  [(156, "C'est juste une habitude.")], ""),
 ("noemie", "La fille de Christophe Lambert ne peut pas faire tout ce qu'elle veut!",
  "Christophe Lambert's daughter can't do whatever she wants!",
  [(159, "la fille de Christophe Lambert"), (159, "faire ce que")], "cue 159 simplified"),
]

OPENER = ("Let's go through it line by line. Camille sees Noémie searching through a desk drawer.")

WALK = [
 (0, None,
  "'Are you looking for something?' In French, the verb 'to look for' has the 'for' built right into it, with no extra word needed."),
 (1, None,
  "'Yes, some medicine. My back hurts.' Literally 'I have ache at the back'. That's the standard pattern for any body ache."),
 (2, None,
  "'I did a rock-climbing course this weekend.' The word for a short training course or workshop is the same word used for an internship."),
 (3, None,
  "'Did you like it?' Hervé is intrigued, using the everyday past tense."),
 (4, None,
  "'Yes, a lot! But I'm a city girl.' Literally 'a girl of the city'."),
 (5, None,
  "'And the rope really hurts!' Same 'makes ache' expression, this time with the thing that causes the pain as the subject. Then Camille looks at her computer screen."),
 (6, None,
  "'Hervé, on the Internet, this actress is ten years older. What do I do?' Literally 'has ten years of more'. Remember that French uses 'to have' for age."),
 (7, None,
  "'Just correct the age.' Literally 'correct the age, all simply'. Hervé doesn't even look up."),
 (8, None,
  "'I can take off another five years!' Camille is getting into the spirit of the job. Then her phone rings."),
 (9, None,
  "'Hello? Yes, thank you! Kiss-kiss!' She hangs up with a cheerful southern farewell, and Noémie freezes in horror."),
 (10, None,
  "'Do you say kiss-kiss to a big star?' Notice that Noémie still uses the formal 'you' with Camille when she's scolding her."),
 (11, None,
  "'No!' Camille tries to deny it."),
 (12, None,
  "'Yes, you did!' There's that special French 'yes' again, used to contradict a negative statement."),
 (13, None,
  "'It's just a habit.' Camille defends herself mildly."),
 (14, None,
  "'Christophe Lambert's daughter can't do whatever she wants!' Remember that since last episode, Noémie is convinced that Camille's secret father is the actor Christophe Lambert."),
]

TRANSITION = "Now let's listen to the whole scene once more."

OUTRO = ("So Noémie is sore from rock climbing, and still thinks Camille is Christophe Lambert's daughter. "
         "Listen out for how French says 'my back hurts' and 'ten years older'. See you next time.")
CLOSING = ("lea", "Allez, bisou-bisou!")
