ID = 'aangan-haveli-s01e02-scene-08'
SHOW, SEASON, EPISODE, SCENE = 'aangan-haveli', 1, 2, 8
TITLE = 'एक कमरा, दो नाम  (Two Names, One Room)'
LEVEL, PAIR = 'A1 — beginner', 'hi-en'
LABELS = {'kavya': 'काव्या', 'mohan': 'मोहन', 'pratap': 'प्रताप'}

INTRO = ('Rain begins pattering into the Jaipur courtyard as Tuesday evening falls. At the reception desk, '
 'Mohan stares at the booking tablet with growing dread. Listen to the closing scene of Episode 2 '
 'in Hindi first.')
OPENER = "Now let's walk through the conversation one line at a time."
TRANSITION = "Now let's listen to the whole scene again from start to finish."
OUTRO = ('Two guests booked into Room 7, pouring rain outside, and only forty minutes before the eight '
 "o'clock train arrives! Join us in Episode 3 as the staff race up to the third-floor attic study.")
CLOSING = ('pratap', 'चलो, चलते हैं!')

STORY = [('mohan',
  'प्रताप... काव्या... कृपया कह दो कि आज रात कमरा छह ख़ाली है।',
  'Pratap... Kavya... please tell me room six is free tonight.'),
 ('kavya',
  'नहीं मोहन जी, दक्षिण से आए पति-पत्नी एक घंटे पहले कमरा छह में आ चुके हैं।',
  'No, Mr Mohan, the couple from the south checked into room six an hour ago.'),
 ('pratap',
  'एक से सात तक हर चाबी जा चुकी है, और कमरा आठ में गीला पेंट है।',
  'Every key from one to seven is taken, and room eight has wet paint.'),
 ('mohan',
  'हाय, अनर्थ हो गया! कल मैंने बिना चश्मे के टैबलेट पर फ़ोन बुकिंग लिखी थी!',
  'Oh, disaster! Yesterday I entered a phone booking on the tablet without my glasses!'),
 ('kavya',
  'रुकिए—मुझे टैबलेट की स्क्रीन और काग़ज़ का रजिस्टर एक साथ देखने दीजिए।',
  'Wait—let me check the tablet screen and the paper register side by side.'),
 ('pratap',
  'मैं समझ गया। आपने किसी को ऐसा कमरा दे दिया जो हमारे पास है ही नहीं?',
  'Let me guess. You promised someone a room we do not even have?'),
 ('kavya',
  'मोहन जी! कमरा सात पहले से भरा है, और आपने कमरा सात में ही दूसरे मेहमान की बुकिंग लिख दी!',
  'Mr Mohan! Room seven is already occupied, and you booked a second guest right into room seven!'),
 ('mohan',
  'और वह शाम आठ बजे की ट्रेन से आ रहा है—बस चालीस मिनट में!',
  "And he is arriving on the eight o'clock evening train—in just forty minutes!"),
 ('pratap', 'मैंने कहा था ना कि यह टैबलेट एक जाल है।', "Didn't I tell you that tablet is a trap?"),
 ('mohan',
  'बाहर बारिश हो रही है और हमारी गली का हर होटल भरा है! अब हम क्या करें?',
  'It is raining outside and every hotel on our lane is full! What do we do now?'),
 ('kavya',
  'रुकिए—सीढ़ियों के ऊपर तीसरी मंज़िल पर क्या है?',
  'Wait—what is up on the third floor above the stairs?'),
 ('pratap',
  'अटारी वाला पुराना रोशन कमरा... मेरे पीछे आओ, जल्दी!',
  'The old bright attic study... follow me, quickly!')]

WALK = [(1,
  None,
  ['\'No, Mr Mohan, the couple from the south checked into room six an hour ago.\' Adding "chuknaa" in ',
   (None, 'आ चुके हैं।'),
   " means 'have already arrived'—handy whenever an action is already done."]),
 (4,
  None,
  ["'Wait—let me check the tablet screen and the paper register side by side.' ",
   (None, 'देखने दीजिए।'),
   ' combines "dekhne" with "deejiye" (\'please give\') to mean \'please let me look\'.']),
 (5,
  None,
  ['\'Let me guess. You promised someone a room we do not even have?\' That tiny word "hee" in ',
   (None, 'है ही नहीं?'),
   " means 'do not have at all!'."]),
 (8,
  None,
  ["'Didn't I tell you that tablet is a trap?' This useful sentence ",
   (None, 'मैंने कहा था ना'),
   " is what you'll hear everywhere for 'I told you so, didn't I?'."]),
 (9,
  None,
  ["'It is raining outside and every hotel on our lane is full! What do we do now?' Asking ",
   (None, 'अब हम क्या करें?'),
   ' uses "karen" to mean \'what should we do now?\'.']),
 (11,
  None,
  ["'The old bright attic study... follow me, quickly!' ",
   (None, 'मेरे पीछे आओ,'),
   " literally means 'come behind me'—the natural way to say 'follow me!'."])]
