# Authoring module for dix-pour-cent s04e02 scene 02 (cues 75-139).
# Build: python3 tools/compose.py out/dix-pour-cent/s04e02/authoring/scene-02.py --out out/dix-pour-cent/s04e02/scene-02.json

ID = "dix-pour-cent-s04e02-scene-02"
SHOW = "dix-pour-cent"
SEASON = 4
EPISODE = 2
SCENE = 2
TITLE = "La bataille des talents  (The Battle for Talent)"
LEVEL = "A1 — débutant"
PAIR = "fr-en"
VOICES = {"narrator": "sky", "lea": "lucie", "camille": "emilie", "herve": "theo"}
LABELS = {"lea": "Andréa", "camille": "Camille", "herve": "Hervé"}
SOURCE_NAME = "Dix pour cent (Call My Agent!) S04E02"
SOURCE_FILE = "sources/dix-pour-cent/s04/e02.fr.dual.srt"
SOURCE_NOTE = ("Cues 75-139. Camille and Herve struggle to reassure Mathias's former stars. Andrea rallies the agency to prevent bankruptcy. Adapted for A1 French.")

INTRO = ("Inside the bustling offices of ASK, the agency fights tooth and nail to retain its marquee clients following Mathias Barneville's departure. "
         "Junior agents Camille and Herve report that several major actors are wavering, skeptical of being handled by less experienced representatives. "
         "With François Cluzet walking away and Dany Boon's loyalty hanging in the balance, Andrea rallies her team to fight for every contract. "
         "Let's listen to the scene in French first.")

STORY = [
 ("camille", "Les anciens talents de Mathias hésitent beaucoup.",
  "Mathias's former talents hesitate a lot.",
  [(81, "sur le dos de Mathias")], "Reported client wavering after partner's departure"),
 ("herve", "Ils réclament tous des agents confirmés.",
  "They all demand senior agents.",
  [(86, "veulent des agents confirmés")], "Explained reluctance to work with junior agents"),
 ("lea", "Vous devez montrer beaucoup plus d'assurance.",
  "You must show much more confidence.",
  [(87, "Montrez plus d'assurance")], "Coached young agents on professional authority"),
 ("lea", "Organisez des rendez-vous avec les associés.",
  "Set up meetings with the partners.",
  [(91, "organisez des rendez-vous")], "Suggested partner support for difficult meetings"),
 ("camille", "Sofia a réussi une audition formidable.",
  "Sofia succeeded in a wonderful audition.",
  [(107, "Sofia a cartonné")], "Shared positive casting development"),
 ("camille", "Elle jouera bientôt avec Fabrice Luchini.",
  "She will soon act with Fabrice Luchini.",
  [(107, "Sofia a cartonné")], "Detailed upcoming prestige co-starring role"),
 ("herve", "En revanche, François Cluzet nous quitte.",
  "On the other hand, François Cluzet leaves us.",
  [(115, "Cluzet, c'est fini")], "Announced loss of major film client"),
 ("herve", "Il ne veut plus aucun agent désormais.",
  "He wants no agent anymore from now on.",
  [(121, "veut plus d'agent")], "Reported client decision to represent himself"),
 ("lea", "Nous ne pouvons pas tout perdre.",
  "We cannot lose everything.",
  [(126, "mettre la clé sous la porte")], "Emphasized critical agency stakes"),
 ("camille", "Où en est le dossier de Dany?",
  "How is Dany's case coming along?",
  [(126, "mettre la clé sous la porte")], "Asked status on top comedy earner"),
 ("lea", "Il tourne actuellement à New York.",
  "He is currently filming in New York.",
  [(126, "mettre la clé sous la porte")], "Updated team on actor's overseas location"),
 ("lea", "Perdre Dany fermerait définitivement notre agence.",
  "Losing Dany would permanently close our agency.",
  [(126, "mettre la clé sous la porte")], "Warned of catastrophic financial impact"),
 ("herve", "Je vais le contacter dès ce soir.",
  "I will contact him tonight.",
  [(126, "mettre la clé sous la porte")], "Volunteered to pursue star talent"),
 ("lea", "Battez-vous pour chaque contrat sans faiblir.",
  "Fight for each contract without faltering.",
  [(87, "Montrez plus d'assurance")], "Rallied staff to relentless defense"),
]

OPENER = "Let's observe as Andrea directs Camille and Herve in the high-stakes retention battle."

WALK = [
 (0, None,
  "'Mathias's former talents hesitate a lot.' A concerning report noting client instability across the agency's roster. Notice how 'hesitate' leads directly into the noun meaning 'talents'."),
 (1, None,
  "'They all demand senior agents.' A professional hurdle showing client reluctance to trust junior representatives. The descriptive adjective for 'experienced' agrees in gender and number with its noun."),
 (2, None,
  "'You must show much more confidence.' An empowering piece of advice urging the young agents to project authority. Andrea uses the polite 'you' form alongside 'must' to keep a respectful professional tone."),
 (3, None,
  "'Set up meetings with the partners.' A practical operational tactic leveraging senior partner presence to reassure clients. Notice how 'organize' leads directly into the noun meaning 'appointments'."),
 (4, None,
  "'Sofia succeeded in a wonderful audition.' A welcome piece of good news celebrating an assistant-turned-actress's triumph. The verb meaning 'has' pairs naturally with the noun for 'casting call' in everyday conversation."),
 (5, None,
  "'She will soon act with Fabrice Luchini.' The clause hinges on the everyday verb meaning 'will act'."),
 (6, None,
  "'On the other hand, Francois Cluzet leaves us.' A sobering announcement confirming the departure of a major movie star. The verb meaning 'leave' pairs naturally with the noun for 'revenge' in everyday conversation."),
 (7, None,
  "'He wants no agent anymore from now on.' A definitive break indicating the actor's choice to work independently. The two-part negative structure wraps around 'wants' to express 'no longer' or 'not anymore'."),
 (8, None,
  "'We cannot lose everything.' An urgent acknowledgment that consecutive departures will imperil the firm. Notice the classic French sandwich negation wrapping right around 'can'."),
 (9, None,
  "'How is Dany's case coming along?' The key noun here means 'case', anchored by its matching French article. The key noun here means 'case', anchored by its matching French article."),
 (10, None,
  "'He is currently filming in New York.' A status report noting geographical distance complicating ongoing negotiations. The clause hinges on the everyday verb meaning 'shoots'."),
 (11, None,
  "'Losing Dany would permanently close our agency.' A stark financial truth highlighting the existential risk facing ASK. Notice how 'to lose' leads directly into the noun meaning 'talent firm'."),
 (12, None,
  "'I will contact him tonight.' A dedicated initiative volunteering to reach out across time zones. Notice how 'am going' leads directly into the noun meaning 'evening hours'."),
 (13, None,
  "'Fight for each contract without faltering.' An inspiring battle cry mobilizing the entire staff for the fight ahead. Notice how 'fight' leads directly into the noun meaning 'business contract'."),
]

TRANSITION = "Now let's listen to Andrea, Camille, and Herve discussing their strategy again at full speed."

OUTRO = ("Realizing that the agency's survival depends on holding onto its remaining stars, Andrea keeps her team focused and motivated. "
         "With every client relationship hanging by a thread, no mistake can be tolerated.")

CLOSING = ("lea", "Notre avenir se joue aujourd'hui.")
