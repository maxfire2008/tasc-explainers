"""ENG315117 English, Module 2 (Adaptation Study): Rita Hayworth and Shawshank Redemption (Stephen King, novella) and
The Shawshank Redemption (Frank Darabont, film).  Criterion 2 (elements 1 to 4) is the one the external exam assesses (Section B).
"""
from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, import_sibling

EC = import_sibling(__file__, 'eng_common.py')
VIS = import_sibling(__file__, 'm2_visuals.py')
Slide = EC.Slide

COURSE, MODULE = 'ENG315117', 'M2'
L.use(style.theme(COURSE, MODULE))

P1 = 'Part 1 · Adaptation and meaning'
P2 = 'Part 2 · The two texts'
P3 = 'Part 3 · Themes and ideas'
P4 = 'Part 4 · How meaning changes'
P5 = 'Part 5 · Responses and contexts'
P6 = 'Part 6 · Writing the comparison'

REFS = {
    'course': Ref('eng315117-9.html', 'Course document, Module 2 Adaptation Study, content descriptions'),
    'standards': Ref('eng315117-9.html', 'Course document, Criterion 2 standards table'),
    'ext': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, Section B: Adaptation Study', page=3),
    'ext4': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, Section B, assessed criteria and response', page=4),
    'ext2': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, assessment and marking tool', page=2),
    'list': Ref('ENG315117-English-Prescribed-Text-List-2026.pdf', 'Prescribed text list 2026, Module 2 Adaptation Study, pair 4', page=3),
    'king': Ref('Different Seasons - Stephen King.epub', 'Rita Hayworth and Shawshank Redemption (King, 1982), quotations'),
    'shaw': Ref('The Shawshank Redemption _1994_ - 1080p AVC.mkv', 'The Shawshank Redemption (Darabont, 1994), dialogue and freeze frames'),
    # other study texts listed so every source in content.csv is referenced
    'nxnw': Ref('North_by_Northwest_1959_1080p_HEVC.mkv', 'Module 1 study text (see the Module 1 video)'),
    'ripley': Ref('The_Talented_Mr_Ripley_1999_1080p_HEVC.mkv', 'Module 1 study text (see the Module 1 video)'),
    'dry': Ref('The Dry - Jane Harper.epub', 'Module 1 study text (see the Module 1 video)'),
    'river': Ref('The Secret River - Kate Grenville.epub', 'Module 3 study text (see the Module 3 video)'),
}

SYLLABUS = {
    'A1': ('Analyse language, structural and stylistic choices in the adaptation intertexts (ACEEN041)', 'course'),
    'A2': ('Analyse and evaluate how similar themes, ideas or concepts are treated in the two texts (ACEEN043)', 'course'),
    'A3': ('Analyse the techniques, codes and conventions used in different mediums and modes (ACEEN044)', 'course'),
    'A4': ('Consider how conventions of genre can be challenged, manipulated or parodied through the adaptation process (ACEEN045)', 'course'),
    'A5': ('How language patterns can create shades of meaning (ACEEN047)', 'course'),
    'A6': ('How the expectations of the responder are met, not met, extended or subverted when one text is adapted into another (ACEEN048)', 'course'),
    'A7': ('How responses to adapting texts may change over time and in different cultural contexts (ACEEN049)', 'course'),
    'A8': ('Transform and adapt texts for different purposes, contexts and audiences (ACEEN050)', 'course'),
    'A9': ('Analyse how different texts represent similar ideas in different ways (ACEEN057)', 'course'),
    'A10': ('Explain how meaning changes when texts are transformed into a different genre or medium (ACEEN058)', 'course'),
    'A11': ('Compare and evaluate the impact of language conventions used in the adaptation intertexts (ACEEN059)', 'course'),
    'A12': ('One pair of texts from the prescribed list: a novella and its film adaptation', 'course'),
    'A13': ('Imaginative multimodal response: reimagine an aspect or character, or remix and re-contextualise content', 'course'),
}
ELEMENTS = {
    1: ('Theme, ideas and concepts: the main themes, ideas and concepts in texts', 'standards'),
    2: ('Representation of themes, ideas and concepts: how representations are constructed', 'standards'),
    3: ('Comparison of representations: how different texts represent similar ideas, themes and concepts in different ways', 'standards'),
    4: ('Transformation of meaning: how meaning changes when texts are transformed into a different medium or genre', 'standards'),
}
EXAM_TOPICS = {
    'X1': ('Section B: one compulsory question answered with reference to two prescribed texts from Module 2', 'ext'),
    'X2': ('Differences in meaning that may be created when a text is adapted into a different genre, form or medium', 'ext'),
    'X3': ('How language, stylistic devices and text conventions are manipulated or challenged in the adaptation process', 'ext'),
    'X4': ('Extended analytical essay in the third person, about sixty minutes, assessed also for Criteria 4 and 6', 'ext4'),
}
CHECKS = []

