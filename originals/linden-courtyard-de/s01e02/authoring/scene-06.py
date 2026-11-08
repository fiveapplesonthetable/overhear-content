# Authoring module for linden-courtyard-de-s01e02-scene-06.
ID = 'linden-courtyard-de-s01e02-scene-06'
SHOW = 'linden-courtyard-de'
SEASON = 1
EPISODE = 2
SCENE = 6
TITLE = 'The Friday Caller  (Der Anrufer für Freitag)'
LEVEL = 'A1 — Anfänger'
PAIR = 'en-de'
LABELS = {'hannah': 'Hannah', 'graham': 'Graham'}
INTRO = 'Nach dem Frühstück kehrt in der Empfangshalle wieder Ruhe ein, während Hannah das große Papierbuch nachträgt und Graham das Türscharnier ölt. Plötzlich klingelt das Telefon auf dem Tresen. Hören wir genau hin.'
OPENER = 'Gehen wir dieses rätselhafte Telefonat nun Zeile für Zeile gemeinsam durch.'
TRANSITION = 'Hören wir uns den ganzen Anruf jetzt noch einmal im natürlichen Sprechtempo an.'
OUTRO = 'Jetzt steht ein fester Zeitpunkt fest — Freitag um zwölf Uhr mittags —, doch die nervöse Stimme am Telefon wollte ihren Namen nicht verraten. Bis gleich in der nächsten Szene!'
CLOSING = ('hannah', 'Bye for now!')
STORY = [('hannah', 'Linden Courtyard Inn, good morning! Hannah speaking.', 'Gasthof Lindenhof, guten Morgen! Hier spricht Hannah.'),
 ('graham', 'Who is it? Another booking for the weekend?', 'Wer ist dran? Noch eine Buchung fürs Wochenende?'),
 ('hannah',
  'Wait, hello, sir! You are calling about the dark blue suitcase?',
  'Warten Sie, guten Tag! Sie rufen wegen des dunkelblauen Koffers an?'),
 ('graham', 'Ask him his name! Write it down!', 'Frag ihn nach seinem Namen! Schreib ihn auf!'),
 ('hannah',
  'Yes, sir, we locked your bag safely in our closet. What is your name, please?',
  'Jawohl, wir haben Ihre Tasche sicher in unserer Kammer eingeschlossen. Wie ist bitte Ihr Name?'),
 ('graham', 'What is he saying? Why are you frowning?', 'Was sagt er denn? Warum runzelst du die Stirn?'),
 ('hannah',
  "Sir? He says, 'Please do not open the white paper package. I will come Friday at noon.'",
  'Hallo? Er sagt: "Bitte öffnen Sie das weiße Papierpäckchen nicht. Ich komme am Freitag um zwölf Uhr mittags."'),
 ('graham', 'Give me the phone, let me ask him properly!', 'Gib mir das Telefon, lass mich ihn ordentlich fragen!'),
 ('hannah', "Too late! He said 'Thank you' and hung up!", 'Zu spät! Er hat "Danke" gesagt und aufgelegt!'),
 ('graham', 'Polite voice? Young or old?', 'Höfliche Stimme? Jung oder alt?'),
 ('hannah',
  'Quiet, polite, maybe thirty-five. He sounded nervous, not angry.',
  'Leise, höflich, vielleicht fünfunddreißig. Er klang nervös, nicht verärgert.'),
 ('graham',
  'Nervous about a wooden toy train? This story gets stranger every hour.',
  'Nervös wegen einer Spielzeugeisenbahn aus Holz? Diese Geschichte wird mit jeder Stunde seltsamer.')]
WALK = [(0,
  None,
  ["'Gasthof Lindenhof, guten Morgen! Hier spricht Hannah.' Am Telefon stellt man sich im Englischen nicht mit ich bin vor, sondern nennt "
   'den Namen in',
   (None, 'Hannah speaking'),
   'für hier spricht Hannah.']),
 (1,
  None,
  ["'Wer ist dran? Noch eine Buchung fürs Wochenende?' Sowohl am Telefon als auch vor der geschlossenen Tür fragt man mit dem neutralen",
   (None, 'Who is it'),
   'nach der Person am anderen Ende.']),
 (2,
  None,
  ["'Warten Sie, guten Tag! Sie rufen wegen des dunkelblauen Koffers an?' Die Verlaufsform in",
   (None, 'You are calling about'),
   'benennt das aktuelle Telefonat samt seinem Anlass.']),
 (3,
  None,
  ["'Frag ihn nach seinem Namen! Schreib ihn auf!' Genau wie bei anprobieren steht das kurze Fürwort in",
   (None, 'Write it down'),
   'zwingend zwischen Verb und Richtungswort.']),
 (4,
  None,
  ["'Jawohl, wir haben Ihre Tasche sicher in unserer Kammer eingeschlossen. Wie ist bitte Ihr Name?' Achten Sie darauf, dass man im "
   'Englischen mit',
   (None, 'What is your name'),
   'immer was statt wie für den Namen fragt.']),
 (5,
  None,
  ["'Was sagt er denn? Warum runzelst du die Stirn?' Wo das Deutsche drei Wörter für die Stirn in Falten legen braucht, genügt im "
   'Englischen das eine anschauliche Verb in',
   (None, 'frowning'),
   'für den fragenden Gesichtsausdruck.']),
 (6,
  None,
  ['\'Hallo? Er sagt: "Bitte öffnen Sie das weiße Papierpäckchen nicht. Ich komme am Freitag um zwölf Uhr mittags."\' Punkt zwölf Uhr '
   'tagsüber heißt im Englischen knapp',
   (None, 'at noon'),
   'mit dem kurzen Verhältniswort für Uhrzeiten.']),
 (7,
  None,
  ["'Gib mir das Telefon, lass mich ihn ordentlich fragen!' Am Satzende beschreibt das Umstandswort",
   (None, 'properly'),
   'dass etwas gründlich und wie es sich gehört erledigt werden soll.']),
 (8,
  None,
  ['\'Zu spät! Er hat "Danke" gesagt und aufgelegt!\' Das zweigliedrige Verb in',
   (None, 'hung up'),
   'stammt noch von alten Wandtelefonen, bei denen man den Hörer nach oben auf die Gabel hängte.']),
 (9,
  None,
  ["'Höfliche Stimme? Jung oder alt?' In schnellen Rückfragen unter Kollegen reicht das knappe Gegensatzpaar",
   (None, 'Young or old'),
   'vollkommen aus.']),
 (10,
  None,
  ["'Leise, höflich, vielleicht fünfunddreißig. Er klang nervös, nicht verärgert.' Nach Verben des Klingens wie in",
   (None, 'sounded nervous'),
   'folgt ein Eigenschaftswort, weil der Eindruck des Sprechers beschrieben wird.']),
 (11,
  None,
  ["'Nervös wegen einer Spielzeugeisenbahn aus Holz? Diese Geschichte wird mit jeder Stunde seltsamer.' Hier ist die Form in",
   (None, 'gets stranger'),
   'nicht das Hauptwort für Fremder, sondern die Steigerungsform seltsamer.'])]
