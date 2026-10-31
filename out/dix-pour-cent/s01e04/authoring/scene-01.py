# Authoring module for dix-pour-cent-s01e04-scene-01.
ID = 'dix-pour-cent-s01e04-scene-01'
SHOW = 'dix-pour-cent'
SEASON = 1
EPISODE = 4
SCENE = 1
TITLE = 'Vingt-trois mois de retard  (Twenty-Three Months Late)'
LEVEL = 'A1 — débutant'
PAIR = 'fr-en'
LABELS = {'audrey': 'Audrey', 'inspecteur': "L'inspecteur", 'mathias': 'Mathias'}
SOURCE_NAME = 'Dix pour cent (Call My Agent!) S01E04'
SOURCE_FILE = 'sources/dix-pour-cent/s01/e04.fr.dual.srt'
INTRO = ('Audrey brings her baby to the tax office with her agent, Mathias. Her tax payment is badly overdue, and Mathias '
 'hopes to talk their way out of trouble. Listen to the whole scene in French first; we will unpack it together '
 'afterwards.')
OPENER = "Let's go back through it step by step. Audrey is carrying her baby son down the corridor as she tries to keep up with Mathias."
TRANSITION = "Now let's listen to the entire dialogue once more."
OUTRO = ("Audrey's comeback has become an urgent promise. You heard how to describe a late payment, contradict a negative "
 'question and add an extra amount. Listen for those patterns when you meet them again. See you next time!')
CLOSING = ('audrey', 'Au revoir!')
STORY = [('audrey',
  'Attendez, vous marchez vite. Je ne veux pas le réveiller.',
  "Wait, you're walking fast. I don't want to wake him.",
  [(1, 'Attends, tu marches trop vite'), (2, 'Je ne veux pas le réveiller')],
  'Actual original French audio uses polite vous, unlike backtranslated dual SRT.'),
 ('audrey',
  "Il n'a pas dormi de la nuit. Il fait ses dents.",
  "He didn't sleep all night. He's teething.",
  [(3, "Il n'a pas dormi de la nuit"), (4, 'Il fait ses dents')],
  ''),
 ('mathias',
  'On ne prend aucun risque. Laissez-moi parler.',
  "We're not taking any risks. Let me do the talking.",
  [(10, 'On ne prend aucun risque'), (10, 'parler')],
  'Original audio: Vous faites profil bas et vous me laissez parler. Shortened polite command preserves the '
  'original register.'),
 ('inspecteur', "C'est votre mari?", 'Is he your husband?', [(16, "C'est votre mari ?")], ''),
 ('mathias', 'Non, son agent.', 'No, her agent.', [(16, 'Non, son agent')], ''),
 ('inspecteur',
  'Madame, vous avez vingt-trois mois de retard.',
  'Madam, you are twenty-three months late.',
  [(19, 'madame'), (20, 'vous avez'), (20, 'mois de retard')],
  ''),
 ('audrey',
  'Oui, mais au moins je paie mes impôts en France!',
  'Yes, but at least I pay my taxes in France!',
  [(21, 'Oui, mais au moins je paie mes impôts en France !')],
  ''),
 ('mathias',
  'Audrey a eu deux enfants en trois ans.',
  'Audrey had two children in three years.',
  [(24, 'Audrey a eu deux enfants en trois ans')],
  ''),
 ('mathias',
  'Maintenant, elle veut retrouver du travail et payer ses impôts.',
  'Now she wants to find work again and pay her taxes.',
  [(28, 'Maintenant, elle'), (28, 'retrouver du travail et payer ses impôts')],
  ''),
 ('inspecteur',
  'Vous ne trouvez pas de travail, madame?',
  "You can't find work, madam?",
  [(30, 'Vous ne trouvez pas de travail, madame ?')],
  ''),
 ('mathias', 'Bien sûr que si!', 'Of course she can!', [(32, 'Bien sûr que si')], ''),
 ('inspecteur',
  "Mais vous avez refusé un rôle dans un film d'action.",
  'But you turned down a role in an action film.',
  [(36, 'vous avez'), (36, 'refusé un rôle'), (37, "Un film d'action")],
  ''),
 ('audrey',
  'Je ne pouvais pas courir après des zombies!',
  "I couldn't run after zombies!",
  [(38, 'Je ne pouvais pas courir après des zombies')],
  ''),
 ('mathias',
  "Le retour d'Audrey sur un tournage est imminent.",
  "Audrey's return to a film shoot is imminent.",
  [(42, "le retour d'Audrey sur un tournage est imminent")],
  ''),
 ('audrey',
  "Oui, c'est un projet énorme.",
  "Yes, it's a huge project.",
  [(44, "Oui, c'est un projet énorme")],
  ''),
 ('inspecteur',
  "J'attends votre chèque cette semaine, avec dix pour cent de plus.",
  'I expect your cheque this week, with ten percent extra.',
  [(47, "J'attends votre chèque cette semaine"), (48, 'majoration de 10 %')],
  'Shortened into one sentence; the source surcharge is ten percent.')]
