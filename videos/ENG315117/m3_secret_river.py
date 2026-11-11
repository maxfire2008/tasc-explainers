"""ENG315117 English, Module 3 (Close Text Study): The Secret River, the play by Andrew Bovell (adapted from Kate Grenville's novel).
Criterion 3 (elements 1 to 4) is the one the external exam assesses for this module (Section C).
"""
from explainer import layout as L, style
from explainer.spec import Video, Scene, Step, Ref, import_sibling

EC = import_sibling(__file__, 'eng_common.py')
VIS = import_sibling(__file__, 'm3_visuals.py')
Slide = EC.Slide

COURSE, MODULE = 'ENG315117', 'M3'
L.use(style.theme(COURSE, MODULE))

P1 = 'Part 1 · The text and its contexts'
P2 = 'Part 2 · Whose perspective?'
P3 = 'Part 3 · How perspective is built'
P4 = 'Part 4 · Choice, violence and the ending'
P5 = 'Part 5 · Interpretation'
P6 = 'Part 6 · Writing the essay'

REFS = {
    'course': Ref('eng315117-9.html', 'Course document, Module 3 Close Text Study, content descriptions'),
    'standards': Ref('eng315117-9.html', 'Course document, Criterion 3 standards table'),
    'ext': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, Section C: Close Text Study', page=4),
    'ext5': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, Section C, focus of response', page=5),
    'ext2': Ref('ENG315117-English-External-Assessment-Specifications.pdf', 'External assessment specifications, assessment and marking tool', page=2),
    'list': Ref('ENG315117-English-Prescribed-Text-List-2026.pdf', 'Prescribed text list 2026, Module 3 Close Text Study', page=4),
    'river': Ref('The Secret River - Kate Grenville.epub', 'The Secret River (Bovell, adapted from Grenville; Currency Press, 2013), quotations'),
    # other study texts listed so every source in content.csv is referenced
    'nxnw': Ref('North_by_Northwest_1959_1080p_HEVC.mkv', 'Module 1 study text (see the Module 1 video)'),
    'ripley': Ref('The_Talented_Mr_Ripley_1999_1080p_HEVC.mkv', 'Module 1 study text (see the Module 1 video)'),
    'dry': Ref('The Dry - Jane Harper.epub', 'Module 1 study text (see the Module 1 video)'),
    'king': Ref('Different Seasons - Stephen King.epub', 'Module 2 study text (see the Module 2 video)'),
    'shaw': Ref('The Shawshank Redemption _1994_ - 1080p AVC.mkv', 'Module 2 study text (see the Module 2 video)'),
}

SYLLABUS = {
    'P1': ('Undertake close analysis of a substantial prescribed text (ACEEN060)', 'course'),
    'P2': ('Examine how each text relates to a particular context or contexts (ACEEN061)', 'course'),
    'P3': ('Examine the contexts in which the text is created and received (ACEEN062)', 'course'),
    'P4': ('Analyse content, purpose and choice of language in the text studied (ACEEN063)', 'course'),
    'P5': ('Analyse the use of voice and point of view in the text studied (ACEEN064)', 'course'),
    'P6': ('Explore other interpretations and aspects of this single text (ACEEN065)', 'course'),
    'P7': ('How texts convey perspectives through the selection of mode, medium, genre and type of text (ACEEN066)', 'course'),
    'P8': ('How points of view and values are represented (ACEEN067)', 'course'),
    'P9': ('Language features that generate empathy or controversy (ACEEN068)', 'course'),
    'P10': ('Sustain a personal voice and point of view, with nuanced language and complex argument (ACEEN069 to 071)', 'course'),
    'P11': ('Substantiate and justify responses using textual evidence, with simple referencing (ACEEN072, 073)', 'course'),
    'P12': ('Learner-created texts: a seminar exploring two different perspectives and a written interpretation', 'course'),
    'P13': ('One text studied from the prescribed list', 'course'),
}
ELEMENTS = {
    1: ('Contextual evaluation: relationships between texts and contexts', 'standards'),
    2: ('Perspective analysis: different perspectives, attitudes and values represented in texts', 'standards'),
    3: ('Construction of perspective: how texts convey perspectives', 'standards'),
    4: ('Interpretation justification: develops, defends and justifies a reasoned interpretation', 'standards'),
}
EXAM_TOPICS = {
    'X1': ('Section C: one compulsory question about one text from Module 3, with no stimulus quotation', 'ext'),
    'X2': ('How perspectives on key ideas are developed through the single text studied', 'ext5'),
    'X3': ('Analysis and evaluation of language, text, context and stylistic features to build your own reasoned interpretation', 'ext5'),
    'X4': ('Extended analytical essay in the first or third person, about sixty minutes, assessed also for Criteria 4 and 6', 'ext'),
}
CHECKS = []
ENG_CREDITS = ('Course content in this video is adapted from material published by {holder}, used under a Creative Commons Attribution 4.0 '
               'International licence. Short quotations and freeze frames from the study texts are shown for study and criticism, and belong to '
               'their creators. The practice questions are original. The full reference list is in the description, along with a link to any '
               'updated version of this video.')

INTRO = Slide('bullets', title='How this module is assessed', chip='Module 3 · Criterion 3', size=31, items=[
    'Internal: a seminar presentation on TWO perspectives, and a written interpretation supported by close analysis',
    'External: Section C of the exam, about 60 minutes, ONE compulsory question on ONE text',
    'Elements of Criterion 3:  1 Context · 2 Perspective analysis · 3 Construction of perspective · 4 Justified interpretation',
    'Element 4 verbs: C develops · B defends · A justifies a reasoned interpretation',
    'Roadmap: contexts → perspectives → how they are built → choice and ending → interpretation → writing',
], foot=['', '', '', 'The key skill: your own interpretation, backed by close analysis of the text.', ''])

CONTEXT_MADE = Slide('bullets', title='Contexts: when the story is set and when it was made', chip='Element 1 · contextual evaluation', size=31, items=[
    'Setting: the Hawkesbury River, September 1813 to April 1814, Dharug country',
    'Thornhill is an emancipist: a transported convict who has been pardoned',
    'Source: Kate Grenville’s 2005 novel, adapted for the stage by Andrew Bovell',
    'First staged in 2013 (the TASC list gives 2012), in a time of public debate about reconciliation and history',
])

