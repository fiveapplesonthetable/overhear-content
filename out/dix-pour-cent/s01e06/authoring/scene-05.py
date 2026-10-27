# Authoring module for dix-pour-cent s01e06 scene 05 (cues 119-144).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e06/authoring/scene-05.py --out out/dix-pour-cent/s01e06/scene-05.json

ID = "dix-pour-cent-s01e06-scene-05"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 6
SCENE = 5
TITLE = "Un casting pour Luc Besson!  (An Audition for Luc Besson!)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E06"
SOURCE_FILE = "sources/dix-pour-cent/s01/e06.fr.dual.srt"
SOURCE_NOTE = ("Cues 119-144. Andrea promises to keep Francois's swimming secret safe. "
               "Meanwhile, at the ASK reception desk, Gabriel surprises Sofia with huge news: he has secured "
               "her an audition for a major supporting role in Luc Besson's next film. The only catch is that "
               "the character must dance hip-hop. Sofia enthusiastically accepts, and Gabriel tells her to get the "
               "music files from Hervé in strict confidence.")

INTRO = ("After promising Francois that his swimming phobia will stay strictly between them, Andrea heads back to work. "
         "Across the hallway at the reception desk, Gabriel approaches Sofia with an exciting opportunity that could "
         "transform her acting career. Let's listen to the scene in French first.")

STORY = [
 ("gabriel", "Tu danses?",
  "Do you dance?",
  [(121, "Tu danses ?")], ""),
 ("lea", "Pourquoi? Tu m'invites à sortir?",
  "Why? Are you asking me out?",
  [(122, "Pourquoi ? Tu m'invites à sortir ?")], ""),
 ("gabriel", "Non, mieux que ça. Un casting pour un film!",
  "No, better than that. An audition for a film!",
  [(123, "Non, mieux que ça. Un casting pour un film !")], ""),
 ("lea", "C'est quoi?",
  "What is it?",
  [(124, "C'est quoi ?")], ""),
 ("gabriel", "Je dis Luc, je dis Besson, je dis Luc Besson!",
  "I say Luc, I say Besson, I say Luc Besson!",
  [(125, "Je dis Luc, je dis Besson, je dis Luc Besson !")], ""),
 ("gabriel", "J'ai pensé à toi.",
  "I thought of you.",
  [(126, "J'ai pensé à toi")], ""),
 ("lea", "Pour de vrai?",
  "For real?",
  [(127, "Pour de vrai ?")], ""),
 ("gabriel", "Oui! Le second rôle, avec un cachet formidable!",
  "Yes! The supporting role, with a huge paycheck!",
  [(127, "Ouais."),
   (128, "Le second rôle"),
   (128, "Avec un cachet de folie")], "Colloquial phrasing adapted for A1 French"),
 ("gabriel", "Une fille magnifique, pleine d'énergie... Et qui danse le hip-hop!",
  "A gorgeous girl, full of energy... And who dances hip-hop!",
  [(131, "Et qui danse... le hip-hop !")], "Slang in cues 129-130 simplified"),
 ("lea", "Elle danse le hip-hop?",
  "She dances hip-hop?",
  [(132, "Elle danse le hip-hop ?")], ""),
 ("gabriel", "Oui! C'est toi, non?",
  "Yes! That is you, isn't it?",
  [(133, "Ouais ! C'est toi, non ?")], ""),
 ("lea", "Oui, oui... C'est tout à fait moi, oui.",
  "Yes, yes... That is completely me, yes.",
  [(134, "Ouais, ouais... C'est tout à fait moi, ouais.")], "Informal 'ouais' normalized to 'oui'"),
 ("gabriel", "Va voir Hervé. Il te donnera les paroles et la musique. Mais bouche cousue, c'est top secret!",
  "Go see Hervé. He will give you the lyrics and the music. But keep quiet, it is top secret!",
  [(135, "Va voir Hervé."),
   (136, "Il te filera les paroles"),
   (137, "Mais surtout, bouche cousue ! C'est top secret !")], "Slang 'filera' adapted to 'donnera'"),
]

OPENER = "Let's follow Gabriel's surprise announcement step by step as we go."

WALK = [
 (0, None,
  "'Do you dance?' Gabriel opens with a sudden question about her movement skills."),
 (1, None,
  "'Why? Are you asking me out?' Sofia jokes about whether he is inviting her on a date."),
 (2, None,
  "'No, better than that. An audition for a film!' He replies that his news is much more exciting than dinner."),
 (3, None,
  "'What is it?' Sofia eagerly asks for more details about the mystery production."),
 (4, None,
  "'I say Luc, I say Besson, I say Luc Besson!' Gabriel reveals the director's name with theatrical flair."),
 (5, None,
  "'I thought of you.' The past tense shows that Sofia was his immediate first choice for the part."),
 (6, None,
  "'For real?' Sofia is stunned and checks whether he is truly serious."),
 (7, None,
  "'Yes! The supporting role, with a huge paycheck!' Gabriel confirms that the role is prominent and well paid."),
 (8, None,
  "'A gorgeous girl, full of energy... And who dances hip-hop!' He describes the character's vibrant urban style."),
 (9, None,
  "'She dances hip-hop?' Sofia repeats the condition with a touch of uncertainty."),
 (10, None,
  "'Yes! That is you, isn't it?' Gabriel assumes that Sofia already knows how to dance hip-hop."),
 (11, None,
  "'Yes, yes... That is completely me, yes.' Eager for the chance, Sofia quickly claims the role fits her perfectly."),
 (12, None,
  "'Go see Herve. He will give you the lyrics and the music. But keep quiet, it is top secret!' Gabriel sends her to his assistant and swears her to secrecy."),
]

TRANSITION = "Now let's listen to Gabriel and Sofia's conversation once more."

OUTRO = ("Sofia has just landed the audition of a lifetime with director Luc Besson, even if her hip-hop dancing skills "
         "might require some urgent improvisation. In the next room, Hervé and Noemie are watching a suspicious luxury "
         "bag on Mathias's desk. See you in the next scene.")

CLOSING = ("lea", "C'est tout à fait moi, oui.")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
