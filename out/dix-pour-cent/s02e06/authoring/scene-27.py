# Authoring module for dix-pour-cent s02e06 scene 27 (cues 765-787).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e06/authoring/scene-27.py --out out/dix-pour-cent/s02e06/scene-27.json

ID = "dix-pour-cent-s02e06-scene-27"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 6
SCENE = 27
TITLE = "Viens à New York  (Come to New York)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie"}
LABELS = {"lea": "Andréa", "camille": "Camille"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E06"
SOURCE_FILE = "sources/dix-pour-cent/s02/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 765-787. At the Cannes party, Andrea and Camille share a heartfelt reunion over drinks. "
               "Andrea proposes that Camille join her in New York as her assistant at international agency UBA. "
               "Adapted for A1 French.")

INTRO = ("At the poolside of the Cannes party, Andrea spots Camille and invites her for a toast. "
         "Reaffirming their bond, Andrea asks Camille to follow her to New York to build a new career abroad. "
         "Let's listen to the scene in French first.")

STORY = [
 ("camille", "Salut Andréa, laisse-moi t'expliquer ma présence...",
  "Hi Andrea, let me explain my presence...",
  [(765, "Salut."), (766, "Laisse-moi expliquer...")], "Camille greets Andrea"),
 ("lea", "Ce n'est absolument pas la peine.",
  "There is absolutely no need.",
  [(767, "Ce n'est pas la peine.")], "Andrea waives explanations"),
 ("lea", "C'est dur de ne plus travailler ensemble!",
  "It is hard to no longer work together!",
  [(768, "C'est dur de ne plus être mon assistante, hein ?")], "Andrea reflects on absence"),
 ("lea", "Trinquons à nos retrouvailles, santé Camille!",
  "Let us toast to our reunion, cheers Camille!",
  [(769, "-Santé ! -Santé !")], "Andrea raises a glass"),
 ("lea", "Tu m'as beaucoup manqué ces derniers jours.",
  "I missed you very much these past days.",
  [(770, "-Tu m'as manqué. -Vraiment ?")], "Andrea admits feelings"),
 ("camille", "C'est vrai? Tu m'as manqué aussi.",
  "Is that true? I missed you too.",
  [(770, "-Tu m'as manqué. -Vraiment ?")], "Camille reciprocates warmly"),
 ("lea", "Et c'est quoi ces drôles de chaussures?",
  "And what are these funny shoes?",
  [(772, "-C'est quoi ces chaussures ? -Oui, je l'avoue !")], "Andrea jokes about footwear"),
 ("camille", "Ce sont les chaussures de ma mère!",
  "These are my mother's shoes!",
  [(773, "Ce sont celles de ma mère.")], "Camille laughs and confesses"),
 ("lea", "Dis-moi, tu connais la ville de New York?",
  "Tell me, do you know the city of New York?",
  [(774, "Tu connais New York ?")], "Andrea pivots conversation"),
 ("camille", "Pas du tout, je n'y suis jamais allée.",
  "Not at all, I have never been there.",
  [(775, "Non. Enfin, si, bien sûr."), (776, "-Mais je n'y suis jamais allée. -Tu parles anglais ?")], "Camille shares honesty"),
 ("lea", "Veux-tu venir à New York avec moi?",
  "Do you want to come to New York with me?",
  [(777, "Tu veux venir à New York avec moi,")], "Andrea invites Camille"),
 ("lea", "On me propose un poste chez UBA.",
  "They are offering me a position at UBA.",
  [(778, "travailler avec moi dans une grande agence ?"), (779, "UBA. J'aurais besoin d'une assistante.")], "Andrea shares news"),
 ("lea", "J'aurai absolument besoin d'une assistante là-bas.",
  "I will definitely need an assistant over there.",
  [(779, "J'aurais besoin d'une assistante.")], "Andrea makes direct offer"),
 ("camille", "Oui, bien sûr, c'est complètement dingue!",
  "Yes, of course, that is completely crazy!",
  [(784, "Ouais !"), (785, "C'est dingue !")], "Camille accepts excitedly"),
 ("lea", "Parfait, nous en reparlerons très vite ensemble.",
  "Perfect, we will discuss it very soon together.",
  [(786, "-Très bien ! -On se reparlera.")], "Andrea promises follow-up"),
]

OPENER = "Let's examine how Andrea rebuilds trust with Camille and offers her a thrilling new horizon in New York step by step."

WALK = [
 (0, None,
  "'Hi Andrea, let me explain my presence...' Camille starts nervously, fearing Andrea might be displeased to see her."),
 (1, None,
  "'There is absolutely no need.' Andrea cuts her off gently, dismissing any awkward tension."),
 (2, None,
  "'It is hard to no longer work together!' Andrea acknowledges the emotional gap created by Camille's departure."),
 (3, None,
  "'Let us toast to our reunion, cheers Camille!' Andrea raises her champagne glass to celebrate their friendship."),
 (4, None,
  "'I missed you very much these past days.' Andrea openly admits her attachment to her former assistant."),
 (5, None,
  "'Is that true? I missed you too.' Camille responds with spontaneous and sincere warmth."),
 (6, None,
  "'And what are these funny shoes?' Andrea playfully points out Camille's slightly oversized party shoes."),
 (7, None,
  "'These are my mother's shoes!' Camille explains the comical rescue arranged by Annick earlier."),
 (8, None,
  "'Tell me, do you know the city of New York?' Andrea introduces a momentous life topic casually."),
 (9, None,
  "'Not at all, I have never been there.' Camille answers with genuine curiosity and modesty."),
 (10, None,
  "'Do you want to come to New York with me?' Andrea extends an extraordinary invitation to cross the Atlantic."),
 (11, None,
  "'They are offering me a position at UBA.' Andrea discloses the confidential offer from the international agency."),
 (12, None,
  "'I will definitely need an assistant over there.' Andrea makes clear that she trusts no one else by her side."),
 (13, None,
  "'Yes, of course, that is completely crazy!' Camille reacts with joyous shock at the incredible prospect."),
 (14, None,
  "'Perfect, we will discuss it very soon together.' Andrea seals the partnership with optimistic confidence."),
]

TRANSITION = "Now let's listen to the scene once more from start to finish."

OUTRO = ("The unexpected reunion in Cannes opens an exhilarating international chapter for Andrea and Camille. "
         "Let's review the friendship and travel vocabulary from this scene.")

CLOSING = ("lea", "Parfait, nous en reparlerons très vite ensemble.")
