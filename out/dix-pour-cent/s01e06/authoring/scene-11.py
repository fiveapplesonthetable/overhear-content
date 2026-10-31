# Authoring module for dix-pour-cent-s01e06-scene-11.
ID = 'dix-pour-cent-s01e06-scene-11'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 6
SCENE = 11
TITLE = 'Notre père  (Our Father)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'camille': 'Camille', 'hippolyte': 'Hippolyte', 'serveur': 'Le serveur'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E06'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e06.fr.dual.srt'
INTRO = ('Refusing to visit the agency while his father Mathias is there, Hippolyte asks Camille to meet him at a cafe. '
 'Sitting outside on a cold Paris afternoon, the two half-siblings sign contracts, talk about their shared father, and '
 "invent a warm new friendship. Let's listen to the scene in French first.")
OPENER = 'Camille and Hippolyte break the ice. Let us examine their lines together.'
TRANSITION = 'Now listen to their cafe conversation once more from start to finish.'
OUTRO = ('Having made peace with their unusual family bond, Camille and Hippolyte raise their cups together. Here is our final '
 'toast. See you next time!')
CLOSING = ('camille', 'Bonne soirée!')
STORY = [('hippolyte', 'Mon père est là?', 'Is my father there?', [(288, 'Mon père est là')], ''),
 ('camille', 'Oui.', 'Yes.', [(289, 'Oui')], ''),
 ('hippolyte',
  'Je ne viens pas, alors. Je ne veux pas le voir.',
  'I am not coming, then. I do not want to see him.',
  [(290, 'Je ne viens pas, alors'), (290, 'Je ne veux pas le voir')],
  ''),
 ('camille',
  'On peut se retrouver ailleurs?',
  'Can we meet somewhere else?',
  [(292, 'On peut se retrouver ailleurs')],
  ''),
 ('hippolyte', 'Salut!', 'Hi!', [(293, 'Salut')], ''),
 ('camille', "Un café, s'il vous plaît.", 'A coffee, please.', [(294, "Un café, s'il vous plaît")], ''),
 ('serveur', "D'accord.", 'All right.', [(294, "D'accord")], ''),
 ('hippolyte',
  "Il a soudainement fait froid. C'est l'enfer en scooter.",
  'It suddenly got cold. It is hell on a scooter.',
  [(295, 'Il a soudainement fait froid'), (296, "C'est l'enfer en scooter")],
  ''),
 ('camille',
  'Il gèle à vélo. Je pédale comme une folle!',
  'It is freezing on a bike. I pedal like crazy!',
  [(297, 'Il gèle à vélo'), (298, 'Je pédale comme une folle')],
  ''),
 ('camille',
  'Voici tes contrats.',
  'Here are your contracts.',
  [(302, 'Vos contrats')],
  'Informal sibling address, matching the source audio register.'),
 ('camille',
  'Je suis désolée.',
  'I am sorry.',
  [(304, 'Désolé')],
  'Her spoken feminine apology is confirmed in original-audio ASR; unrelated pen ownership is omitted.'),
 ('hippolyte',
  "C'est mon père qui devrait s'excuser, pas toi.",
  'My father is the one who should apologize, not you.',
  [(306, "C'est mon père qui devrait s'excuser, pas toi")],
  ''),
 ('camille',
  "Notre père! C'est trop bizarre.",
  'Our father! It is so weird.',
  [(307, 'Notre père'), (308, "C'est trop bizarre")],
  ''),
 ('hippolyte',
  'On va juste oublier ça et devenir amis.',
  'We are just going to forget about that and become friends.',
  [],
  ''),
 ('hippolyte',
  'Tu es ma sœpote et je suis ton frote!',
  'You are my sister-buddy and I am your brother-buddy!',
  [(300, 'suis'), (300, 'suis')],
  ''),
 ('camille', 'Tchin, frote!', 'Cheers, brother-buddy!', [], '')]
WALK = [(0,
  None,
  "'Is my father there?' The final word means 'there'. With rising intonation, the ordinary statement 'my father is "
  "there' becomes a question about Mathias's location."),
 (1,
  None,
  "'Yes.' One word supplies the entire affirmative answer. Nothing needs to be repeated because the question already "
  'names her father and his location.'),
 (2,
  None,
  "'I am not coming, then. I do not want to see him.' The first negative denies coming. The second denies wanting to "
  "see him. The small object before 'see' refers back to his father."),
 (3,
  None,
  "'Can we meet somewhere else?' The final word means 'elsewhere'. The action in the middle means meeting up, so "
  'Camille proposes a different place rather than cancelling.'),
 (4, None, "'Hi!' This familiar greeting can mean hello or goodbye. Here it opens their meeting, so it means 'hi'."),
 (5,
  None,
  "'A coffee, please.' French orders coffee by naming the drink with 'a'. The fixed ending adds 'please' politely, "
  'suitable for speaking to a waiter.'),
 (6,
  None,
  "'All right.' The reply is an everyday 'okay'. The small attached word at the beginning belongs to the whole "
  'expression, rather than naming a separate object.'),
 (7,
  None,
  "'It suddenly got cold. It is hell on a scooter.' The first sentence describes a sudden change in the weather. The "
  "second calls travel by scooter 'hell', an exaggerated description of the cold."),
 (8,
  None,
  "'It is freezing on a bike. I pedal like crazy!' The opening weather statement means it is freezing. The comparison "
  "after 'I pedal' literally says 'like a crazy woman', matching Camille."),
 (9,
  None,
  "'Here are your contracts.' The first word presents something: 'here are'. The plural word for 'your' belongs to the "
  'contracts, while addressing one person familiarly.'),
 (10,
  None,
  "'I am sorry.' The final word has a feminine ending because Camille is speaking. This apology leads Hippolyte to say "
  'that their father should be the one apologizing.'),
 (11,
  None,
  "'My father is the one who should apologize, not you.' The beginning singles out his father as the person who should "
  "apologize. The last two words mean 'not you', explicitly releasing Camille from blame."),
 (12,
  None,
  "'Our father! It is so weird.' Camille changes 'my' to 'our'. That single possessive acknowledges they share a "
  "father. The later word means 'too' or, here, emphatically 'so'."),
 (13,
  None,
  "'We are just going to forget about that and become friends.' The opening 'we are going' introduces their plan. The "
  "two later actions mean 'forget' and 'become': leave the confusion behind and become friends."),
 (14,
  None,
  "'You are my sister-buddy and I am your brother-buddy!' These two invented nicknames blend the French words for "
  'sister or brother with the slang word for buddy. They are playful family-specific names, not standard vocabulary.'),
 (15,
  None,
  "'Cheers, brother-buddy!' The opening is a toast, like 'cheers'. Camille then uses their newly invented word for her "
  'brother who will also be her friend.')]