INTRO = Slide('bullets', title='How this module is assessed', chip='Module 2 · Criterion 2', size=32, items=[
    'Internal: a comparative response and an imaginative, multimodal response to the pair of texts',
    'External: Section B of the exam, about 60 minutes, ONE compulsory question, TWO texts',
    'Elements of Criterion 2:  1 Themes · 2 Representation · 3 Comparison · 4 Transformation of meaning',
    'C explains  ·  B analyses  ·  A evaluates',
    'Roadmap: adaptation → the two texts → themes → how meaning changes → writing',
], foot=['', '', '', 'Element 4 is the one that is unique to this module: how meaning changes when a text is transformed.', ''])

TOOLKIT = Slide('grid', title='What can change in an adaptation?', chip='Element 4 · transformation of meaning', cols=4, per=2, size=19, ch_max=0.36, items=[
    ('MEDIUM', 'Page to screen', 'Words become images, sound, performance and editing. Each medium has its own codes.'),
    ('VOICE', 'Who tells the story', 'First-person narration may become voiceover, or disappear.'),
    ('CHARACTERS', 'Merged, added or recast', 'Roles can be combined, expanded or cut. Casting adds meaning.'),
    ('STRUCTURE', 'Order and pace', 'Events are compressed or rearranged to suit screen time.'),
    ('SETTING', 'Place and context', 'The time and culture of the making shape what is shown.'),
    ('THEMES', 'New emphasis', 'A theme can be strengthened, softened or replaced.'),
    ('CONVENTIONS', 'Genre habits', 'Conventions can be followed, challenged or manipulated.'),
    ('ENDING', 'Open or closed', 'A different ending changes what the audience takes away.'),
])

HOW = Slide('bullets', title='Comparing an adaptation: four questions', chip='Elements 3 and 4', size=34, items=[
    'WHAT is kept? The same idea, line or image carried across.',
    'WHAT is changed, added or cut?',
    'WHY might the change be made: medium, audience, context?',
    'WHAT is the effect: how does the meaning shift?',
])

CONTEXT = Slide('media', title='Two texts, two mediums', chip='Element 4 · medium and genre',
                img=['sh_wall'], cap=['The prison yard in the film'], credit=['The Shawshank Redemption, 1994'],
                bullets=['Novella: written by Stephen King, published in 1982 in the collection Different Seasons',
                         'Told in first person by Red, a long-term prisoner, as a written account',
                         'Film: written and directed by Frank Darabont, released in 1994',
                         'Same title idea, new title: the film drops “Rita Hayworth”'])

HOPE = Slide('media', title='Theme: hope', chip='Elements 1 and 3 · theme and comparison',
             img=['sh_hope', 'sh_letter'], cap=['Red in the film warns Andy about hope', 'Red reads Andy’s letter after parole'],
             credit=['The Shawshank Redemption, 1994'],
             quote=[('“Hope is a dangerous thing. Hope can drive a man insane.”', 'Red, in the film'),
                    ('“…hope is a good thing, Red, maybe the best of things, and no good thing ever dies.”', 'Andy’s letter, in the novella'),
                    ('“I hope the Pacific is as blue as it has been in my dreams.”', 'Red, in both texts')],
             bullets=['Both texts treat hope as the central idea',
                      'The film dramatises the argument: Red and Andy disagree out loud',
                      'The novella builds it in Red’s reflective voice, ending on hope'])

INSTITUTION = Slide('media', title='Theme: institutionalisation', chip='Elements 1 and 2',
                    img=['sh_brooks'], cap=['Brooks Hatlen, the librarian, in the film'], credit=['The Shawshank Redemption, 1994'],
                    quote=[('“Because you do get institutionalized.”', 'Red, in the novella'),
                           ('“These walls are funny. First you hate ’em…”', 'Red, in the film'),
                           ('“He was crying when he left. Shawshank was his world.”', 'Red on Brooks, in the novella')],
                    bullets=['Both texts show prison shaping a mind: walls become habit',
                             'Brooks is the proof case: freedom becomes frightening',
                             'The novella reports it; the film shows it on screen'])

