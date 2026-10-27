# Authoring module for dix-pour-cent s01e06 scene 06 (cues 145-176).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-06.py --out out/dix-pour-cent/s01e06/scene-06.json

ID = "dix-pour-cent-s01e06-scene-06"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 6
TITLE = "Jean Gabin, sors de là!  (Jean Gabin, Get Out of There!)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo"}
LABELS = {"lea": "Noemie", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 145-176. Outside Mathias's office, Noemie and Hervé discuss the bag of cash brought by Catherine's father. "
               "Noemie dreams of becoming Mathias's indispensable right hand and sneaks inside to take a closer look. "
               "While Hervé keeps watch, Arlette's dog Jean Gabin wanders in and ruins the cash. "
               "Meanwhile, Andrea meets Christophe Bel to propose a compromise about the duck and the swimming pool.")

INTRO = ("Outside Mathias's office, the assistants are buzzing with curiosity. A mysterious luxury bag has arrived, "
         "and Noemie is convinced it contains a massive cash loan from Catherine's wealthy father to finance Mathias's "
         "takeover of the agency. Let's listen to the scene in French first.")

STORY = [
 ("herve", "Il ne paierait pas en liquide!",
  "He would not pay in cash!",
  [(145, "Il ne paierait pas en liquide !")], ""),
 ("lea", "Si! Le beau-père a des biens immobiliers à Paris.",
  "Yes he would! The father-in-law owns real estate in Paris.",
  [(146, "Si ! Le beau-père a des biens immobiliers à Paris.")], ""),
 ("lea", "Quand les acheteurs achètent, ils paient en liquide. C'est bien connu.",
  "When buyers purchase property, they pay in cash. That is well known.",
  [(147, "Quand les Russes et les Qataris achètent, ils paient cash. C'est bien connu.")], "Slang 'cash' replaced with 'en liquide'"),
 ("herve", "Donc c'est du liquide.",
  "So it is cash.",
  [(148, "Donc c'est du liquide.")], ""),
 ("lea", "C'est comme ça que Mathias va devenir notre patron.",
  "That is how Mathias is going to become our boss.",
  [(149, "C'est comme ça que Mathias va devenir notre patron.")], ""),
 ("lea", "Et moi je deviendrai son bras droit.",
  "And I will become his right-hand woman.",
  [(150, "Et moi je deviendrai sa bras droit.")], "Subtitle typo 'sa' corrected to masculine 'son bras droit'"),
 ("herve", "Alors il te demandera en mariage.",
  "Then he will ask you to marry him.",
  [(151, "Alors il te demandera en mariage.")], ""),
 ("lea", "Tu crois? Non! Je vais jeter un coup d'œil.",
  "You think so? No! I am going to take a look.",
  [(152, "Tu crois ? Non !"),
   (153, "Non."),
   (154, "Je vais jeter un œil.")], "'jeter un œil' expanded to standard 'jeter un coup d'œil'"),
 ("herve", "Non, Noémie! Tu es folle? Fais attention!",
  "No, Noemie! Are you crazy? Be careful!",
  [(155, "Non, Noémie ! T'es folle ?"),
   (162, "Fais attention.")], "Spoken 't'es' normalized to 'tu es'"),
 ("lea", "Mathias sait que tout ce que je fais, c'est pour son bien.",
  "Mathias knows that everything I do is for his own good.",
  [(157, "Mathias sait que tout ce que je fais, c'est pour son bien.")], ""),
 ("lea", "Donc il récompensera ma loyauté. Fais le guet, d'accord?",
  "So he will reward my loyalty. Keep watch, okay?",
  [(159, "il récompensera ma loyauté et ma discrétion."),
   (160, "Fais le guet, d'accord ?")], ""),
 ("herve", "Jean Gabin! Quoi? Jean Gabin est en train d'abîmer l'argent!",
  "Jean Gabin! What? Jean Gabin is ruining the money!",
  [(163, "Jean Gabin !"),
   (163, "Quoi ?"),
   (164, "Jean Gabin est en train de pisser sur l'argent des Qataris.")], "Vulgar verb cleaned up for A1 learners"),
 ("lea", "Rends-le, Jean Gabin! Ce n'est pas vrai!",
  "Give it back, Jean Gabin! I cannot believe it!",
  [(165, "Rends-le, Jean Gabin !"),
   (166, "Merde, c'est pas vrai !")], "Swear word removed and negation normalized"),
 ("herve", "Noémie, sors de là!",
  "Noemie, get out of there!",
  [(167, "Noémie, sors de là !")], ""),
]

OPENER = "Let's examine how Noemie's curiosity leads to immediate chaos."

WALK = [
 (0, None,
  "'He would not pay in cash!' Herve expresses disbelief that an agency buyout would arrive in bank notes."),
 (1, None,
  "'Yes he would! The father-in-law owns real estate in Paris.' Noemie explains that Catherine's father has massive property holdings."),
 (2, None,
  "'When buyers purchase property, they pay in cash. That is well known.' She points out that luxury deals often involve cash."),
 (3, None,
  "'So it is cash.' Herve concedes that the bag might actually be filled with currency."),
 (4, None,
  "'That is how Mathias is going to become our boss.' Noemie dreams about Mathias taking over the agency."),
 (5, None,
  "'And I will become his right-hand woman.' She imagines herself as his indispensable deputy."),
 (6, None,
  "'Then he will ask you to marry him.' Herve teases her gently about her feelings for Mathias."),
 (7, None,
  "'You think so? No! I am going to take a look.' Flustered by the remark, she resolves to peek inside the bag."),
 (8, None,
  "'No, Noemie! Are you crazy? Be careful!' Herve warns her that sneaking into the office is reckless."),
 (9, None,
  "'Mathias knows that everything I do is for his own good.' She rationalizes her snooping as pure devotion."),
 (10, None,
  "'So he will reward my loyalty. Keep watch, okay?' Noemie orders Herve to guard the corridor."),
 (11, None,
  "'Jean Gabin! What? Jean Gabin is ruining the money!' Herve gasps as the dog damages the cash on the floor."),
 (12, None,
  "'Give it back, Jean Gabin! I cannot believe it!' Noemie desperately tries to rescue the bills from the puppy."),
 (13, None,
  "'Noemie, get out of there!' Herve urgently tells her to escape before anyone discovers the catastrophe."),
]

TRANSITION = "Now let's listen to the scene between Noemie and Hervé once more."

OUTRO = ("Noemie's secret inspection has ended in total catastrophe thanks to Jean Gabin the dog. Meanwhile, Andrea "
         "is meeting director Christophe Bel at a restaurant, striking a delicate deal to keep the plastic duck in "
         "the production while sparing Francois from entering the pool. See you in the next scene.")

CLOSING = ("herve", "Noémie, sors de là!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
