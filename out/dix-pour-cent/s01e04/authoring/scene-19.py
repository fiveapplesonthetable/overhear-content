ID = "dix-pour-cent-s01e04-scene-19"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 4
SCENE = 19
TITLE = "Le chagrin de Noémie  (Noémie's Heartbreak)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "herve": "theo", "mathias": "marcel"}
LABELS = {"lea": "Noémie", "herve": "Hervé", "mathias": "Mathias"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E04"
SOURCE_FILE = "sources/dix-pour-cent/s01/e04.fr.dual.srt"

INTRO = ("At Mathias's house, Catherine walked in on Hippolyte and Camille and warmly invited Camille to stay for "
         "dinner, saying Mathias was out at a film screening. Back at the agency, though, Mathias is just leaving "
         "for the evening and admits to Noémie that he doesn't feel like going to the screening at all. When he "
         "forgets his phone on her desk, a message pops up on the screen and breaks Noémie's heart. "
         "Let's listen to the scene in French first; don't worry about catching every word.")

STORY = [
 ("lea", "Bon, je m'en vais. Profitez bien de la projection.", "Right, I'm leaving. Enjoy the screening.",
  [(474, "Bon, je m'en vais. Profitez bien de la projection")], ""),
 ("mathias", "Je n'en ai vraiment pas envie. À demain.", "I really don't feel like it. See you tomorrow.",
  [(475, "Je n'en ai vraiment pas envie"), (476, "À demain")], ""),
 ("lea", "Oui, Mathias.", "Yes, Mathias.",
  [(476, "Oui, Mathias")], ""),
 ("lea", "Il a oublié son téléphone. Mathias!", "He forgot his phone. Mathias!",
  [(477, "Il a oublié son téléphone"), (478, "Mathias")], ""),
 ("lea", "Contrat envoyé par e-mail. Une nouvelle aventure commence.",
  "Contract sent by email. A new adventure begins.",
  [(479, "Contrat envoyé par e-mail. Une nouvelle aventure commence")],
  "Noémie reads the text message on Mathias's screen; guillemets removed"),
 ("mathias", "Quoi? Oh, merci. À demain, Noémie.", "What? Oh, thanks. See you tomorrow, Noémie.",
  [(480, "Quoi ? Oh, merci"), (481, "À demain")], "'Noémie' added to avoid duplicating line 1"),
 ("herve", "Noémie? Qu'est-ce qu'il y a?", "Noémie? What's wrong?",
  [(482, "Noémie"), (484, "Qu'est-ce qu'il y a")], ""),
 ("lea", "Je ne comprends pas. C'est Mathias.", "I don't understand. It's Mathias.",
  [(485, "Je ne comprends pas"), (486, "C'est Mathias")], ""),
 ("lea", "Il part avec toutes ses stars à StarMédia.", "He's leaving with all his stars for StarMédia.",
  [(487, "Il part, avec toutes ses stars")], "'Starmédia' capitalised as 'StarMédia'"),
 ("lea", "Il ne m'a même pas demandé de venir avec lui.", "He didn't even ask me to come with him.",
  [(488, "Il ne m'a même pas demandé de venir avec lui")], ""),
 ("lea", "Il m'abandonne.", "He's abandoning me.",
  [(489, "Il m'abandonne")], ""),
 ("lea", "Je ne suis rien pour lui.", "I'm nothing to him.",
  [], "cue 490 ('Je suis une merde') retold cleanly"),
 ("herve", "Mais non, Noémie.", "Of course not, Noémie.",
  [(491, "Non")], "expanded from 'Non'"),
 ("lea", "Je veux mourir, Hervé.", "I want to die, Hervé.",
  [(492, "Je veux mourir, Hervé")], ""),
]

OPENER = ("Let's go through it slowly. At the end of the day, Noémie says goodbye to Mathias.")

WALK = [
 (0, "Bon, je m'en vais.",
  "'Right, I'm leaving.' Literally 'I go away from here': a very common everyday way to say you are heading off."),
 (0, "Profitez bien de la projection.",
  "'Enjoy the screening.' A polite command using the formal 'you', which Noémie always uses with Mathias at the office."),
 (1, None,
  "'I really don't feel like it. See you tomorrow.' Literally 'I really don't have the desire of it'. That is why Mathias is about to go straight home instead."),
 (2, None,
  "'Yes, Mathias.' Quiet and devoted as always."),
 (3, None,
  "'He forgot his phone. Mathias!' The verb 'to forget' in the everyday past tense. She runs after him to give it back."),
 (4, None,
  "'Contract sent by email. A new adventure begins.' She glances at the screen and sees a message from the rival agency StarMédia."),
 (5, None,
  "'What? Oh, thanks. See you tomorrow, Noémie.' Mathias takes his phone back without realising she read the message."),
 (6, None,
  "'Noémie? What's wrong?' A moment later, Hervé finds her crying in the agency washroom."),
 (7, None,
  "'I don't understand. It's Mathias.' The negative wraps around the verb 'understand'."),
 (8, None,
  "'He's leaving with all his stars for StarMédia.' Present tense used for something about to happen."),
 (9, None,
  "'He didn't even ask me to come with him.' Notice the word for 'even' placed right after the negative word."),
 (10, None,
  "'He's abandoning me.' The little word for 'me' shortens before the vowel of the verb."),
 (11, None,
  "'I'm nothing to him.' In the negative, the second little word means 'nothing'."),
 (12, None,
  "'Of course not, Noémie.' Hervé tries to comfort her."),
 (13, None,
  "'I want to die, Hervé.' Poor Noémie is always dramatic when it comes to Mathias."),
]

TRANSITION = "Now let's hear the whole scene again from start to finish."

OUTRO = ("Noémie now knows that Mathias has signed his contract with StarMédia—and worse for her, he didn't ask her to "
         "follow him. Meanwhile, since Mathias skipped the screening, he is heading straight home, where Camille is "
         "sitting at his dinner table. See you in the next scene.")
CLOSING = ("herve", "Courage, Noémie!")
