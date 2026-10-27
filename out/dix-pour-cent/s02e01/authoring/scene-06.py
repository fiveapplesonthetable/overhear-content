# Authoring module for dix-pour-cent s02e01 scene 06 (cues 124-149, incorporating merged scene 05).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e01/authoring/scene-06.py --out out/dix-pour-cent/s02e01/scene-06.json

ID = "dix-pour-cent-s02e01-scene-06"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 1
SCENE = 6
TITLE = "Panique et rumeurs  (Panic and Rumors)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "arlette": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Noémie", "arlette": "Arlette", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E01"
SOURCE_FILE = "sources/dix-pour-cent/s02/e01.fr.dual.srt"
SOURCE_NOTE = ("Cues 124-149. Arlette spots rival Francois Brehier dining with Helene Kerr at Mansart. "
               "Meanwhile, Gabriel and Noemie examine the paparazzi photo of Virginie Efira in a gossip magazine. "
               "Arlette arrives at ASK to warn the team of a hostile takeover. Adapted for A1 French.")

INTRO = ("Outside the Mansart restaurant, senior agent Arlette spots their ruthless rival Francois Brehier dining with "
         "Samuel Kerr's widow. Meanwhile at the ASK agency, Gabriel and Noemie examine a sensational gossip magazine "
         "revealing Virginie Efira's secret lover. Let's listen to the scene in French first.")

STORY = [
 ("arlette", "C'est le directeur de StarMedia avec la femme de Samuel Kerr.",
  "That is the director of StarMedia with Samuel Kerr's wife.",
  [(124, "C'est pas le directeur de StarMedia,"),
   (125, "avec la femme de Samuel Kerr ?")], "Arlette spots their rival outside the restaurant"),
 ("gabriel", "Elle trompe Ramzy? Ce n'est pas possible.",
  "She is cheating on Ramzy? That is not possible.",
  [(128, "-Elle trompe Ramzy ? -Non.")], "Gabriel examines the scandalous gossip magazine"),
 ("lea", "Elle le quitte? Des histoires de couple, c'est ma veine.",
  "She is leaving him? Couple dramas are just my luck.",
  [(130, "Elle le quitte ?"),
   (131, "Ne me demande pas. Des histoires de couple, c'est ma veine.")], ""),
 ("gabriel", "On sait qui est le type sur la photo?",
  "Do we know who the guy in the photo is?",
  [(132, "On sait qui est le type ?")], ""),
 ("lea", "Un mètre soixante-quinze, plutôt poilu, beau postérieur... C'est toi, Gabriel?",
  "Five feet nine, quite hairy, nice rear... Is it you, Gabriel?",
  [(133, "Un mètre soixante-quinze,"),
   (134, "plutôt poilu, beau postérieur,"),
   (135, "léger bourrelet... C'est toi, Gabriel ?")], "Noemie teases Gabriel about the blurry photograph"),
 ("gabriel", "Une rupture pendant la sortie du film, c'est mauvais pour nous.",
  "A breakup during the film release is bad for us.",
  [(136, "Une rupture pendant la sortie du film, c'est mauvais pour nous.")], ""),
 ("lea", "Au contraire, ça va faire le buzz! C'est pimenté!",
  "On the contrary, it will create buzz! It is spicy!",
  [(137, "Au contraire, ça va faire le buzz."),
   (138, "C'est pimenté !")], ""),
 ("gabriel", "Noémie! Je parle d'image, pas de buzz.",
  "Noemie! I am talking about image, not buzz.",
  [(139, "Noémie !"),
   (140, "Je parle d'image, pas de buzz.")], ""),
 ("gabriel", "Des acteurs qui se séparent, c'est un désastre. Le film va faire un bide.",
  "Actors splitting up is a disaster. The movie is going to flop.",
  [(141, "Des acteurs qui se séparent, c'est un désastre en termes de comm."),
   (142, "Le film va faire un bide.")], "Omitted colloquial 'en termes de comm'"),
 ("arlette", "Il ne manquait plus que ça! Tout va mal ce matin.",
  "That is the last thing we needed! Everything is going wrong this morning.",
  [(144, "Il ne manquait plus que ça.")], "Arlette bursts into the office with alarming news"),
 ("gabriel", "Comment ça? Qu'est-ce qui se passe?",
  "What do you mean? What is happening?",
  [(145, "Comment ça ?")], ""),
 ("arlette", "Je viens de voir François Bréhier avec Hélène Kerr chez Mansart.",
  "I just saw Francois Brehier with Helene Kerr at Mansart.",
  [(146, "Je viens de voir François Bréhier avec Hélène Kerr."),
   (147, "Chez Mansart. Ça ne me plaît pas.")], ""),
 ("lea", "Il veut nous racheter? C'est notre plus grand rival!",
  "He wants to buy us out? He is our biggest rival!",
  [(148, "Il veut nous racheter ?")], "Noemie realizes the danger of a hostile buyout"),
 ("arlette", "Bréhier est un charognard. Il ferait n'importe quoi pour nous couler.",
  "Brehier is a scavenger. He would do anything to sink us.",
  [(149, "Bréhier est un charognard.")], "Cleaned vulgar idiom to standard French"),
]

OPENER = "Let's examine how rumors and rivalries threaten the agency step by step."

WALK = [
 (0, None,
  "'That is the director of StarMedia with Samuel Kerr\\'s wife.' Arlette recognizes their bitter competitor holding a private lunch."),
 (1, None,
  "'She is cheating on Ramzy? That is not possible.' Gabriel is shocked by the tabloid headline about their star couple."),
 (2, None,
  "'She is leaving him? Couple dramas are just my luck.' Noemie remarks on the constant relationship trouble at the agency."),
 (3, None,
  "'Do we know who the guy in the photo is?' Gabriel tries to identify the mystery lover in the blurry picture."),
 (4, None,
  "'Five feet nine, quite hairy, nice rear... Is it you, Gabriel?' Noemie jokes that the physical description matches Gabriel."),
 (5, None,
  "'A breakup during the film release is bad for us.' Gabriel points out that bad personal publicity hurts box office sales."),
 (6, None,
  "'On the contrary, it will create buzz! It is spicy!' Noemie argues that scandal attracts media attention."),
 (7, None,
  "'Noemie! I am talking about image, not buzz.' Gabriel insists that prestige and trust matter more than gossip."),
 (8, None,
  "'Actors splitting up is a disaster. The movie is going to flop.' The idiom faire un bide means to fail completely at the cinema."),
 (9, None,
  "'That is the last thing we needed! Everything is going wrong this morning.' Arlette announces that an even bigger crisis is brewing."),
 (10, None,
  "'What do you mean? What is happening?' Gabriel asks for clarification about her warning."),
 (11, None,
  "'I just saw Francois Brehier with Helene Kerr at Mansart.' The construction venir de followed by an infinitive indicates a recent action."),
 (12, None,
  "'He wants to buy us out? He is our biggest rival!' Noemie expresses immediate alarm at StarMedia acquiring their shares."),
 (13, None,
  "'Brehier is a scavenger. He would do anything to sink us.' The metaphor charognard describes someone who preys ruthlessly on the vulnerable."),
]

TRANSITION = "Now let's listen to the entire conversation once more from start to finish."

OUTRO = ("Arlette's discovery confirms the agents' worst fears: Francois Brehier is actively trying to buy out ASK while "
         "Virginie and Ramzy's romance unravels. Mathias immediately gathers all the partners in the conference room "
         "for an emergency financial meeting. See you in the next scene.")

CLOSING = ("arlette", "Bréhier est un charognard.")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