CONTEXT_RECEIVED = Slide('quotes', title='Contexts: how audiences receive the play', chip='Elements 1 and 3', rows=2, size=32, items=[
    ('“Grenville wasn’t writing about them. She was writing about us.”', 'Andrew Bovell, introduction to the published script', 'RECEPTION',
     'Today’s audiences are asked to recognise the past as theirs.'),
    ('“There are no surtitles.”', 'Henry Reynolds, foreword, on the Dharug dialogue', 'AUDIENCE POSITION',
     'The audience experiences not understanding, as the settlers did.'),
])

CHARACTERS = Slide('grid', title='Six perspectives to know', chip='Element 2 · perspective analysis', cols=3, per=2, size=21, ch_max=0.34, items=[
    ('THORNHILL', 'The settler who wants more', 'Poor, pardoned and driven by the chance of land of his own.'),
    ('SAL', 'The wife who looks again', 'Wants a home, and comes to see the Dharug as people with a place.'),
    ('SMASHER AND DAN', 'Hostile settlers', 'Treat the Dharug as thieves and threats. Urge violence.'),
    ('BLACKWOOD', 'The neighbour who shares', 'Understands give and take, and shows another way to live on the river.'),
    ('YALAMUNDI AND NGALAMALUM', 'The Dharug people', 'Claim country, speak their own language and divide on how to respond.'),
    ('DHIRRUMBIN', 'The narrator, the river', 'A witness who knows the ending and frames the whole story.'),
])

THORNHILL = Slide('quotes', title='Thornhill: desire and entitlement', chip='Element 2 · perspective analysis', rows=3, size=32, items=[
    ('“A different life is what I’m after.”', 'Thornhill, prologue', 'MOTIVE',
     'Poverty and the English class system push him to risk everything.'),
    ('“And why not? If it’s there for the taking.”', 'Thornhill, prologue', 'ENTITLEMENT',
     'The settler’s view: land is empty until a man claims it.'),
    ('“This is my place now. You got all the rest.”', 'Thornhill to Yalamundi, Act One', 'CLAIM',
     'Said to a man whose country it already is. Dramatic irony.'),
])

SAL = Slide('quotes', title='Sal: home, empathy and challenge', chip='Element 2 · perspective analysis', rows=3, size=32, items=[
    ('“I don’t care what I’ll be. I’ll be home.”', 'Sal, prologue', 'VALUES',
     'Her aim is belonging, not wealth. It sets her apart from her husband.'),
    ('“’Cause you weren’t looking, Will. You didn’t want to see no sign.”', 'Sal, Act One', 'CHALLENGE',
     'She names his wilful blindness to the Dharug presence.'),
    ('“They was here… Like you and me was in London.”', 'Sal, Act Two', 'EMPATHY',
     'She sees the Dharug camp as a home, as theirs was.'),
])

DHARUG = Slide('quotes', title='The Dharug: country and voice', chip='Element 2 · perspective analysis', rows=3, size=32, items=[
    ('“This is our place. Our country.”', 'Yalamundi, spoken in Dharug, translated in the script', 'COUNTRY',
     'The audience hears the Dharug language, not this English.'),
    ('“He calls it his place.”', 'Ngalamalum, translated in the script', 'IRONY',
     'The Dharug see Thornhill’s claim as a strange idea.'),
    ('“This me… My place.”', 'Ngalamalum, final scene', 'ECHO',
     'Thornhill’s line returns in broken English at the close.'),
])

SETTLERS = Slide('quotes', title='Hostile settlers and a different path', chip='Element 2 · perspective analysis', rows=3, size=32, items=[
    ('“Tell your husband to keep a whip at hand.”', 'Smasher Sullivan to Sal', 'HOSTILITY',
     'Advice delivered as common sense. Violence is normalised.'),
    ('“Get rid of ’em and Sal will stay, Will.”', 'Dan Oldfield to Thornhill', 'PRESSURE',
     'Fear of losing his family is used to push him.'),
    ('“Best get what’s left.”', 'Mrs Herring', 'LOOKING AWAY',
     'Bovell says she keeps the peace by looking away when she needs to.'),
])

NARRATOR = Slide('bullets', title='Voice and point of view: the river narrates', chip='Element 3 · construction of perspective', size=31, items=[
    'Dhirrumbin is the narrator and also the Dharug name for the river',
    'She knows how it ends, so the telling has a prophetic sadness',
    'She tells us what Thornhill hides from himself: a “closed room” of memory',
    'The audience is given both an inside view and a witness view',
])

LANGUAGE = Slide('quotes', title='Language: how perspectives are voiced', chip='Elements 2 and 3', rows=3, size=32, items=[
    ('“You might as well bloody bark.”', 'Thornhill to Yalamundi', 'DEHUMANISING',
     'He turns an unknown language into animal noise.'),
    ('“Even a dog would understand it.”', 'Stage direction, Act One', 'STAGE DIRECTION',
     'The narration itself echoes the settlers’ comparison, and invites judgement.'),
    ('“I’m not Lady bloody Muck.”', 'Sal, on arrival', 'DIALECT AND CLASS',
     'Voice shows who the Thornhills are, and what they are not.'),
])

STAGECRAFT = Slide('grid', title='Mode and medium: what the stage does', chip='Elements 3 and 4', cols=3, per=2, size=21, ch_max=0.34, items=[
    ('LANGUAGE', 'Dharug without surtitles', 'The audience cannot understand, which mirrors the settlers’ position.'),
    ('SONG', 'London Bridge', 'A lullaby sung by Sal becomes a battle cry sung by the armed men.'),
    ('CAST', 'Actors play dogs and kangaroos', 'A shared ensemble makes the world feel collective and physical.'),
    ('SILENCE', 'What is not said', 'Pauses and stage directions carry attitude as much as lines do.'),
    ('IMAGE', 'The fence', 'It is painted on the back wall and comes to look like prison bars.'),
    ('MODE', 'Live, shared, immediate', 'The audience watches the violence together, so response is collective.'),
])

EMPATHY = Slide('quotes', title='Empathy and controversy: juxtaposition', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“Ain’t nothing I can do for you, lad.”', 'Thornhill, holding a dying Dharug boy', 'EMPATHY',
     'A tender moment gives the settler humanity.'),
    ('“He knew he would never share with Sal the picture of this boy.”', 'Dhirrumbin', 'CONCEALMENT',
     'He locks it away. Empathy is felt and then buried.'),
    ('“Thornhill drank and said nothing.”', 'Dhirrumbin, before the decision', 'COMPLICITY',
     'Silence leads to the choice. Controversy rises.'),
])

