# Authoring module for dix-pour-cent s02e02 scene 06 (cues 177-196).
# Build: python3 tools/compose.py out/dix-pour-cent/s02e02/authoring/scene-06.py --out out/dix-pour-cent/s02e02/scene-06.json

ID = "dix-pour-cent-s02e02-scene-06"
SHOW = "dix-pour-cent"
SEASON = 2
EPISODE = 2
SCENE = 6
TITLE = "Le rôle de Dario  (The Role of Dario)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "dario": "marcel"}
LABELS = {"lea": "Noémie", "mathias": "Mathias", "dario": "Dario"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S02E02"
SOURCE_FILE = "sources/dix-pour-cent/s02/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 177-196. Noemie explains her beaver totem animal to Mathias. "
               "Mathias presents an exciting supporting film role opposite Guy Marchand "
               "to young actor Dario. Adapted for A1 French.")

INTRO = ("Inside Mathias's office, Noemie enthusiastically shares the spiritual revelations she gained from her shaman. "
         "Mathias quickly steers the conversation back to work as young actor Dario arrives to discuss a major film audition. "
         "Let's listen to the scene in French first.")

STORY = [
 ("mathias", "Le contrat pour Nathalie Baye est prêt?",
  "Is the contract for Nathalie Baye ready?",
  [(177, "Le contrat pour Nathalie Baye est prêt ?")], ""),
 ("lea", "C'est vraiment incroyable, en fait. Il m'a ouvert les yeux.",
  "It is really incredible, actually. He opened my eyes.",
  [(178, "C'est vraiment incroyable, en fait."),
   (179, "Il m'a vraiment ouvert les yeux.")], ""),
 ("lea", "Grâce à lui, j'ai découvert mon animal totem.",
  "Thanks to him, I discovered my totem animal.",
  [(180, "Grâce à lui, j'ai découvert mon animal totem.")], ""),
 ("lea", "Le castor! Oui, Mathias, je viens d'une famille de bâtisseurs!",
  "The beaver! Yes, Mathias, I come from a family of builders!",
  [(181, "Le castor."),
   (182, "je viens d'une famille de bâtisseurs !")], ""),
 ("mathias", "Guy Marchand est en tête d'affiche.",
  "Guy Marchand has top billing.",
  [(184, "Guy Marchand est en tête d'affiche.")], ""),
 ("dario", "D'accord, super! C'est quel genre d'histoire?",
  "Okay, great! What kind of story is it?",
  [(184, "-D'accord."),
   (186, "-Super !")], ""),
 ("mathias", "Tu es Dario, le cheminot et second rôle.",
  "You are Dario, the railway worker and supporting role.",
  [(185, "Tu es Dario, le cheminot et second rôle.")], ""),
 ("mathias", "C'est un jeune idéaliste engagé politiquement.",
  "He is a young politically committed idealist.",
  [(187, "C'est un jeune idéaliste engagé politiquement,")], ""),
 ("mathias", "Il n'est pas très à l'aise avec les filles...",
  "He is not very comfortable with girls...",
  [(188, "pas très à l'aise avec les filles...")], ""),
 ("dario", "Alors tu as pensé à moi!",
  "So you thought of me!",
  [(189, "Alors tu as pensé à moi !")], ""),
 ("mathias", "Exactement! Tu as le profil idéal.",
  "Exactly! You have the ideal profile.",
  [(190, "Exactement !")], ""),
 ("mathias", "Noémie s'est battue pour te décrocher l'audition.",
  "Noemie fought hard to land you the audition.",
  [(191, "pour te décrocher l'audition.")], "Adapted vulgar expression to clean A1 French"),
 ("dario", "Eh bien, merci beaucoup! Au revoir!",
  "Well, thank you very much! Goodbye!",
  [(193, "Eh bien, merci."),
   (196, "Au revoir.")], ""),
]

OPENER = "Let's examine how Mathias pitches the film role to his client step by step."

WALK = [
 (0, None,
  "'Is the contract for Nathalie Baye ready?' Mathias asks his assistant for an urgent legal document."),
 (1, None,
  "'It is really incredible, actually. He opened my eyes.' The idiom ouvrir les yeux means to bring clarity or revelation."),
 (2, None,
  "'Thanks to him, I discovered my totem animal.' Noemie explains her mystical discovery with the shaman."),
 (3, None,
  "'The beaver! Yes, Mathias, I come from a family of builders!' The noun batisseur refers to someone who builds structures."),
 (4, None,
  "'Guy Marchand has top billing.' The expression tete d\\'affiche refers to the headline star of a movie."),
 (5, None,
  "'Okay, great! What kind of story is it?' Dario is thrilled to hear about the prestigious cast."),
 (6, None,
  "'You are Dario, the railway worker and supporting role.' The noun cheminot refers to a railroad worker."),
 (7, None,
  "'He is a young politically committed idealist.' Mathias outlines the character's intellectual background."),
 (8, None,
  "'He is not very comfortable with girls...' The idiom etre a l\\'aise means to feel comfortable or at ease."),
 (9, None,
  "'So you thought of me!' Dario jokes about matching the socially awkward character description."),
 (10, None,
  "'Exactly! You have the ideal profile.' Mathias affirms that Dario fits the casting requirements perfectly."),
 (11, None,
  "'Noemie fought hard to land you the audition.' The verb decrocher means to obtain or win a hard-to-get opportunity."),
 (12, None,
  "'Well, thank you very much! Goodbye!' Dario politely thanks his agent and takes his leave."),
]

TRANSITION = "Now let's listen to the pitch meeting once more from beginning to end."

OUTRO = ("Dario leaves delighted with the film opportunity, while Noemie continues to reflect on her spirit animal. "
         "On his way out of the building, Mathias steps into the elevator with his son Hippolyte. "
         "See you in the next scene.")

CLOSING = ("dario", "Eh bien, merci beaucoup! Au revoir!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
