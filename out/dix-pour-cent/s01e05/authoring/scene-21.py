ID = "dix-pour-cent-s01e05-scene-21"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 5
SCENE = 21
TITLE = "Dîner pour deux dans la chambre seize  (Dinner for Two in Room Sixteen)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "receptionniste": "emilie", "gabriel": "theo"}
LABELS = {"lea": "Andréa", "receptionniste": "La réceptionniste", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E05"
SOURCE_FILE = "sources/dix-pour-cent/s01/e05.fr.dual.srt"

INTRO = ("The next morning at the country hotel near the film set, Gabriel stops at the reception desk. "
         "The receptionist is struggling with her computer, and when Gabriel leans over to help her, "
         "he spots something very interesting on the screen: dinner for two and champagne in room sixteen, Andréa's room. "
         "Curiosity gets the better of him, and he marches straight upstairs with a breakfast tray. "
         "Let's hear the scene in French first.")

STORY = [
 ("receptionniste", "Désolée, on a ce nouveau logiciel.", "Sorry, we have this new software.",
  [(421, "on a ce nouveau logiciel")], "'Désolé' written as feminine 'Désolée'"),
 ("gabriel", "Peut-être que je peux aider.", "Maybe I can help.",
  [(422, "Peut-être que je peux aider")], ""),
 ("receptionniste", "Merci, mais il faut un diplôme pour ça!",
  "Thank you, but you need a degree for this!",
  [(423, "Merci, mais il faut un diplôme pour ça")], ""),
 ("receptionniste", "Par exemple, dîner pour deux et champagne dans la chambre seize.",
  "For example, dinner for two and champagne in room sixteen.",
  [(425, "Par exemple, dîner pour deux et champagne dans la chambre")], "'16' written out as 'seize'"),
 ("gabriel", "Quelle chambre?", "Which room?", [(428, "Quelle chambre")], ""),
 ("gabriel", "C'est moi, ouvre-moi! C'est vraiment urgent.",
  "It's me, open up! It's really urgent.",
  [(430, "C'est moi, ouvre-moi"), (431, "C'est vraiment urgent")], ""),
 ("lea", "Je ne peux pas là. Quoi?", "I can't right now. What?",
  [(431, "Je ne peux pas là"), (432, "Quoi")], ""),
 ("gabriel", "Tu étais si fatiguée hier soir, j'étais inquiet. Tu vas mieux?",
  "You were so tired last night, I was worried. Are you feeling better?",
  [(434, "Tu étais si fatiguée hier soir, j'étais inquiet. Tu vas mieux")], ""),
 ("lea", "Oui, ça va.", "Yes, I'm fine.", [(436, "ça va")], "'Ouais' -> 'Oui'"),
 ("gabriel", "Tu avais une petite faim?", "Were you a little hungry?",
  [(437, "Tu avais une petite faim")], ""),
 ("lea", "Je ne pouvais pas dormir, alors j'ai travaillé et ça m'a donné faim.",
  "I couldn't sleep, so I worked and that made me hungry.",
  [(439, "dormir, alors j'ai travaillé et ça m'a donné faim")], "'Je n'arrivais pas à dormir' -> 'Je ne pouvais pas dormir'"),
 ("gabriel", "Arrête de raconter n'importe quoi!", "Stop talking nonsense!",
  [(441, "Arrête de raconter n'importe quoi")], ""),
 ("gabriel", "Je sais que tu n'étais pas seule hier soir. C'est qui?",
  "I know you weren't alone last night. Who is it?",
  [(442, "Je sais que tu n'étais pas seule hier soir. C'est qui")], ""),
 ("lea", "Tu me connais, jamais au travail!", "You know me, never at work!",
  [(445, "Tu me connais, jamais au")], "'boulot' -> 'travail'"),
 ("gabriel", "Je veux savoir. Je reste.", "I want to know. I'm staying.",
  [(446, "Je veux savoir. Je reste")], ""),
]

OPENER = "Let's walk through it. At the front desk, the receptionist apologises for the delay."

WALK = [
 (0, None,
  "'Sorry, we have this new software.' She uses the everyday word for 'we', and Gabriel offers a hand."),
 (1, None,
  "'Maybe I can help.' The word for 'maybe' literally means 'can be'."),
 (2, None,
  "'Thank you, but you need a degree for this!' The impersonal expression in the middle means 'it is necessary' or 'you need'."),
 (3, None,
  "'For example, dinner for two and champagne in room sixteen.' She points at an entry on the screen, and Gabriel's ears perk up."),
 (4, None,
  "'Which room?' The question word takes its feminine form to match 'room'. Seconds later, he is knocking on Andréa's door."),
 (5, None,
  "'It's me, open up! It's really urgent.' An informal command with 'to me' attached. Colette quickly hides in the bathroom before Andréa opens the door."),
 (6, None,
  "'I can't right now. What?' Andréa tries to block the doorway, but Gabriel walks right in carrying a tray."),
 (7, None,
  "'You were so tired last night, I was worried. Are you feeling better?' Both verbs at the start are in the past tense for states of mind. Notice that 'tired' is feminine for Andréa, and 'worried' is masculine for Gabriel."),
 (8, None,
  "'Yes, I'm fine.' Then Gabriel looks down at the two empty plates from the night before."),
 (9, None,
  "'Were you a little hungry?' Literally 'you had a little hunger?'. Andréa scrambles for an excuse."),
 (10, None,
  "'I couldn't sleep, so I worked and that made me hungry.' First the past tense for background ('I couldn't sleep'), then the past with 'have' for what she did next."),
 (11, None,
  "'Stop talking nonsense!' Gabriel doesn't believe a word of it."),
 (12, None,
  "'I know you weren't alone last night. Who is it?' He looks straight at the closed bathroom door."),
 (13, None,
  "'You know me, never at work!' Gabriel guesses it's an intern from the film crew, and Andréa protests."),
 (14, None,
  "'I want to know. I'm staying.' He sits down and refuses to budge until she tells him the truth."),
]

TRANSITION = "Now let's listen to the whole scene again."

OUTRO = ("Cornered in her hotel room with Colette hiding in the bathroom, Andréa has no choice left "
         "but to confess to Gabriel on the drive to the film set. See you next time.")
CLOSING = ("lea", "À bientôt!")
