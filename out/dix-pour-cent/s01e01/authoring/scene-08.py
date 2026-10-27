ID = "dix-pour-cent-s01e01-scene-08"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 8
TITLE = "Andréa engage Camille  (Andréa Hires Camille)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "andrea": "emilie"}
LABELS = {"lea": "Camille", "andrea": "Andréa"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Down at reception, Andréa is looking for a new assistant, fast. "
         "Since we last saw her, she fired Magali before Magali could quit, then offered the job to Sofia, the receptionist. "
         "Sofia said no thank you: she only works here part-time, she's really an actress, and she even invited Andréa to her play. "
         "Andréa wasn't interested. And then she notices the young woman from the south who has been waiting in reception all morning: Camille. "
         "She takes her outside and fires questions at her. We stay with Camille. "
         "As usual, French first, and you really don't need every word.")

STORY = [
 ("andrea", "Tu viens, oui ou non?", "Are you coming or not?",
  [(251, "Tu viens, oui ou non ?")], ""),
 ("andrea", "Tu viens d'où?", "Where are you from?",
  [(252, "Tu viens d'où ?")], ""),
 ("lea", "Je viens de la Côte d'Azur. Près de Cannes.", "I'm from the Côte d'Azur. Near Cannes.",
  [(253, "Je viens... de la Côte d'Azur"), (254, "Près de Cannes")], "pause dots removed"),
 ("andrea", "Cannes? Tu as travaillé au festival?", "Cannes? Did you work at the festival?",
  [(255, "Cannes ? Tu as travaillé au festival ?")], ""),
 ("lea", "Oui, exactement. Le Festival de Cannes.", "Yes, exactly. The Cannes Film Festival.",
  [(256, "Oui, exactement. Le Festival de Cannes")], ""),
 ("andrea", "Pour faire quoi?", "Doing what?",
  [(257, "Pour faire quoi ?")], ""),
 ("lea", "Ça dépend. Au début, j'étais dans les sous-vêtements des stars.", "It depends. At first, I was in the stars' underwear department.",
  [(258, "Ça dépend. Au début"), (259, "J'étais dans les sous-vêtements"), (260, "des stars")], "cues 258-260 joined"),
 ("lea", "Ne pleurez pas, on va arranger ça!", "Don't cry, we're going to fix this!",
  [(264, "Pleurez pas. On va arranger ça")], "'Pleurez pas' -> 'Ne pleurez pas'; what she told the stars"),
 ("andrea", "Tu as un petit ami?", "Have you got a boyfriend?",
  [(270, "Tu as un petit ami ?")], ""),
 ("lea", "Non.", "No.",
  [(270, "Non")], ""),
 ("andrea", "Des amis à Paris?", "Friends in Paris?",
  [(272, "Des amis à Paris ?")], ""),
 ("lea", "Non, je viens d'arriver. Mon père, mais c'est compliqué.", "No, I've just arrived. My dad, but it's complicated.",
  [(273, "Non, je viens d'arriver"), (274, "Mon père, mais c'est compliqué")], ""),
 ("andrea", "Tu t'occupes de lui?", "Do you look after him?",
  [(275, "Tu t'occupes de lui ?")], ""),
 ("lea", "Hors de question!", "No way!",
  [(276, "Hors de question")], ""),
 ("andrea", "Je peux t'appeler à quatre heures du matin? Tu travailles le dimanche?", "Can I call you at four in the morning? Do you work on Sundays?",
  [(278, "Je peux t'appeler"), (278, "à quatre heures du matin"), (279, "le dimanche")],
  "'n'importe quel jour' dropped; 'Tu travailleras' -> 'Tu travailles'"),
 ("lea", "Oui à tout.", "Yes to everything.",
  [(282, "Oui à tout")], ""),
 ("andrea", "Très bien. Tu peux commencer maintenant?", "Very good. Can you start now?",
  [(283, "Très bien"), (284, "Tu peux commencer maintenant ?")], ""),
 ("lea", "Oui, maintenant!", "Yes, right now!",
  [], ""),
]

