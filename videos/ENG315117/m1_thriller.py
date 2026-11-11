"""ENG315117 English, Module 1 (Genre Study, thriller elective): codes, conventions and themes.

Texts: North by Northwest (film, 1959), The Talented Mr Ripley (film, 1999), The Dry (novel, 2016).
Criterion 1 (elements 1 to 3) is the one the external exam assesses for this module (Section A).
"""
from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, import_sibling

EC = import_sibling(__file__, 'eng_common.py')
VIS = import_sibling(__file__, 'm1_visuals.py')
Slide = EC.Slide

COURSE, MODULE = 'ENG315117', 'M1'
L.use(style.theme(COURSE, MODULE))

P1 = 'Part 1 · The thriller genre'
P2 = 'Part 2 · North by Northwest'
P3 = 'Part 3 · The Talented Mr Ripley'
P4 = 'Part 4 · The Dry'
P5 = 'Part 5 · Comparing the texts'
P6 = 'Part 6 · Writing the essay'

# --------------------------------------------------------------------------- references
REFS = {
    'course': Ref('eng315117-9.html', 'Course document, Module 1 Genre Study, content descriptions'),
    'standards': Ref('eng315117-9.html', 'Course document, Criterion 1 standards table'),
    'crit2': Ref('eng315117-9.html', 'Course document, Criterion 2 standards table'),
    'ext': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, Section A: Genre Study', page=3),
    'ext6': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, marking tool for Criterion 6', page=6),
    'ext2': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, assessment and marking tool', page=2),
    'list': Ref('ENG315117-English-Prescribed-Text-List-2026.pdf', 'Prescribed text list 2026, Module 1 Genre Study: Thriller', page=2),
    'nxnw': Ref('North_by_Northwest_1959_1080p_HEVC.mkv', 'North by Northwest (Hitchcock, 1959), dialogue and freeze frames'),
    'ripley': Ref('The_Talented_Mr_Ripley_1999_1080p_HEVC.mkv', 'The Talented Mr Ripley (Minghella, 1999), dialogue and freeze frames'),
    'dry': Ref('The Dry - Jane Harper.epub', 'The Dry (Harper, 2016), quotations'),
    # the other study texts live in the same content.csv; they are listed so every source is referenced
    'king': Ref('Different Seasons - Stephen King.epub', 'Module 2 study text (see the Module 2 video)'),
    'shaw': Ref('The Shawshank Redemption _1994_ - 1080p AVC.mkv', 'Module 2 study text (see the Module 2 video)'),
    'river': Ref('The Secret River - Kate Grenville.epub', 'Module 3 study text (see the Module 3 video)'),
}

SYLLABUS = {
    'S1': ('Analyse language, structural and stylistic choices (ACEEN041)', 'course'),
    'S2': ('Explain how each text conforms to or challenges the codes and conventions of a genre (ACEEN042)', 'course'),
    'S3': ('Analyse and evaluate how similar themes, ideas or concepts are treated in a particular genre (ACEEN043)', 'course'),
    'S4': ('Analyse the techniques, codes and conventions used in different genres, mediums and modes (ACEEN044)', 'course'),
    'S5': ('Consider how the conventions of genres can be challenged, manipulated or parodied (ACEEN045)', 'course'),
    'S6': ('Examine how genres and their conventions may have changed and adapted over time (ACEEN046)', 'course'),
    'S7': ('How language patterns can create shades of meaning (ACEEN047)', 'course'),
    'S8': ('How expectations of genres have developed and the effect when they are met, not met, extended or subverted (ACEEN048)', 'course'),
    'S9': ('How responses to texts and genres may change over time and in different cultural contexts (ACEEN049)', 'course'),
    'S10': ('Analyse how different texts within a genre represent similar ideas in different ways (ACEEN057)', 'course'),
    'S11': ('Compare and evaluate the impact of language conventions used in a variety of texts and genres (ACEEN059)', 'course'),
    'S12': ('Sustain analysis and argument, with simple referencing and accurate metalanguage (ACEEN053, 054, 056)', 'course'),
    'S13': ('Three prescribed texts for the elective, including one print and one non-print text', 'course'),
}
ELEMENTS = {
    1: ('Text, genre and context links: relationships between texts from similar or different genres and contexts', 'standards'),
    2: ('Distinctive features of genres: compare, contrast and evaluate', 'standards'),
    3: ('Codes and conventions: how they invite response and shape meaning', 'standards'),
}
EXAM_TOPICS = {
    'X1': ('Section A: one of three questions, answered with reference to two or three prescribed texts that the question does not name', 'ext'),
    'X2': ('Relationships between texts from one genre and the contexts in which they were created', 'ext'),
    'X3': ('How genre codes and conventions invite response and shape meaning', 'ext'),
    'X4': ('Analysis and evaluation of codes and conventions across forms, mediums and modes', 'ext'),
    'X5': ('Extended analytical essay in the third person, about sixty minutes, assessed also for Criterion 6', 'ext'),
}
CHECKS = []
ENG_CREDITS = ('Course content in this video is adapted from material published by {holder}, used under a Creative Commons Attribution 4.0 '
               'International licence. Short quotations and freeze frames from the study texts are shown for study and criticism, and belong to '
               'their creators. The practice questions are original. The full reference list is in the description, along with a link to any '
               'updated version of this video.')

# --------------------------------------------------------------------------- slides
TITLE = VIS.title_card

INTRO = Slide('bullets', title='How this module is assessed', chip='Module 1 · Criterion 1', size=34, items=[
    'Internal: an oral presentation, a comparative essay and an imaginative piece in the genre',
    'External: Section A of the exam, about 60 minutes, ONE of THREE questions',
    'Elements of Criterion 1:  1 Text, genre and context links · 2 Distinctive features of genres · 3 Codes and conventions',
    'C explains  ·  B analyses  ·  A evaluates',
    'Roadmap: the genre → three texts → comparing → writing the essay',
], foot=['', '', '', 'The verbs matter: marks move up as you go from explain to analyse to evaluate.', ''])

GENRE = Slide('grid', title='What a thriller promises its audience', chip='Element 2 · distinctive features', cols=4, per=2, size=19, ch_max=0.36, items=[
    ('SUSPENSE', 'Tension that builds', 'The audience fears what might happen. Delay, silence and withheld information stretch the wait.'),
    ('PROTAGONIST', 'An ordinary person in danger', 'A wrong man, a haunted investigator, or even a criminal we are drawn to follow.'),
    ('SECRETS', 'Identity and deception', 'Disguises, false names and lies. Nobody is quite who they claim to be.'),
    ('PURSUIT', 'Threat and a ticking clock', 'Chases, deadlines and an enemy who seems to know every move.'),
    ('PUZZLE', 'Red herrings and twists', 'Clues that mislead, then a revelation that makes us reread everything.'),
    ('SETTING', 'Places that press in', 'Crowded cities, isolated landscapes or sunlit beauty hiding something rotten.'),
    ('MORALS', 'Blurred lines', 'Guilt, justice and revenge are never simple. Heroes can do wrong.'),
    ('RESOLUTION', 'An ending that answers or denies', 'Order is restored, or it is not. Both choices carry a message.'),
])

CODES = Slide('grid', title='Codes and conventions: the toolkit', chip='Element 3 · codes and conventions', cols=3, per=1, size=26, ch_max=0.5, items=[
    ('FILM · TECHNICAL', 'How it is filmed and heard', 'Camera angle and shot size, lighting, editing, sound and music, framing, movement.'),
    ('FILM · SYMBOLIC', 'What is placed in the frame', 'Colour, costume, props, setting and repeated visual symbols.'),
    ('PRINT', 'How it is written', 'Word choice, imagery, symbolism, tropes, point of view, structure, motif and setting.'),
])

CODES_HOW = Slide('bullets', title='Writing about a code: name it, show it, explain it', chip='Element 3 · codes and conventions', size=34, items=[
    'NAME the convention or technique, with the right metalanguage',
    'SHOW it with a short quotation or a precise description of the shot',
    'EXPLAIN what it does to the audience: how it invites a response and shapes meaning',
    'LINK it back to the genre, the context and the question',
])

CHALLENGE = Slide('bullets', title='Conforming, challenging and changing', chip='Elements 2 and 3', size=34, items=[
    'Conform: the text delivers what the genre promises, so audiences feel at home',
    'Challenge or subvert: a convention is bent or broken, so meaning and surprise rise',
    'Parody or play: the genre is used with a wink, so humour sits beside the tension',
    'Over time: conventions adapt as audiences, technology and values change',
    'Responses change too: readers in new times and cultures notice different things',
])

