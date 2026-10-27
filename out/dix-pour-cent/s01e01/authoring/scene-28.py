ID = "dix-pour-cent-s01e01-scene-28"
SHOW = "dix-pour-cent"
SEASON = 1
EPISODE = 1
SCENE = 28
TITLE = "Juste les joues  (Just the Cheeks)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "mathias": "theo", "miranda": "emilie"}
LABELS = {"lea": "Cécile", "mathias": "Mathias", "miranda": "Miranda"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S01E01"
SOURCE_FILE = "sources/dix-pour-cent/s01/e01.fr.dual.srt"

INTRO = ("While Camille packs up her desk, Cécile de France is sitting in Mathias's office. "
         "Remember: she left Gabriel and signed with Mathias, and Mathias put pressure on Tarantino's producer, "
         "Miranda Jones, by telling her that without Cécile there would be no permits to shoot in Paris. "
         "So Miranda is back at the table, and Cécile thinks she's about to hear good news. "
         "There's a catch, though. Here it is in French first; don't try to catch every word, the story will carry you.")

STORY = [
 ("mathias", "Quentin a réfléchi. Il te veut vraiment.", "Quentin has thought it over. He really wants you.",
  [(735, "Quentin a réfléchi. Il te veut vraiment")], ""),
 ("lea", "Merci, c'est super!", "Thanks, that's great!", [(736, "Merci, c'est super")], ""),
 ("mathias", "Mais il veut une femme plus jeune.", "But he wants a younger woman.",
  [(737, "une femme plus jeune")], "'que l'immortelle soit' (subjunctive) dropped"),
 ("mathias", "Si tu veux le rôle, tu dois changer.", "If you want the part, you have to change.",
  [(738, "si tu veux le rôle, tu dois changer")], ""),
 ("lea", "Je ne comprends pas.", "I don't understand.", [(739, "Je ne comprends pas")], ""),
 ("mathias", "Tu as de la chance. Il faut juste faire les joues.", "You're lucky. You just need to have your cheeks done.",
  [(740, "T'as de la chance"), (740, "les joues")], "'t'as juste les joues à faire' retold with 'il faut'; speaker assumed to be Mathias (tu)"),
 ("lea", "Une opération? Tu es sérieux?", "An operation? Are you serious?", [],
  "new; replaces 'Tu veux que je me fasse opérer?' (subjunctive)"),
 ("mathias", "Non. C'est du lipofilling.", "No. It's lipofilling.", [(742, "Non"), (743, "Du lipofilling")],
  "'Du lipofilling' is said by Miranda in the source; given to Mathias to keep his 'Non' and the explanation together"),
 ("miranda", "C'est totalement différent.", "It's totally different.", [(744, "C'est totalement différent")], ""),
 ("lea", "Désolée, je ne touche pas à mon visage.", "Sorry, I'm not touching my face.",
  [(746, "Désolée, je ne touche pas à mon visage")], ""),
 ("mathias", "Attends, Cécile. Écoutons Miranda.", "Wait, Cécile. Let's listen to Miranda.",
  [(747, "Attends, Cécile"), (748, "Écoutons")], "'ce que Miranda a à dire' shortened"),
 ("miranda", "C'est tellement simple.", "It's so simple.", [(749, "C'est tellement simple")], ""),
 ("miranda", "Et voilà, c'est terminé. Tête de bébé!", "And there you go, it's done. Baby face!",
  [(751, "Et voilà"), (751, "terminé"), (752, "Tête de bébé")], "'réglé' dropped"),
 ("lea", "Non, c'est facile de dire terminé.", "No, it's easy to say done.",
  [(753, "c'est facile de dire")], "quotation marks around 'terminé' dropped (no guillemets in spoken lines)"),
 ("lea", "Elles commencent avec un peu de Botox. Après, elles ne peuvent plus s'arrêter.",
  "They start with a bit of Botox. Then they can't stop anymore.",
  [(754, "Elles commencent avec un peu de Botox"), (754, "elles ne peuvent plus s'arrêter")], "split into two sentences"),
 ("mathias", "Tu veux jouer l'immortelle?", "Do you want to play the immortal woman?",
  [(756, "Tu veux jouer l'immortelle")], ""),
 ("lea", "Oui, bien sûr, mais…", "Yes, of course, but…", [(756, "Oui, bien sûr, mais")], ""),
 ("lea", "Je ne sais plus.", "I don't know anymore.", [(757, "Je ne sais plus")], ""),
]

OPENER = ("Let's go back through it. Mathias opens with what sounds like the best news of Cécile's year.")

WALK = [
 (0, "Quentin a réfléchi.",
  "'Quentin has thought it over.' Quentin is Tarantino, and Mathias calls him by his first name, like an old friend. That's an agent showing off."),
 (0, "Il te veut vraiment.",
  "'He really wants you.' Mathias uses the casual 'you' with Cécile: they've known each other for years. Cécile is thrilled."),
 (1, None,
  "'Thanks, that's great!' The last word sounds just like its English cousin, and the French use it all the time for anything they like. But then comes the catch."),
 (2, None,
  "'But he wants a younger woman.' The phrase for 'younger' is 'more young': the word for 'more' goes before the adjective, a simple way to compare. Mathias spells it out."),
 (3, None,
  "'If you want the part, you have to change.' The second half uses the verb 'must'. Cécile doesn't see what he means."),
 (4, None,
  "'I don't understand.' Notice the two little negative words around the verb. Keep that in mind; there's a variation at the end of the scene."),
 (5, "Tu as de la chance.",
  "'You're lucky.' Literally 'you have some luck'. French often uses 'to have' where English uses 'to be'."),
 (5, "Il faut juste faire les joues.",
  "'You just need to have your cheeks done.' The first two words mean 'it is necessary', a very handy way to say what has to happen, without saying who. Cécile can't believe it."),
 (6, None,
  "'An operation? Are you serious?' She asks with her voice rising, no special question words needed. Mathias says no, not surgery, something else."),
 (7, None,
  "'No. It's lipofilling.' A cosmetic treatment where fat is moved into the face to fill it out. The producer backs him up."),
 (8, None,
  "'It's totally different.' It isn't, of course, but she says it with a smile. Cécile is very clear."),
 (9, None,
  "'Sorry, I'm not touching my face.' The word for 'sorry' has a feminine ending, because Cécile is a woman. And the negative wraps around the verb again. Mathias asks her to stay calm."),
 (10, None,
  "'Wait, Cécile. Let's listen to Miranda.' The second command ends in the sound for 'let's', which means 'we' are doing it together. Miranda makes it sound like nothing."),
 (11, None,
  "'It's so simple.' The middle word means 'so' or 'really', and it makes anything stronger."),
 (12, None,
  "'And there you go, it's done. Baby face!' The first phrase is one of the most French expressions there is, the 'ta-da' you say when something is finished. Cécile isn't fooled."),
 (13, None,
  "'No, it's easy to say done.' She throws Miranda's own word back at her. Then she says what she's seen around her."),
 (14, None,
  "'They start with a bit of Botox. Then they can't stop anymore.' She means other actresses. In the second sentence, the negative changes: the second little word now means 'anymore'. Mathias goes straight to the point."),
 (15, None,
  "'Do you want to play the immortal woman?' The part in the film is an immortal woman, which is ironic, since the whole problem is her age."),
 (16, None,
  "'Yes, of course, but…' She wants the role badly, and she can't finish her sentence."),
 (17, None,
  "'I don't know anymore.' Compare it with 'I don't know', which would end with the usual negative word. Here, the word for 'anymore' takes its place. One small swap, and you go from not knowing to no longer knowing."),
]

TRANSITION = "Here's the scene again from start to finish."

OUTRO = ("That's a hard choice for Cécile, and a good one for you to remember: 'not' and 'not anymore' "
         "are built the same way, only the second little word changes. We'll find out what she decides soon.")
CLOSING = ("lea", "À bientôt!")