CHOICE = Slide('quotes', title='The decision: how choice is shown', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“We got to deal with them. Get them before they get us.”', 'Smasher', 'FEAR AS ARGUMENT',
     'Violence is framed as defence.'),
    ('“It’s like a knot in old rope. Hard as a fist.”', 'Dhirrumbin', 'IMAGERY',
     'Cutting, not untying: a choice presented as quick and final.'),
    ('“Tonight then.”', 'Thornhill', 'SHORT SENTENCE',
     'Two words carry the whole turn of the play.'),
])

MASSACRE = Slide('quotes', title='The massacre: restraint and silence', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“Until the birds lifted from the trees at the sound of the first gunshot.”', 'Dhirrumbin', 'SOUND',
     'The violence is heard in the world around, not described in detail.'),
    ('The men sing as they advance, guns raised', 'Stage direction', 'SONG AS WEAPON',
     'The nursery tune from the opening is now a battle cry.'),
    ('“Just a farmer burning the cleared timber from his block, they thought.”', 'Dhirrumbin', 'IRONY',
     'The town reads smoke as normal life. Complicity is silence.'),
])

ENDING = Slide('quotes', title='The ending: two answers to “my place”', chip='Elements 2, 3 and 4', rows=3, size=32, items=[
    ('“Here, Jack, keep yourself warm.”', 'Thornhill, offering his old coat', 'KINDNESS AS CONTROL',
     'Charity from the man who took the land.'),
    ('“This me… My place.”', 'Ngalamalum', 'REFUSAL',
     'Short, broken English: a claim that has not gone away.'),
    ('As Thornhill builds his fence…', 'Final stage direction', 'IMAGE',
     'The close shows ownership as enclosure, and perhaps imprisonment.'),
])

INTERPS = Slide('grid', title='Three readings you can argue', chip='Element 4 · interpretation', cols=3, per=1, size=23, ch_max=0.5, items=[
    ('READING 1', 'The tragedy of a man shaped by poverty', 'Thornhill’s hunger for a different life makes his choice understandable, though not excusable.'),
    ('READING 2', 'An indictment of colonial violence', 'The massacre and “my place” show dispossession as a deliberate wrong that shaped the nation.'),
    ('READING 3', 'A mirror for today', '“She was writing about us”: the play asks how the past still shapes silence and belonging.'),
])

JUSTIFY = Slide('bullets', title='Justifying an interpretation', chip='Element 4 · interpretation', size=32, items=[
    'CLAIM: one clear reading, in your own words',
    'EVIDENCE: close analysis of language, staging and structure',
    'CONTEXT: when it was made, and how audiences receive it',
    'OTHER READINGS: say how they support or challenge yours',
    'JUDGEMENT: why your reading is the most convincing',
])

PLAN = Slide('bullets', title='Section C: the plan', chip='Exam · Section C', size=33, items=[
    'About 60 minutes, ONE compulsory question, ONE text',
    'No stimulus quotation: you need your own key moments and quotes',
    'First or third person: choose and stay consistent',
    'Open with a clear interpretation, then prove it paragraph by paragraph',
    'Criterion 6 counts: accurate, controlled, precise language',
])

MODEL = Slide('model', title='A model paragraph', chip='Exam · Section C',
              question='Discuss how The Secret River develops perspectives on belonging.',
              size=26, parts=[
    ('CLAIM', 'The play presents belonging as a claim that two peoples make in opposite ways.'),
    ('EVIDENCE', 'Thornhill says, “This is my place now”, while Ngalamalum ends the play with “This me… My place.”'),
    ('ANALYSIS', 'The echo, in different voices and levels of power, shows ownership as a settler claim and belonging as a relationship to country.'),
    ('CONTEXT AND JUDGEMENT', 'For a 2013 audience, the final image of the fence asks who is enclosed, which makes belonging an unresolved question.'),
])

TIPS = Slide('tips', title='Exam tips for Section C', chip='Exam · Section C', cols=2, size=26, items=[
    ('Build an interpretation', 'The question has no quotation to react to, so decide your reading before you start.'),
    ('Know key moments', 'Learn four or five moments and the lines that matter in them.'),
    ('Analyse, do not retell', 'Name the technique, show it, then say what it does to perspective.'),
    ('Use two perspectives', 'Show how at least two characters see the same idea differently.'),
    ('Use stagecraft', 'It is a play: comment on staging, song, silence and the narrator.'),
    ('Use the context', 'Link choices to the time of setting and the time of making.'),
    ('Mention other readings', 'Say how they resonate with or challenge your own.'),
    ('Keep your language precise', 'Criterion 6 is a key criterion: control and clarity matter.'),
])

SUMMARY = Slide('grid', title='Module 3 in one screen', chip='Summary', cols=3, per=3, size=24, ch_max=0.3, items=[
    ('CONTEXT', 'Then and now', 'Hawkesbury 1813, and a 2013 audience reading it as “about us”.'),
    ('PERSPECTIVES', 'Whose view?', 'Thornhill, Sal, hostile settlers, Blackwood, the Dharug and Dhirrumbin.'),
    ('CONSTRUCTION', 'How it is built', 'Narrator, language, song, silence, staging, juxtaposition.'),
    ('CHOICE', 'Tonight then', 'Fear, pressure and silence lead to the massacre.'),
    ('ENDING', 'Whose place?', 'A coat, a fence and “my place” leave the question open.'),
    ('INTERPRETATION', 'Claim and proof', 'Justify your own reading, and engage other readings.'),
])