NX_CONTEXT = Slide('media', title='North by Northwest (1959): context', chip='Element 1 · text, genre, context',
                   img=['nx_title'], cap=['Opening titles: kinetic typography by Saul Bass'], credit=['North by Northwest, 1959'],
                   bullets=['Directed by Alfred Hitchcock, known as the master of suspense',
                            'Made in the Cold War: spies, secrets and fear of hidden enemies',
                            'The wrong man story: a stranger swept into a plot he does not understand'])

NX_IDENTITY = Slide('media', title='North by Northwest: identity as the engine', chip='Element 3 · codes and conventions',
                    img=['nx_mistaken'], cap=['Roger Thornhill is mistaken for a man who does not exist'], credit=['North by Northwest, 1959'],
                    quote=[('“My name is Thornhill. Roger Thornhill. It’s never been anything else.”', 'Roger Thornhill'),
                           ('“With such expert play-acting, you make this very room a theater.”', 'Vandamm'),
                           ('“How can he get mistaken for George Kaplan when he doesn’t even exist?”', 'An intelligence officer')],
                    bullets=['Dialogue: a man loses control of his own name',
                             'Irony: an advertising man who trades in image is trapped by one',
                             'Theme: identity is a performance others can write for you'])

NX_FIELD = Slide('media', title='North by Northwest: the crop duster', chip='Element 3 · codes and conventions',
                 img=['nx_field', 'nx_plane_clip', 'nx_corn'],
                 cap=['An empty field in bright daylight', 'The plane turns on him', 'He runs for cover in the corn'],
                 credit=['North by Northwest, 1959'],
                 quote=[('“That plane’s dusting crops where there ain’t no crops.”', 'A bystander'), None, None],
                 bullets=['Setting: no shadows, no crowd, no place to hide',
                          'Sound: long silence, then the engine, with no music at first',
                          'Camera: long shot isolates him, then cuts close on the plane',
                          'Convention subverted: danger arrives in broad daylight'])

NX_END = Slide('media', title='North by Northwest: climax and resolution', chip='Elements 2 and 3',
               img=['nx_climb', 'nx_wives', 'nx_tunnel'],
               cap=['A chase across a national monument', 'Humour while hanging from a cliff', 'The final cut: a train enters a tunnel'], credit=['North by Northwest, 1959'],
               quote=[None, ('“My wives divorced me… I think they said I led too dull a life.”', 'Roger Thornhill'), ('“Come along, Mrs. Thornhill.”', 'Roger Thornhill')],
               bullets=['Set piece in an iconic location: spectacle and peril together',
                        'Order is restored: the hero is cleared and the couple united',
                        'Tone stays witty and romantic: a thriller that plays with its own conventions'])

RP_CONTEXT = Slide('media', title='The Talented Mr Ripley (1999): context', chip='Element 1 · text, genre, context',
                   img=['rp_title'], cap=['Opening titles: a face half hidden'], credit=['The Talented Mr Ripley, 1999'],
                   bullets=['Directed by Anthony Minghella, from Patricia Highsmith’s 1955 novel',
                            'Set in the late fifties but made in 1999: a modern look at old-style glamour',
                            'The protagonist is the criminal, so we watch the plot from inside his head'])

RP_IDENTITY = Slide('media', title='Ripley: identity, class and longing', chip='Element 3 · codes and conventions',
                    img=['rp_fake', 'rp_type'],
                    cap=['Tom explains why he lies', 'Tom types letters in another man’s name'], credit=['The Talented Mr Ripley, 1999'],
                    quote=[('“…better to be a fake somebody than a real nobody.”', 'Tom Ripley'), None],
                    bullets=['Dialogue: the line that unlocks his motive',
                             'Props: the typewriter and signature show identity as something made',
                             'Theme: class, envy and the cost of reinvention'])

RP_SETTING = Slide('media', title='Ripley: a sunlit setting for dark acts', chip='Element 3 · codes and conventions',
                   img=['rp_beach', 'rp_blood', 'rp_cabin'],
                   cap=['Bright Italian light and open water', 'Aftermath of a killing at sea', 'The closing cabin scene'],
                   credit=['The Talented Mr Ripley, 1999'],
                   quote=[None, ('“…put it in a room in the basement, and lock the door.”', 'Tom Ripley'), ('“I’m gonna be stuck in the basement, aren’t I?”', 'Tom Ripley')],
                   bullets=['Colour and light: beauty is the disguise for violence',
                            'Sound: jazz in the world of the story sets the mood',
                            'Ending: no justice, and Tom is trapped by his own lies',
                            'Convention challenged: the genre’s usual moral order is withheld'])

DRY_CONTEXT = Slide('bullets', title='The Dry (2016): context', chip='Element 1 · text, genre, context', size=34, items=[
    'Jane Harper’s debut novel, a crime thriller in the style often called rural noir',
    'Set in Kiewarra, a drought-struck Victorian farming town',
    'A federal agent, Aaron Falk, returns for a funeral and is drawn into a double investigation',
    'Past and present run side by side, so the truth about one death threatens the other',
])

DRY_QUOTES = Slide('quotes', title='The Dry: setting, tension and the hook', chip='Element 3 · codes and conventions', rows=3, size=32, items=[
    ('“To them there was little difference between a carcass and a corpse.”', 'The Dry, prologue', 'JUXTAPOSITION',
     'Blowflies make death ordinary. A cold, dark-humoured tone opens the book.'),
    ('“‘It’ll break,’ the farmers said as the months ticked over into a second year.”', 'The Dry, prologue', 'SETTING AS PRESSURE',
     'Drought wears down the town. The repeated hope sounds like a prayer.'),
    ('“Luke lied. You lied. Be at the funeral.”', 'The Dry, chapter one', 'ENIGMA',
     'Short sentences, a hook, and a secret that links two time frames.'),
])

DRY_TWIST = Slide('bullets', title='The Dry: structure, red herrings and the ending', chip='Elements 2 and 3', size=34, items=[
    'Structure: present investigation interleaved with flashbacks to the past',
    'Red herrings: the town blames Luke, then Falk, then others',
    'Reveal: the Hadler murders and Ellie’s death have different killers',
    'Ending: “The river was still gone. He hoped one day it would come back.”',
    'Convention extended: justice is partial, and the drought is a lasting wound',
])

THEMES = Slide('table', title='Themes across the three texts', chip='Criterion 2 · themes in genre', head=['', 'North by Northwest', 'The Talented Mr Ripley', 'The Dry'],
               size=25, label_w=0.16, rows=[
    ('Identity', 'A false name traps the hero, then frees him', 'Reinvention becomes a trap that grows', 'Past identity follows Falk home'),
    ('Truth and guilt', 'Innocence is proved by action', 'Guilt is hidden and never answered', 'Truth is uncovered at personal cost'),
    ('Community', 'Institutions hide the truth', 'Wealthy circles open, then close', 'A town protects its secrets'),
    ('Power and class', 'Spies manipulate ordinary people', 'Money decides who belongs', 'Land, water and reputation'),
    ('Nature and place', 'Open landscape becomes a threat', 'Sun and sea mask violence', 'Drought presses on everyone'),
])

COMPARE = Slide('table', title='Comparing conventions and mediums', chip='Elements 1 to 3', head=['', 'North by Northwest', 'Ripley', 'The Dry'],
                size=25, label_w=0.16, rows=[
    ('Protagonist', 'Innocent man on the run', 'Criminal at the centre', 'Haunted investigator'),
    ('Mood', 'Witty, romantic, suspenseful', 'Seductive, then claustrophobic', 'Heavy and unsettling'),
    ('Medium', 'Film: camera, music, editing', 'Film: light, jazz, performance', 'Print: voice, sentence rhythm, structure'),
    ('Ending', 'Order restored, with a joke', 'Order denied', 'Partial justice, lasting loss'),
])

OVER_TIME = Slide('bullets', title='How the genre changes over time', chip='Elements 1 and 2', size=34, items=[
    '1959: spectacle and romance, with Cold War fear kept at arm’s length',
    '1999: psychological and morally murky, looking back at the fifties through modern eyes',
    '2016: place and community take centre stage, with drought as a living threat',
    'Reception changes too: today’s audiences notice questions of class, sexuality and climate that earlier viewers might not',
])

