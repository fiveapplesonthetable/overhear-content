# Authoring module for dix-pour-cent-s01e06-scene-10.
ID = 'dix-pour-cent-s01e06-scene-10'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 6
SCENE = 10
TITLE = 'La menace de procès  (The Threat of a Lawsuit)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'andrea': 'Andréa', 'camille': 'Camille', 'directeur': 'Le directeur'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E06'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e06.fr.dual.srt'
INTRO = ('After François Berléand punches young theatre director Christophe Bel in a fury over the swimming pool staging, the '
 'theatre director threatens to sue ASK for cancelling the production. Andréa is terrified of a public scandal, while '
 "Camille suggests offering a commercial gesture. Let's listen to the scene in French first.")
OPENER = 'The theatre director is furious. Let us listen to each sentence again with explanations.'
TRANSITION = 'Now listen to the full conversation once more at a natural pace.'
OUTRO = ("Hippolyte answers Camille's call, but when he asks if his father Mathias is at the office, he refuses to come in and "
 'suggests meeting Camille somewhere else instead. Here is our final takeaway line. See you next time!')
CLOSING = ('directeur', 'À demain!')
STORY = [('directeur', 'Faites quelque chose.', 'Do something.', [(267, 'Faites quelque chose')], ''),
 ('directeur',
  "Sinon je vais devoir vous poursuivre, je n'ai pas le choix.",
  'Otherwise I will have to sue you, I have no choice.',
  [(268, 'Sinon je vais devoir vous poursuivre'), (268, "je n'ai pas le choix")],
  ''),
 ('andrea',
  'Oui, bien sûr. Vous pouvez compter sur moi.',
  'Yes, of course. You can count on me.',
  [(269, 'Vous pouvez compter sur moi')],
  ''),
 ('andrea', "C'est une catastrophe pour l'agence.", 'It is a disaster for the agency.', [], ''),
 ('camille',
  "C'est si grave que ça? C'est du théâtre, quand même.",
  'Is it that bad? It is only theatre, after all.',
  [(271, "C'est si grave que ça"), (271, "C'est du théâtre, quand même")],
  ''),
 ('andrea',
  'Vous savez ce que ça pourrait coûter?',
  'Do you know what this could cost?',
  [(272, 'Vous savez ce que ça pourrait coûter')],
  ''),
 ('andrea',
  'On ne peut pas laisser filtrer cette histoire de coup de poing.',
  'We cannot let this punch story get out.',
  [(274, 'on ne peut pas laisser filtrer cette histoire de coup de poing')],
  ''),
 ('andrea',
  'Il faut étouffer ça maintenant.',
  'We must stifle this right now.',
  [(277, 'Il faut étouffer ça maintenant')],
  ''),
 ('camille',
  'Pour un client mécontent, ma mère baisse les tarifs.',
  'For an unhappy client, my mother lowers the prices.',
  [(278, 'Quand ma mère a un client mécontent'), (278, 'elle fait un geste pour ses amis')],
  'Adapted from her commercial goodwill gesture and the following mention of reduced rates.'),
 ('camille',
  'Elle ne perd pas de clientèle.',
  'She does not lose any customers.',
  [(279, 'Elle ne perd pas de clientèle')],
  ''),
 ('andrea',
  'Donc on baisse les tarifs pour toutes nos stars?',
  'So we lower the rates for all our stars?',
  [(280, 'Donc on baisse les tarifs pour toutes nos stars')],
  ''),
 ('andrea', 'Appelez-les vous-même, alors!', 'Call them yourself, then!', [(281, 'Appelez-les vous-même, alors')], ''),
 ('camille',
  "Allô, Hippolyte? Bonjour, c'est Camille, d'ASK.",
  'Hello, Hippolyte? Hello, this is Camille from ASK.',
  [(284, "Allô, Hippolyte ? Bonjour, c'est Camille, d'ASK")],
  ''),
 ('camille',
  "Andréa m'a demandé de vous appeler au sujet de vos contrats.",
  'Andréa asked me to call you about your contracts.',
  [(285, "Andréa m'a demandé de vous appeler au sujet de vos contrats")],
  ''),
 ('camille',
  'Vous pouvez passer les vérifier et les signer?',
  'Can you come by to check them and sign them?',
  [(287, 'Vous pouvez passer les vérifier et les signer')],
  '')]
WALK = [(0,
  None,
  "'Do something.' The opening is the polite or plural command for 'do'. The two words after it mean 'something', "
  'leaving the action for Andréa to choose.'),
 (1,
  None,
  "'Otherwise I will have to sue you, I have no choice.' The first word means 'otherwise'. The next sequence means 'I "
  "am going to have to'. The legal action is suing; the ending says he has no choice."),
 (2,
  None,
  "'Yes, of course. You can count on me.' The first reassurance means 'of course'. The following action literally says "
  "'count on me', a promise that the director can rely on her."),
 (3,
  None,
  "'It is a disaster for the agency.' The opening points to 'a disaster'. The final words specify who faces it: the "
  'agency, whose name begins with a vowel after the shortened article.'),
 (4,
  None,
  "'Is it that bad? It is only theatre, after all.' The little word before 'bad' means 'so' here. The final expression "
  "softens or challenges the claim, rather like 'after all'."),
 (5,
  None,
  "'Do you know what this could cost?' The beginning asks whether Camille knows. The later 'could' makes the cost a "
  'possibility, rather than an amount that Andréa has already calculated.'),
 (6,
  None,
  "'We cannot let this punch story get out.' The first word means 'we' here. Letting a story filter out means allowing "
  'it to leak; the final three words name a punch.'),
 (7,
  None,
  "'We must stifle this right now.' The opening is an impersonal 'it is necessary', meaning 'we must'. The final word "
  'adds urgency: it must happen now.'),
 (8,
  None,
  "'For an unhappy client, my mother lowers the prices.' The unhappy person is a client. Camille describes her "
  "mother's response with the action 'lower' and the plural word for prices or rates."),
 (9,
  None,
  "'She does not lose any customers.' The two negative words surround 'loses'. After that denial, the short word "
  'before customers works with the negative: she does not lose customers.'),
 (10,
  None,
  "'So we lower the rates for all our stars?' The opening 'so' introduces Andréa's sarcastic conclusion. The action is "
  'lowering rates; the final words extend that idea to every star they represent.'),
 (11,
  None,
  "'Call them yourself, then!' The command for 'call' has the object 'them' attached by a hyphen. The following words "
  "mean 'yourself', insisting that Camille should make those calls."),
 (12,
  None,
  "'Hello, Hippolyte? Hello, this is Camille from ASK.' The first word answers or opens a telephone call. Camille then "
  "identifies herself, with a shortened 'from' attached to the agency's initials."),
 (13,
  None,
  "'Andréa asked me to call you about your contracts.' The completed action says Andréa asked her. The little attached "
  "object means 'me'. The final words identify the subject of the call: his contracts."),
 (14,
  None,
  "'Can you come by to check them and sign them?' The question begins with the polite 'you can'. Two later objects "
  "mean 'them', referring to the contracts: first checking them, then signing them.")]