SCENES = [
    Scene('title', P1, 'Welcome', VIS.title_card, [
        Step("Welcome. This video revises Module three of English, the close text study, using The Secret River, the play by Andrew Bovell, adapted "
             "from the novel by Kate Grenville. It is for class tests and other internal assessment, and for Section C of the end of year exam. "
             "By the end you will be able to discuss the perspectives in the play, explain how they are built, and justify your own reading.",
             refs=['course', 'list'], covers=['P13'], exam=['X1']),
    ]),
    Scene('intro', P1, 'How the module is assessed', INTRO, [
        Step("In school, you give a seminar presentation that explores two different perspectives, and you write an interpretation supported by close "
             "textual analysis. In the exam, Section C is about sixty minutes. There is one compulsory question about your text, and no stimulus quotation.",
             refs=['course', 'ext'], covers=['P12', 'P13'], exam=['X1', 'X4']),
        Step("Criterion three has four elements. Element one is contextual evaluation. Element two is analysing perspectives, attitudes and values. "
             "Element three is how perspective is constructed. Element four is justifying your own interpretation.",
             refs=['standards'], elements=[1, 2, 3, 4]),
        Step("Elements one to three use the same verbs: explain, analyse, evaluate. For element four, a C response develops a reasoned interpretation, "
             "a B response defends it, and an A response justifies it, with considered and coherent argument.", refs=['standards'], elements=[1, 2, 3, 4]),
        Step("Today: contexts, perspectives, how they are built, the choice and the ending, interpretation, and then how to write it.",
             refs=['course'], covers=['P1']),
    ]),
    Scene('context_made', P1, 'Context: setting and making', CONTEXT_MADE, [
        Step("The play is set on the Hawkesbury River between September eighteen thirteen and April eighteen fourteen. The Dharug people lived "
             "there, and knew the river by their own name.", refs=['river'], covers=['P2', 'P1'], elements=[1]),
        Step("William Thornhill is an emancipist, a transported convict who has been pardoned. He sees the land as a chance of a different life.",
             refs=['river'], covers=['P2', 'P8'], elements=[1, 2]),
        Step("The play was adapted by Andrew Bovell from Kate Grenville's twenty oh five novel. It was staged in twenty thirteen, though the TASC "
             "list gives twenty twelve. It was made at a time of public debate about reconciliation and history.", refs=['river', 'list'], covers=['P3', 'P2'], elements=[1]),
    ]),
    Scene('context_received', P1, 'Context: reception', CONTEXT_RECEIVED, [
        Step("Context also means how a text is received. Bovell writes, Grenville wasn't writing about them, she was writing about us. The play asks "
             "a modern audience to recognise the past as its own.", refs=['river'], covers=['P3', 'P6'], elements=[1, 4]),
        Step("The foreword says there are no surtitles for the Dharug dialogue. So the audience experiences not understanding, as the settlers did. "
             "A strong essay links a staging choice to the audience's position.", refs=['river'], covers=['P3', 'P7'], elements=[1, 3]),
    ]),
    Scene('characters', P2, 'Six perspectives', CHARACTERS, [
        Step("There are many perspectives in the play. Thornhill is the settler who wants more: poor, pardoned and driven by the chance of land. Sal "
             "wants a home, and she comes to see the Dharug as people with a place.", refs=['river'], covers=['P5', 'P8'], elements=[2]),
        Step("Smasher Sullivan and Dan Oldfield are hostile settlers who treat the Dharug as thieves and threats. Thomas Blackwood is a neighbour who "
             "understands give and take, and shows another way to live on the river.", refs=['river'], covers=['P8'], elements=[2]),
        Step("The Dharug characters, Yalamundi and Ngalamalum, claim country, speak their own language and disagree about how to respond. And the "
             "narrator, Dhirrumbin, is the river itself, a witness who knows the ending.", refs=['river'], covers=['P5', 'P8'], elements=[2, 3]),
    ]),
    Scene('thornhill', P2, 'Thornhill', THORNHILL, [
        Step("Thornhill says, a different life is what I'm after. Poverty and the English class system push him to risk everything. The short, plain "
             "sentence tells us he is not a villain at the start.", refs=['river'], covers=['P4', 'P8'], elements=[2]),
        Step("He says, and why not, if it's there for the taking. That is the settler's view: land is empty until a man claims it.",
             refs=['river'], covers=['P4', 'P8'], elements=[2]),
        Step("Then, to Yalamundi, he says, this is my place now, you got all the rest. This is dramatic irony. He says it to a man whose country "
             "it already is.", refs=['river'], covers=['P4', 'P8', 'P9'], elements=[2, 3]),
    ]),
    Scene('sal', P2, 'Sal', SAL, [
        Step("Sal says, I don't care what I'll be, I'll be home. Her value is belonging, not wealth, which sets her apart from her husband.",
             refs=['river'], covers=['P8', 'P4'], elements=[2]),
        Step("She challenges him: you weren't looking, Will, you didn't want to see no sign. Notice her dialect, which shows class, and her "
             "directness, which shows courage.", refs=['river'], covers=['P4', 'P8'], elements=[2, 3]),
        Step("Later, she says, they was here, like you and me was in London. She sees the Dharug camp as a home, as theirs was. That is empathy, "
             "expressed through a comparison.", refs=['river'], covers=['P9', 'P8'], elements=[2, 3]),
    ]),
    Scene('dharug', P2, 'The Dharug', DHARUG, [
        Step("The Dharug are not seen only through settlers' eyes. Yalamundi speaks in Dharug, and the script translates it as, this is our place, "
             "our country. But the audience hears the language, not the English.", refs=['river'], covers=['P5', 'P7', 'P8'], elements=[2, 3]),
        Step("Ngalamalum translates Thornhill's claim as, he calls it his place. To the Dharug, it is a strange idea.",
             refs=['river'], covers=['P8', 'P4'], elements=[2]),
        Step("In the final scene, Ngalamalum says, this me, my place. Thornhill's line returns, in broken English, and it has not gone away.",
             refs=['river'], covers=['P4', 'P9'], elements=[2, 3]),
    ]),
    Scene('settlers', P2, 'Settler attitudes', SETTLERS, [
        Step("Compare the settlers. Smasher says, tell your husband to keep a whip at hand. It is offered as common sense, and that normalises violence.",
             refs=['river'], covers=['P8', 'P9'], elements=[2]),
        Step("Dan tells Thornhill, get rid of them and Sal will stay. Fear of losing his family is used to push him.",
             refs=['river'], covers=['P8'], elements=[2]),
        Step("And Mrs Herring says, best get what's left. Bovell says she keeps the peace by looking away when she needs to. Different "
             "perspectives, one situation.", refs=['river'], covers=['P8', 'P6'], elements=[2]),
    ]),
    Scene('river_flat', P2, 'One river flat, two claims', VIS.river_flat, [
        Step("Picture the river flat. A river runs through it.", refs=['river'], covers=['P1'], elements=[3], anim=None),
        Step("On one side, Thornhill claims a hundred acres, and says, this is my place.", refs=['river'], covers=['P8'], elements=[2]),
        Step("On the other, a Dharug camp and country, and the Dharug say, this is our place.", refs=['river'], covers=['P8'], elements=[2]),
        Step("The two claims overlap, because the yams Thornhill digs up are food the Dharug depend on. This is where the conflict starts, and "
             "it begins with misunderstanding.", refs=['river'], covers=['P4', 'P8'], elements=[2, 3]),
        Step("At the end, a fence is painted, which comes to look like bars. Bovell says it is not clear which side of the bars Thornhill is standing on.",
             refs=['river'], covers=['P4', 'P6', 'P9'], elements=[3, 4]),
    ]),
    Scene('narrator', P3, 'The river narrates', NARRATOR, [
        Step("Voice is a key idea in the course. The narrator, Dhirrumbin, is also the Dharug name for the Hawkesbury River. In effect she is "
             "the river, present before, during and after the events.", refs=['river'], covers=['P5', 'P7'], elements=[3]),
        Step("She knows how it ends, so her telling has a prophetic sadness. She moves the story forward and stands apart to comment on it.",
             refs=['river'], covers=['P5', 'P7'], elements=[3]),
        Step("She tells us what Thornhill hides from himself. After the dying boy, she says he would lock the picture in a closed room of memory. "
             "That gives an inside view and a witness view at once.", refs=['river'], covers=['P5', 'P9'], elements=[3]),
        Step("So when you write about point of view, name who is speaking, who is silent, and what the audience knows that the characters do not.",
             refs=['river'], covers=['P5', 'P10'], elements=[3]),
    ]),
    Scene('language', P3, 'Language and attitude', LANGUAGE, [
        Step("Language shows attitude. Thornhill tells Yalamundi, you might as well bloody bark. He turns an unknown language into animal noise. "
             "That is dehumanising language, and the audience is invited to judge it.", refs=['river'], covers=['P4', 'P9'], elements=[2, 3]),
        Step("The stage direction says, even a dog would understand it. The writing itself echoes the settlers' comparison, which invites us to "
             "notice it.", refs=['river'], covers=['P4', 'P9'], elements=[2, 3]),
        Step("Sal says she is not Lady bloody Muck. Dialect and class are carried in the voice. Always link a language feature to what it "
             "reveals about values.", refs=['river'], covers=['P4', 'P10'], elements=[2, 3]),
    ]),
    Scene('stagecraft', P3, 'Mode and medium', STAGECRAFT, [
        Step("Because this is a play, mode and medium matter. The Dharug language is spoken without surtitles, so the audience cannot understand, "
             "which mirrors the settlers' position. And the song London Bridge is a lullaby early on, but later a battle cry.",
             refs=['river'], covers=['P7', 'P9'], elements=[3]),
        Step("The cast play dogs and kangaroos, so the world feels collective and physical. Silence and stage directions carry attitude as much "
             "as lines do.", refs=['river'], covers=['P7'], elements=[3]),
        Step("The fence is painted on the back wall and comes to look like prison bars. And because it is live, the audience watches the violence "
             "together. Always name a theatre technique, then explain its effect on perspective.", refs=['river'], covers=['P7', 'P9'], elements=[3, 4]),
    ]),
    Scene('empathy', P3, 'Empathy and controversy', EMPATHY, [
        Step("The play generates empathy and controversy together. At Darkey Creek, Thornhill holds a dying Dharug boy and says, ain't nothing I can "
             "do for you, lad. A tender moment gives the settler humanity.", refs=['river'], covers=['P9', 'P8'], elements=[2, 3]),
        Step("But the narrator adds that he would never share the picture of this boy with Sal. Empathy is felt and then buried. "
             "Juxtaposition makes the audience hold both.", refs=['river'], covers=['P9', 'P5'], elements=[3]),
        Step("Later, in the inn, the narrator says, Thornhill drank and said nothing. Silence leads to the choice, so the controversy rises.",
             refs=['river'], covers=['P9', 'P8'], elements=[2, 3]),
    ]),
    Scene('choice', P4, 'The decision', CHOICE, [
        Step("At the inn, Smasher says, we got to deal with them, get them before they get us. Violence is framed as defence.",
             refs=['river'], covers=['P8', 'P4'], elements=[2, 3]),
        Step("The narrator describes the decision as a knot in old rope, hard as a fist, which you cut and do not untie. It is a quick, final image.",
             refs=['river'], covers=['P4', 'P5'], elements=[3]),
        Step("Thornhill says, tonight then. Two words carry the whole turn of the play.", refs=['river'], covers=['P4', 'P1'], elements=[2, 3]),
    ]),
    Scene('massacre', P4, 'The massacre', MASSACRE, [
        Step("The massacre is shown with restraint. The narrator says it begins when the birds lifted from the trees at the sound of the first "
             "gunshot. The violence is heard in the world around, not described in detail.", refs=['river'], covers=['P4', 'P9'], elements=[3]),
        Step("The men sing as they advance, and the nursery tune from the opening is now a weapon. That is a powerful echo.",
             refs=['river'], covers=['P7', 'P9'], elements=[3]),
        Step("Afterwards, the town sees the smoke and thinks it is a farmer burning the cleared timber from his block. The irony is that complicity "
             "is silence.", refs=['river'], covers=['P9', 'P5'], elements=[2, 3]),
    ]),
    Scene('ending', P4, 'The ending', ENDING, [
        Step("In the final scene, Thornhill offers Ngalamalum his old coat and says, here Jack, keep yourself warm. This is charity from the man who "
             "took the land, and that gives it a sour edge.", refs=['river'], covers=['P4', 'P8'], elements=[2, 3]),
        Step("Ngalamalum refuses: this me, my place. Short, broken English, and a claim that has not gone away.", refs=['river'], covers=['P4', 'P8'], elements=[2, 3]),
        Step("The last stage direction says, as Thornhill builds his fence. Ownership is shown as enclosure, and perhaps imprisonment. "
             "Your essay can argue what that image means.", refs=['river'], covers=['P4', 'P6'], elements=[3, 4]),
    ]),
    Scene('interps', P5, 'Three readings', INTERPS, [
        Step("Element four asks for your own interpretation. Here are three readings you can argue. Reading one: the tragedy of a man shaped by "
             "poverty. His hunger for a different life makes the choice understandable, though not excusable.",
             refs=['river'], covers=['P6', 'P10'], elements=[4]),
        Step("Reading two: an indictment of colonial violence. The massacre and the words, my place, show dispossession as a deliberate wrong.",
             refs=['river'], covers=['P6'], elements=[4]),
        Step("Reading three: a mirror for today. The play asks how the past still shapes silence and belonging. A strong essay may combine "
             "readings, but it should still have one clear line.", refs=['river'], covers=['P6', 'P3'], elements=[1, 4]),
    ]),
    Scene('justify', P5, 'Justifying an interpretation', JUSTIFY, [
        Step("To justify a reading, state a clear claim in your own words. Prove it with close analysis of language, staging and structure. Link it to context. "
             "Say how other readings support or challenge yours, and finish with a judgement about why your reading is the most convincing.",
             refs=['course', 'standards'], covers=['P6', 'P10', 'P11'], elements=[4]),
    ]),
    Scene('plan', P6, 'The Section C plan', PLAN, [
        Step("Section C is about sixty minutes, with one compulsory question on your text. There is no stimulus quotation, so you need your own "
             "key moments and lines. You may write in the first or third person, so choose and stay consistent.",
             refs=['ext', 'ext5'], covers=['P11'], exam=['X1', 'X4']),
        Step("Open with a clear interpretation, then prove it paragraph by paragraph. Criterion six counts too: accurate, controlled and precise language.",
             refs=['ext5'], covers=['P10', 'P11'], elements=[4], exam=['X2', 'X3']),
    ]),
    Scene('model', P6, 'A model paragraph', MODEL, [
        Step("Here is an original practice question. Discuss how The Secret River develops perspectives on belonging. The claim: the play presents "
             "belonging as a claim that two peoples make in opposite ways.", refs=['ext5'], covers=['P10', 'P11'], elements=[2, 4], exam=['X2'],
             problem='Discuss how The Secret River develops perspectives on belonging.'),
        Step("The evidence: Thornhill says, this is my place now, while Ngalamalum ends the play with, this me, my place.", refs=['river'],
             covers=['P11', 'P4'], elements=[2, 3]),
        Step("The analysis: the echo, in different voices and levels of power, shows ownership as a settler claim and belonging as a relationship to country.",
             refs=['river'], covers=['P10', 'P4'], elements=[3, 4], exam=['X3']),
        Step("The context and judgement: for a twenty thirteen audience, the final image of the fence asks who is enclosed, which makes belonging "
             "an unresolved question. That paragraph argues, proves and judges.", refs=['river'], covers=['P3', 'P10'], elements=[1, 4], exam=['X3']),
    ]),
    Scene('exam_tips', P6, 'Exam and test tips', TIPS, [
        Step("Tip: build an interpretation. The question has no quotation to react to, so decide your reading before you start.", refs=['ext'], elements=[4], exam=['X1']),
        Step("Tip: know four or five key moments and the lines that matter in them.", refs=['ext'], covers=['P1'], exam=['X1']),
        Step("Tip: analyse, do not retell. Name the technique, show it, then say what it does to perspective.", refs=['standards'], elements=[3]),
        Step("Tip: use two perspectives. Show how at least two characters see the same idea differently.", refs=['standards'], elements=[2]),
        Step("Tip: it is a play, so use stagecraft: staging, song, silence and the narrator.", refs=['ext5'], covers=['P7'], elements=[3]),
        Step("Tip: use the context, both the time of setting and the time of making.", refs=['standards'], covers=['P3'], elements=[1]),
        Step("Tip: mention other readings, and say how they resonate with or challenge your own.", refs=['course'], covers=['P6'], elements=[4]),
        Step("Tip: keep your language precise. Criterion six is a key criterion, and the marking tool rewards control, clarity and structure. "
             "Use your fifteen minutes of preparation time to plan.", refs=['ext2'], exam=['X4']),
    ]),
    Scene('summary', P6, 'Module 3 in one screen', SUMMARY, [
        Step("Module three in one screen. Context: then and now. Perspectives: Thornhill, Sal, the hostile settlers, Blackwood, the Dharug and "
             "Dhirrumbin. Construction: narrator, language, song, silence, staging and juxtaposition.", refs=['river'], covers=['P1', 'P5'], elements=[1, 2, 3]),
        Step("Choice: fear, pressure and silence lead to the massacre. The ending leaves the question of whose place it is. And interpretation: a "
             "clear claim, proved with close analysis.", refs=['river'], covers=['P6', 'P11'], elements=[3, 4]),
        Step("Good luck with your class tests, your seminar and your interpretation, and with Section C of the exam.", refs=['ext']),
    ]),
]