PLAN = Slide('bullets', title='Section A: the plan', chip='Exam · Section A', size=34, items=[
    'About 60 minutes, ONE of THREE questions, third person',
    'Use two or three texts, even though the question will not name them',
    'Argue a clear line about genre, context, and how conventions shape response',
    'Build each paragraph: claim, evidence, analysis, link',
    'Criterion 6 counts: accurate, controlled language and logical structure',
])

MODEL = Slide('model', title='A model paragraph', chip='Exam · Section A',
              question='“In thrillers, ordinary settings are often the most threatening.” Discuss, with reference to two or three texts.',
              size=28, parts=[
    ('CLAIM', 'In thrillers, a familiar setting becomes menacing when the audience expects safety.'),
    ('EVIDENCE', 'In North by Northwest, the crop duster scene takes place in an empty field in daylight.'),
    ('ANALYSIS', 'Long shots and silence expose Thornhill, subverting the convention that danger hides in shadow and city streets.'),
    ('LINK', 'Similarly, The Dry makes drought-struck Kiewarra a place where nothing is safe, so the setting itself pressures every character.'),
])

TIPS = Slide('tips', title='Exam tips for Section A', chip='Exam · Section A', cols=2, size=26, items=[
    ('Answer the question', 'Use the words of the question in your first sentence and again at the end.'),
    ('Use the third person', 'Do not write “I”. The marking tool penalises it in Criterion 4.'),
    ('Two or three texts', 'Select texts that fit the question. Two strong texts beat three thin ones.'),
    ('Name the convention', 'Use metalanguage: shot, juxtaposition, motif, narrative structure.'),
    ('Quote briefly', 'Short, exact quotations or precise shot descriptions are enough.'),
    ('Evaluate for an A', 'Say which convention matters most and why, not only what each does.'),
    ('Use the context', 'Link each text to when and why it was made, and who received it.'),
    ('Plan for 15 minutes', 'Use the preparation time to choose texts and sketch your argument.'),
])

SUMMARY = Slide('grid', title='Module 1 in one screen', chip='Summary', cols=3, per=3, size=24, ch_max=0.3, items=[
    ('CONVENTIONS', 'Know the toolkit', 'Suspense, wrong-man plots, secrets, red herrings, setting, moral ambiguity.'),
    ('CODES', 'Name, show, explain', 'Technical and symbolic codes in film. Language and structure in print.'),
    ('CHANGE', 'Conform, challenge, evolve', 'Subverted expectations drive meaning, and the genre shifts over time.'),
    ('THEMES', 'Identity, truth, community', 'Compare how each text treats the same idea differently.'),
    ('CONTEXT', 'When and why', 'Cold War, late fifties glamour, drought-struck rural Australia.'),
    ('ESSAY', 'Claim, evidence, analysis, link', 'Third person, controlled language, two or three texts.'),
])

