# Authoring module for dix-pour-cent s01e05 scene 11 (cues 205-217).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-11.py --out out/dix-pour-cent/s01e05/scene-11.json

ID = "dix-pour-cent-s01e05-scene-11"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 11
TITLE = "Un pote dans la panade  (A Friend in Trouble)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "joey": "marcel"}
LABELS = {"lea": "Julie", "gabriel": "Gabriel", "joey": "JoeyStarr"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"
SOURCE_NOTE = ("Cues 205-217. Julie Gayet is the viewpoint character (lea). Andréa's line in cue 207 is given to "
               "Gabriel to stay within three speaking roles, and two short lines (9-10) make the visual action of "
               "the locked greenhouse door and the high window clear in audio.")

INTRO = ("Back in Paris, Mathias has just ordered Noémie to send apology flowers to the soap writer Marie-Sophie "
         "Garnier. Meanwhile, out at the chateau film set, Julie Gayet and JoeyStarr are still refusing to act "
         "together. To force them to talk, Andréa and Gabriel lure both stars into the old glass greenhouse in the "
         "park, fake an urgent phone call, and lock the door from the outside. Listen to the French first, without "
         "worrying about catching every word.")

STORY = [
 ("lea", "Comment on va parler avec eux là-bas?", "How are we going to talk with them in there?",
  [(205, "Comment"), (205, "parler avec"), (205, "là-bas")], "adapted from cue 205"),
 ("gabriel", "On a promis d'être là.", "We promised to be here.",
  [(206, "promis d'être là")], "pluperfect 'On avait promis' -> passé composé 'On a promis'"),
 ("gabriel", "Mais on n'a pas dit quand!", "But we didn't say when!",
  [(207, "Mais on n'a pas dit quand")], "Andréa's line given to Gabriel"),
 ("gabriel", "Allô? Oui, d'accord, j'arrive.", "Hello? Yes, okay, I'm on my way.",
  [(208, "Allô"), (209, "D'accord, j'arrive")], "'Ouais' -> 'Oui'"),
 ("gabriel", "Oui, tout de suite.", "Yes, right away.",
  [(210, "tout de suite")], "'Ouais' -> 'Oui'"),
 ("gabriel", "Un pote dans la panade. Je dois y aller.", "A mate in trouble. I have to go.",
  [(211, "Un pote dans la panade. Je dois y aller")], ""),
 ("joey", "Oui, bien sûr.", "Yes, of course.",
  [(212, "bien sûr")], "'Ouais' -> 'Oui'"),
 ("joey", "Mais je peux récupérer mon téléphone avant ton départ?", "But can I get my phone back before you leave?",
  [(213, "Je peux récupérer mon téléphone avant")], "subjunctive 'avant que tu partes' -> A1 'avant ton départ'"),
 ("lea", "La porte est fermée! Je ne veux pas rester ici.", "The door is locked! I don't want to stay here.",
  [], "new: Julie discovers they are locked in the greenhouse"),
 ("lea", "Regardez, il y a une fenêtre là-haut!", "Look, there's a window up there!",
  [], "new: Julie spots the high window and climbs the ladder"),
 ("joey", "Julie! Qu'est-ce que vous faites?", "Julie! What are you doing?",
  [(215, "Julie")], "as Julie climbs the ladder"),
 ("joey", "Attention, Julie!", "Careful, Julie!",
  [(216, "Julie")], "as Julie slips off the ladder"),
 ("gabriel", "Didier? Didier!", "Didier? Didier!",
  [(214, "Didier"), (215, "Didier")], "outside the greenhouse"),
 ("gabriel", "Qu'est-ce qui se passe?", "What's going on?",
  [(217, "Qu'est-ce qui se passe")], ""),
]

OPENER = ("Let's go through it line by line. First, outside the greenhouse, the agents set their trap.")

WALK = [
 (0, None,
  "'How are we going to talk with them in there?' After 'with', French uses the stressed pronoun for 'them'."),
 (1, None,
  "'We promised to be here.' The agents told their stars they would meet them in the greenhouse."),
 (2, None,
  "'But we didn't say when!' Inside the greenhouse, Gabriel pretends his phone is ringing."),
 (3, None,
  "'Hello? Yes, okay, I'm on my way.' Literally 'I arrive', which French uses for 'I am coming right now'."),
 (4, None,
  "'Yes, right away.' A three-word phrase you will hear constantly for 'immediately'."),
 (5, None,
  "'A mate in trouble. I have to go.' He uses casual slang for a friend and for being in a tight spot."),
 (6, None,
  "'Yes, of course.' JoeyStarr suspects nothing yet."),
 (7, None,
  "'But can I get my phone back before you leave?' Literally 'before your departure'. Instead of handing back the "
  "phone, Gabriel and Andréa slip out and turn the key in the lock."),
 (8, None,
  "'The door is locked! I don't want to stay here.' Julie rattles the handle in vain."),
 (9, None,
  "'Look, there's a window up there!' In her eighteenth-century silk gown, Julie starts climbing a wooden ladder "
  "toward a high window."),
 (10, None,
  "'Julie! What are you doing?' JoeyStarr rushes over beneath the ladder."),
 (11, None,
  "'Careful, Julie!' Too late: the ladder wobbles, and Julie falls straight down onto JoeyStarr with a loud crash."),
 (12, None,
  "'Didier? Didier!' Outside, Gabriel hears the commotion using JoeyStarr's real first name, Didier."),
 (13, None,
  "'What's going on?' Literally 'what is it that happens?'. The agents unlock the door and find both stars tangled "
  "on the floor."),
]

TRANSITION = "Now let's hear the whole greenhouse scene again."

OUTRO = ("So locking the two stars in the greenhouse only landed Julie on top of Didier with a bruised backside. "
         "Back in Paris, Mathias is about to clash with Arlette. See you in the next scene.")
CLOSING = ("lea", "Aïe, mon dos!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)], cwd=root))