# =========================================================================== key scenes, quotes and requirements (added)
def K(text, refs, covers=(), elements=(), **kw):
    return Step(text, refs=list(refs), covers=list(covers), elements=list(elements), **kw)


REQS = Slide('grid', title='What you must be able to discuss', chip='Requirements · Module 3', cols=2, per=1, size=26, ch_max=0.36, items=[
    ('CONTEXT', 'Element 1', 'Explain how the play relates to the time it is set, the time it was made, and how audiences receive it.'),
    ('PERSPECTIVES', 'Element 2', 'Analyse different perspectives, attitudes and values: settlers, Sal, the Dharug people, and the narrator.'),
    ('CONSTRUCTION', 'Element 3', 'Show how perspective is built through voice, language, staging, juxtaposition and structure.'),
    ('INTERPRETATION', 'Element 4', 'Develop and justify your own reading, using close analysis and other readings.'),
])

REQ_HOW = Slide('bullets', title='How the scene guides work', chip='Requirements · Module 3', size=32, items=[
    'Each key scene gives quotations from the script, with the speaker',
    'It names the PERSPECTIVE, the CONSTRUCTION and the CONTEXT',
    'It says how the scene supports a reading you could argue',
    'Two quote banks follow, grouped by perspective',
])

SC_PROLOGUE = Slide('quotes', title='Key scene: the prologue', chip='Elements 1 and 3', rows=3, size=28, items=[
    ('“Let us begin with the sound of water as it laps against the riverbank…”', 'Opening stage direction', 'MODE',
     'The play begins with sound, not people, which makes the place the first voice.'),
    ('“This way and back. This way and back.”', 'Dhirrumbin, the river', 'POINT OF VIEW',
     'A watching voice that has seen the boats, and knows what they mean.'),
    ('“Then let them… Let them see me. I’ll tell them my name is William Thornhill.”', 'Thornhill', 'CHARACTER',
     'A man who wants to be seen as someone, at last.'),
])

