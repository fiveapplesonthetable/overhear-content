# Authoring module for dix-pour-cent s01e04 scene 07 (cues 193-210).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e04/authoring/scene-07.py --out out/dix-pour-cent/s01e04/scene-07.json

ID = "dix-pour-cent-s01e04-scene-07"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 7
TITLE = "Trop exotique ou pas assez  (Too Exotic or Not Enough)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Sofia", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("At the cafe, Mathias has just pitched Audrey Fleurot the role of an ecologist stripper in Augustin's film. "
         "Meanwhile, out on a Paris street, Gabriel is walking with Sofia, his newest client, while arguing on the "
         "phone with a casting director who has just turned her down for several roles in a row. "
         "We'll hear it in French first; don't worry about catching every word.")

STORY = [
 ("gabriel", "Et Sofia Leprince? Trop exotique?", "And Sofia Leprince? Too exotic?",
  [(193, "Et Sofia Leprince ?"), (193, "trop exotique.")], ""),
 ("gabriel", "Tu veux dire trop noire?", "Do you mean too black?",
  [(194, "Tu veux dire trop noire ?")], ""),
 ("gabriel", "Et pas assez exotique pour le rôle de la nounou?",
  "And not exotic enough for the part of the nanny?",
  [(195, "pas assez exotique pour la nounou.")], ""),
 ("gabriel", "Elle est trop blanche? Mais elle a du talent!", "She's too white? But she has talent!",
  [(197, "Trop blanche ?"), (199, "Elle a du talent !")], "cues 196-199 condensed cleanly"),
 ("gabriel", "Et pour le rôle de l'étudiante?", "And for the part of the student?",
  [(200, "L'étudiante")], "'L'étudiante qui écrit sa thèse?' simplified"),
 ("gabriel", "Non? D'accord, merci.", "No? Okay, thank you.",
  [(201, "Non")], "Gabriel hangs up on the casting director"),
 ("gabriel", "Sofia, tout le monde te trouve fantastique.", "Sofia, everyone thinks you're fantastic.",
  [(202, "Tout le monde te trouve fantastique.")], ""),
 ("lea", "Fantastique? Alors pourquoi je n'ai pas de rôle?", "Fantastic? Then why don't I get a part?",
  [(203, "Fantastique"), (204, "Alors pourquoi je ne")], "'je ne décroche rien' -> 'je n'ai pas de rôle'"),
 ("gabriel", "Tu commences juste. Les refus, c'est normal.", "You're just starting out. Rejections are normal.",
  [(205, "Les refus, c'est normal.")], "'Tu débutes à peine' -> 'Tu commences juste'"),
 ("lea", "Trois auditions ratées!", "Three failed auditions!",
  [(206, "Trois auditions ratées.")], ""),
 ("gabriel", "Tu sais combien d'auditions Cécile de France a ratées?",
  "Do you know how many auditions Cécile de France failed?",
  [(206, "Tu sais combien Cécile de France")], ""),
 ("lea", "Trois?", "Three?",
  [(207, "Trois ?")], ""),
 ("gabriel", "Euh, oui, trois. Mais courage, Sofia!", "Er, yes, three. But hang in there, Sofia!",
  [(207, "Trois ?")], ""),
]

OPENER = ("Let's walk through it. Gabriel is on the phone with a casting director, getting more annoyed by the second.")

WALK = [
 (0, None,
  "'And Sofia Leprince? Too exotic?' The word before 'exotic' means 'too' or 'too much'."),
 (1, None,
  "'Do you mean too black?' Literally 'you want to say too black?'. That's how French says 'you mean'. Notice the feminine ending on the colour word, for Sofia."),
 (2, None,
  "'And not exotic enough for the part of the nanny?' The two words before 'exotic' mean 'not enough'. Then the casting director says the opposite."),
 (3, None,
  "'She's too white? But she has talent!' For one role she is supposedly too dark, and for another too light. Gabriel is fed up with the excuses."),
 (4, None,
  "'And for the part of the student?' He tries one last character in the script, using the feminine word for a university student."),
 (5, None,
  "'No? Okay, thank you.' The casting director turns that down too, saying Sofia's background would become the whole story. Gabriel hangs up and turns to Sofia."),
 (6, None,
  "'Sofia, everyone thinks you're fantastic.' Literally 'finds you fantastic'. He tries to soften the blow."),
 (7, None,
  "'Fantastic? Then why don't I get a part?' After a negative verb, 'a part' becomes 'any part'."),
 (8, None,
  "'You're just starting out. Rejections are normal.' Literally 'the refusals, it's normal'."),
 (9, None,
  "'Three failed auditions!' The word at the end is the past form of a verb that means 'to miss' a train or 'to fail' an exam or audition."),
 (10, None,
  "'Do you know how many auditions Cécile de France failed?' Gabriel reaches for an inspiring example from his biggest star client."),
 (11, None,
  "'Three?' Sofia guesses the worst number she can think of."),
 (12, None,
  "'Er, yes, three. But hang in there, Sofia!' Clearly Cécile de France only ever failed three, so Gabriel's example backfires a little, though his heart is in the right place."),
]

TRANSITION = "Now let's hear the whole scene once more."

OUTRO = ("Sofia's first auditions with Gabriel haven't gone well, and right after this Mathias walks into the agency "
         "on the phone with Audrey, joking that if her dress is too small she shouldn't eat until tomorrow. "
         "Listen out for the words meaning 'too' and 'not enough'. See you next time.")
CLOSING = ("gabriel", "Tu as du talent, Sofia!")