TABLE = Slide('table', title='What the film changes (1 of 2)', chip='Element 4 · transformation of meaning',
              head=['', 'Novella (1982)', 'Film (1994)'], size=26, label_w=0.17, rows=[
    ('Voice', 'Red writes a first-person account', 'Red’s voiceover guides the viewer, with images'),
    ('Red', 'A man with red hair who says it is because he is Irish', 'Played by Morgan Freeman, so the Irish joke lands differently'),
    ('Wardens', 'Two wardens, Dunahy then Norton', 'One central warden, Norton, as the villain'),
    ('Tommy', 'Transferred to another prison', 'Killed after he can prove Andy’s innocence'),
])

TABLE2 = Slide('table', title='What the film changes (2 of 2)', chip='Element 4 · transformation of meaning',
               head=['', 'Novella (1982)', 'Film (1994)'], size=26, label_w=0.17, rows=[
    ('Brooks', 'Paroled, dies soon after, reported in brief', 'Dramatised: a pivotal scene and a suicide'),
    ('Title', '“Rita Hayworth and Shawshank Redemption”', '“The Shawshank Redemption”'),
    ('Ending', 'Open: a letter and a hope', 'Closed: the two friends reunited on a beach'),
])

NORTON = Slide('media', title='The warden: villain by design', chip='Elements 2 and 4',
               img=['sh_norton', 'sh_sampler'], cap=['Warden Norton, a church pin on his lapel', 'A framed Bible verse in the warden’s office'],
               credit=['The Shawshank Redemption, 1994'],
               quote=[None, ('“Salvation lies within.”', 'Warden Norton')],
               bullets=['Film merges the authority figures into one clear antagonist',
                        'The novella mentions his church pin; the film puts it in the frame',
                        'Irony: a warden who preaches salvation runs a corrupt prison',
                        'Effect: sharper moral clarity, which suits a mainstream film'])

MOZART = Slide('media', title='A scene only film can give', chip='Elements 2 and 4',
               img=['sh_mozart'], cap=['Andy plays opera over the prison speakers'], credit=['The Shawshank Redemption, 1994'],
               quote=[('“…made those walls dissolve away.”', 'Red, in the film')],
               bullets=['Music and image replace Red’s written reflection',
                        'Sound is a film code: the music reaches every prisoner at once',
                        'The film’s voiceover still explains it, so word and sound work together'])

TITLE_POSTER = Slide('media', title='The poster and the title', chip='Elements 2 and 4',
                     img=['sh_poster'], cap=['A poster hides the tunnel'], credit=['The Shawshank Redemption, 1994'],
                     bullets=['Novella: the poster is part of the title and a key to the escape',
                              'Both texts use a run of posters to mark the years; the film shows them',
                              'The new title moves the focus from an object to an idea: redemption',
                              'Meaning shifts from escape trick to moral and spiritual journey'])

ENDING = Slide('media', title='The ending: open or closed?', chip='Elements 3 and 4',
               img=['sh_letter', 'sh_beach_clip', 'sh_ocean'],
               cap=['Red finds Andy’s letter', 'Andy repairs a boat on the beach', 'The film’s last image: the open Pacific'],
               credit=['The Shawshank Redemption, 1994'],
               quote=[('“Get busy living or get busy dying.”', 'Red in the novella; Andy in the film'), ('“I hope the Pacific is as blue as it has been in my dreams.”', 'Red, in both texts'), None],
               bullets=['Same final speech, but the novella stops there',
                        'The film adds a reunion: the audience’s hope is answered',
                        'Expectations are met and extended: a happy ending that was earned'])

RESPONSES = Slide('bullets', title='Contexts and responses', chip='Elements 3 and 4', size=32, items=[
    'Context of making: 1982 short fiction versus 1994 mainstream cinema',
    'Audience: a reader alone with a voice, or a crowd watching images and hearing music',
    'Expectations: the film follows the prison-drama pattern, then rewards it',
    'Over time: responses shift, so a text can be read differently in new cultures',
])

PLAN = Slide('bullets', title='Section B: the plan', chip='Exam · Section B', size=33, items=[
    'About 60 minutes, ONE compulsory question, TWO texts, third person',
    'Organise by idea, not text by text: each paragraph compares both texts',
    'Always say what is kept, what changes, and the effect on meaning',
    'Use short quotations and shots, and name the medium’s techniques',
    'Criterion 6 counts: accurate, controlled language',
])