SC_ARRIVAL = Slide('quotes', title='Key scene: arrival on the river', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“I don’t need no path made. I’m not Lady bloody Muck.”', 'Sal, stepping into mud', 'VOICE AND CLASS',
     'Dialect and humour show who Sal is, and her practical strength.'),
    ('“I don’t care what I’ll be. I’ll be home.”', 'Sal', 'VALUES',
     'Her aim is home, not wealth.'),
    ('“A different life is what I’m after.”', 'Thornhill', 'MOTIVE',
     'Two aims, one family: the difference matters later.'),
])

SC_BLACKWOOD = Slide('quotes', title='Key scene: Blackwood, a different path', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“…plant your backside somewhere and leave it there long enough and it’s yours.”', 'Thornhill, quoting Blackwood', 'SETTLER IDEA',
     'Possession by staying put, which ignores those already there.'),
    ('“They give you a fright, Will?”', 'Blackwood', 'QUESTION AS PERSPECTIVE',
     'He treats the Dharug as people who can frighten, not as thieves.'),
    ('“It was a matter of give a little, take a little, and of knowing your place.”', 'Bovell, on Blackwood, in the introduction', 'CONTEXT',
     'The playwright names the alternative that history did not choose.'),
])

SC_CORN = Slide('quotes', title='Key scene: the corn', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“They’d a taken the lot. Six months’ work.”', 'Thornhill', 'SETTLER PERSPECTIVE',
     'Loss is measured as labour and money.'),
    ('“I heard you the first time, Will.”', 'Sal', 'SUBTEXT',
     'Her short reply carries her disagreement and distance.'),
    ('“By morning Sal had become a woman turned to wood.”', 'Dhirrumbin', 'IMAGERY',
     'The narrator shows what Sal cannot say.'),
])

