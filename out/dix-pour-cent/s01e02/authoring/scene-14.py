ID = "dix-pour-cent-s01e02-scene-14"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 2
SCENE = 14
TITLE = "Hélène veut vendre  (Hélène Wants to Sell)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "helene": "emilie", "mathias": "theo"}
LABELS = {"lea": "Andréa", "helene": "Hélène", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E02"
SOURCE_FILE = "sources/dix-pour-cent/s01/e02.fr.dual.srt"

INTRO = ("That evening, the agency's future is suddenly on the table. "
         "After his row with Andréa, Gabriel started to have doubts himself: he called Line Renaud to say he had "
         "reread the script, that it was really violent, and that he had got a bit carried away. "
         "Line didn't seem worried at all, and rushed off to the Lido. "
         "Then the four partners got a text: emergency meeting at nine, at the Westin hotel. "
         "Samuel's widow, Hélène Kerr, wants to see them. Andréa arrives at the hotel bar still on the phone "
         "with Gabor, the director, who thinks he's dying of a cold. "
         "Listen to it in French first; the gist is all you need.")

STORY = [
 ("lea", "Non, Gabor, tu ne vas pas mourir. Je t'appelle demain.", "No, Gabor, you're not going to die. I'll call you tomorrow.",
  [(396, "Non, Gabor, tu ne vas pas mourir"), (400, "Je t'appelle demain")], "cues 396 and 400"),
 ("lea", "Désolée. Je suis là.", "Sorry. I'm here.",
  [(402, "Désolée. Je suis là")], ""),
 ("mathias", "Hélène, vous pouvez compter sur nous.", "Hélène, you can count on us.",
  [(403, "Hélène"), (404, "vous pouvez compter sur nous")], "speaker not given in the cues; 'si vous avez besoin de quoi que ce soit' left out"),
 ("helene", "Merci. Samuel n'a pas laissé de testament.", "Thank you. Samuel didn't leave a will.",
  [(405, "Merci"), (408, "Samuel n'a pas laissé de testament")], ""),
 ("helene", "J'hérite donc de toutes ses parts.", "So I inherit all his shares.",
  [(409, "J'hérite donc de toutes ses parts")], ""),
 ("helene", "Je ne veux pas travailler à l'agence. Je veux vendre.", "I don't want to work at the agency. I want to sell.",
  [(412, "je veux vendre")], "first sentence simplifies cue 411"),
 ("lea", "À qui?", "To whom?",
  [(418, "À qui ?")], ""),
 ("helene", "Je ne sais pas. Au plus rapide.", "I don't know. To the quickest.",
  [(419, "Je ne sais pas"), (420, "Au plus rapide")], "'et au plus offrant' left out"),
 ("mathias", "On peut racheter les parts de Samuel.", "We can buy back Samuel's shares.",
  [(426, "On peut racheter les parts de Samuel")], ""),
 ("helene", "Que voulez-vous dire, on?", "What do you mean, we?",
  [(427, "Que voulez-vous dire")], "guillemets around 'on' removed"),
 ("mathias", "Nous. Nous quatre.", "Us. The four of us.",
  [(428, "Nous. Nous quatre")], ""),
 ("lea", "Moi, je n'ai rien. Je suis locataire.", "Me, I have nothing. I rent my flat.",
  [(430, "Moi j'ai rien"), (431, "je suis locataire")], "full negation 'je n'ai'; speaker not given in the cues"),
 ("mathias", "L'argent, ça se trouve.", "Money can always be found.",
  [(436, "L'argent, ça se trouve")], ""),
 ("lea", "C'est facile à dire quand on en a!", "That's easy to say when you have some!",
  [(437, "c'est facile à dire quand on en a")], "'Ouais' left out"),
 ("mathias", "Tu pourrais gagner plus.", "You could earn more.",
  [(438, "Tu pourrais gagner plus")], "'en faisant des choix artistiques différents' left out"),
 ("lea", "Avec des films nuls? Non, merci.", "With rubbish films? No, thank you.",
  [(440, "des films nuls")], "adapted from cue 440; 'Non, merci.' new"),
 ("mathias", "Tu préférerais qu'ASK disparaisse?", "Would you rather ASK disappeared?",
  [(444, "Tu préférerais qu'ASK disparaisse ?")], ""),
]

OPENER = ("Let's go back through it slowly. Andréa is still on the phone with Gabor, the director, who has a bad cold "
          "and is very dramatic about it.")

WALK = [
 (0, "Non, Gabor, tu ne vas pas mourir.",
  "'No, Gabor, you're not going to die.' The verb 'to go' plus another verb is the near future; here it's negative, "
  "so the two little words for 'not' wrap around the verb 'to go'."),
 (0, "Je t'appelle demain.",
  "'I'll call you tomorrow.' French often uses the present tense for a near plan like this."),
 (1, None,
  "'Sorry. I'm here.' The word for 'sorry' ends with an extra letter because Andréa is a woman. She hangs up and joins "
  "the others."),
 (2, None,
  "'Hélène, you can count on us.' Mathias uses the formal 'you' with Samuel's widow. It's polite, and a bit cold."),
 (3, None,
  "'Thank you. Samuel didn't leave a will.' After a negative, French uses a short little word before the noun, "
  "instead of 'a'. Samuel died suddenly, so nothing is written down."),
 (4, None,
  "'So I inherit all his shares.' The word in the middle means 'so' or 'therefore'. Samuel's part of the agency now "
  "belongs to her."),
 (5, None,
  "'I don't want to work at the agency. I want to sell.' Two sentences built the same way: the verb for 'want', then "
  "another verb in its basic form. First negative, then positive."),
 (6, None,
  "'To whom?' Two short words, and Andréa is already worried."),
 (7, None,
  "'I don't know. To the quickest.' Whoever pays fastest. Hélène doesn't care who the buyer is."),
 (8, None,
  "'We can buy back Samuel's shares.' Mathias has a plan. The word he uses for 'we' is the everyday spoken one, "
  "with the verb in the 'he or she' form."),
 (9, None,
  "'What do you mean, we?' Literally 'what do you want to say'. That's how French asks what someone means."),
 (10, None,
  "'Us. The four of us.' The four partners: Mathias, Andréa, Gabriel and Arlette."),
 (11, None,
  "'Me, I have nothing. I rent my flat.' Starting with the strong word for 'me' puts the focus on herself. Andréa "
  "doesn't own a home, so she has nothing to put in."),
 (12, None,
  "'Money can always be found.' Literally 'money, that finds itself'. Easy for Mathias, who is the richest of them."),
 (13, None,
  "'That's easy to say when you have some!' The small word just before the last verb means 'some of it', the money."),
 (14, None,
  "'You could earn more.' The ending on the verb makes it 'could'. Mathias thinks Andréa chooses her actors badly."),
 (15, None,
  "'With rubbish films? No, thank you.' The word for 'rubbish' is a very common way to say something is bad. Andréa "
  "would rather work with artists she believes in."),
 (16, None,
  "'Would you rather ASK disappeared?' A long sentence, but you can hear the key words: 'you would prefer' and the name "
  "of the agency. In the end it's Arlette who breaks the tension, joking that being sold would be a bit like having "
  "Mathias as their boss."),
]

TRANSITION = "Let's hear the whole meeting again, all in French."

OUTRO = ("That was a tough business meeting, and you got through it in French. "
         "Listen for 'I want to sell' when you watch: it changes everything for the agency. See you soon.")
CLOSING = ("lea", "Bonne soirée!")