MODEL = Slide('model', title='A model paragraph', chip='Exam · Section B',
              question='“Adaptation changes what a story means, not just how it is told.” Discuss, with reference to your two texts.',
              size=26, parts=[
    ('CLAIM', 'Darabont’s adaptation shifts the meaning of hope from a quiet idea to a dramatised argument.'),
    ('KEPT', 'Both texts end on Red’s wish that the Pacific is as blue as in his dreams.'),
    ('CHANGED', 'The film makes Red declare that hope is a dangerous thing, then adds a beach reunion the novella withholds.'),
    ('EFFECT', 'So the novella leaves hope open, while the film answers it. The medium lets the viewer see hope rewarded.'),
])

TIPS = Slide('tips', title='Exam tips for Section B', chip='Exam · Section B', cols=2, size=26, items=[
    ('Answer the question', 'Use its key words in your first sentence. Keep returning to meaning.'),
    ('Third person only', 'The marking tool penalises responses not in the required third person.'),
    ('Compare as you go', 'Weave both texts through each paragraph, rather than text by text.'),
    ('Name the medium', 'Use terms such as voiceover, shot, mise-en-scène, narrator, structure.'),
    ('Kept, changed, effect', 'This three-part move keeps analysis on meaning, not plot summary.'),
    ('Quote briefly', 'A short exact quotation or a precise shot description is enough.'),
    ('Evaluate for an A', 'Judge which change matters most, and explain why.'),
    ('Use the context', 'Link choices to the time and audience of each text.'),
])

SUMMARY = Slide('grid', title='Module 2 in one screen', chip='Summary', cols=3, per=3, size=24, ch_max=0.3, items=[
    ('KEPT', 'Common ground', 'Narrator Red, the hope speech, the escape, the friendship.'),
    ('CHANGED', 'Wardens, Tommy, Brooks', 'Merged villains, a killing, a vivid scene of institutionalisation.'),
    ('MEDIUM', 'Page versus screen', 'Voice, image, music, performance, editing.'),
    ('THEMES', 'Hope and institution', 'Treated differently in each text, with new emphasis in the film.'),
    ('ENDING', 'Open versus closed', 'A reunion on a beach answers the hope the novella leaves open.'),
    ('ESSAY', 'Kept, changed, effect', 'Third person, both texts in each paragraph.'),
])