SC_CAMP = Slide('quotes', title='Key scene: Sal at the deserted camp', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“They are here. Out there. This very minute. They ain’t going nowhere.”', 'Sal', 'EMPATHY',
     'She understands that the Dharug have not left, and cannot.'),
    ('“Even got a broom to keep it clean, Will.”', 'Sal', 'DOMESTIC DETAIL',
     'A broom links two homes, and two women.'),
    ('“We had to go. Wasn’t our choice. Now it’s them that has to.”', 'Thornhill', 'JUSTIFICATION',
     'He sees his own loss as the reason for another’s.'),
])

SC_PARDON = Slide('quotes', title='Key scene: the pardon replayed', chip='Elements 2 and 3', rows=3, size=28, items=[
    ('“THAT’S MY NAME!”', 'Thornhill, in the inn', 'MEMORY AND VOICE',
     'The shout returns him to the cell and to being judged.'),
    ('“You’re to live, you miserable sod. Life, man. It’s yours. Take it.”', 'The turnkey', 'POWER',
     'Mercy comes as an order, from someone above him.'),
    ('“Get them before they get us.”', 'Smasher', 'FEAR',
     'The scene links Thornhill’s own fear of power to his choice to use it.'),
])

BANK_CHARS = Slide('grid', title='Quote bank: Thornhill, Sal and the Dharug', chip='Learn these', cols=2, per=2, size=24, ch_max=0.3, items=[
    ('THORNHILL', '“This is my place now. You got all the rest.”', 'His claim to country that is already someone’s.'),
    ('THORNHILL', '“We had to go. Wasn’t our choice. Now it’s them that has to.”', 'The justification of dispossession.'),
    ('SAL', '“They was here… Like you and me was in London.”', 'Empathy by comparison.'),
    ('SAL', '“I don’t care what I’ll be. I’ll be home.”', 'Belonging over wealth.'),
    ('DHARUG', '“This is our place. Our country.”', 'Yalamundi, in translation.'),
    ('DHARUG', '“This me… My place.”', 'Ngalamalum’s final refusal.'),
])

BANK_OTHERS = Slide('grid', title='Quote bank: settlers and the narrator', chip='Learn these', cols=2, per=2, size=24, ch_max=0.3, items=[
    ('SMASHER', '“Tell your husband to keep a whip at hand.”', 'Violence offered as common sense.'),
    ('DAN', '“Get rid of ’em and Sal will stay, Will.”', 'Fear of loss turned into pressure.'),
    ('MRS HERRING', '“Best get what’s left.”', 'Looking away, to keep the peace.'),
    ('DHIRRUMBIN', '“It’s like a knot in old rope. Hard as a fist.”', 'The decision presented as final.'),
    ('DHIRRUMBIN', '“Thornhill sat at the door, the gun loaded. Ready to kill a man.”', 'The narrator’s verdict on the man.'),
    ('DHIRRUMBIN', '“He knew he would never share with Sal the picture of this boy.”', 'Concealment and guilt.'),
])