# --------------------------------------------------------------------------- scenes
SCENES = [
    Scene('title', P1, 'Welcome', TITLE, [
        Step("Welcome. This video revises Module one of English, the thriller genre study, using North by Northwest, "
             "The Talented Mr Ripley and The Dry. It is for class tests and other internal assessment, and for Section A of the end of year "
             "exam. By the end you will be able to name the key codes and conventions, explain how each text uses or challenges them, "
             "and compare the themes.", refs=['course', 'ext'], covers=['S13'], exam=['X1']),
    ]),
    Scene('intro', P1, 'How the module is assessed', INTRO, [
        Step("In school, this module gives you an oral presentation, a comparative essay and an imaginative piece in your genre. "
             "In the exam, Section A is about sixty minutes. You answer one of three questions, using two or three of your texts.",
             refs=['course', 'ext'], covers=['S13'], exam=['X1', 'X5']),
        Step("The marking is built on the three elements of Criterion one. Element one is text, genre and context links. Element two is the "
             "distinctive features of genres. Element three is codes and conventions.", refs=['standards'], elements=[1, 2, 3]),
        Step("The standards climb in three verbs. A C response explains, a B response analyses, and an A response evaluates. So do not just "
             "say what a convention is. Say how it shapes meaning and whether it matters.", refs=['standards'], elements=[1, 2, 3]),
        Step("First, the genre. Then North by Northwest, The Talented Mr Ripley and The Dry in turn. After that, comparing themes, and finally "
             "how to write the essay.", refs=['list', 'course'], covers=['S13']),
    ]),
    Scene('genre', P1, 'What a thriller promises', GENRE, [
        Step("A thriller promises suspense. The audience fears what might happen, and the writer stretches the wait with delay, silence and "
             "withheld information. The protagonist is usually an ordinary person in danger, though some thrillers follow a criminal instead.",
             refs=['course'], covers=['S4', 'S8'], elements=[2], exam=['X3']),
        Step("Secrets drive the plot. Disguises, false names and lies mean nobody is quite who they claim to be. A pursuit adds threat and a "
             "ticking clock, with an enemy who seems to know every move.", refs=['course'], covers=['S4'], elements=[2]),
        Step("There are puzzles too. Red herrings mislead us, then a twist makes us reread everything. Settings press in, whether a crowded "
             "city, an empty landscape or a beautiful place hiding something rotten.", refs=['course'], covers=['S4'], elements=[2]),
        Step("Finally, morals are blurred. Guilt, justice and revenge are never simple. And the ending either restores order or denies it. "
             "Both choices carry a message about the world.", refs=['course'], covers=['S4', 'S8'], elements=[2]),
    ]),
    Scene('codes', P1, 'Codes and conventions', CODES, [
        Step("Conventions are the habits of a genre. Codes are the tools used to deliver them. In film, technical codes are how a scene is filmed "
             "and heard: camera angle and shot size, lighting, editing, sound and music.", refs=['standards'], covers=['S4', 'S1'], elements=[3]),
        Step("Symbolic codes are what is placed in the frame: colour, costume, props, setting and repeated symbols.",
             refs=['standards'], covers=['S4', 'S1'], elements=[3]),
        Step("In print, codes are language choices and literary devices: word choice, imagery, symbolism, tropes, point of view, structure, "
             "motif and setting. The course glossary says the same, so use the right metalanguage.", refs=['standards'], covers=['S4', 'S7', 'S12'], elements=[3]),
    ]),
    Scene('codes_how', P1, 'Writing about a code', CODES_HOW, [
        Step("Here is a simple method for every paragraph. Name the technique. Show it with a short quotation or a precise description of the shot. "
             "Explain what it does to the audience. Then link it back to the genre and the question.",
             refs=['standards'], covers=['S1', 'S7', 'S11'], elements=[3]),
    ]),
    Scene('challenge', P1, 'Conforming, challenging and changing', CHALLENGE, [
        Step("A text can conform to the genre, which makes the audience feel at home. It can challenge or subvert a convention, which raises both "
             "meaning and surprise. It can also parody the genre, using it with a wink.", refs=['course'], covers=['S2', 'S5', 'S8'], elements=[2, 3]),
        Step("Conventions also change over time as audiences, technology and values change. And responses change too: readers in new times and "
             "cultures notice different things in the same text.", refs=['course'], covers=['S6', 'S9'], elements=[1, 2]),
    ]),
    Scene('nx_context', P2, 'Context and plot', NX_CONTEXT, [
        Step("North by Northwest was released in nineteen fifty nine, directed by Alfred Hitchcock, known as the master of suspense. It was made "
             "in the Cold War, a time of spies, secrets and fear of hidden enemies. The opening titles, by Saul Bass, already signal style and tension.",
             refs=['nxnw', 'list'], covers=['S1', 'S13'], elements=[1]),
        Step("Its plot is the wrong man story: an advertising man is swept into a spy plot he does not understand. That is a classic thriller "
             "convention, but Hitchcock plays with it.", refs=['nxnw'], covers=['S2', 'S5'], elements=[1, 2]),
    ]),
    Scene('nx_identity', P2, 'Identity as the engine', NX_IDENTITY, [
        Step("The film's engine is mistaken identity. Roger Thornhill says, my name is Thornhill, Roger Thornhill, it's never been anything else. "
             "But he has lost control of his own name. This is dialogue doing thematic work.", refs=['nxnw'], covers=['S1', 'S7', 'S10'], elements=[3]),
        Step("There is irony. Vandamm tells him, with such expert play-acting, you make this very room a theater. Thornhill is an advertising man, and a man who "
             "trades in image is trapped by an image someone else has made.", refs=['nxnw'], covers=['S7', 'S3'], elements=[3]),
        Step("The other side is that the agency invented George Kaplan. One officer asks, how can he get mistaken for George Kaplan when he doesn't "
             "even exist? So identity is a performance others can write for you. That is a theme you can compare across all three texts.",
             refs=['nxnw'], covers=['S3', 'S10'], elements=[1, 3]),
    ]),
    Scene('nx_field', P2, 'The crop duster', NX_FIELD, [
        Step("In the crop duster scene, Thornhill waits at a bus stop in an empty field in bright daylight. A bystander says, that plane's dusting "
             "crops where there ain't no crops. The setting has no shadows, no crowd and no place to hide.", refs=['nxnw'], covers=['S1', 'S4', 'S5'], elements=[3]),
        Step("Hitchcock uses long shots to isolate him, then cuts close to the plane. The sound is mostly silence, then the engine, with no music "
             "at first. Notice how little dialogue there is: the action is carried by the camera and sound.", refs=['nxnw'], covers=['S4', 'S11'], elements=[3], anim=2.4),
        Step("This subverts the convention that danger hides in shadow and city streets. Here it arrives in broad daylight. The same technique, "
             "withholding music, is one you can name and evaluate in an essay.", refs=['nxnw'], covers=['S5', 'S8'], elements=[2, 3]),
    ]),
    Scene('nx_end', P2, 'Climax and resolution', NX_END, [
        Step("The climax takes place on Mount Rushmore, an iconic national monument, which mixes spectacle with peril.",
             refs=['nxnw'], covers=['S4', 'S9'], elements=[3]),
        Step("Even at the cliff edge, the tone is playful. Thornhill jokes, my wives divorced me, I think they said I led too dull a life. Humour in peril is a "
             "convention Hitchcock extends, so suspense and comedy sit together.", refs=['nxnw'], covers=['S5', 'S8'], elements=[2, 3]),
        Step("The film ends with order restored: the hero is cleared and the couple united. At the cliff edge he says, come along, Mrs. Thornhill, and "
             "the final cut shows a train entering a tunnel. The tone stays witty and romantic, so this is a thriller that plays with its own conventions.",
             refs=['nxnw'], covers=['S5', 'S8', 'S2'], elements=[2, 3]),
    ]),
    Scene('rp_context', P3, 'Context and plot', RP_CONTEXT, [
        Step("The Talented Mr Ripley was released in nineteen ninety nine, directed by Anthony Minghella. It is based on Patricia Highsmith's "
             "nineteen fifty five novel, and set in the late fifties, so it looks back at an earlier era with modern eyes.",
             refs=['ripley', 'list'], covers=['S6', 'S13'], elements=[1]),
        Step("Tom Ripley, a poor young man, is sent to Italy to bring home a rich man's son, Dickie Greenleaf. The twist is that the protagonist is "
             "the criminal, so we watch the plot from inside his head.", refs=['ripley'], covers=['S2', 'S5'], elements=[1, 2]),
    ]),
    Scene('rp_identity', P3, 'Identity, class and longing', RP_IDENTITY, [
        Step("Identity is again central, but this time it is chosen. Tom says it would be better to be a fake somebody than a real nobody. "
             "That line unlocks his motive: class, envy and the longing to belong.", refs=['ripley'], covers=['S3', 'S10'], elements=[3]),
        Step("Props carry meaning. When Tom types letters in Dickie's name, we see identity as something made. Compare this with North by "
             "Northwest, where identity is forced on a man from outside.", refs=['ripley', 'nxnw'], covers=['S10', 'S11'], elements=[1, 3]),
    ]),
    Scene('rp_setting', P3, 'A sunlit setting', RP_SETTING, [
        Step("The setting is the opposite of classic noir. Colour and bright Italian light make beauty the disguise for violence. "
             "Jazz in the world of the story sets the mood and shows the glamour Tom wants.", refs=['ripley'], covers=['S4', 'S6'], elements=[3]),
        Step("After the killing at sea, the film moves from open water to enclosed rooms. Tom talks about putting the past in a room in the basement and locking the door. His lies close in on him.",
             refs=['ripley'], covers=['S1', 'S4'], elements=[3]),
        Step("In the final cabin scene, Tom says, I'm gonna be stuck in the basement, aren't I? The ending withholds "
             "justice, so the genre's usual moral order is challenged, and the audience is left unsettled.", refs=['ripley'], covers=['S5', 'S8'], elements=[2, 3]),
    ]),
    Scene('dry_context', P4, 'Context and plot', DRY_CONTEXT, [
        Step("The Dry is Jane Harper's debut novel, published in twenty sixteen. It is a crime thriller in the style often called rural noir. "
             "Federal agent Aaron Falk returns to Kiewarra, a drought-struck Victorian farming town, for a funeral.", refs=['dry', 'list'], covers=['S6', 'S13'], elements=[1]),
        Step("Past and present run side by side, so the truth about one death threatens the other. As a print text, it uses language, rhythm and "
             "structure where the films use camera and sound.", refs=['dry'], covers=['S4', 'S1'], elements=[1, 3]),
    ]),
    Scene('dry_quotes', P4, 'Setting, tension and the hook', DRY_QUOTES, [
        Step("In the prologue, the writer says, to them there was little difference between a carcass and a corpse. The blowflies are a "
             "juxtaposition. They make death ordinary, and the tone is cold and dark.", refs=['dry'], covers=['S1', 'S7'], elements=[3]),
        Step("Next, the farmers say, it'll break, as the months tick over into a second year. The repetition sounds like a prayer. Setting is "
             "pressure here, wearing the whole town down.", refs=['dry'], covers=['S4', 'S7'], elements=[3]),
        Step("Then the letter. Luke lied. You lied. Be at the funeral. Short sentences, a hook, and a secret that links two time frames. This is how "
             "print builds suspense without a camera.", refs=['dry'], covers=['S1', 'S7', 'S11'], elements=[3]),
    ]),
    Scene('dry_twist', P4, 'Structure and the ending', DRY_TWIST, [
        Step("Structure is a key convention in The Dry. The present investigation is interleaved with flashbacks to the past. The town blames Luke, "
             "then Falk, then others, which are classic red herrings.", refs=['dry'], covers=['S1', 'S4', 'S8'], elements=[3]),
        Step("The reveal is that the Hadler murders and Ellie's death have different killers. That is a twist that rewards reading carefully.",
             refs=['dry'], covers=['S2', 'S8'], elements=[2, 3]),
        Step("The novel ends with Falk at the dry riverbed. The river was still gone. He hoped one day it would come back. Justice is partial and the "
             "drought is a lasting wound. A convention is extended, because the ending is neither fully happy nor fully hopeless.",
             refs=['dry'], covers=['S5', 'S8'], elements=[2, 3]),
    ]),
    Scene('themes', P5, 'Themes across the texts', THEMES, [
        Step("Now compare themes. Identity: in North by Northwest a false name traps the hero and then frees him. In Ripley, reinvention becomes a "
             "trap that grows. In The Dry, the past identity of Falk follows him home.", refs=['nxnw', 'ripley', 'dry', 'crit2'], covers=['S3', 'S10'], elements=[1]),
        Step("Truth and guilt: Thornhill proves innocence through action. Tom Ripley hides his guilt and is never answered. Falk uncovers truth at "
             "personal cost.", refs=['nxnw', 'ripley', 'dry'], covers=['S3', 'S10'], elements=[1]),
        Step("Community: institutions hide the truth in the film from nineteen fifty nine. The wealthy circles in Ripley open, then close. In the novel, "
             "a small town protects its secrets.", refs=['nxnw', 'ripley', 'dry'], covers=['S3', 'S9'], elements=[1]),
        Step("Power and class: spies manipulate ordinary people, money decides who belongs, and land, water and reputation hold the town together.",
             refs=['nxnw', 'ripley', 'dry'], covers=['S3', 'S10'], elements=[1]),
        Step("Nature and place: an open landscape becomes a threat, sun and sea mask violence, and drought presses on everyone.",
             refs=['nxnw', 'ripley', 'dry'], covers=['S3', 'S4'], elements=[1]),
    ]),
    Scene('compare', P5, 'Comparing conventions and mediums', COMPARE, [
        Step("Compare protagonists. North by Northwest has an innocent man on the run. Ripley has a criminal at the centre. The Dry has a haunted "
             "investigator.", refs=['nxnw', 'ripley', 'dry'], covers=['S2', 'S10'], elements=[1, 2]),
        Step("Compare mood. The film from nineteen fifty nine is witty and romantic. Ripley is seductive, then claustrophobic. The Dry is heavy and unsettling.",
             refs=['nxnw', 'ripley', 'dry'], covers=['S10', 'S11'], elements=[2, 3]),
        Step("Compare medium. Film uses camera, music, light and performance. Print uses voice, sentence rhythm and structure. A strong answer "
             "explains what each medium can do that the other cannot.", refs=['nxnw', 'ripley', 'dry'], covers=['S4', 'S11'], elements=[2, 3], exam=['X4']),
        Step("Compare endings. Order is restored with a joke, order is denied, or justice is partial and loss lasts. The ending is where each text "
             "makes its clearest statement about its genre.", refs=['nxnw', 'ripley', 'dry'], covers=['S8', 'S10'], elements=[2, 3], exam=['X2']),
    ]),
    Scene('over_time', P5, 'How the genre changes', OVER_TIME, [
        Step("Over time, the genre shifts. Nineteen fifty nine: spectacle and romance, with Cold War fear kept at arm's length. Nineteen ninety nine: "
             "psychological and morally murky. Twenty sixteen: place and community take centre stage, and drought is a living threat.",
             refs=['nxnw', 'ripley', 'dry'], covers=['S6', 'S8'], elements=[1, 2]),
        Step("Reception changes too. Today's audiences may notice questions of class, sexuality and climate that earlier viewers did not. "
             "Responses to texts and genres change over time and across cultures, and a good essay can say so.",
             refs=['nxnw', 'ripley', 'dry'], covers=['S9'], elements=[1]),
    ]),
    Scene('plan', P6, 'The Section A plan', PLAN, [
        Step("In Section A you have about sixty minutes and one of three questions. Write in the third person. Use two or three texts, even though "
             "the question will not name them. Argue a clear line about genre, context, and how conventions shape response.",
             refs=['ext'], covers=['S12'], elements=[1, 2, 3], exam=['X1', 'X5']),
        Step("Build each paragraph as claim, evidence, analysis and link. Criterion six counts too: accurate, controlled language and a logical "
             "structure. A C on Criterion six is needed for a satisfactory achievement award or above, so keep control of your sentences.",
             refs=['ext', 'ext6'], covers=['S12'], exam=['X5']),
    ]),
    Scene('model', P6, 'A model paragraph', MODEL, [
        Step("Here is an original practice question. In thrillers, ordinary settings are often the most threatening. Discuss, with reference to two "
             "or three texts. First, the claim: in thrillers, a familiar setting becomes menacing when the audience expects safety.",
             refs=['ext'], covers=['S12'], elements=[1, 2, 3], exam=['X1'],
             problem='In thrillers, ordinary settings are often the most threatening. Discuss, with reference to two or three texts.'),
        Step("The evidence: in North by Northwest, the crop duster scene takes place in an empty field in daylight.", refs=['nxnw'],
             covers=['S12', 'S1'], elements=[3]),
        Step("The analysis: long shots and silence expose Thornhill, subverting the convention that danger hides in shadow and city streets.",
             refs=['nxnw'], covers=['S12', 'S5'], elements=[3]),
        Step("The link: similarly, The Dry makes drought-struck Kiewarra a place where nothing is safe. So the setting pressures every character. "
             "That is a short, controlled paragraph that compares two texts.", refs=['dry'], covers=['S12', 'S10'], elements=[1, 3]),
    ]),
    Scene('exam_tips', P6, 'Exam and test tips', TIPS, [
        Step("Tip: answer the question. Use its words in your first sentence and again at the end.", refs=['ext'], covers=['S12'], exam=['X1']),
        Step("Tip: write in the third person. The marking tool says responses not in the required third person are penalised in Criterion four.",
             refs=['ext2'], covers=['S12'], exam=['X5']),
        Step("Tip: choose two or three texts that fit the question. Two strong texts beat three thin ones, and the marking tool says that "
             "referring to two rather than three is not a lesser response.", refs=['ext2'], covers=['S13'], exam=['X1']),
        Step("Tip: name the convention with the right metalanguage, such as shot, juxtaposition, motif or narrative structure.",
             refs=['standards'], covers=['S12', 'S1'], elements=[3]),
        Step("Tip: quote briefly. Short exact quotations or precise shot descriptions are enough, and the exam only needs simplified referencing.",
             refs=['ext2'], covers=['S12']),
        Step("Tip: for an A, evaluate. Say which convention matters most and why, not only what each does.", refs=['standards'], elements=[1, 2, 3]),
        Step("Tip: use context. Link each text to when and why it was made, and who received it.", refs=['standards'], covers=['S6', 'S9'], elements=[1]),
        Step("Tip: use the fifteen minutes of preparation time to choose your texts and sketch your argument. In class tests, plan too.",
             refs=['ext2'], covers=['S12'], exam=['X5']),
    ]),
    Scene('summary', P6, 'Module 1 in one screen', SUMMARY, [
        Step("Module one in one screen. Know the toolkit of conventions. Name, show and explain each code. Conform, challenge and evolve: that is "
             "where meaning lives.", refs=['course'], covers=['S2', 'S4'], elements=[2, 3]),
        Step("Compare themes of identity, truth and community. Know when and why each text was made. And write in claim, evidence, analysis, link.",
             refs=['course'], covers=['S3', 'S6'], elements=[1]),
        Step("Good luck with your class tests, your oral and your essays, and with Section A of the exam.", refs=['ext']),
    ]),
]

