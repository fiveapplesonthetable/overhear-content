# Authoring module for dix-pour-cent s01e01 scene 12 (cues 400-421).
# Build: python3 tools/compose.py out/dix-pour-cent/s01e01/authoring/scene-12.py --out out/dix-pour-cent/s01e01/scene-12.json

ID = "dix-pour-cent-s01e01-scene-12"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "J'ai encore un agent?  (Do I Still Have an Agent?)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo", "herve": "marcel"}
LABELS = {"lea": "Cécile", "gabriel": "Gabriel", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("We left Camille in the middle of her tour, just as someone looked out of the window and shouted that Cécile "
         "de France was downstairs. Remember what Cécile doesn't know: Tarantino turned her down because of her age, "
         "and Gabriel, her agent, still hasn't told her. He has been dodging her calls all morning. "
         "So Cécile has decided to come in person. She walks onto the agents' floor, looks for Gabriel's assistant Hervé, "
         "and asks a rather awkward question. Gabriel, meanwhile, would love to be anywhere else. "
         "First the French version. Don't try to catch everything; the shape of it is enough.")

STORY = [
 ("lea", "Bonjour. Je suis là pour voir Gabriel.", "Hello. I'm here to see Gabriel.",
  [(400, "Je suis là pour voir")], "'Bonjour.' and the name added; the cue breaks off"),
 ("herve", "Pas maintenant!", "Not now!",
  [(402, "Pas maintenant")], "Hervé is too busy to look up"),
 ("lea", "Hervé! Hervé!", "Hervé! Hervé!",
  [(403, "Hervé"), (404, "Hervé")], ""),
 ("herve", "Oh! Bonjour, Cécile.", "Oh! Hello, Cécile.",
  [(405, "Bonjour, Cécile")], "'Oh!' added"),
 ("lea", "J'ai encore un agent ici?", "Do I still have an agent here?",
  [(406, "J'ai encore un agent ici")], ""),
 ("herve", "Oui, pourquoi?", "Yes, why?",
  [(406, "Oui, pourquoi")], ""),
 ("lea", "C'est peut-être dans ma tête.", "Maybe it's all in my head.",
  [(407, "C'est peut-être dans ma tête")], ""),
 ("lea", "Mais j'ai l'impression que Gabriel m'évite.", "But I have the feeling Gabriel is avoiding me.",
  [(407, "mais j'ai l'impression que Gabriel m'évite")], ""),
 ("gabriel", "Il est une heure. Je vais déjeuner.", "It's one o'clock. I'm going to lunch.",
  [(409, "Il est une heure, je vais déjeuner")], ""),
 ("gabriel", "Sofia, tu veux venir avec moi?", "Sofia, do you want to come with me?",
  [(410, "Tu veux")], "addressed to Sofia, the receptionist (she lunches with him in scene 16); 'te joindre à moi' (cue 411) simplified to 'venir avec moi'; her 'Avec plaisir' told by the narrator"),
 ("lea", "Gabriel? Qu'est-ce qui se passe ici?", "Gabriel? What's going on here?",
  [(413, "Qu'est-ce qui se passe ici")], "speaker not certain in the source; given to Cécile"),
 ("gabriel", "Je suis désolé. Je dois répondre, c'est urgent.", "I'm sorry. I have to answer, it's urgent.",
  [(414, "Je suis désolé"), (415, "Je dois répondre, c'est urgent")], ""),
 ("gabriel", "Oui, allô? Ça fait des mois que j'attends ton appel!", "Yes, hello? I've been waiting for your call for months!",
  [(416, "Oui, allô"), (419, "Ça fait des mois que j'attends ton appel")], "the fake call; '?' instead of '.' after allô"),
 ("lea", "Un appel urgent? Vraiment?", "An urgent call? Really?", [], "new: Cécile sees through it"),
 ("herve", "Il a beaucoup de travail, Cécile.", "He has a lot of work, Cécile.", [], "new: Hervé covers for his boss"),
 ("lea", "Bon. Alors, je vais attendre.", "Fine. Then I'll wait.", [], "new"),
]

OPENER = ("Let's walk through it. Cécile arrives and tells the room why she's here, "
          "with a handy way of saying what you've come for.")

WALK = [
 (0, "Je suis là pour voir Gabriel.",
  "'I'm here to see Gabriel.' Word for word: I am there, to see Gabriel. The French often say 'there' when they mean 'here'. "
  "Hervé is buried in his work and doesn't even look up."),
 (1, None,
  "'Not now!' Two words, and no verb at all. He has no idea who he's talking to. So she calls him again."),
 (2, None,
  "Just his name, twice, a little louder. And this time he looks up."),
 (3, None,
  "'Oh! Hello, Cécile.' He uses her first name: in this world, agents and stars are on first-name terms. "
  "Then comes her question."),
 (4, None,
  "'Do I still have an agent here?' The word in the middle means 'still', and it's what makes the question sting. "
  "Notice the question is just a statement with a rising voice; no special word order needed."),
 (5, None,
  "'Yes, why?' Hervé plays innocent, as if he had no idea. So Cécile explains, carefully."),
 (6, None,
  "'Maybe it's all in my head.' Literally 'it's perhaps in my head'. The word for 'maybe' sits right after the verb."),
 (7, None,
  "'But I have the feeling Gabriel is avoiding me.' French says 'I have the impression that' for 'I feel that'. "
  "And just then Gabriel walks past, very busy all of a sudden."),
 (8, "Il est une heure.",
  "'It's one o'clock.' For the time, French says 'it is one hour'."),
 (8, "Je vais déjeuner.",
  "'I'm going to lunch.' Here's a pattern you'll use every day: the verb 'to go' plus another verb in its basic form "
  "talks about what you're about to do. I'm going to eat lunch."),
 (9, None,
  "'Sofia, do you want to come with me?' He asks Sofia, the receptionist, using the casual 'you'. "
  "She happily accepts, and the two of them head for the door. But Cécile isn't fooled."),
 (10, None,
  "'Gabriel? What's going on here?' A very useful question whenever something feels odd. "
  "Gabriel grabs his phone."),
 (11, "Je suis désolé.",
  "'I'm sorry.' He's a man, so the word for 'sorry' is in its masculine form. A woman writes it with an extra letter at the end."),
 (11, "Je dois répondre, c'est urgent.",
  "'I have to answer, it's urgent.' Another verb plus a basic-form verb: I must, then 'answer'. "
  "And he starts talking to someone, or perhaps to no one."),
 (12, "Oui, allô?",
  "'Yes, hello?' This greeting is only used on the phone."),
 (12, "Ça fait des mois que j'attends ton appel!",
  "'I've been waiting for your call for months!' Literally 'it makes months that I wait for your call'. "
  "A bit much, for a call that may not exist."),
 (13, None,
  "'An urgent call? Really?' Cécile has seen this act before."),
 (14, None,
  "'He has a lot of work, Cécile.' Loyal Hervé covers for his boss. The phrase for 'a lot of' is followed by a small word "
  "meaning 'of', just like in English."),
 (15, None,
  "'Fine. Then I'll wait.' The 'go plus verb' pattern once more: I'm going to wait. Cécile isn't going anywhere."),
]

TRANSITION = "Right, here's the whole scene again, a little faster."

OUTRO = ("Nicely done. Next time someone tells you they have to take an urgent call, you'll know exactly what to think. "
         "See you soon for what happens next.")
CLOSING = ("lea", "À tout à l'heure!")
