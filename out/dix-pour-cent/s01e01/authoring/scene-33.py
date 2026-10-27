ID = "dix-pour-cent-s01e01-scene-33"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 33
TITLE = "Il faut qu'on parle  (We Have to Talk)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "gabriel": "theo"}
LABELS = {"lea": "Cécile", "gabriel": "Gabriel"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("Arlette's teasing has worked: she told Gabriel that Samuel never taught him to hang on, and now he wants "
         "to win Cécile back. He drives out of Paris to her riding school and finds her up on a big chestnut horse, "
         "which she still can't really control. The two old friends have not spoken since she called him a liar. "
         "You'll hear the scene in French first, so just let it wash over you; there's no need to follow every word.")

STORY = [
 ("gabriel", "Bonjour, je cherche Cécile de France.", "Hello, I'm looking for Cécile de France.",
  [(848, "je cherche Cécile de France")], ""),
 ("gabriel", "Cécile! Il faut qu'on parle.", "Cécile! We have to talk.",
  [(850, "Cécile ! Il faut qu'on parle")], ""),
 ("lea", "Gabriel? Qu'est-ce que tu fais là?", "Gabriel? What are you doing here?",
  [(851, "Qu'est-ce que tu fais là")], "'Gabriel?' added"),
 ("lea", "Stop! Stop! Je ne peux pas!", "Stop! Stop! I can't!",
  [(851, "Stop"), (852, "je peux pas")], "'ne' restored in the negation; she shouts at the horse"),
 ("gabriel", "Cécile, tu es vraiment nulle à ça.", "Cécile, you're really bad at this.",
  [(853, "vraiment nulle à ça")], "'t'es' -> 'tu es'"),
 ("gabriel", "Tu m'as dit que tu savais monter. Tu as menti.", "You told me you could ride. You lied.",
  [(854, "Tu m'avais dit que"), (855, "Tu as menti")], "'tu m'avais dit que tu maîtrisais' simplified"),
 ("lea", "Je n'ai pas menti, Gabriel.", "I didn't lie, Gabriel.",
  [(855, "Je n'ai pas menti, Gabriel")], ""),
 ("lea", "Je prends des cours. Je vais bientôt être assez bonne.", "I'm taking lessons. I'm soon going to be good enough.",
  [(856, "bientôt assez bonne")], "'je pensais juste que je serais bientôt assez bonne' simplified; 'Je prends des cours.' new"),
 ("gabriel", "Regarde comme tu es mauvaise!", "Look how bad you are!",
  [(858, "Regarde comme")], "'t'es' -> 'tu es'"),
 ("lea", "Et toi aussi, tu m'as menti!", "And you lied to me too!",
  [(858, "Toi aussi tu m'as menti")], "'Et' added"),
 ("gabriel", "Il y a mentir et mentir.", "There's lying and there's lying.",
  [(859, "Il y a mentir et mentir")], ""),
 ("gabriel", "Je ne voulais pas te faire de mal.", "I didn't want to hurt you.",
  [(860, "pas te faire de mal")], "'je voulais juste pas' -> 'je ne voulais pas'"),
 ("lea", "Oh non! Il ne s'arrête pas!", "Oh no! He won't stop!", [], "new: the horse bolts"),
 ("gabriel", "Attendez! Cécile, accroche-toi!", "Wait! Cécile, hold on!",
  [(861, "Attendez"), (862, "Cécile, accroche-toi")], "in the episode the riding instructor shouts the advice"),
 ("gabriel", "Attention, tu arrives sur la route!", "Careful, you're heading for the road!",
  [(864, "tu arrives sur la route")], "'Fais attention' -> 'Attention'; shouted by the instructor in the episode"),
]

OPENER = ("Let's go back through it slowly. Gabriel walks into the riding school and asks a member of staff "
          "where his star is.")

WALK = [
 (0, None,
  "'Hello, I'm looking for Cécile de France.' The verb for looking for already contains the 'for', so nothing "
  "else is needed before her name. Someone points across the field, and he calls out to her."),
 (1, "Il faut qu'on parle.",
  "'We have to talk.' The opening two words mean 'it is necessary', a very common way to say that something "
  "must happen. The little word in the middle is the everyday way of saying 'we'."),
 (2, None,
  "'Gabriel? What are you doing here?' She uses the casual 'you'. These two have worked together for years, "
  "so they always speak to each other as friends."),
 (3, "Je ne peux pas!",
  "'I can't!' She is shouting at the horse to stop, and it isn't listening. Notice how the negation wraps around "
  "the verb: one small word goes before it, and the word for 'not' comes after it."),
 (4, None,
  "'Cécile, you're really bad at this.' Not very kind, but he is hurt. The word for 'bad at' or 'useless' here "
  "ends in a feminine way, because he is talking about a woman."),
 (5, "Tu m'as dit que tu savais monter.",
  "'You told me you could ride.' On the phone that morning she had promised him she had it under control."),
 (5, "Tu as menti.",
  "'You lied.' A short past tense: the helper verb meaning 'to have', then the past form of 'to lie'. "
  "Cécile protests."),
 (6, None,
  "'I didn't lie, Gabriel.' Here is the same negation pattern in the past: the two pieces wrap around the helper "
  "verb, not around the word for 'lied'. She explains."),
 (7, "Je vais bientôt être assez bonne.",
  "'I'm soon going to be good enough.' To talk about the near future, take the verb 'to go' and put a plain verb "
  "after it, exactly like 'going to' in English. The word for 'good' is feminine again."),
 (8, None,
  "'Look how bad you are!' He is giving orders now, in the casual form, just as she wobbles past him."),
 (9, None,
  "'And you lied to me too!' Now it's her turn to attack. He kept the truth about Tarantino from her."),
 (10, None,
  "'There's lying and there's lying.' Literally 'there is to lie and to lie'. It's his excuse: some lies are "
  "worse than others."),
 (11, None,
  "'I didn't want to hurt you.' Again the negation wraps around the verb, this time a past form for wanting. "
  "And at that very moment, the horse decides it has heard enough."),
 (12, None,
  "'Oh no! He won't stop!' The verb for stopping takes an extra little word for 'itself', because in French a "
  "horse stops itself. The horse is off, with Cécile hanging on."),
 (13, None,
  "'Wait! Cécile, hold on!' The first word is polite, shouted at nobody in particular. The second order is the "
  "casual one, for her: grab something and don't let go."),
 (14, None,
  "'Careful, you're heading for the road!' The very first word is the classic warning shout. "
  "The argument will have to wait."),
]

TRANSITION = "Now let's hear the whole scene once more, at normal speed."

OUTRO = ("That's the riding school. If you can now hear the difference between saying something and saying you "
         "didn't, you've got the main idea of this scene. Until next time.")
CLOSING = ("gabriel", "Accroche-toi!")