# =========================================================================== key scenes, quotes and requirements (added)
def K(text, refs, covers=(), elements=(), **kw):
    return Step(text, refs=list(refs), covers=list(covers), elements=list(elements), **kw)


REQS = Slide('grid', title='What you must be able to discuss', chip='Requirements · Module 1', cols=3, per=1, size=26, ch_max=0.5, items=[
    ('CODES AND CONVENTIONS', 'Element 3 · Section A', 'Name codes and conventions, show them in a scene or quotation, and explain how they invite a response and shape meaning.'),
    ('GENRE AND CONTEXT', 'Elements 1 and 2', 'Compare the distinctive features of the thriller across your texts, and link each text to its time, place and audience.'),
    ('THEMES', 'Criterion 2 · themes in genre', 'Say how each text represents identity, truth and guilt, and community and place, and compare them.'),
])

REQ_HOW = Slide('bullets', title='How the scene guides work', chip='Requirements · Module 1', size=32, items=[
    'Each key scene shows: what happens, the freeze frame, the quotation',
    'CODE or CONVENTION: the technique, and how it shapes response',
    'THEME: the idea the scene carries, ready to compare across texts',
    'CONTEXT: the time, place or audience that explains the choice',
    'Each text ends with a quote bank to learn',
])

NX_TAXI = Slide('media', title='Key scene: the advertising man', chip='Element 3 · codes and conventions',
                img=['nx_taxi'], cap=['Thornhill dictates to his secretary in a taxi'], credit=['North by Northwest, 1959'],
                quote=[('“In the world of advertising, there’s no such thing as a lie.”', 'Roger Thornhill'),
                       ('“There’s only the expedient exaggeration.”', 'Roger Thornhill')],
                bullets=['Opening scene: a busy modern city and a man who sells images',
                         'Quick, witty dialogue sets the light tone of the whole film',
                         'Theme planted early: identity is something you can shape'],
                tagline=['CODE: dialogue · THEME: image', 'CODE: dialogue · THEME: image'])

NX_UN = Slide('media', title='Key scene: the wrong man at the United Nations', chip='Elements 2 and 3',
              img=['nx_un'], cap=['At the United Nations, just before the killing'], credit=['North by Northwest, 1959'],
              quote=[('“Listen to me. I had nothing to do with this.”', 'Roger Thornhill'), ('“Listen to me. I had nothing to do with this.”', 'Roger Thornhill')],
              bullets=['A public place, a crowd, and a killing in front of everyone',
                       'Thornhill picks up the knife, so he looks guilty',
                       'Convention: the innocent hero is framed and must run'],
              tagline=['CONVENTION: wrong man · THEME: guilt', 'CONVENTION: wrong man · THEME: guilt'])