OPENER = ("Let's go through it together. Andréa first calls Camille with the polite 'you', then changes her mind halfway "
          "and switches to the casual one, and she is already walking away.")

WALK = [
 (0, None,
  "'Are you coming or not?' Literally 'you're coming, yes or no?'. Here is our grammar point for today: the verb 'to come'. "
  "In this short form it means 'are you coming?'. Out on the street, Andréa uses the very same verb again."),
 (1, None,
  "'Where are you from?' The same verb plus the little word for 'from' at the end: 'you come from where?'. "
  "That's how French asks where someone is from. Camille answers with the same verb."),
 (2, None,
  "'I'm from the Côte d'Azur. Near Cannes.' The Côte d'Azur is the sunny south coast of France, and Cannes is the town "
  "with the famous film festival. Andréa jumps on that."),
 (3, None,
  "'Cannes? Did you work at the festival?' This is the everyday past tense: a form of 'to have' plus 'worked'. "
  "Camille isn't going to let a good chance go."),
 (4, None,
  "'Yes, exactly. The Cannes Film Festival.' The word for exactly looks almost like English, so it's an easy one. "
  "Andréa wants details."),
 (5, None,
  "'Doing what?' Literally 'to do what?'. Short and very blunt, which is how Andréa talks to everyone."),
 (6, "Ça dépend.",
  "'It depends.' Camille buys herself a second to think. And then she makes up a wonderful job."),
 (6, "Au début, j'étais dans les sous-vêtements des stars.",
  "'At first, I was in the stars' underwear.' She means she handled underwear emergencies for the stars: "
  "a strap that snaps, a line that shows. Then she acts out what she used to tell them."),
 (7, None,
  "'Don't cry, we're going to fix this!' Notice she uses the polite 'you' to the stars. The second half is the near future: "
  "a form of 'to go' plus a verb, exactly like 'going to' in English. Andréa takes a phone call, then carries on with her list."),
 (8, None,
  "'Have you got a boyfriend?' Literally 'a little friend'. That's how French says boyfriend. "
  "Camille doesn't even blink."),
 (9, None,
  "'No.' That's the first of many short answers. Andréa moves on."),
 (10, None,
  "'Friends in Paris?' No verb at all, just the words that matter. Camille's answer brings back our verb."),
 (11, "Non, je viens d'arriver.",
  "'No, I've just arrived.' The verb 'to come', then the word for 'from', then another verb: that means 'I have just done it'. "
  "So the same verb gave us 'coming', 'from' and 'just'. Then she adds something more personal."),
 (11, "Mon père, mais c'est compliqué.",
  "'My dad, but it's complicated.' We know why: her dad is Mathias, the agent upstairs, and nobody here knows. "
  "Andréa asks one more question about him."),
 (12, None,
  "'Do you look after him?' The verb means to take care of someone, or to deal with something. Camille's answer is firm."),
 (13, None,
  "'No way!' Literally 'out of the question'. Andréa likes that. Then she gets to the real test."),
 (14, None,
  "'Can I call you at four in the morning? Do you work on Sundays?' The first question uses 'can' followed by a verb, "
  "the way English does. It's the job description of an agent's assistant. Camille doesn't hesitate."),
 (15, None,
  "'Yes to everything.' Andréa has found someone as tireless as she is."),
 (16, None,
  "'Very good. Can you start now?' 'Can' plus a verb again, the same pattern as before. And Camille, who came to Paris "
  "looking for a job in films, gets one in five minutes."),
 (17, None,
  "'Yes, right now!' Just the two words she needs."),
]

TRANSITION = "Listen to the whole conversation one more time."

OUTRO = ("Camille walked in looking for her father and walks out with a job at his agency. "
         "Upstairs, Samuel still has one piece of advice for Gabriel before his plane, and we'll find out what it was. "
         "Well done, and see you next time.")
CLOSING = ("lea", "Merci, Andréa!")
