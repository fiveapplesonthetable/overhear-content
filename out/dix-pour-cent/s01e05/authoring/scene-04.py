# Authoring module for dix-pour-cent s01e05 scene 04 (cues 68-88).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-04.py --out out/dix-pour-cent/s01e05/scene-04.json

ID = "dix-pour-cent-s01e05-scene-04"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 4
TITLE = "Tu as le trac?  (Have You Got Stage Fright?)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "joey": "theo", "assistant": "marcel"}
LABELS = {"lea": "Sofia", "joey": "JoeyStarr", "assistant": "L'assistant"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"

INTRO = ("Back in Paris, Camille has just turned twenty-three, and Mathias handed her a work envelope without "
         "remembering her birthday at all. "
         "Meanwhile, out in the countryside on the chateau film set, Sofia has arrived for her big day: a two-line "
         "part in the eighteenth-century costume drama opposite JoeyStarr and Julie Gayet. "
         "We'll hear the scene in French first; don't worry about catching every word.")

STORY = [
 ("lea", "J'ai une scène avec JoeyStarr!", "I have a scene with JoeyStarr!",
  [(68, "J'ai une scène avec JoeyStarr.")], ""),
 ("lea", "J'ai deux répliques, mais elles sont assez longues.", "I have two lines, but they're quite long.",
  [(69, "répliques"), (70, "Deux, mais elles sont assez longues.")], "cues 68-70 combined for Sofia"),
 ("assistant", "Julie attend. On est déjà en retard.", "Julie is waiting. We're already late.",
  [(74, "Julie attend. On est déjà en retard.")], ""),
 ("joey", "Elle peut attendre.", "She can wait.",
  [(75, "Elle peut attendre.")], ""),
 ("joey", "Salut! Tu fais quoi?", "Hi! What are you doing?",
  [(77, "Salut."), (78, "Tu fais quoi ?")], ""),
 ("lea", "Salut! Je joue une servante, comme toi.", "Hi! I'm playing a servant, like you.",
  [(77, "Salut."), (79, "je joue une servante, comme toi.")], ""),
 ("joey", "Je n'ai pas une scène avec toi?", "Don't I have a scene with you?",
  [(80, "une scène avec toi ?")], "'J'ai pas' expanded to 'Je n'ai pas'"),
 ("lea", "Si, c'est ça!", "Yes, that's right!",
  [(80, "Si, c'est ça !")], ""),
 ("joey", "Tu as le trac?", "Have you got stage fright?",
  [(81, "le trac ?")], "'T'as' expanded to 'Tu as'"),
 ("lea", "Non. Enfin, oui, beaucoup!", "No. Well, yes, a lot!",
  [(81, "Non. Enfin")], "'Si. Carrément!' -> 'oui, beaucoup!'"),
 ("assistant", "Joey, Julie s'énerve. Elle va quitter le plateau!",
  "Joey, Julie is getting angry. She's going to walk off the set!",
  [(83, "Joey, Julie s'énerve. Elle va quitter le plateau.")], ""),
 ("joey", "Dis-moi tes répliques.", "Tell me your lines.",
  [(84, "Dis-moi tes répliques.")], ""),
 ("lea", "Vraiment? D'accord.", "Really? Okay.",
  [(85, "Vraiment ?")], "'Okay' -> 'D'accord'"),
 ("lea", "Baissez les yeux devant la duchesse!", "Lower your eyes before the duchess!",
  [(86, "Baissez les yeux devant la duchesse !")], ""),
 ("lea", "Prenez garde! Elle peut vous coûter la vie!", "Beware! She could cost you your life!",
  [(87, "Prenez garde ! Elle"), (87, "vous coûter la vie !")], "'pourrait' -> 'peut'"),
 ("joey", "C'est très bien! Allez, on arrive.", "That's very good! Come on, we're on our way.",
  [(88, "on arrive.")], ""),
]

OPENER = ("Let's walk through it line by line. Sofia is in her eighteenth-century costume, talking excitedly in the dressing room.")

WALK = [
 (0, None,
  "'I have a scene with JoeyStarr!' Even a tiny role is a big deal when it's opposite the star."),
 (1, None,
  "'I have two lines, but they're quite long.' The word for an actor's lines in a script is feminine, so 'they' and 'long' take feminine plural endings."),
 (2, None,
  "'Julie is waiting. We're already late.' Outside at the coffee table, the assistant director tries to hurry JoeyStarr onto the set."),
 (3, None,
  "'She can wait.' JoeyStarr is in no hurry at all. Instead, he spots Sofia."),
 (4, None,
  "'Hi! What are you doing?' Casual and friendly, putting the question word at the end."),
 (5, None,
  "'Hi! I'm playing a servant, like you.' The feminine word for a servant has a feminine ending, while JoeyStarr plays a male servant."),
 (6, None,
  "'Don't I have a scene with you?' He asks a negative question, so listen to Sofia's first word."),
 (7, None,
  "'Yes, that's right!' There is the special word for 'yes' after a negative question."),
 (8, None,
  "'Have you got stage fright?' Literally 'do you have the stage fright?'. A great theatre expression to know."),
 (9, None,
  "'No. Well, yes, a lot!' First she tries to sound brave, then admits she is terrified."),
 (10, None,
  "'Joey, Julie is getting angry. She's going to walk off the set!' The assistant director is panicking, using 'is going to leave'."),
 (11, None,
  "'Tell me your lines.' JoeyStarr ignores the assistant and calmly offers to rehearse with Sofia."),
 (12, None,
  "'Really? Okay.' Sofia can hardly believe her luck, and takes a deep breath."),
 (13, None,
  "'Lower your eyes before the duchess!' She switches into grand eighteenth-century French, using the formal plural command."),
 (14, None,
  "'Beware! She could cost you your life!' Literally 'take guard!'. She gives it all the drama she has."),
 (15, None,
  "'That's very good! Come on, we're on our way.' JoeyStarr is impressed, and finally heads toward the set."),
]

TRANSITION = "Now let's hear the whole scene once more."

OUTRO = ("Sofia has rehearsed her two lines with JoeyStarr himself, while Julie Gayet is losing patience on the set. "
         "Listen out for that useful phrase meaning 'to have stage fright'. See you next time.")
CLOSING = ("lea", "Baissez les yeux devant la duchesse!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