NX_DECOY = Slide('media', title='Key scene: the agency’s decoy', chip='Element 1 · text, genre, context',
                 quote=[('“Our non-existent decoy, George Kaplan… has fortuitously become a live decoy.”', 'An intelligence officer'),
                        ('“We do nothing.”', 'An intelligence officer')],
                 bullets=['The agency invented Kaplan to distract the enemy',
                          'Then it chooses to leave Thornhill in danger',
                          'Context: Cold War secrecy, where ordinary people are tools'],
                 tagline=['CONTEXT: Cold War · THEME: power', 'CONTEXT: Cold War · THEME: power'])

NX_DINING = Slide('media', title='Key scene: the train and Eve Kendall', chip='Elements 2 and 3',
                  img=['nx_dining'], cap=['Thornhill in the dining car'], credit=['North by Northwest, 1959'],
                  quote=[('“I never discuss love on an empty stomach.”', 'Eve Kendall')],
                  bullets=['Dialogue as flirtation: sharp and playful, in a dangerous situation',
                           'Convention: the glamorous woman whose loyalties are unclear',
                           'Theme: trust and performance, since she plays a role too'],
                  tagline=['CONVENTION: ambiguous ally · THEME: trust'])

NX_AUCTION = Slide('media', title='Key scene: the auction', chip='Elements 2 and 3',
                   img=['nx_auction'], cap=['The villain at the auction'], credit=['North by Northwest, 1959'],
                   quote=[('“I didn’t realize you were an art collector. I thought you just collected corpses.”', 'Roger Thornhill')],
                   bullets=['Setting: a polite, wealthy room where nothing can be done openly',
                            'Tone: witty insults under threat',
                            'Theme: power and class, as the villain is cultured and rich'],
                   tagline=['CODE: tone and wit · THEME: power'])

NX_BANK = Slide('grid', title='Quote bank: North by Northwest', chip='Learn these', cols=2, per=2, size=19, ch_max=0.3, items=[
    ('IDENTITY', '“My name is Thornhill. Roger Thornhill. It’s never been anything else.”', 'Thornhill at the Plaza: a name that others rewrite.'),
    ('IMAGE', '“There’s only the expedient exaggeration.”', 'Advertising logic, ironically turned on the hero.'),
    ('DECEPTION', '“Our non-existent decoy, George Kaplan…”', 'The agency invents a person, then risks a real one.'),
    ('SETTING', '“That plane’s dusting crops where there ain’t no crops.”', 'Danger in daylight: a subverted convention.'),
    ('WIT AND POWER', '“I thought you just collected corpses.”', 'Humour under threat at the auction.'),
    ('RESOLUTION', '“Come along, Mrs. Thornhill.”', 'Order restored with a romantic, playful close.'),
])

RP_TALENT = Slide('media', title='Key scene: Tom names his talents', chip='Elements 2 and 3',
                  img=['rp_herbert'], cap=['Tom with Dickie in Italy'], credit=['The Talented Mr Ripley, 1999'],
                  quote=[('“Forging signatures, telling lies, impersonating practically anybody.”', 'Tom Ripley, listing his talents')],
                  bullets=['Dialogue: a joke that is also a confession',
                           'Foreshadowing: the whole plot is built from these skills',
                           'Theme: identity as performance'],
                  tagline=['CODE: foreshadowing · THEME: identity'])

RP_SUN = Slide('media', title='Key scene: the sun and the cold', chip='Elements 2 and 3',
               img=['rp_sun', 'rp_sun'], cap=['Marge in the Italian sun', 'Tom describes what Dickie does'], credit=['The Talented Mr Ripley, 1999'],
               quote=[('“It’s like the sun shines on you, and it’s glorious.”', 'Tom Ripley, about Dickie'),
                      ('“And then he forgets you and it’s very, very cold.”', 'Tom Ripley, about Dickie')],
               bullets=['Imagery: sun and cold show how Dickie’s attention feels',
                        'It explains Tom’s longing and his later anger',
                        'Theme: envy, class and belonging'],
               tagline=['CODE: imagery · THEME: envy', 'CODE: imagery · THEME: envy'])

RP_BOAT = Slide('media', title='Key scene: the boat', chip='Elements 2 and 3',
                img=['rp_boat'], cap=['Dickie and Tom, moments before the killing'], credit=['The Talented Mr Ripley, 1999'],
                quote=[('“The funny thing is, I’m not pretending to be somebody else, and you are.”', 'Dickie')],
                bullets=['Dickie mocks Tom’s pretending, which is the wound that triggers the killing',
                         'A calm sea becomes a trap: violence arrives suddenly',
                         'Convention: a turning point in the middle of the story'],
                tagline=['CODE: setting and sudden violence · THEME: class'])

RP_BASEMENT = Slide('media', title='Key scene: the room in the basement', chip='Elements 2 and 3',
                    img=['rp_basement'], cap=['Tom talks about how to live with the past'], credit=['The Talented Mr Ripley, 1999'],
                    quote=[('“…take the past and put it in a room in the basement, and lock the door…”', 'Tom Ripley')],
                    bullets=['Motif: the basement stands for hidden guilt',
                             'Language: a domestic image for a troubled mind',
                             'It returns in the final scene, which closes the pattern'],
                    tagline=['CODE: motif · THEME: guilt'])

RP_END = Slide('media', title='Key scene: the closing cabin', chip='Elements 2 and 3',
               img=['rp_cabin', 'rp_dark'], cap=['The final cabin scene', 'Tom’s face in shadow'], credit=['The Talented Mr Ripley, 1999'],
               quote=[('“I’m gonna be stuck in the basement, aren’t I?”', 'Tom Ripley'),
                      ('“Tom is talented. Tom is tender. Tom is beautiful.”', 'Closing scenes')],
               bullets=['Light and framing: enclosed rooms and shadow',
                        'A list of good qualities sits beside a murderer',
                        'The ending denies justice, which challenges the genre’s moral order'],
               tagline=['CODE: framing · THEME: guilt', 'CODE: irony · THEME: truth'])

RP_BANK = Slide('grid', title='Quote bank: The Talented Mr Ripley', chip='Learn these', cols=2, per=2, size=19, ch_max=0.3, items=[
    ('TALENT', '“Forging signatures, telling lies, impersonating practically anybody.”', 'Tom’s skills, and the engine of the plot.'),
    ('ENVY', '“It’s like the sun shines on you, and it’s glorious.”', 'How Dickie’s attention feels, and why Tom wants it.'),
    ('MOTIVE', '“…better to be a fake somebody than a real nobody.”', 'The line that explains Tom’s choices.'),
    ('CLASS', '“The funny thing is, I’m not pretending to be somebody else, and you are.”', 'Dickie’s cruel remark before the killing.'),
    ('GUILT', '“…put it in a room in the basement, and lock the door.”', 'Concealment as a motif.'),
    ('ENDING', '“I’m gonna be stuck in the basement, aren’t I?”', 'The last scene’s answer: confinement without justice.'),
])

DRY_PROLOGUE = Slide('quotes', title='Key scene: the prologue', chip='Element 3 · codes and conventions', rows=3, size=26, items=[
    ('“It wasn’t as though the farm hadn’t seen death before, and the blowflies didn’t discriminate.”', 'The Dry, prologue', 'TONE',
     'Matter-of-fact violence, which is chilling.'),
    ('“Just one human heart beat within a kilometre radius of the farm.”', 'The Dry, prologue', 'FOCALISATION',
     'A cold, camera-like view: only one person is alive.'),
    ('“So nothing reacted when deep inside the house, the baby started crying.”', 'The Dry, prologue', 'HOOK',
     'The last line withholds the detail we most want.'),
])

DRY_RETURN = Slide('quotes', title='Key scene: the funeral and the return', chip='Elements 2 and 3', rows=3, size=26, items=[
    ('“The funeral, the wake, one night and he was gone. Eighteen hours, he calculated. No more.”', 'The Dry, chapter one', 'CLOCK',
     'The outsider who does not want to be there, with a limit set.'),
    ('“Still the same, were the words that sprang to mind. Three coffins said differently.”', 'The Dry, chapter one', 'JUXTAPOSITION',
     'Appearance set against fact, a core thriller tension.'),
    ('“Aaron Falk, don’t you bloody dare leave.”', 'The Dry, chapter two', 'PAST AS PRESSURE',
     'Old bonds pull him back into the town.'),
])