WALK = [(0,
  'Attendez, vous marchez vite.',
  "'Wait, you're walking fast.' Audrey uses a polite command, followed by the matching polite form of 'you walk'. "
  'She is worried about waking her baby.'),
 (0,
  'Je ne veux pas le réveiller.',
  "'I don't want to wake him.' The negative wraps around 'want', and the little word for 'him' sits right before "
  "the action word 'to wake'."),
 (1,
  "Il n'a pas dormi de la nuit.",
  "'He didn't sleep all night.' French uses a negative statement about sleeping, followed by an expression that "
  'covers the whole night.'),
 (1,
  'Il fait ses dents.',
  "'He's teething.' The baby is teething. French describes this literally as making his teeth."),
 (2,
  None,
  "'We're not taking any risks. Let me do the talking.' The negative word after the action means 'not any'. The "
  'command keeps polite address to one person. Mathias expects a familiar inspector, but a stricter replacement '
  'is now at the desk.'),
 (3, None, "'Is he your husband?' The inspector uses the polite 'your' as they sit down."),
 (4,
  None,
  "'No, her agent.' The possessive follows the gender of the job title, not the owner. A male agent therefore "
  'takes the same form whether he represents a woman or a man.'),
 (5,
  None,
  "'Madam, you are twenty-three months late.' French describes lateness as having an amount of delay. The number "
  'of months tells us how long the payment has been overdue.'),
 (6,
  None,
  "'Yes, but at least I pay my taxes in France!' Listen for the two-word expression meaning 'at least'. It sets a "
  'minimum positive point against the bad news about her late payment.'),
 (7,
  None,
  "'Audrey had two children in three years.' You hear two forms of 'to have' together: the short helping word, "
  "then the past form meaning 'had'. Both children were born within those three years."),
 (8,
  None,
  "'Now she wants to find work again and pay her taxes.' The French verb for finding again has a prefix that "
  'marks repetition. English does something similar with the word redo, meaning to do again.'),
 (9,
  None,
  "'You can't find work, madam?' After a negative expression, this little French word shortens. The sentence asks "
  'whether she can find any work at all.'),
 (10,
  None,
  "'Of course she can!' French has a special affirmative response for contradicting a negative question. Mathias "
  'uses it to reject the suggestion that Audrey cannot find work.'),
 (11,
  None,
  "'But you turned down a role in an action film.' Here 'you have' helps make a past action: 'you refused'. It "
  'does not mean that she currently owns something.'),
 (12,
  None,
  "'I couldn't run after zombies!' The form of 'can' places her inability in the past. The word after 'run' means "
  "'after' here, as in chasing someone."),
 (13,
  None,
  "'Audrey's return to a film shoot is imminent.' The short linking sound before her name connects the return "
  'with Audrey. Mathias promises that she will be back on set very soon.'),
 (14,
  None,
  "'Yes, it's a huge project.' The describing word comes after 'project'. It has the same spoken form for a "
  'masculine or feminine thing, so you can reuse it to describe either kind of thing.'),
 (15,
  None,
  "'I expect your cheque this week, with ten percent extra.' At the end, the word for 'more' means an added "
  "amount. It does not mean 'no longer': there is no negative around it.")]