SCENES = [
    Scene('title', P1, 'Welcome', VIS.title_card, [
        Step("Welcome. This video revises Module two of English, the adaptation study, using Stephen King's novella Rita Hayworth and Shawshank "
             "Redemption and Frank Darabont's film, The Shawshank Redemption. It is for class tests and other internal assessment, and for Section B "
             "of the end of year exam. By the end you will be able to compare themes and explain how meaning changes from page to screen.",
             refs=['course', 'list'], covers=['A12'], exam=['X1']),
    ]),
    Scene('intro', P1, 'How the module is assessed', INTRO, [
        Step("In school, you write a comparative response and make an imaginative, multimodal response to the pair of texts. In the exam, Section B is "
             "about sixty minutes. There is one compulsory question, and it asks you to use both texts.", refs=['course', 'ext'], covers=['A12', 'A13'], exam=['X1', 'X4']),
        Step("Criterion two has four elements. Element one is themes, ideas and concepts. Element two is how those are represented. Element three "
             "is comparing representations. Element four is transformation of meaning.", refs=['standards'], elements=[1, 2, 3, 4]),
        Step("The standards climb in three verbs again. A C response explains, a B response analyses, and an A response evaluates.",
             refs=['standards'], elements=[1, 2, 3, 4]),
        Step("Today: what adaptation is, the two texts, their themes, how meaning changes, and how to write the answer.",
             refs=['course'], covers=['A12']),
    ]),
    Scene('toolkit', P1, 'What can change', TOOLKIT, [
        Step("An adaptation is not a copy. The medium changes from page to screen, so words become images, sound, performance and editing. "
             "Each medium has its own codes. The voice may change too: first-person narration can become voiceover, or disappear.",
             refs=['course'], covers=['A3', 'A8', 'A10'], elements=[4], exam=['X2']),
        Step("Characters can be merged, added or recast, and casting adds meaning of its own. Structure is compressed and rearranged to suit "
             "screen time.", refs=['course'], covers=['A1', 'A8'], elements=[4]),
        Step("Setting and context matter: the time and culture of the making shape what is shown. Themes can be strengthened, softened or "
             "replaced.", refs=['course'], covers=['A7', 'A8'], elements=[1, 4]),
        Step("Genre conventions can be followed, challenged or manipulated. And a different ending changes what the audience takes away.",
             refs=['course'], covers=['A4', 'A6'], elements=[4], exam=['X3']),
    ]),
    Scene('how', P1, 'Four questions', HOW, [
        Step("Here is a method for every comparison. What is kept? What is changed, added or cut? Why might the change be made? And what is the "
             "effect: how does the meaning shift? Always finish on effect.", refs=['course'], covers=['A9', 'A10', 'A11'], elements=[3, 4]),
    ]),
    Scene('context', P2, 'Two texts, two mediums', CONTEXT, [
        Step("The novella was published in nineteen eighty two in Stephen King's collection Different Seasons. It is told in first person by Red, "
             "a long-term prisoner, as a written account.", refs=['king', 'list'], covers=['A12', 'A1'], elements=[2]),
        Step("The film was written and directed by Frank Darabont and released in nineteen ninety four. The title idea changes, as the film drops "
             "the words Rita Hayworth. Remember that the TASC list gives the film date as nineteen ninety five, so use the date your teacher gives.",
             refs=['shaw', 'list'], covers=['A12', 'A8'], elements=[4]),
    ]),
    Scene('hope', P3, 'Hope', HOPE, [
        Step("Hope is the central theme of both texts. In the film, Red tells Andy, hope is a dangerous thing, hope can drive a man insane. "
             "The film turns the idea into an argument between two characters.", refs=['shaw'], covers=['A2', 'A9'], elements=[1, 2, 3]),
        Step("In the novella, the idea is built in Red's reflective voice and in Andy's letter: remember that hope is a good thing, Red, maybe "
             "the best of things, and no good thing ever dies.", refs=['king'], covers=['A2', 'A5'], elements=[1, 2, 3]),
        Step("Both texts end on the same wish: I hope the Pacific is as blue as it has been in my dreams. The words are shared, but, as you will "
             "see, the effect is not.", refs=['king', 'shaw'], covers=['A9', 'A11'], elements=[3]),
    ]),
    Scene('institution', P3, 'Institutionalisation', INSTITUTION, [
        Step("Another shared idea is institutionalisation: prison shaping a mind. In the novella, Red says, because you do get institutionalized. "
             "In the film, he says, these walls are funny. First you hate them, then you get used to them.", refs=['king', 'shaw'], covers=['A2', 'A5', 'A9'], elements=[1, 3]),
        Step("Brooks is the proof case. In the novella, a short report says he was crying when he left, because Shawshank was his world. The film "
             "makes it a pivotal scene on screen.", refs=['king', 'shaw'], covers=['A1', 'A10'], elements=[2, 4]),
    ]),
    Scene('table', P4, 'What the film changes', TABLE, [
        Step("Voice. In the novella, Red writes a first-person account. In the film, Red's voiceover guides the viewer, but the images show "
             "what he describes.", refs=['king', 'shaw'], covers=['A1', 'A3', 'A10'], elements=[2, 4], exam=['X2']),
        Step("Red himself. In the novella, he has red hair and says his skill might come from being Irish. The film keeps the joke, but Red is "
             "played by Morgan Freeman, so the line carries a new edge.", refs=['king', 'shaw'], covers=['A5', 'A8'], elements=[3, 4]),
        Step("Wardens. The novella has two, Dunahy and then Norton. The film uses one central warden, Norton, as the villain.",
             refs=['king', 'shaw'], covers=['A4', 'A8'], elements=[2, 4]),
        Step("Tommy. In the novella, he is transferred to another prison. In the film, he is killed after he can prove Andy's innocence.",
             refs=['king', 'shaw'], covers=['A6', 'A10'], elements=[2, 4]),
    ]),
    Scene('table2', P4, 'What the film changes (2)', TABLE2, [
        Step("Brooks. In the novella, he is paroled and dies soon after, reported in brief. In the film, his story is dramatised, with a suicide.",
             refs=['king', 'shaw'], covers=['A1', 'A10'], elements=[2, 4]),
        Step("The title. From Rita Hayworth and Shawshank Redemption to The Shawshank Redemption: a poster and a place become an idea.",
             refs=['king', 'shaw'], covers=['A8', 'A10'], elements=[4]),
        Step("The ending. The novella ends open, with a letter and a hope. The film closes the story with the two friends reunited on a beach.",
             refs=['king', 'shaw'], covers=['A6', 'A10'], elements=[3, 4], exam=['X3']),
    ]),
    Scene('norton', P4, 'The warden', NORTON, [
        Step("Why merge the wardens? The film wants one clear antagonist. Warden Norton wears a church pin on his lapel.",
             refs=['shaw'], covers=['A3', 'A4'], elements=[2]),
        Step("In his office, a framed Bible verse hangs on the wall, and he says, salvation lies within. The novella mentions the pin, but the film "
             "puts it, and the verse, in the frame. The irony is that a warden who preaches salvation runs a corrupt prison.", refs=['shaw'], covers=['A3', 'A4', 'A5'], elements=[2]),
        Step("The effect is sharper moral clarity, which suits a mainstream film, and it changes where the meaning sits. In the novella, the system "
             "is more diffuse. In the film, one man embodies it.", refs=['shaw', 'king'], covers=['A10', 'A8'], elements=[3, 4]),
    ]),
    Scene('mozart', P4, 'A scene only film can give', MOZART, [
        Step("Some scenes use the film's own codes. Andy plays an opera over the prison speakers, and Red says, it made those walls dissolve away.",
             refs=['shaw'], covers=['A3', 'A1'], elements=[2, 4]),
        Step("Music reaches every prisoner at once, and the image shows faces looking up. The voiceover explains it, so word and sound work "
             "together. The novella has no matching scene, so this is meaning created by the medium.", refs=['shaw', 'king'], covers=['A3', 'A10', 'A11'], elements=[2, 4], exam=['X2']),
    ]),
    Scene('poster', P4, 'The poster and the title', TITLE_POSTER, [
        Step("In the novella, the poster is part of the title and a key to the escape. Both texts use a run of posters to mark the years, but the film "
             "shows them, and a poster hides the tunnel in plain sight.", refs=['king', 'shaw'], covers=['A1', 'A3', 'A10'], elements=[2, 4]),
        Step("The new title moves from an object to an idea: redemption. Meaning shifts from an escape trick to a moral and spiritual journey. "
             "A strong paragraph says what a title change does.", refs=['king', 'shaw'], covers=['A8', 'A10'], elements=[4], exam=['X2']),
    ]),
    Scene('ending', P4, 'Open or closed ending', ENDING, [
        Step("The ending is the biggest change. Both texts have the line, get busy living or get busy dying. In the novella, Red thinks it. In the film, "
             "Andy says it first, and Red repeats it, so a thought becomes an exchange between friends.",
             refs=['king', 'shaw'], covers=['A6', 'A9'], elements=[3, 4]),
        Step("The final speech is shared: I hope the Pacific is as blue as it has been in my dreams. The novella stops there. The film adds a "
             "reunion on the beach, so the audience's hope is answered.", refs=['king', 'shaw'], covers=['A6', 'A10', 'A11'], elements=[3, 4], exam=['X3'], anim=2.4),
        Step("Expectations are met and extended, because a happy ending that was earned fits the prison-drama pattern, while the open ending of the "
             "novella leaves hope as a feeling, not a fact. Evaluate which is more powerful and why.", refs=['king', 'shaw'], covers=['A6', 'A4'], elements=[3, 4]),
    ]),
    Scene('responses', P5, 'Contexts and responses', RESPONSES, [
        Step("Context shapes both. The novella was a nineteen eighty two story in a collection. The film was mainstream cinema in nineteen "
             "ninety four, made for a crowd. The audience changes how the story is told.", refs=['king', 'shaw'], covers=['A7', 'A8'], elements=[4]),
        Step("Expectations also differ. The film follows the prison-drama pattern, then rewards it. And responses change over time and in different "
             "cultures, so a text can be read differently by new audiences.", refs=['shaw'], covers=['A6', 'A7'], elements=[4]),
        Step("This is also the starting point for your imaginative, multimodal response. You might reimagine a character, or remix and "
             "re-contextualise content, but always keep the key choice in view: what do you keep, and what do you change?", refs=['course'], covers=['A13', 'A8']),
    ]),
    Scene('plan', P6, 'The Section B plan', PLAN, [
        Step("In Section B you have about sixty minutes and one compulsory question about both texts. Write in the third person. Organise by "
             "idea, not text by text, so each paragraph compares both.", refs=['ext', 'ext4'], covers=['A12'], elements=[3], exam=['X1', 'X4']),
        Step("Always say what is kept, what changes, and the effect on meaning. Use short quotations and name the medium's techniques. Criterion six "
             "counts too: accurate, controlled language.", refs=['ext4'], covers=['A11'], elements=[2, 3, 4], exam=['X3', 'X4']),
    ]),
    Scene('model', P6, 'A model paragraph', MODEL, [
        Step("Here is an original practice question. Adaptation changes what a story means, not just how it is told. Discuss, with reference to "
             "your two texts. Start with the claim: Darabont's adaptation shifts the meaning of hope from a quiet idea to a dramatised argument.",
             refs=['ext4'], covers=['A9', 'A10'], elements=[3, 4], exam=['X1'],
             problem='“Adaptation changes what a story means, not just how it is told.” Discuss, with reference to your two texts.'),
        Step("What is kept: both texts end on Red's wish that the Pacific is as blue as in his dreams.", refs=['king', 'shaw'],
             covers=['A9', 'A11'], elements=[3]),
        Step("What changes: the film makes Red declare that hope is a dangerous thing, and then adds a beach reunion the novella withholds.",
             refs=['king', 'shaw'], covers=['A10', 'A6'], elements=[3, 4]),
        Step("The effect: the novella leaves hope open, while the film answers it. The medium lets the viewer see hope rewarded. That is analysis "
             "of meaning, not retelling.", refs=['king', 'shaw'], covers=['A10', 'A11'], elements=[2, 3, 4]),
    ]),
    Scene('exam_tips', P6, 'Exam and test tips', TIPS, [
        Step("Tip: answer the question. Use its key words in your first sentence, and keep returning to meaning.", refs=['ext'], exam=['X1']),
        Step("Tip: third person only. The marking tool says responses not in the required third person are penalised.", refs=['ext2'], exam=['X4']),
        Step("Tip: compare as you go. Weave both texts through each paragraph, rather than writing about one text and then the other.",
             refs=['ext4'], elements=[3]),
        Step("Tip: name the medium's techniques, with terms such as voiceover, shot, mise-en-scène, narrator and structure.",
             refs=['standards'], covers=['A3'], elements=[2]),
        Step("Tip: kept, changed, effect. This three-part move keeps you on meaning, not plot summary.", refs=['standards'], elements=[4]),
        Step("Tip: quote briefly. A short exact quotation or a precise shot description is enough, and only simple referencing is expected in the exam.",
             refs=['ext2'], elements=[2]),
        Step("Tip: for an A, evaluate. Judge which change matters most, and explain why.", refs=['standards'], elements=[3, 4]),
        Step("Tip: use the context. Link choices to the time and audience of each text, and use your fifteen minutes of preparation time well.",
             refs=['ext2'], covers=['A7'], elements=[4]),
    ]),
    Scene('summary', P6, 'Module 2 in one screen', SUMMARY, [
        Step("Module two in one screen. Know what is kept: the narrator, the hope speech, the escape and the friendship. Know what changes: wardens, "
             "Tommy and Brooks.", refs=['course'], covers=['A9', 'A10'], elements=[3, 4]),
        Step("Know what the medium does: voice, image, music, performance. Compare hope and institutionalisation. And write in kept, changed, effect.",
             refs=['course'], covers=['A3', 'A2'], elements=[1, 2]),
        Step("Good luck with your class tests, your comparative response and your multimodal piece, and with Section B of the exam.", refs=['ext']),
    ]),
]

VIDEO = Video(
    id='ENG315117_M2_adaptation', course=COURSE, course_name='English', module=MODULE,
    module_name='Module 2: Adaptation Study (Shawshank)', title='ENG315117 English: Module 2, Adaptation (Rita Hayworth and Shawshank Redemption)',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=None, checks=CHECKS, render_scale=1,
    keywords=['adaptation', 'medium', 'voiceover', 'transformation of meaning', 'kept', 'changed', 'effect'],
    thumbnail=VIS.thumbnail,
    description='Revision for TASC English Level 3 Module 2: adaptation study. Comparing Stephen King\'s novella and Frank Darabont\'s film '
                'The Shawshank Redemption, with themes, changes of meaning and essay technique.',
)