DRY_TOWN = Slide('quotes', title='Key scene: the town, the drought and the fire', chip='Elements 2 and 3', rows=3, size=26, items=[
    ('“The drought. It’s going to kill this town.”', 'Whitlam, the school principal', 'SETTING AS THREAT',
     'Said as a worry about money, which hides a darker meaning.'),
    ('“Two years without decent rainfall and now doused in alcohol. They were standing on a matchbox.”', 'The Dry, the fire', 'CLIMAX IMAGERY',
     'Drought becomes a physical danger in the final chase.'),
    ('“If my dad finds out, he will kill me.”', 'Ellie Deacon’s diary', 'REVELATION',
     'A teenage voice from the past shows who the danger was.'),
])

DRY_END = Slide('quotes', title='Key scene: the ending', chip='Elements 2 and 3', rows=3, size=26, items=[
    ('“Twenty years was twenty years, but some things shouldn’t be swept away.”', 'The Dry, final chapters', 'MEMORY',
     'Remembering Ellie is a moral act, so the ending is about justice for the past.'),
    ('“Its secrets and lies and fear.”', 'The Dry, final chapters', 'COMMUNITY',
     'The town’s real enemy was what it hid.'),
    ('“See you in another twenty years.”', 'Gretchen to Falk', 'TONE',
     'Wary and unsentimental, so no easy reconciliation.'),
])

DRY_BANK = Slide('grid', title='Quote bank: The Dry', chip='Learn these', cols=2, per=2, size=19, ch_max=0.3, items=[
    ('SETTING', '“‘It’ll break,’ the farmers said as the months ticked over into a second year.”', 'Drought as pressure and prayer.'),
    ('HOOK', '“Luke lied. You lied. Be at the funeral.”', 'The letter that links two time frames.'),
    ('JUXTAPOSITION', '“Three coffins said differently.”', 'What looks the same is not.'),
    ('THREAT', '“They were standing on a matchbox.”', 'Drought and fire in the climax.'),
    ('TRUTH', '“If my dad finds out, he will kill me.”', 'Ellie’s voice reveals the real danger.'),
    ('MEMORY', '“…some things shouldn’t be swept away.”', 'The moral of the ending.'),
])

QUOTE_THEMES = Slide('table', title='Quote bank: themes across the texts', chip='Criterion 2 · themes in genre',
                     head=['', 'North by Northwest', 'Mr Ripley', 'The Dry'], size=23, label_w=0.14, rows=[
    ('Identity', '“My name is Thornhill. Roger Thornhill.”', '“…a fake somebody than a real nobody.”', '“Luke lied. You lied.”'),
    ('Truth and guilt', '“I had nothing to do with this.”', '“…put it in a room in the basement…”', '“Three coffins said differently.”'),
    ('Community', '“…a live decoy.”', '“…the sun shines on you…”', '“Its secrets and lies and fear.”'),
    ('Place', '“…dusting crops where there ain’t no crops.”', '“…stuck in the basement…”', '“The river was still gone.”'),
])