NEW = {
    'reqs': Scene('reqs', P1, 'What you must discuss', REQS, [
        K("What do you need to be able to talk about? Four things, one for each element. Element one: context. Explain how the play relates to the time it is set, "
          "the time it was made, and how audiences receive it.", ['standards', 'ext'], ['P2', 'P3'], [1], exam=['X1']),
        K("Element two: perspectives, attitudes and values. Analyse the settlers, Sal, the Dharug people and the narrator.", ['standards'], ['P8'], [2]),
        K("Element three: construction. Show how perspective is built through voice, language, staging, juxtaposition and structure.", ['standards', 'ext5'], ['P5', 'P7'], [3], exam=['X2']),
        K("Element four: interpretation. Develop and justify your own reading, using close analysis and other readings.", ['standards', 'ext5'], ['P6'], [4], exam=['X3']),
    ]),
    'req_how': Scene('req_how', P1, 'How the scene guides work', REQ_HOW, [
        K("From here, there are key scene guides. Each gives quotations from the script, with the speaker, and names the perspective, the construction and "
          "the context. It also says how the scene supports a reading you could argue. Two quote banks follow, grouped by perspective, for you to learn.",
          ['course', 'ext'], ['P11', 'P1'], [1, 2, 3, 4], exam=['X1']),
    ]),
    'sc_prologue': Scene('sc_prologue', P2, 'Key scene: the prologue', SC_PROLOGUE, [
        K("Key scene: the prologue. The stage direction begins, let us begin with the sound of water as it laps against the riverbank. The play opens with sound, not "
          "people, so the place is the first voice.", ['river'], ['P7', 'P1'], [3]),
        K("The narrator, Dhirrumbin, says, this way and back, this way and back, about the boats. It is a watching voice that knows what the boats mean. "
          "That is point of view.", ['river'], ['P5'], [3]),
        K("Then Thornhill says, then let them see me, I'll tell them my name is William Thornhill. A man who wants, at last, to be seen as someone. His "
          "desire to be someone is the engine of the story.", ['river'], ['P4', 'P8'], [2]),
    ]),
    'sc_arrival': Scene('sc_arrival', P2, 'Key scene: arrival', SC_ARRIVAL, [
        K("Key scene: arrival on the river. Sal steps into the mud and says, I don't need no path made, I'm not Lady bloody Muck. Dialect and humour show who "
          "she is, and her practical strength.", ['river'], ['P4', 'P5'], [2, 3]),
        K("She says, I don't care what I'll be, I'll be home. Thornhill says, a different life is what I'm after. Two aims in one family, and the difference "
          "matters later.", ['river'], ['P8'], [2]),
    ]),
    'sc_blackwood': Scene('sc_blackwood', P2, 'Key scene: Blackwood', SC_BLACKWOOD, [
        K("Key scene: Blackwood. Thornhill repeats a settler idea, plant your backside somewhere and leave it there long enough and it's yours. Possession by staying "
          "put, which ignores those already there.", ['river'], ['P8', 'P2'], [1, 2]),
        K("Blackwood asks, they give you a fright, Will? He treats the Dharug as people who can frighten, not as thieves. And Bovell writes that Blackwood "
          "understood give a little, take a little, and knowing your place. That is the alternative that history did not choose.", ['river'], ['P3', 'P8'], [1, 2]),
    ]),
    'sc_corn': Scene('sc_corn', P2, 'Key scene: the corn', SC_CORN, [
        K("Key scene: the corn. After the confrontation, Thornhill says, they'd a taken the lot, six months' work. Loss is measured as labour and money.",
          ['river'], ['P8'], [2]),
        K("Sal replies, I heard you the first time, Will. Her short sentence carries disagreement and distance. And the narrator says, by morning Sal had "
          "become a woman turned to wood. Imagery shows what she cannot say.", ['river'], ['P4', 'P5', 'P9'], [2, 3]),
    ]),
    'sc_camp': Scene('sc_camp', P2, 'Key scene: the deserted camp', SC_CAMP, [
        K("Key scene: the deserted camp. Sal says, they are here, out there, this very minute, they ain't going nowhere. She understands the Dharug have not left, "
          "and cannot. She notices the broom: even got a broom to keep it clean, Will. A domestic detail links two homes.", ['river'], ['P8', 'P9'], [2, 3]),
        K("Thornhill answers, we had to go, wasn't our choice, now it's them that has to. He sees his own loss as the reason for another's. That "
          "is justification, and it is the perspective an essay must analyse, not endorse.", ['river'], ['P8', 'P6'], [2, 4]),
    ]),
    'sc_pardon': Scene('sc_pardon', P4, 'Key scene: the pardon replayed', SC_PARDON, [
        K("Key scene: the inn. Thornhill shouts, that's my name, and hears a turnkey say, you're to live, you miserable sod, life man, it's yours, take it. "
          "Mercy comes as an order, and the memory of being judged is the pressure behind his choice.", ['river'], ['P4', 'P5'], [2, 3]),
        K("Smasher says, get them before they get us. The scene links Thornhill's own fear of power to his choice to use it. Use it to support a reading of "
          "Thornhill as shaped by the system that once condemned him.", ['river'], ['P6', 'P8'], [2, 4], exam=['X3']),
    ]),
    'bank_chars': Scene('bank_chars', P4, 'Quote bank: the main characters', BANK_CHARS, [
        K("Quote bank, part one. Thornhill: this is my place now, you got all the rest; and we had to go, wasn't our choice, now it's them that has to.",
          ['river'], ['P8', 'P11'], [2], exam=['X1']),
        K("Sal: they was here, like you and me was in London; and I don't care what I'll be, I'll be home.", ['river'], ['P8', 'P11'], [2]),
        K("The Dharug: this is our place, our country; and this me, my place. Use pairs like these to show perspectives that clash.", ['river'], ['P8', 'P11'], [2, 3]),
    ]),
    'bank_others': Scene('bank_others', P4, 'Quote bank: settlers and narrator', BANK_OTHERS, [
        K("Quote bank, part two. Smasher: tell your husband to keep a whip at hand. Dan: get rid of them and Sal will stay. Mrs Herring: best get what's left.",
          ['river'], ['P8', 'P11'], [2]),
        K("The narrator: it's like a knot in old rope, hard as a fist; Thornhill sat at the door, the gun loaded, ready to kill a man; and he knew he would never share "
          "with Sal the picture of this boy.", ['river'], ['P5', 'P11'], [2, 3]),
        K("Learn each quote with the speaker, the technique, and the perspective it shows. That is what turns a quotation into analysis.",
          ['river', 'standards'], ['P10', 'P11'], [3, 4], exam=['X3']),
    ]),
}


def _after(anchor, *new):
    i = [s.id for s in SCENES].index(anchor) + 1
    SCENES[i:i] = list(new)


_after('intro', NEW['reqs'], NEW['req_how'])
_after('settlers', NEW['sc_prologue'], NEW['sc_arrival'], NEW['sc_blackwood'], NEW['sc_corn'], NEW['sc_camp'])
_after('empathy', NEW['sc_pardon'])
_after('ending', NEW['bank_chars'], NEW['bank_others'])

VIDEO = Video(
    id='ENG315117_M3_secret_river', course=COURSE, course_name='English', module=MODULE,
    module_name='Module 3: Close Text Study (The Secret River)', title='ENG315117 English: Module 3, The Secret River and perspectives',
    refs=REFS, syllabus=SYLLABUS, elements=ELEMENTS, exam_topics=EXAM_TOPICS, scenes=SCENES,
    info_sheet=None, checks=CHECKS, render_scale=1, credits_narration=ENG_CREDITS,
    keywords=['perspective', 'point of view', 'interpretation', 'context', 'juxtaposition', 'dramatic irony', 'stagecraft'],
    thumbnail=VIS.thumbnail,
    description='Revision for TASC English Level 3 Module 3: close text study. Perspectives, context, language and staging in Andrew Bovell\'s '
                'play The Secret River, with quotations and interpretation skills.',
)
