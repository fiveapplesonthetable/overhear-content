# Authoring module for dix-pour-cent s01e05 scene 06 (cues 103-115).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e05/authoring/scene-06.py --out out/dix-pour-cent/s01e05/scene-06.json

ID = "dix-pour-cent-s01e05-scene-06"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 6
TITLE = "Ça peut te valoir un César  (That Could Win You a César)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "julie": "emilie", "joey": "theo"}
LABELS = {"lea": "Andrea", "julie": "Julie", "joey": "JoeyStarr"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"

INTRO = ("Outside on the chateau set, Julie Gayet has just walked off into her trailer after JoeyStarr ruined his "
         "lines again, just as Andrea and Gabriel arrived from Paris. "
         "Now the two agents split up: Andrea goes inside Julie's dressing room to calm her down, while out in the "
         "courtyard JoeyStarr complains to Gabriel and the director Samir. "
         "We'll hear the scene in French first; don't worry about catching every word.")

STORY = [
 ("julie", "Je ne retourne pas sur ce plateau!", "I'm not going back onto that set!",
  [(103, "Je ne"), (103, "pas"), (103, "sur ce plateau")], "'Je ne remets pas les pieds sur ce plateau' simplified"),
 ("julie", "Il doit s'excuser avant!", "He has to apologise first!",
  [(103, "il")], "'tant qu'il ne s'est pas excusé' simplified"),
 ("julie", "J'ai travaillé dur pour ce rôle. J'ai étudié l'époque!",
  "I worked hard for this part. I studied the period!",
  [(104, "dur pour ce rôle"), (104, "l'époque")], "'J'ai bossé dur... j'ai fait des recherches sur l'époque' simplified"),
 ("julie", "Et lui, il improvise!", "And he just improvises!",
  [(105, "et lui il improvise !")], ""),
 ("lea", "Reste calme, Julie. Pense à ta carrière.", "Stay calm, Julie. Think of your career.",
  [(106, "Reste"), (106, "ta carrière.")], "'Reste concentrée sur toi, sur ta carrière' simplified"),
 ("lea", "Un film en costumes, c'est difficile à tourner.", "A costume drama is difficult to shoot.",
  [(107, "Un film en costumes"), (107, "difficile à tourner")], ""),
 ("lea", "Mais ça peut te valoir un César! Au minimum!", "But that could win you a Cesar! At least!",
  [(108, "Ça peut te valoir un César. Au minimum.")], ""),
 ("lea", "Ça vaut bien un petit effort.", "It's well worth a little effort.",
  [(109, "Ça vaut bien un petit effort.")], ""),
 ("julie", "Non, Andréa, c'est trop dur.", "No, Andrea, it's too hard.",
  [(110, "Non")], "Julie is still reluctant"),
 ("joey", "Vous avez entendu son accent, sa façon de parler?",
  "Have you heard her accent, her way of speaking?",
  [(111, "Vous avez entendu son accent, sa façon de parler ?")], ""),
 ("joey", "Elle se prend pour le prince Charles?", "Does she think she's Prince Charles?",
  [(112, "Elle se prend pour le prince Charles ?")], ""),
 ("joey", "Elle prend des cours de musique ancienne!", "She takes lessons in old music!",
  [(113, "de")], "retells cue 113 'le prof de clavecin'"),
 ("joey", "Elle dit toujours: oui, j'adore la musique de Bach!",
  "She always says: yes, I love Bach's music!",
  [(114, "Oui, j'adore"), (114, "de Bach.")], "'cette toccata de Bach' -> 'la musique de Bach'; vulgar cue 115 omitted"),
]

OPENER = ("Let's walk through it line by line. Inside her dressing room, Julie is pacing up and down.")

WALK = [
 (0, None,
  "'I'm not going back onto that set!' She uses the present tense for a firm refusal."),
 (1, None,
  "'He has to apologise first!' The verb for 'to apologise' literally means 'to excuse oneself'."),
 (2, None,
  "'I worked hard for this part. I studied the period!' Both sentences use the everyday past tense with 'have'."),
 (3, None,
  "'And he just improvises!' Notice the stressed word for 'him' at the start, used for contrast before 'he'."),
 (4, None,
  "'Stay calm, Julie. Think of your career.' Andrea tries to appeal to her ambition."),
 (5, None,
  "'A costume drama is difficult to shoot.' Literally 'a film in costumes'. And the verb for 'to turn' also means 'to shoot' a film."),
 (6, None,
  "'But that could win you a Cesar! At least!' The verb here means 'to be worth' or 'to earn you' something."),
 (7, None,
  "'It's well worth a little effort.' The same verb 'to be worth' in its third-person present form."),
 (8, None,
  "'No, Andrea, it's too hard.' Julie still isn't ready to forgive her co-star. Meanwhile, outside in the courtyard, JoeyStarr is complaining to Gabriel and Samir."),
 (9, None,
  "'Have you heard her accent, her way of speaking?' Literally 'her manner of speaking'."),
 (10, None,
  "'Does she think she's Prince Charles?' Literally 'she takes herself for Prince Charles?'. A very common French idiom when someone puts on airs."),
 (11, None,
  "'She takes lessons in old music!' In the episode, he complains about her harpsichord teacher."),
 (12, None,
  "'She always says: yes, I love Bach's music!' He puts on a grand voice to mock her love of classical music."),
]

TRANSITION = "Now let's hear the whole scene once more."

OUTRO = ("Andrea is dangling a Cesar award in front of Julie, while JoeyStarr is mocking her classical music lessons "
         "in the courtyard. Listen out for that verb meaning 'to be worth' or 'to win you'. See you next time.")
CLOSING = ("lea", "Pense au César, Julie!")

if __name__ == "__main__":
    import subprocess, sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[4]
    out = Path(__file__).resolve().parents[1] / f"scene-{SCENE:02d}.json"
    sys.exit(subprocess.call([sys.executable, str(root / "tools/compose.py"), __file__, "--out", str(out)]))