NEW = {
    'reqs': Scene('reqs', P1, 'What you must discuss', REQS, [
        K("What do you need to be able to talk about? Three things. First, codes and conventions: name them, show them in a scene or a quotation, and explain how they "
          "invite a response and shape meaning. That is element three, and the heart of Section A.", ['standards', 'ext'], ['S2', 'S4'], [3], exam=['X3']),
        K("Second, genre and context. Compare the distinctive features of the thriller across your texts, and link each text to its time, place and audience. "
          "Those are elements one and two.", ['standards'], ['S6', 'S10'], [1, 2], exam=['X2']),
        K("Third, themes. Say how each text represents identity, truth and guilt, and community and place, and compare them. Criterion two covers this in "
          "its three genre elements.", ['crit2'], ['S3', 'S10'], [1, 2, 3]),
    ]),
    'req_how': Scene('req_how', P1, 'How the scene guides work', REQ_HOW, [
        K("From here, each text gets key scene guides. Each one shows what happens, a freeze frame, and a quotation. Then it names the code or convention, the "
          "theme, and the context. Each text ends with a quote bank, so you can learn the lines that matter most.", ['course', 'ext'], ['S1', 'S12'], [1, 2, 3], exam=['X1']),
    ]),
    'nx_taxi': Scene('nx_taxi', P2, 'Key scene: the advertising man', NX_TAXI, [
        K("Key scene one is the opening in New York. Roger Thornhill dictates to his secretary in a taxi and says, in the world of advertising, there's no "
          "such thing as a lie. The busy city and the grey suit introduce a man who sells images.", ['nxnw'], ['S1', 'S7'], [3]),
        K("He adds, there's only the expedient exaggeration. The code is witty dialogue, which sets the light tone that Hitchcock later plays against danger. "
          "The theme is planted early: identity is something you can shape.", ['nxnw'], ['S3', 'S7'], [3]),
    ]),
    'nx_un': Scene('nx_un', P2, 'Key scene: the wrong man', NX_UN, [
        K("Key scene: the United Nations. Thornhill is looking for a man called Townsend, who is killed in front of everyone. Thornhill picks up the knife, and "
          "cries, listen to me, I had nothing to do with this. A public place, a crowd, and he looks guilty.", ['nxnw'], ['S2', 'S4'], [2, 3]),
        K("The convention is the wrong man: an innocent hero framed and forced to run. For an A, say how this invites sympathy, and how the theme "
          "of guilt and appearance is built.", ['nxnw'], ['S2', 'S3'], [2, 3]),
    ]),
    'nx_decoy': Scene('nx_decoy', P2, 'Key scene: the decoy', NX_DECOY, [
        K("Key scene: the agency. An officer calls George Kaplan, our non-existent decoy, who has fortuitously become a live decoy. Then the answer to the "
          "danger is, we do nothing. Context matters here: Cold War secrecy treats ordinary people as tools. Theme: power.", ['nxnw'], ['S3', 'S6'], [1]),
    ]),
    'nx_dining': Scene('nx_dining', P2, 'Key scene: the train', NX_DINING, [
        K("Key scene: the train. Eve Kendall says, I never discuss love on an empty stomach. The dialogue is flirtatious and playful, while the situation is "
          "dangerous. Eve is the glamorous woman whose loyalties are unclear, a thriller convention, and she plays a role too. Theme: trust.", ['nxnw'], ['S2', 'S4'], [2, 3]),
    ]),
    'nx_auction': Scene('nx_auction', P2, 'Key scene: the auction', NX_AUCTION, [
        K("Key scene: the auction. Thornhill tells the villain, I didn't realize you were an art collector, I thought you just collected corpses. The room "
          "is polite and wealthy, so insults come as wit. Tone and wit are codes of this film, and the theme is power and class.", ['nxnw'], ['S1', 'S4'], [2, 3]),
    ]),
    'nx_bank': Scene('nx_bank', P2, 'Quote bank: North by Northwest', NX_BANK, [
        K("Here is the quote bank for North by Northwest. For identity, my name is Thornhill, Roger Thornhill, it's never been anything else. For image, "
          "there's only the expedient exaggeration.", ['nxnw'], ['S3', 'S7'], [1, 3], exam=['X1']),
        K("For deception, our non-existent decoy, George Kaplan. For setting and a subverted convention, that plane's dusting crops where there ain't no crops.",
          ['nxnw'], ['S5', 'S7'], [2, 3]),
        K("For wit and power, I thought you just collected corpses. And for resolution, come along, Mrs. Thornhill. Learn each line with the code, "
          "theme or convention it proves.", ['nxnw'], ['S8', 'S11'], [2, 3]),
    ]),
    'rp_talent': Scene('rp_talent', P3, 'Key scene: the talents', RP_TALENT, [
        K("Key scene: Tom names his talents. He answers, forging signatures, telling lies, impersonating practically anybody. It is a joke that is also a "
          "confession. The code is foreshadowing, because the whole plot is built from these skills. The theme is identity as performance.", ['ripley'], ['S1', 'S3'], [3]),
    ]),
    'rp_sun': Scene('rp_sun', P3, 'Key scene: the sun and the cold', RP_SUN, [
        K("Key scene: Tom tells Marge about Dickie. He says, it's like the sun shines on you, and it's glorious.", ['ripley'], ['S1', 'S7'], [3]),
        K("Then, and then he forgets you and it's very, very cold. The imagery of sun and cold shows how Dickie's attention feels, and explains Tom's longing. "
          "Theme: envy, class and belonging.", ['ripley'], ['S3', 'S7'], [2, 3]),
    ]),
    'rp_boat': Scene('rp_boat', P3, 'Key scene: the boat', RP_BOAT, [
        K("Key scene: the boat. Dickie mocks Tom's pretending: the funny thing is, I'm not pretending to be somebody else, and you are. That wound triggers the "
          "killing. A calm sea becomes a trap, and violence arrives suddenly at the turning point. Theme: class.", ['ripley'], ['S2', 'S4'], [2, 3]),
    ]),
    'rp_basement': Scene('rp_basement', P3, 'Key scene: the room in the basement', RP_BASEMENT, [
        K("Key scene: the basement. Tom talks about how to live with the past: take it and put it in a room in the basement, and lock the door. The "
          "motif of the basement stands for hidden guilt. It returns in the final scene, which closes the pattern.", ['ripley'], ['S1', 'S7'], [3]),
    ]),
    'rp_end': Scene('rp_end', P3, 'Key scene: the ending', RP_END, [
        K("Key scene: the closing cabin. Tom says, I'm gonna be stuck in the basement, aren't I? Light and framing give enclosed rooms and shadow.",
          ['ripley'], ['S5', 'S8'], [2, 3]),
        K("A list says Tom is talented, Tom is tender, Tom is beautiful, which sits beside a murderer. That is irony. The ending denies justice, so it "
          "challenges the genre's moral order.", ['ripley'], ['S5', 'S8'], [2, 3]),
    ]),
    'rp_bank': Scene('rp_bank', P3, 'Quote bank: Ripley', RP_BANK, [
        K("Quote bank for Ripley. Talent: forging signatures, telling lies, impersonating practically anybody. Envy: it's like the sun shines on you, "
          "and it's glorious.", ['ripley'], ['S3', 'S7'], [1, 3], exam=['X1']),
        K("Motive: better to be a fake somebody than a real nobody. Class: the funny thing is, I'm not pretending to be somebody else, and you are.",
          ['ripley'], ['S3', 'S10'], [2, 3]),
        K("Guilt: put it in a room in the basement, and lock the door. And the ending: I'm gonna be stuck in the basement, aren't I?",
          ['ripley'], ['S5', 'S8'], [2, 3]),
    ]),
    'dry_prologue': Scene('dry_prologue', P4, 'Key scene: the prologue', DRY_PROLOGUE, [
        K("Key scene: the prologue. It begins, it wasn't as though the farm hadn't seen death before, and the blowflies didn't discriminate. The tone is matter-of-fact, "
          "which makes the violence chilling.", ['dry'], ['S1', 'S7'], [3]),
        K("Then, just one human heart beat within a kilometre radius of the farm. The view is cold and almost camera-like: only one person is alive. "
          "The point of view is a code you can name.", ['dry'], ['S1', 'S4'], [3]),
        K("The prologue ends, so nothing reacted when deep inside the house, the baby started crying. The last line is a hook, because it withholds the "
          "detail we most want.", ['dry'], ['S7', 'S8'], [3]),
    ]),
    'dry_return': Scene('dry_return', P4, 'Key scene: the funeral', DRY_RETURN, [
        K("Key scene: the funeral. Falk limits his own time: the funeral, the wake, one night and he was gone, eighteen hours, he calculated, no more. This is the "
          "outsider who does not want to be there, with a clock.", ['dry'], ['S2', 'S8'], [2, 3]),
        K("Then, still the same, were the words that sprang to mind, three coffins said differently. Juxtaposition sets appearance against fact, a core "
          "thriller tension.", ['dry'], ['S7', 'S11'], [3]),
        K("In chapter two, a voice says, Aaron Falk, don't you bloody dare leave. Old bonds pull him back, so the past is a pressure on the present.",
          ['dry'], ['S3', 'S10'], [1, 2]),
    ]),
    'dry_town': Scene('dry_town', P4, 'Key scene: the town and the fire', DRY_TOWN, [
        K("Key scene: the town. The school principal says, the drought, it's going to kill this town. It sounds like a worry about money, but it hides a darker "
          "meaning. Setting works as a threat.", ['dry'], ['S4', 'S7'], [2, 3]),
        K("In the climax, two years without decent rainfall and now doused in alcohol: they were standing on a matchbox. Drought becomes a physical danger in "
          "the final chase.", ['dry'], ['S4', 'S8'], [3]),
        K("And the reveal comes from a teenage voice from the past, in a diary: if my dad finds out, he will kill me. It shows who the danger really was, "
          "and it is why the ending feels earned.", ['dry'], ['S8', 'S10'], [2, 3]),
    ]),
    'dry_end': Scene('dry_end', P4, 'Key scene: the ending', DRY_END, [
        K("Key scene: the ending. Falk thinks, twenty years was twenty years, but some things shouldn't be swept away. Remembering Ellie is a moral act. "
          "The theme is memory.", ['dry'], ['S3', 'S8'], [1, 3]),
        K("The town's real enemy was its secrets and lies and fear. That is the theme of community, and it links back to the funeral and the first letter.",
          ['dry'], ['S3', 'S10'], [1]),
        K("The tone stays wary. Gretchen says, see you in another twenty years. There is no easy reconciliation, so the genre's neat endings are extended.",
          ['dry'], ['S5', 'S8'], [2, 3]),
    ]),
    'dry_bank': Scene('dry_bank', P4, 'Quote bank: The Dry', DRY_BANK, [
        K("Quote bank for The Dry. Setting: it'll break, the farmers said as the months ticked over into a second year. Hook: Luke lied, you lied, be at the funeral.",
          ['dry'], ['S7', 'S8'], [1, 3], exam=['X1']),
        K("Juxtaposition: three coffins said differently. Threat: they were standing on a matchbox.", ['dry'], ['S4', 'S7'], [2, 3]),
        K("Truth: if my dad finds out, he will kill me. And memory: some things shouldn't be swept away.", ['dry'], ['S3', 'S8'], [1, 3]),
    ]),
    'quote_themes': Scene('quote_themes', P5, 'Quote bank: themes', QUOTE_THEMES, [
        K("Here are the theme quotes side by side. Identity: my name is Thornhill; better to be a fake somebody than a real nobody; Luke lied, you lied.",
          ['nxnw', 'ripley', 'dry'], ['S3', 'S10'], [1], exam=['X2']),
        K("Truth and guilt: I had nothing to do with this; put it in a room in the basement; three coffins said differently.",
          ['nxnw', 'ripley', 'dry'], ['S3', 'S10'], [1]),
        K("Community: a live decoy; the sun shines on you; its secrets and lies and fear.", ['nxnw', 'ripley', 'dry'], ['S3', 'S10'], [1]),
        K("Place: dusting crops where there ain't no crops; stuck in the basement; the river was still gone. Use any of these as evidence, and always say which "
          "code, convention or theme it proves.", ['nxnw', 'ripley', 'dry'], ['S3', 'S10', 'S12'], [1, 3]),
    ]),
}


def _after(anchor, *new):
    i = [s.id for s in SCENES].index(anchor) + 1
    SCENES[i:i] = list(new)


_after('intro', NEW['reqs'], NEW['req_how'])
_after('nx_context', NEW['nx_taxi'])
_after('nx_identity', NEW['nx_un'], NEW['nx_decoy'], NEW['nx_dining'])
_after('nx_field', NEW['nx_auction'])
_after('nx_end', NEW['nx_bank'])
_after('rp_context', NEW['rp_talent'])
_after('rp_identity', NEW['rp_sun'], NEW['rp_boat'])
_after('rp_setting', NEW['rp_basement'], NEW['rp_end'], NEW['rp_bank'])
_after('dry_context', NEW['dry_prologue'], NEW['dry_return'])
_after('dry_quotes', NEW['dry_town'])
_after('dry_twist', NEW['dry_end'], NEW['dry_bank'])
_after('themes', NEW['quote_themes'])

VIDEO = Video(
    id='ENG315117_M1_thriller', course=COURSE, course_name='English', module=MODULE,
    module_name='Module 1: Genre Study (Thriller)', title='ENG315117 English: Module 1, Thriller codes, conventions and themes',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=None, checks=CHECKS, render_scale=1, credits_narration=ENG_CREDITS,
    keywords=['codes and conventions', 'genre', 'thriller', 'subvert', 'metalanguage', 'suspense', 'juxtaposition'],
    thumbnail=VIS.thumbnail,
    description='Revision for TASC English Level 3 Module 1: the thriller genre. Codes, conventions, themes and essay technique, '
                'using North by Northwest, The Talented Mr Ripley and The Dry, with freeze frames and quotations.',
)
