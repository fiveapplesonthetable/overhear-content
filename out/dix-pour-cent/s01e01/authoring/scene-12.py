# Authoring module for dix-pour-cent-s01e01-scene-12.
ID = 'dix-pour-cent-s01e01-scene-12'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 1
SCENE = 12
TITLE = "J'ai encore un agent?  (Do I Still Have an Agent?)"
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'cecile': 'Cécile', 'gabriel': 'Gabriel', 'herve': 'Hervé'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E01'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e01.fr.dual.srt'
INTRO = ("Gabriel has been avoiding Cecile's calls, so she has come to the agency in person. His assistant Herve has "
 'to answer an awkward question while Gabriel tries to slip away. Hear the French conversation first; there '
 'is no need to understand every word.')
OPENER = "Let's go back through the visit. Cecile starts by explaining who she has come to see."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("You have heard a visitor's request, a question about the time and several excuses. Listen again for the "
 "short actions that follow 'want', 'must' and 'go'; see you next time.")
CLOSING = ('cecile', "À tout à l'heure!")
STORY = [('cecile',
  'Bonjour. Je suis là pour voir Gabriel.',
  "Hello. I'm here to see Gabriel.",
  [(400, 'Je suis là pour voir')],
  ''),
 ('herve', 'Pas maintenant!', 'Not now!', [(402, 'Pas maintenant')], ''),
 ('cecile', 'Hervé! Hervé!', 'Herve! Herve!', [(403, 'Hervé'), (404, 'Hervé')], ''),
 ('herve', 'Oh! Bonjour, Cécile.', 'Oh! Hello, Cécile.', [(405, 'Bonjour, Cécile')], ''),
 ('cecile',
  "J'ai encore un agent ici?",
  'Do I still have an agent here?',
  [(406, "J'ai encore un agent ici")],
  ''),
 ('herve', 'Oui, pourquoi?', 'Yes, why?', [(406, 'Oui, pourquoi')], ''),
 ('cecile',
  "C'est peut-être dans ma tête.",
  "Maybe it's all in my head.",
  [(407, "C'est peut-être dans ma tête")],
  ''),
 ('cecile',
  "Mais j'ai l'impression que Gabriel m'évite.",
  'But I have the feeling Gabriel is avoiding me.',
  [(407, "mais j'ai l'impression que Gabriel m'évite")],
  ''),
 ('gabriel',
  'Il est une heure. Je vais déjeuner.',
  "It's one o'clock. I'm going to lunch.",
  [(409, 'Il est une heure, je vais déjeuner')],
  ''),
 ('gabriel', 'Sofia, tu veux venir avec moi?', 'Sofia, do you want to come with me?', [(410, 'Tu veux')], ''),
 ('cecile',
  "Gabriel? Qu'est-ce qui se passe ici?",
  "Gabriel? What's going on here?",
  [(413, "Qu'est-ce qui se passe ici")],
  ''),
 ('gabriel',
  "Je suis désolé. Je dois répondre, c'est urgent.",
  "I'm sorry. I have to answer; it's urgent.",
  [(414, 'Je suis désolé'), (415, "Je dois répondre, c'est urgent")],
  ''),
 ('gabriel',
  "Oui, allô? Ça fait des mois que j'attends ton appel!",
  "Yes, hello? I've been waiting for your call for months!",
  [(416, 'Oui, allô'), (419, "Ça fait des mois que j'attends ton appel")],
  ''),
 ('cecile', 'Un appel urgent? Vraiment?', 'An urgent call? Really?', [], ''),
 ('herve', 'Il a beaucoup de travail, Cécile.', 'He has a lot of work, Cécile.', [], ''),
 ('cecile', 'Bon. Alors, je vais attendre.', "Fine. Then I'll wait.", [], '')]
WALK = [(0,
  'Je suis là pour voir Gabriel.',
  "'I'm here to see Gabriel.' The short word meaning 'here' locates Cecile, and the linking word after it "
  "explains her purpose. The plain action 'see' comes at the end of that pattern."),
 (1,
  None,
  "'Not now!' Hervé snaps back in two words, with no action word at all. He has no idea who he's talking to. "
  'So she calls him again.'),
 (2,
  None,
  "'Herve! Herve!' She repeats his name to get his attention. This time he looks up and recognises her."),
 (3,
  None,
  "'Oh! Hello, Cecile.' The opening sound shows surprise. Herve follows it with the ordinary daytime "
  'greeting and her first name.'),
 (4,
  None,
  "'Do I still have an agent here?' The word in the middle means 'still', and it's what makes the question "
  'sting. Notice the question is just a statement with a rising voice; no special word order needed.'),
 (5,
  None,
  "'Yes, why?' The short question word can stand on its own after an answer. Herve is asking why Cecile "
  'doubts that she still has an agent.'),
 (6,
  None,
  "'Maybe it's all in my head.' Literally, the phrase begins 'it is perhaps'. The word meaning 'maybe' "
  "follows the form of 'be', and 'my' has a feminine form to match 'head'."),
 (7,
  None,
  "'But I have the feeling Gabriel is avoiding me.' French says 'I have the impression that' for 'I feel "
  "that'. And just then Gabriel walks past, very busy all of a sudden."),
 (8, 'Il est une heure.', "'It's one o'clock.' For the time, French says 'it is one hour'."),
 (8,
  'Je vais déjeuner.',
  "'I'm going to lunch.' Here's a pattern you'll use every day: the verb 'to go' plus another verb in its "
  "basic form talks about what you're about to do. I'm going to eat lunch."),
 (9,
  None,
  "'Sofia, do you want to come with me?' 'Want' is followed by the plain action 'come'. After 'with', the "
  "pronoun meaning 'me' has a different shape from the one used before an action."),
 (10,
  None,
  "'Gabriel? What's going on here?' The opening question expression supplies 'what', while the following "
  "action means 'is happening'. The final word asks about this place, here in the office."),
 (11,
  'Je suis désolé.',
  "'I'm sorry.' The description is masculine because Gabriel is speaking about himself. A woman adds a "
  'written letter at the end, but the apology sounds the same.'),
 (11,
  "Je dois répondre, c'est urgent.",
  "'I have to answer, it's urgent.' Another verb plus a basic-form verb: I must, then 'answer'. And he "
  'starts talking to someone, or perhaps to no one.'),
 (12,
  'Oui, allô?',
  "'Yes, hello?' This particular greeting is used for answering the telephone. It suits Gabriel's attempt to "
  'make his call sound real.'),
 (12,
  "Ça fait des mois que j'attends ton appel!",
  "'I've been waiting for your call for months!' French uses a present form of 'wait' after the expression "
  'for elapsed time. The waiting began earlier and, in his story, continues until this call.'),
 (13,
  None,
  "'An urgent call? Really?' The description follows the noun for 'call'. The final adverb questions whether "
  "Gabriel's excuse is true."),
 (14,
  None,
  "'He has a lot of work, Cécile.' Loyal Hervé covers for his boss. The phrase for 'a lot of' is followed by "
  "a small word meaning 'of', just like in English."),
 (15,
  None,
  "'Fine. Then I'll wait.' Once more, 'go' followed by a plain action expresses an intention. This time "
  'Cecile announces that she will stay rather than let him escape.')]
