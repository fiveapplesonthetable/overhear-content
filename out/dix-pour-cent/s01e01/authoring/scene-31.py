ID = "dix-pour-cent-s01e01-scene-31"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 31
TITLE = "Je vous garde  (I'm Keeping You)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie"}
LABELS = {"lea": "Camille", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("While Mathias was phoning Miranda with the good news about Cécile, Camille was packing up her things. "
         "Remember, Andréa fired her for telling Cécile the truth about her age, on her very first day. "
         "But earlier, Andréa had also given her an almost impossible task: find out how much money Mathias was offered for one of his star actors. "
         "Camille found those figures anyway. Now she leaves them on Andréa's desk with a little note, and walks out. "
         "First, the whole scene in French. Relax and listen; nobody catches everything the first time.")

STORY = [
 ("lea", "Voilà. J'ai les chiffres que vous vouliez.", "There. I have the figures you wanted.",
  [(805, "J'ai les chiffres que vous vouliez")], "the note Camille leaves on the desk, read aloud; 'Voilà.' added"),
 ("lea", "Au revoir, Andréa.", "Goodbye, Andréa.", [], "new: she leaves without a word in the source"),
 ("andrea", "Je vous rappelle, d'accord?", "I'll call you back, okay?",
  [(806, "Je vous rappelle, d'accord")], "Andréa ends a phone call when she sees the note"),
 ("andrea", "Camille, attendez!", "Camille, wait!",
  [(807, "Camille, attendez")], ""),
 ("andrea", "Richard, bonjour! Le Tchekhov était fabuleux.", "Richard, hello! The Chekhov was fabulous.",
  [(809, "Richard, bonjour"), (810, "Le Tchekhov était fabuleux")], "she greets a man in the street while running after Camille"),
 ("lea", "Andréa? Mais je ne suis plus votre assistante.", "Andréa? But I'm not your assistant anymore.",
  [], "new: what Camille's face says when Andréa catches up"),
 ("andrea", "Bon, donnez-moi les chiffres.", "Okay, give me the figures.",
  [(812, "Bon, donnez-moi les chiffres")], ""),
 ("lea", "Tenez. Les voilà.", "Here. There they are.", [], "new: she hands them over"),
 ("lea", "Et alors?", "So?",
  [(813, "Et alors")], ""),
 ("andrea", "Je vous garde.", "I'm keeping you.",
  [(814, "Je vous garde")], ""),
 ("lea", "C'est sûr?", "Really? For sure?",
  [(815, "C'est sûr")], ""),
 ("andrea", "Oui, c'est sûr.", "Yes, for sure.",
  [(815, "Oui")], "'c'est sûr' added to Andréa's 'Oui'"),
 ("lea", "Oh, merci! Merci, Andréa!", "Oh, thank you! Thank you, Andréa!",
  [(816, "Merci")], "the swear word before 'Merci' left out"),
 ("lea", "Je veux tellement ce poste!", "I want this job so much!",
  [(817, "Je veux ce poste")], "'Je veux ce poste tellement fort' smoothed to the usual word order"),
 ("lea", "Je vais tout donner!", "I'm going to give it everything!",
  [(818, "Je vais tout donner")], ""),
 ("andrea", "Vous allez à votre bureau?", "Are you going to your desk?",
  [(820, "Vous allez à votre bureau")], "speaker attribution of 820-822 inferred from the dialogue"),
 ("lea", "Oui! Et comment!", "Yes! You bet!",
  [(821, "Oui"), (822, "Et comment")], ""),
]

OPENER = ("Let's take it slowly. Camille writes a short note, puts it on top of the figures, and quietly leaves.")

WALK = [
 (0, "Voilà.",
  "'There.' A tiny word for 'here it is' or 'that's it', and you'll hear it in every French conversation."),
 (0, "J'ai les chiffres que vous vouliez.",
  "'I have the figures you wanted.' Camille writes the formal 'you' to her boss. The last verb is in a past form that describes what someone wanted for a while."),
 (1, None,
  "'Goodbye, Andréa.' The standard polite goodbye, literally 'until seeing again'. Camille heads for the stairs. Andréa, on the phone, sees the note."),
 (2, None,
  "'I'll call you back, okay?' She hangs up fast. The verb is in the present tense, but it means something that will happen soon, which French does a lot."),
 (3, None,
  "'Camille, wait!' This is a command with the formal 'you': it's simply the formal present tense form, used without the word for 'you'. Andréa runs down the stairs after her."),
 (4, None,
  "'Richard, hello! The Chekhov was fabulous.' Even while running, Andréa greets a man she knows from the theatre and praises a play by Chekhov. She never stops being an agent."),
 (5, None,
  "'Andréa? But I'm not your assistant anymore.' Here, 'not anymore' is two little words around the verb: the first one, and then one that means 'more'."),
 (6, None,
  "'Okay, give me the figures.' Another formal command. The word for 'me' goes after the verb, joined with a hyphen, when you give an order."),
 (7, None,
  "'Here. There they are.' The first word is what you say when you hand something to someone you call by the formal 'you'."),
 (8, None,
  "'So?' Literally 'and then?'. Camille waits while Andréa reads, with her heart beating."),
 (9, None,
  "'I'm keeping you.' Just three words. The formal 'you' sits before the verb, the usual place for these small object words."),
 (10, None,
  "'Really? For sure?' Literally 'it's sure?'. Camille can't believe it."),
 (11, None,
  "'Yes, for sure.' Andréa means it. The firing is cancelled."),
 (12, None,
  "'Oh, thank you! Thank you, Andréa!' In the show, Camille also lets a rude word slip out of pure joy. We kept the thank-yous."),
 (13, None,
  "'I want this job so much!' The verb is 'to want', and the word in the middle makes it 'so much'."),
 (14, None,
  "'I'm going to give it everything!' Here's a really useful pattern: the verb 'to go' plus another verb gives you the near future, just like 'going to' in English."),
 (15, None,
  "'Are you going to your desk?' The verb 'to go' again, this time on its own, with the formal 'you'. Andréa is telling her, without saying it, to get back to work."),
 (16, None,
  "'Yes! You bet!' The last two words literally mean 'and how!', and they're a happy, very French way of saying 'absolutely'."),
]

TRANSITION = "Right, let's hear the whole scene once more, start to finish."

OUTRO = ("And that's how Camille got her job back. Don't worry if some lines went by quickly; "
         "you'll recognise the formal 'you' and the 'going to' future when you watch the episode. See you soon.")
CLOSING = ("lea", "À demain, Andréa!")
