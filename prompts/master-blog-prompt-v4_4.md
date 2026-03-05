# MASTER BLOG CREATION PROMPT
## Version 3.3 — Complete Edition
### Integrates: SEO · AEO · GEO · E-E-A-T · Voice · Polish · Mobile-First Readability · AI Detection Defense · Canva Image Creation · Manual Design Specs

---

> **HOW TO USE THIS PROMPT**
> 1. Fill in Section A (Capability Mode) — select one, delete the others
> 2. Fill in Section B (Brief Input) — 3 required fields, up to 4 optional
> 3. Paste the entire prompt to Claude
> 4. Claude handles everything else autonomously across 5 sequential phases
> 5. Review the Editor Flags before publishing — everything else is ready
> 6. After approving the blog, trigger Section E to create all blog images via Canva

---

## SECTION A — CAPABILITY MODE
*Select one mode. Delete the others before running.*

```
MODE: Standard
Claude operates on trained knowledge only.
Flag all real-time data gaps with [VERIFY WITH SEO TOOL].
Proceed with best available estimates where live data is unavailable.
```

```
MODE: Web Search
Claude uses web search during all research phases before drafting.
Search for: current ranking pages, live statistics, trending angles,
PAA questions, and authoritative sources to cite.
Run searches during Phase 1 before any structural decisions are made.
```

```
MODE: Full Tool Access
Claude uses [specify tools: Ahrefs / SEMrush / GSC / other]
for all keyword, SERP, and competition data.
Pull hard data before any structural decision is made.
Flag any tool retrieval failures and proceed with estimates.
```

---

## SECTION B — BRIEF INPUT
*The only fields you fill in. Everything else Claude determines autonomously.*

```
TOPIC:          [insert topic or seed idea — vague or specific, either works]
AUDIENCE:       [one sentence: who is reading this, what do they care about]
GOAL:           [rank on Google / inform / convert / build trust / go viral]

— OPTIONAL —
Competitor URL: [URL to outperform, or leave blank]
Target keyword: [specific keyword to target, or leave blank]
Funnel stage:   [Top / Middle / Bottom, or leave blank]
Format hint:    [listicle / guide / comparison / story-led, or leave blank]
```

**Autonomous completion rule:** If any optional field is blank, research
and decide it yourself before proceeding. Do not ask for clarification —
make the best strategic decision and proceed.

---

## SECTION C — EXECUTION PIPELINE
*Run all five phases sequentially. Output each phase visibly before
proceeding to the next. Do not begin drafting until Phase 2 is complete.*

---

### ─── PHASE 1: PRE-RESEARCH ───────────────────────────────────────────

*Complete all research now. Output a full research summary before
proceeding to Phase 2. This is the intelligence foundation — every
subsequent decision builds on it.*

**If Web Search or Full Tool mode is active:** run all relevant searches
and tool queries now, before producing the Phase 1 output.

Determine and output all of the following:

**1. KEYWORD STRATEGY**
- Primary keyword — highest intent, most relevant to the topic
- 3–5 secondary keywords — semantic variations and related terms
- Full semantic field — the complete expert vocabulary of this topic:
  the terms, concepts, sub-topics, and related ideas that any
  authoritative, comprehensive post on this subject would naturally use
- Keyword density target: 0.5–1.5% for primary keyword

**2. SEARCH INTELLIGENCE**
- Primary search intent: informational / navigational /
  commercial / transactional
- Likely snippet format: paragraph / list / table / definition
  (based on the primary keyword query type)
- Competition assessment: is this topic dominated by high-authority
  domains, or are there open ranking opportunities?
  Flag with [VERIFY WITH SEO TOOL] if live data would change this assessment.

**3. CONTENT STRATEGY**
- Best content format: listicle / pillar guide / comparison /
  story-led / FAQ-led / how-to (based on intent and audience)
- Ideal word count: calibrated to topic complexity and competition —
  not an arbitrary number. Reasoning must be stated.
- YMYL assessment: does this topic touch health, finance, legal,
  safety, or news? Yes / No. (Triggers heightened E-E-A-T standards
  if yes — see Section D.)

**4. AUDIENCE AND VOICE**
- Voice position: authoritative / warm-practical / energetic /
  curious / conversational
  (inferred from the audience description in the brief)
- Reading level target: Grade 7–8 for general consumer /
  Grade 10–12 for professional audience
- Vocabulary register: technical / semi-technical / plain language

**5. QUESTION AND ANGLE MAPPING**
- 6–8 PAA-style questions: the actual questions people ask about
  this topic, sourced from known search patterns, Reddit, Quora,
  and forum behavior
- 3 distinct angles or use cases through which this topic can be
  approached — these become the 3 primary H2 clusters and increase
  GEO query coverage
- Narrative thread: the journey from not-knowing to knowing —
  the progressive revelation arc the reader will travel

**6. GEO PREPARATION**
- 3–5 authoritative external sources likely to be relevant for citation
- 1 named original framework opportunity — a concept or process in
  this topic that can be given a distinct name and developed as
  original intellectual property
- 5–8 quotable insight opportunities — ideas in this topic that
  can be expressed as standalone citable sentences of 15–30 words

---

### ─── PHASE 2: OUTLINE CONSTRUCTION ──────────────────────────────────

*Build and output the complete outline before writing any draft content.
The outline is the blueprint — nothing gets built without it.*

**A. TITLE AND META FIELDS**

Generate 3 H1 options:
- Each must contain the primary keyword naturally
- Each must signal the content format (guide / list / how-to / etc.)
- Each must be 55–60 characters
- Select the strongest one with a one-line rationale
- The selected H1 becomes the post title

Title Tag:
- 55–60 characters
- Primary keyword as close to the front as possible
- Include a power word or number where natural
- Must not duplicate the H1 exactly — slight variation required

Meta Description:
- 150–160 characters
- Primary keyword included naturally
- Written as a value proposition, not a summary
- Include a subtle CTA: "Learn why..." / "Discover how..." / "Find out..."

URL Slug:
- Primary keyword included, as close to the front as possible
- All lowercase, words separated by hyphens
- Short and readable: 3–6 words maximum
- No stop words (a, the, in, of, for, and, etc.) unless
  removing them makes the slug unreadable
- Must clearly describe the page content
- Example: "ergonomic-chair-guide" not
  "the-complete-guide-to-choosing-an-ergonomic-chair-for-your-body"

**B. OPENING BLOCK PLAN**

Note the Hook-Answer-Promise structure for the opening paragraph:
- Hook: one attention-arresting sentence (surprising stat,
  counterintuitive claim, vivid scenario, or challenged assumption)
- Answer: direct answer to the core question in 1–2 sentences
  (40–60 words total, standalone, no prior context required,
  primary keyword in the first sentence — this is the AEO
  snippet-capture paragraph)
- Promise: what the reader gains by reading the full post

**C. FULL H2 / H3 STRUCTURE**

Rules for every header in the outline:
- H2s: written for human readability — engaging, no vague labels
  like "Introduction", "Overview", "Conclusion", "Final Thoughts",
  "Wrapping Up", "The Bottom Line", or "Final Words."
  This applies to ALL H2s including the conclusion section.
- H3s: written as exact search queries or questions — the precise
  phrases a user would type into Google (PAA and long-tail capture)
- No two H2s may overlap in topic or intent
- Every H2 must have at least one H3 beneath it
- At least one H2 per post must address a voice-search angle
  (conversational, question-format, spoken-word friendly)
- The 3 angles identified in Phase 1 must each have their own H2
- Structure must deliver progressive revelation — each H2 builds
  on the last, not sits beside it independently

**D. CONTENT ELEMENT PLANNING**

For each H2 section, decide whether any non-paragraph elements
would serve the reader better than prose alone:
- Comparison of 2+ items with multiple attributes → table
- Sequential process or ranked items → numbered list
- Unordered set of options, tips, or features → bullet list
- Binary or multi-option decisions → table or short list

Note the planned element type in the outline next to the
relevant H2/H3. If a section is best served by paragraphs alone,
leave it as prose. Do not insert tables, lists, or other elements
purely for visual variety. Every non-paragraph element must earn
its place by communicating the information more clearly than
prose would.

**E. CONCLUSION PLAN**

The conclusion must be concise and impactful. It does three things:
- Reinforce the core answer (AEO signal)
- Deliver a specific next step or CTA
- End with a memorable final insight or reframe

The conclusion is not a summary. Do not recap what the post covered.
Do not restate points already made. A conclusion that reads like a
summary is a conclusion that lost the reader. Get in, land the
final insight, and get out.

**Conclusion H2 naming rule:**
The conclusion H2 follows the same rules as every other H2 in the
post. It must be engaging, specific, and relevant to the topic.
Never use generic labels like "Conclusion," "Final Thoughts,"
"To Conclude," "Wrapping Up," "The Bottom Line," or "Final Words."
Write it as a real H2 that signals what the reader gains from
this closing section.

**Content order:** The conclusion appears before the FAQ section
in the published post. The FAQ is always the last content section.

**F. FAQ SECTION**

- 4–6 questions sourced from the PAA questions identified in Phase 1
- Format: question as H3 header, answer as a normal paragraph below
- Each answer must be 40–60 words and fully standalone
- Questions must be real — things people actually ask, not
  invented questions nobody would search
- The FAQ section is always the last section of the post,
  positioned after the conclusion

**G. INTERNAL LINK MAP**

Identify 5–7 internal link opportunities within the post.

**Internal link distribution rule — non-negotiable:**
Links must be spread quasi-evenly throughout the body of the post.
Do not cluster links in the conclusion or in any single section.
If the post has 5 H2 sections, the links should touch at least
3–4 of those sections. No more than 2 internal links in any
single H2 section. The conclusion may contain at most 1 internal
link (as part of a CTA), but this is optional, not default.

**Internal linking rules — all four are non-negotiable:**

1. ONE DESTINATION PER POST — each linked page may appear only once
   across the entire post. If a page has already been linked,
   do not link to it again under any circumstances.

2. ONE ANCHOR TEXT PER POST — each anchor text phrase may be used
   only once. No anchor text may be reused for a different link
   or repeated for the same link.

3. CONTEXTUAL ANCHOR TEXT — the anchor text must describe the
   specific content of the destination page, not just the topic.
   Wrong: "ergonomic chairs" linking to a guide on choosing ergonomic chairs
   Right: "how to choose the right ergonomic chair for your body type"
   The anchor text should tell the reader exactly what they will find
   if they click — not just the broad subject area it belongs to.

4. NATURAL IN SENTENCE — the anchor text must read naturally within
   its sentence. Do not restructure a sentence awkwardly to force
   a keyword into the link.

Format known URLs as: [anchor text](https://yoursite.com/page-slug)
Format unknown URLs as: [anchor text](INTERNAL LINK → topic/page description)
so the editor can replace the placeholder with the real URL before publishing.

Before finalising the internal link map, run this self-check:
- List all anchor texts — are any identical or near-identical? Fix.
- List all destination pages — does any page appear more than once? Fix.
- Read each anchor text in isolation — does it clearly and specifically
  describe the destination content? If not, rewrite it.
- Check distribution — are links spread across multiple H2 sections? Fix if clustered.

---

### ─── PHASE 3: DRAFT WRITING ──────────────────────────────────────────

*Write the full draft. All rules below are active simultaneously from
the first word. These are not a post-draft checklist — they are
writing instructions embedded into every paragraph as it is created.*

---

#### ■ SEO RULES

**Keyword placement (non-negotiable):**
- Primary keyword must appear in the first sentence of the post.
  If it cannot appear naturally in the first sentence, it must
  appear within the first paragraph at the latest.
- Primary keyword in: H1, first sentence/paragraph, at least one H2,
  title tag, meta description
- Secondary keywords distributed naturally across H2s, H3s, and body
  — never clustered in one section
- Semantic field vocabulary woven organically throughout the full post
  — not front-loaded into the intro
- Keyword density: 0.5–1.5% for primary keyword
- Golden rule: if the primary keyword cannot be placed naturally,
  skip it. Natural language always overrides keyword placement.

**Readability — mobile-first:**
- Default: maximum 2 sentences per paragraph
- Exception: a paragraph may contain 3 sentences only when the
  subject is technically complex AND all three sentences are
  under 12 words each. If any of the three exceeds 12 words,
  the paragraph must be split. This exception should be rare.
- Maximum sentence length: 20 words. Hard ceiling. If a sentence
  exceeds 20 words, split it or rewrite it. No exceptions.
  A 21-word sentence is a sentence that needs editing.
- Sentence rhythm: after every 2–3 sentences of 15–20 words,
  write one short sentence of 5–10 words. Let it land.
- Transition sentence between every major H2 section
- Reading level matched to the target audience (from Phase 1)
- Active voice default — passive voice under 10% of sentences
- Calibrate depth and length to topic complexity, not word count targets

**Content element usage:**
Use non-paragraph elements where the content structure calls for them:
- Comparison of items with multiple attributes → use a table
- Sequential steps or ranked items → use a numbered list
- Unordered set of options, features, or tips → use a bullet list
- Binary or multi-option decision → use a table or short list

These elements improve scannability, engagement, and snippet capture.
But they must serve the content. If a section communicates best as
prose, keep it as prose. Never insert a table or list just for
visual variety.

---

#### ■ AEO RULES

**Opening paragraph — Hook-Answer-Promise:**
- Structure exactly as planned in Phase 2
- Total: 40–70 words
- The Answer portion (40–60 words) must be standalone —
  extractable by Google with no surrounding context
- Primary keyword must appear in the first sentence
- No throat-clearing opener under any circumstances

**Snippet format matching:**
Match the most critical section's format to the snippet type
identified in Phase 1:
- Paragraph snippet → 40–60 word direct answer paragraph
  immediately after the relevant header
- List snippet → clean numbered or bulleted list, each item
  a complete standalone point
- Table snippet → properly formatted comparison or data table
- Definition snippet → bolded term + 1–2 sentence definition

**QAC Formula — apply to every H3:**
- Q → the question as the H3 header (exact search query format)
- A → direct 40–60 word answer immediately below the header
  (fully standalone, snippet-ready)
- C → elaboration, evidence, and supporting detail in
  subsequent paragraphs

**40–60 Word Rule:**
Every H2 and every H3 opens with a direct, self-contained
40–60 word paragraph before any elaboration. This creates
snippet-capture opportunities throughout the entire post,
not just at the top.

**Voice search:**
At least one H3 per major H2 section must be written in
conversational, spoken-word format — phrased as someone
would ask it aloud, answered in a tone that reads naturally
when spoken.

**Schema-mirroring:**
- FAQ section: question as H3 header, answer as normal paragraph below
- How-to sections: numbered steps beginning with action verbs
- Definition sections: bolded term followed by concise definition

**Freshness:**
- Reference currency where relevant: "as of 2025...",
  "current research shows...", "the latest data indicates..."

---

#### ■ GEO RULES

**Factual density:**
Every major claim must be accompanied by a specific statistic,
data point, study reference, or concrete example.
Prohibited without immediate supporting specifics:
"many studies show", "research suggests", "some experts believe",
"it is generally accepted."
If a claim cannot be supported with a real source and URL,
reframe it or remove it.

**Quotable insights — craft 5–8 throughout the post:**
Each must:
- Be 15–30 words, a complete idea with no dangling references
- Convey a specific insight, not a generality
- Be memorable enough that a human would want to repeat it
- Be fully standalone — citable without surrounding context
Mark each with [QUOTABLE] during drafting

**Original framework:**
Introduce the named framework identified in Phase 1.
Give it a distinct name. Define it with 3–5 components.
Frame it as original intellectual property of this post.
Example framing: "The [Name] Framework identifies three stages..."

**External citation:**
For each major factual claim, cite the most authoritative
available source.
Format: "According to [Source Name](URL), [specific finding]."
Always include a real URL — search for the source if needed.
If a source cannot be verified, do not cite it at all.
Do not invent or hallucinate URLs or citations.
Acceptable sources: peer-reviewed research, institutional data,
government statistics, industry reports, established expert consensus.

**Structured data language:**
- Definition-first paragraphs: define before elaborating
- Explicit categorization: "There are three types of X: [1], [2], [3]"
- Comparative structures: "X differs from Y in three key ways..."
- Numbered hierarchies for all processes and ordered sequences
Write as if the content will be parsed by a machine as well as
read by a human — because it will be.

**Multi-angle coverage:**
The post must address the topic from all 3 angles identified
in Phase 1, each with its own clearly delineated H2.
This increases the number of query types the post can be
retrieved for across AI systems.

**Brand and author attribution:**
Frame original analysis, frameworks, and data interpretations
with explicit attribution language suitable for AI extraction.
Examples: "Our analysis of X shows..." /
"The [Framework Name], developed here, suggests..." /
"[Brand]'s approach to X identifies..."

---

#### ■ E-E-A-T RULES

**YMYL protocol** (activate if YMYL = Yes from Phase 1):
- Every factual claim requires a verifiable source
- All recommendations framed as general information,
  not personal advice
- Include appropriate disclaimer:
  "This content is for informational purposes only.
  Consult a qualified [professional] before..."

**Experience signals — minimum 3 per post:**
Write from an experiential perspective throughout.
Include at least 3 observations, caveats, or insights that
imply direct engagement with the subject — not just knowledge of it.
Language that signals experience:
"what you'll actually notice", "what most guides skip",
"in practice", "in real use", "the thing nobody tells you",
"what changes after you try this"

**Expertise signals — minimum 1 per H2 section:**
Include at least one nuance, caveat, common misconception, or
expert-level observation per major section.
The reader should feel they are learning from someone who
genuinely knows this subject deeply — not from someone who
read the same top 10 articles they have.

**Authority tone:**
Take clear positions. Defend them with evidence.
Avoid excessive hedging language: "it might be", "some could argue",
"it's possible that", "in some cases."
One hedge on a genuinely uncertain claim is appropriate.
More than one hedge on the same claim signals low authority.
Write with the confidence of a subject matter leader.

**Trustworthiness:**
Where legitimate counterarguments or limitations exist,
acknowledge them. A post that presents only one side of a
nuanced topic reads as promotional, not authoritative.
Acknowledge complexity, then guide the reader to the
most evidence-supported conclusion.
No internal contradictions. Every claim consistent throughout.

**Helpful Content self-check** (apply before concluding the draft):
Ask internally:
- Does this post offer original information or insight?
- Is it complete — does the reader need to go elsewhere?
- Would a reader feel genuinely informed after reading?
- Is every paragraph earning its place?
Remove or rewrite any section that fails this test.

---

#### ■ DRAFTING AND VOICE RULES

**Voice — apply the position determined in Phase 1:**
- Authoritative: clear, direct, evidence-forward, no filler
- Warm-practical: knowledgeable friend, not a textbook
- Energetic: short sentences, high momentum, no academic hedging
- Curious: invite the reader into the investigation
- Conversational: writer and reader as equals exploring together
Voice must feel consistent from the first sentence to the last —
as if the same person wrote every paragraph.

**Anti-AI writing rules — enforce throughout:**

AI detection tools (ZeroGPT, GPTZero, Originality, Turnitin) measure
two core metrics: perplexity (how predictable word choices are) and
burstiness (how varied sentence structure and length are). AI text
scores low on both. The rules below are designed to produce writing
that scores high on both, while also avoiding the stylometric
patterns that Google's Helpful Content system flags as low-quality
automated output.

**PERPLEXITY: make word choices less predictable**

1. Choose the precise word, not the probable word.
   Where a generic AI would write "improve," write "sharpen,"
   "accelerate," or "overhaul" if that's more accurate.
   Where it would write "significant," write "measurable,"
   "outsized," or "hard to ignore." The goal is not to be
   fancy. The goal is to be specific, because specific is
   unpredictable.

2. Use contractions naturally.
   "You'll" not "You will." "It's" not "It is." "Don't" not
   "Do not." Formal non-contracted prose is a strong AI signal.
   Exception: skip contractions where emphasis or formality
   genuinely requires the full form.

3. Include colloquialisms and natural phrasing.
   "The math doesn't add up." "This is where things get messy."
   "That's the whole point." These are phrases a real writer
   uses. AI defaults to formal, sanitized alternatives.

4. Avoid the AI vocabulary blacklist — never use these words:
   delve, crucial, pivotal, landscape (figurative), tapestry,
   intricate/intricacies, meticulous/meticulously, underscore
   (figurative), testament, vibrant, bolstered, fostering,
   showcasing, highlighting, enhance (when "improve" works),
   leverage (when "use" works), streamline, utilize (when "use"
   works), comprehensive (when "complete" or "thorough" works),
   robust, seamless, elevate (figurative), navigate (figurative),
   realm, multifaceted, cornerstone, empower, synergy,
   game-changer, harness.
   These words are statistically overrepresented in AI output.
   Every one of them has a more natural alternative. Use it.

5. Zero filler transitions — never use:
   Furthermore / Moreover / Additionally / In conclusion /
   It's worth noting / It's important to remember /
   In today's world / It goes without saying / That being said /
   It should be noted / Moving forward / At the end of the day /
   plays a significant role in shaping.
   Connect ideas with logic, not filler words.

**BURSTINESS: vary structure aggressively**

6. Sentence length must swing, not settle.
   If three consecutive sentences are between 12 and 20 words,
   the fourth must be under 8. Or over 15 with a different
   structure. AI writes sentences that cluster around 15–20
   words with uniform structure. Humans don't.

7. Mix sentence types within every section.
   Declarative. Interrogative. Imperative. Fragment.
   Not every section needs all four, but no section should
   be 100% declarative statements. A well-placed question
   or a two-word fragment breaks the AI pattern.

8. Vary paragraph length asymmetrically.
   One paragraph: single sentence. Next: two sentences.
   Then maybe another single sentence for emphasis.
   AI produces evenly-sized paragraphs. Humans don't.
   Let importance and impact dictate paragraph length,
   not uniformity.

9. Vary depth by section importance.
   Not every H2 section deserves equal depth. AI gives every
   section the same weight and word count. Human writers
   spend 300 words on the most important point and 80 on the
   supporting one. Let the content's importance dictate length.

**STYLOMETRIC SIGNALS: write like a human, not a model**

10. Start some sentences with "And," "But," "So," or "Or."
    This breaks the formal pattern AI defaults to.
    Use sparingly (2–4 per post), not in every paragraph.

11. Use parenthetical asides naturally.
    (This is how humans think on the page.)
    AI almost never uses parentheses in body copy.
    One or two per post is enough.

12. Include rhetorical questions at key moments.
    Not as a crutch, but as a genuine invitation to think.
    One rhetorical question every 400–600 words feels natural.
    More than that becomes a pattern of its own.

13. No throat-clearing openers — ever.
    Start with the most interesting, specific, or useful thing
    you have to say. The first sentence must make the reader
    want to read the second.

14. Direct claims — one hedge maximum per uncertain statement.
    Stack of qualifiers = loss of authority.

15. Advancing conclusion — the conclusion must deliver a final
    insight, reframe, or next step. It must not summarize.

16. No em dashes (—) anywhere in the post — ever.
    Em dashes are a strong AI writing signal and must not appear
    in body copy, headers, meta fields, or any output field.
    Replace with: a comma, a colon, a period, parentheses,
    or a restructured sentence. Do a dedicated scan before
    passing Phase 4. Zero em dashes is the only acceptable count.

17. Concrete before abstract — lead with the example, scenario,
    or data point. Draw the principle from it afterward.
    Discovery is more engaging than lecture.

18. Take positions — neutrality without resolution is abdication.
    Where evidence points in a clear direction, state it clearly.

**Sentence-level craft:**
- 2–3 single-sentence paragraphs per post for maximum
  emphasis. Never more — they lose impact through overuse.
- Replace every vague quantity, timeframe, or reference with
  the most specific version available.
- Show before telling — illustrate the claim with a scenario,
  data point, or example before stating the abstract principle.

**Narrative thread:**
- Structure sections as progressive revelation — each H2 builds
  on the last, adding a new layer of understanding
- Open each major H2 with a tension or question; resolve it
  before moving to the next H2
- Plant at least one callback: an idea introduced early that
  resurfaces with greater meaning in a later section

**Engagement mechanics:**
- 2–3 bucket brigade phrases between sections to pull the reader
  forward: "Here's where it gets interesting." /
  "But there's a catch." / "The next part changes everything."
  Used sparingly — 2–3 maximum, or they lose effect.
- At least one open loop: introduce a concept early, defer
  its full resolution to a later section deliberately
- Deliberate 'you' address at key insight or emotional moments
  — not constantly (becomes patronizing), but pointedly
- Subtext acknowledgment: when the reader is likely to have
  an objection, address it before they can raise it mentally

**Image and media placeholders:**
Place image markers at natural breakpoints in the post where a
visual would enhance understanding or break up long text runs.

There are three marker types:

[IMAGE-FEATURED: description of visual concept | text overlay]
[IMAGE-CONTENT: description of visual concept | type: illustrative]
[IMAGE-DATA: description of infographic/diagram content | type: infographic / diagram]

Rules:
- Exactly 1 [IMAGE-FEATURED] marker at the top of the post (before H1 content).
  This is the blog's hero/thumbnail image. Text overlay must be a
  shortened version of the blog title containing the primary keyword.
  Maximum 6–8 words. Never a full sentence, tagline, or subtitle.
- [IMAGE-CONTENT] markers for conceptual, illustrative images.
  Claude will generate these via Canva.
- [IMAGE-DATA] markers for infographics, diagrams, charts, or any
  visual that presents statistical data, processes, or comparisons.
  Claude will NOT generate these via Canva. Instead, Claude provides
  detailed design specs so the user can build them manually in Canva.
- When a section needs an infographic or diagram, place TWO markers:
  first an [IMAGE-CONTENT] (conceptual image, generated by Claude),
  then an [IMAGE-DATA] (infographic/diagram, built manually by user)
  directly below it. The conceptual image comes first in the content.
- Not every H2 needs an image. Place them where a visual adds value,
  not for decoration.
- Alt text descriptions must be specific (e.g., "flowchart showing the
  three stages of the Content Velocity Framework" not "diagram of framework").
- Text overlay suggestions should be minimal: a short phrase or key stat,
  never a full sentence. If no text overlay is needed, omit it.

**Niche adaptation:**
Keep structural craft and writing quality constant across
all niches. Adapt only:
- Vocabulary register (technical / semi-technical / plain)
- Example types (match to the niche's natural scenario space)
- Emotional tone (urgency / calm / enthusiasm / precision)

---

### ─── PHASE 4: SELF-AUDIT ─────────────────────────────────────────────

*Run all eight passes before declaring the draft complete.
Each pass has a single focus. Do not combine passes.*

---

**PASS 1 — STRUCTURAL INTEGRITY**
Read headers only (H1, H2s, H3s, FAQ). Ask:
- Does the header sequence tell a coherent, logical story alone?
- Is any H2 removable without weakening the post?
- Is any H2 missing that the reader would expect?
- Do any two H2s overlap in topic or intent?
- Are all H3s genuine sub-topics of their parent H2?
Output: "Structure holds" or list specific issues to resolve.

**PASS 2 — PROMISE-DELIVERY ALIGNMENT**
Reread the opening paragraph and H1. Then read the full post.
- Did the post deliver exactly what the opening promised?
- Does the conclusion resolve the opening promise?
- Are there any promise-delivery gaps?
Flag gaps: [DELIVERY GAP] — resolve in the body or
revise the opening to match what was actually delivered.

**PASS 3 — EVIDENCE VERIFICATION**
Read only factual claims — skip transitions and context.
- Is every claim supported by a citation, data point, or example?
- Does every citation include a real, working URL?
- Are there unsupported claims dressed as facts?
Flag unsupported claims: [NEEDS EVIDENCE]

**PASS 4 — VOICE CONSISTENCY**
Read specifically listening for voice — not content.
- Is tone consistent from first paragraph to last?
- Are there sections that sound noticeably more generic or formal?
- Are there any paragraphs that sound like default AI prose?
- Are prohibited filler transitions present anywhere?
- Are there any em dashes (—) anywhere in the draft?
  If yes, rewrite every instance. Zero is the only acceptable count.
Flag voice breaks: rewrite before proceeding.

**PASS 5 — AI DETECTION SWEEP**
Read the entire draft specifically scanning for AI writing patterns.
This pass targets the two metrics AI detectors measure:
perplexity (word predictability) and burstiness (structural variation).

Perplexity check:
- Scan for any word from the AI vocabulary blacklist (rule 4 in
  anti-AI writing rules). Replace every instance. Zero tolerance.
- Identify sentences where every word is the most statistically
  probable choice. Rewrite with more precise, less predictable
  alternatives that still fit the context.
- Check for contractions. If fewer than 60% of eligible
  contractions are contracted, add more.
- Check for filler transitions from the banned list. Remove all.

Burstiness check:
- Read sentence lengths across every H2 section. If any section
  has 4+ consecutive sentences within the same 5-word length range
  (e.g., all between 15–20 words), rewrite to vary them.
- Check that every H2 section contains at least one sentence
  under 8 words and at least one over 15 words.
- Verify paragraph lengths vary within each H2 section. Three
  consecutive same-length paragraphs = rewrite.
- Confirm section depths are asymmetric. If all H2 sections are
  within 50 words of each other in length, redistribute. Important
  sections should be noticeably longer than supporting sections.

Stylometric check:
- Are there at least 2–4 sentences starting with "And," "But,"
  "So," or "Or" across the full post?
- Is there at least 1 parenthetical aside in the post?
- Are there rhetorical questions at natural points (roughly
  1 per 400–600 words)?
- Does the post use any three-part list pattern more than twice?
  ("X, Y, and Z" repeated = AI pattern.) Vary the structure.
- Read the first sentence of every paragraph. Do they follow
  the same grammatical structure? If yes, vary them.

If any check fails, rewrite before proceeding. Do not flag
for later. Fix it now.

**PASS 6 — DENSITY AND PADDING**
Read looking only for waste.
Test every sentence: does this add information, evidence,
nuance, or momentum not present elsewhere?
If no — it is padding.
Flag padding: [PADDING] — cut or transform.
Target: the post should emerge leaner and more powerful.
Not shorter for the sake of it — tighter for the sake of quality.

**PASS 7 — READER EXPERIENCE AND MOBILE READABILITY**
Read as the target audience member on a mobile phone
encountering this for the first time.
- Is there any moment of confusion or lost thread?
- Is there assumed knowledge the reader may not have?
- Is there undefined jargon?
- Does any paragraph exceed 2 sentences? If so, does it
  qualify for the 3-sentence technical exception (all under
  12 words)? If not, split it.
- Does any sentence exceed 20 words? If so, split or rewrite.
- Is there any section where reading feels like work?
- Is there any moment you'd want to close the tab?
- Would a reader finish this feeling genuinely informed and served?
- Are content elements (tables, lists) used where they would
  communicate more clearly than prose?
Flag friction: [READER FRICTION] — resolve before proceeding.

**PASS 8 — PUBLISHING READINESS**
Confirm every item:
- [ ] H1 selected and within 55–60 characters
- [ ] Title tag finalized, under 60 characters, keyword-forward
- [ ] Meta description finalized, under 160 characters,
      written as value proposition
- [ ] URL slug finalized, 3–6 words, keyword-forward, no stop words
- [ ] Primary keyword appears in the first sentence of the post
- [ ] FAQ schema JSON-LD generated and matches FAQ section
- [ ] No paragraph exceeds 2 sentences (or 3 sentences under
      12 words each for technical exception)
- [ ] No sentence exceeds 20 words
- [ ] Internal link audit complete:
      — 5–7 internal links present
      — Links distributed quasi-evenly across H2 sections
      — No more than 2 links in any single H2 section
      — No more than 1 link in the conclusion
      — No destination page linked more than once
      — No anchor text used more than once
      — Every anchor text describes the destination specifically,
        not just the broad topic
      — All links read naturally within their sentences
- [ ] All external citations include a real working URL
- [ ] All [QUOTABLE] sentences marked
- [ ] FAQ formatted as H3 questions with normal paragraph answers
- [ ] Author bio block complete (see Phase 5)
- [ ] Word count appropriate to complexity from Phase 1
- [ ] Conclusion is concise, has engaging H2 (not generic label),
      contains a CTA, does not summarize
- [ ] Conclusion appears before FAQ in content order
- [ ] At least one named original framework present
- [ ] 5–8 [QUOTABLE] sentences present
- [ ] Opening paragraph follows Hook-Answer-Promise structure
- [ ] Exactly 1 [IMAGE-FEATURED] marker at top of post
- [ ] Conceptual [IMAGE-CONTENT] markers where appropriate
- [ ] [IMAGE-DATA] markers paired with [IMAGE-CONTENT] markers above them
- [ ] All image markers include specific visual descriptions
- [ ] Image Brief Part A and Part B ([13]) are complete
- [ ] Part B design specs include layout, colours, data, hierarchy
- [ ] Content order: body sections → conclusion → FAQ (last)
- [ ] Content elements (tables/lists) used where appropriate
- [ ] Zero em dashes in the entire post
- [ ] Zero words from the AI vocabulary blacklist
- [ ] Contractions used naturally (60%+ of eligible instances)
- [ ] Sentence lengths vary within every H2 section
- [ ] Section depths are asymmetric (not all H2s same length)
- [ ] At least 2 sentences start with "And," "But," "So," or "Or"
- [ ] At least 1 parenthetical aside present
- [ ] Zero filler transitions from banned list

Output: [READY TO PUBLISH] only when all items confirmed.
If any item is unresolved, list it and resolve before proceeding.

---

**COMPRESSION — apply after all eight passes:**
Remove throughout:
- Opening qualifiers: "It's important to understand that..." →
  cut the qualifier, start with the content
- Redundant pairs: "various and diverse", "each and every",
  "first and foremost" → pick one
- Weak intensifiers: "very", "really", "quite", "rather",
  "somewhat" → cut or replace with a stronger word
- Passive constructions: "it has been found that" →
  state the finding directly
- Throat-clear clauses: "When it comes to X, the thing to
  know is..." → just say the thing

**CONSISTENCY AUDIT — apply after compression:**
Audit and resolve inconsistencies in:
- Terminology: same term used consistently throughout
- Tone: voice does not drift between sections
- Claims: no internal contradictions
- Header formatting: H3s consistently formatted as questions
  or consistently as statements — not mixed
- Data: statistics cited identically wherever they appear
Flag: [INCONSISTENCY] — resolve to the correct version throughout.

**SEO FINAL VERIFICATION:**
- Primary keyword present in first sentence, H1,
  at least one H2, title tag, meta description, URL slug
- URL slug is 3–6 words, keyword-forward, no stop words
- Read the post listening for unnatural keyword repetition
- Secondary keywords distributed — none clustered in one section
- Semantic field vocabulary present throughout — not front-loaded
- Internal links distributed quasi-evenly, not clustered
- Meta title and description are final and within character limits
- FAQ schema JSON-LD matches FAQ section exactly

**ORIGINALITY CHECK:**
Does this post contain at least one idea, framework, insight,
or perspective that the reader could not get from the top 3
currently ranking posts on this topic?
If no — add it now. One original insight is sufficient to
differentiate the post from everything competing with it.
This is non-negotiable before declaring the post ready.

---

### ─── PHASE 5: FINAL OUTPUT ───────────────────────────────────────────

*Deliver the complete final package directly in the chat window
in markdown format. Do NOT create or save a separate file.*

---

**[1] POST METADATA**
```
Primary keyword:
Secondary keywords:
Search intent:
Snippet format targeted:
Voice position:
Word count:
Reading level:
YMYL: Yes / No
```

**[2] TITLE TAG**
*(final, under 60 characters)*

**[3] META DESCRIPTION**
*(final, under 160 characters)*

**[4] URL SLUG**
*(final, 3–6 words, keyword-forward, no stop words)*

**[5] SELECTED H1**
*(with rationale for selection)*

**[6] FULL POLISHED DRAFT**
Complete post with all placeholders intact:
[anchor text](INTERNAL LINK → topic) — for unresolved internal links
[anchor text](https://actual-url.com) — for resolved internal links and external citations
[QUOTABLE]
[IMAGE-FEATURED: description | text overlay]
[IMAGE-CONTENT: description | type: illustrative]
[IMAGE-DATA: description | type: infographic / diagram]
[NEEDS EVIDENCE] — if any remain unresolved

Content order in the draft:
1. Opening (Hook-Answer-Promise)
2. Body H2/H3 sections (with image markers where appropriate)
3. Conclusion (engaging H2, not a generic label)
4. FAQ section (always last)

**[7] FAQ SCHEMA**
Ready-to-use FAQ structured data in JSON-LD format.
Generate from the FAQ section of the post.
Output as a complete, copy-paste-ready script block:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[question from FAQ section]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[answer from FAQ section]"
      }
    }
  ]
}
</script>
```
Include all 4–6 FAQ questions and answers from the post.
Answers must match the published FAQ answers exactly.

**[8] INTERNAL LINK MAP**
Complete list of all link opportunities with anchor text and
their location in the post (which H2 section):
- [anchor text](INTERNAL LINK → topic description) — in H2: [section name] — URL unknown
- [anchor text](https://yoursite.com/page-slug) — in H2: [section name] — URL known
...

**[9] SOCIAL PULL QUOTES**
The 5–8 [QUOTABLE] sentences extracted and ready to copy
for social media, newsletters, or promotional use.

**[10] EDITOR FLAGS — RESOLVE BEFORE PUBLISHING**
Consolidated list of all items requiring human verification:
- [NEEDS EVIDENCE]: list any claims still requiring support
- Broken or unverified URLs: list any links that could not be confirmed

**[11] AUTHOR BIO BLOCK**
60–80 words, third person.
Establish expertise relevant to this specific topic.
Include 2–3 credibility signals appropriate to the niche
(years of experience, specific background, publications,
relevant achievements, certifications).

**[12] PUBLISHING READINESS VERDICT**
```
Status: READY TO PUBLISH / NOT READY
Outstanding items (if not ready): [list]
```

**[13] IMAGE BRIEF**
This brief is split into two parts: images Claude generates via Canva,
and data visuals the user builds manually in Canva.

**Part A — Canva-generated images (featured + conceptual)**
These are generated by Claude via Section E.

| # | Type | Placement | Visual concept | Text overlay | Dimensions |
|---|------|-----------|---------------|-------------|------------|
| 1 | Featured | Top of post | [description] | [shortened title with keyword, 6–8 words max] | 1920x1080 |
| 2 | Conceptual | H2: [section] | [description] | [text or "none"] | 1920x1080 |
| ... | ... | ... | ... | ... | ... |

Rules for Part A:
- Featured image: shortened blog title with primary keyword,
  6–8 words max. Never a full sentence.
- Conceptual images: illustrative visuals for general concepts,
  tips, and section breaks. Also required as a companion above
  every infographic/diagram (one conceptual image per data visual).
- All images: 1920x1080 px (16:9 landscape), no exceptions.

**Part B — Manual design specs (infographics, diagrams, charts)**
These are NOT generated by Canva. The user builds them manually.
Provide a complete visual spec for each.

For each infographic/diagram, output:

```
DATA VISUAL #[number]
Placement: H2: [section name] (below conceptual image #[X])
Type: [infographic / diagram / chart / comparison table]
Dimensions: 1920x1080 px (16:9 landscape). If data cannot fit
in one image, split into multiple 1920x1080 images.

CONTENT:
- Title/headline: [text]
- Data points / items:
  [list all data, statistics, labels, values, categories]

LAYOUT:
- Structure: [e.g., left-to-right flow / top-to-bottom hierarchy /
  grid / side-by-side comparison / radial / timeline]
- Sections: [describe how information is grouped]
- Visual hierarchy: [what is most prominent, what is secondary]

COLOUR PALETTE:
- Primary colour: [hex code + name] — used for [what]
- Secondary colour: [hex code + name] — used for [what]
- Accent colour: [hex code + name] — used for [what]
- Background: [colour or gradient]
(Do NOT default to brand colours. Choose colours that suit the
data and the section's mood. Each data visual can have its own palette.)

TYPOGRAPHY:
- Font: Open Sans only
- Headline: Open Sans Bold, [size suggestion]
- Body/labels: Open Sans Regular, [size suggestion]

ELEMENTS:
- [Describe specific visual elements: icons, arrows, shapes,
  dividers, number callouts, progress bars, etc.]
- [Describe relationships between elements: what connects to what,
  flow direction, grouping]

ALT TEXT:
[Specific, descriptive alt text for this image]
```

---

## SECTION D — GLOBAL RULES
*Active at all times throughout the entire pipeline.
These override any instruction that conflicts with them.*

1. **Mobile-first, always.**
   Write for readers on a phone screen. Short paragraphs,
   short sentences, scannable structure. Every screen-scroll
   should deliver value. If a paragraph looks like a wall of
   text on a 6-inch screen, break it up.

2. **Primary keyword in the first sentence. No exceptions.**
   The primary keyword must appear naturally in the very first
   sentence of the post. Not the first paragraph. Not the first
   100 words. The first sentence. If this rule conflicts with
   any other drafting instruction, this rule wins.

3. **Humans first, algorithms second.**
   If a sentence reads as optimized rather than natural,
   rewrite it. SEO serves the writing — the writing does not
   serve the SEO.

4. **Never summarize when you can illustrate.**
   An example, scenario, or data point is always more
   valuable than an abstract restatement.

5. **Every sentence earns its place.**
   If removing a sentence loses nothing, remove it.

6. **Specificity over generality — always.**
   At every level: claims, examples, data, language.

7. **Be the most useful resource available.**
   The post must be the most comprehensive, trustworthy,
   and genuinely helpful resource a reader could find
   on this topic. If it isn't, it isn't finished.

8. **Never invent citations.**
   If a source cannot be verified with a real URL, do not cite it.
   Omit the claim or reframe it without citing a specific source.
   A missing citation is recoverable. A hallucinated one
   destroys trust permanently.

9. **The pipeline is sequential.**
   Phase 1 before Phase 2. Phase 2 before Phase 3.
   Phase 3 before Phase 4. Phase 4 before Phase 5.
   Do not collapse phases or skip steps.

---

## SECTION E — CANVA IMAGE CREATION
*This section is triggered manually AFTER the blog content is approved.
Do not execute this section during the blog writing pipeline (Phases 1–5).
When the user says "create the images," "make the blog images,"
or similar, execute this section using the Image Brief from [13].*

*This section ONLY generates featured and conceptual images (Part A
of the Image Brief). Infographics, diagrams, and charts (Part B)
are built manually by the user using the design specs provided
in Phase 5.*

---

### TRIGGER
The user explicitly requests image creation after reviewing
and approving the blog draft from Phase 5.

### SETUP

**Step 1 — Retrieve brand kit**
Use the Canva `list-brand-kits` tool to retrieve the user's brand kit.
Pass the brand kit ID to the generate-design tool.

However, the brand kit's colours must NOT drive the design's colour
palette. The brand kit is attached for logo access and font fallback
only. The actual colour palette for each image is chosen independently
based on the content and mood of the section. Brand colours should
not appear as backgrounds, dominant fills, or primary colour schemes.
If they appear at all, they appear as minor accents (a thin border,
a small logo watermark, an icon tint).

**Step 2 — Create blog folder**
Use the Canva `create-folder` tool to create a new folder named:
`Blog — [short blog title or primary keyword]`
All images for this post will be moved into this folder after creation.

### IMAGE CREATION SEQUENCE

Process only Part A of the Image Brief (featured + conceptual images).
Skip Part B (those are for manual design by the user).

For each image in Part A:

**A. Generate the design**
Use the Canva `generate-design` tool with:
- `query`: a detailed description of the visual, derived from the
  Image Brief's "Visual concept" and "Text overlay" columns.
  Be specific. Include style direction, composition notes, and
  any text that should appear on the image.
  Always include in the query: "landscape orientation, 16:9 aspect
  ratio, 1920x1080 pixels, wide horizontal layout."
- `design_type`: ALWAYS use `presentation` for all blog images.
  The `presentation` preset in Canva produces 1920x1080 px designs,
  which is the exact dimension and 16:9 aspect ratio required.
  Do not use `poster`, `infographic`, `flyer`, or any other type.
  These produce portrait or non-standard dimensions.
- `brand_kit_id`: the brand kit ID retrieved in Step 1.

**B. Font rule — all images**
Include in every query: "Use Open Sans as the only font.
Open Sans Regular for body text, Open Sans Bold for headlines.
No other fonts."

**C. Colour rule — all images**
Do NOT rely on the brand kit for the colour palette.
Each image gets its own colour palette based on its content and mood.
Brand colours must not be the dominant colour of any image.

Include in every query: "Do not use brand colours as the primary
palette. Choose a fresh colour palette that suits this specific
visual concept. Use 2–3 complementary colours. The design should
feel visually distinct, not branded. Brand colours may appear as
minor accents only (thin border, small logo, icon tint) if at all."

Different images across the same blog post should look varied in
colour, not uniform.

**D. Featured image style guidance**
The featured image must not look like a raw AI-generated photo.
Include in the query:
- Graphical elements (shapes, overlays, colour blocks, icons)
- Text overlay: use ONLY a shortened version of the blog title
  that contains the primary keyword. Maximum 6–8 words.
  If the blog title is already short, use it as-is.
  If it's long, condense to its essence.
  Never include subtitles, taglines, descriptions, or full
  sentences on the featured image.
- A composition that looks designed, not just generated

**E. Conceptual image style guidance**
Conceptual images are illustrative visuals that complement a
section's content. They are similar in style to the featured
image: designed, graphical, visually interesting.
- With or without text overlay. Keep text minimal if used.
- Should feel like a natural visual companion to the section,
  not a stock photo or generic illustration.
- Each conceptual image should look different from the others
  and from the featured image (different palette, different
  composition, different visual approach).

**F. Select the best candidate**
The `generate-design` tool returns multiple candidates.
Present all candidates to the user with their preview thumbnails.
Ask the user to select their preferred option.

**G. Create the design from the selected candidate**
Use `create-design-from-candidate` with the selected candidate's
`candidate_id` and `job_id`.

**H. Verify dimensions**
After creation, verify the design is 1920x1080 px and landscape.
If the design was generated in portrait or wrong dimensions,
use `resize-design` with custom dimensions:
`{ "type": "custom", "width": 1920, "height": 1080 }`
Do not proceed to export until the design is confirmed at
1920x1080 px in landscape orientation.

**I. Export**
Use `export-design` to export each image as JPG with regular quality.

**J. Organize**
Use `move-item-to-folder` to move the finished design into the
blog folder created in Step 2.

### COMPLETION

After all Part A images are created, exported, and organized, output:

```
IMAGE CREATION COMPLETE
Folder: Blog — [title]
Canva-generated images: [count]
Manual design specs (Part B): [count] — see Image Brief for specs

| # | Type | File | Dimensions | Status |
|---|------|------|------------|--------|
| 1 | Featured | [design name] | 1920x1080 | Exported (JPG) |
| 2 | Conceptual | [design name] | 1920x1080 | Exported (JPG) |
| ... | ... | ... | ... | ... |

MANUAL DESIGNS NEEDED:
| # | Type | Placement | Status |
|---|------|-----------|--------|
| 1 | [infographic/diagram] | H2: [section] | Design spec in Image Brief Part B |
| ... | ... | ... | ... |
```

Provide the Canva folder link so the user can review all images
in one place. Remind the user that Part B designs need to be
built manually using the design specs in the Image Brief.

### IMAGE CREATION RULES

1. **Part A only.** Section E generates only featured and conceptual
   images. Never attempt to generate infographics, diagrams, or
   charts via Canva. Those are designed manually by the user.

2. **One image at a time.** Generate, select, create, verify dimensions,
   export, and organize each image before moving to the next.

3. **User selects every image.** Never auto-select a candidate.
   Always present options and wait for the user's choice.

4. **Always use `presentation` design type.** This is the only
   design type that produces 1920x1080 px landscape images.
   Never use poster, infographic, flyer, or any other type.

5. **Always 1920x1080 landscape.** Every generated image must be
   1920x1080 px in landscape orientation (16:9). No exceptions.

6. **Open Sans only.** No other fonts. Open Sans Regular for body text,
   Open Sans Bold for headlines.

7. **Brand colours are NOT the palette.** Do not use brand colours
   as the dominant colour scheme for any image. Each image gets its
   own colour palette based on its content. Brand colours may appear
   as minor accents only (thin border, small logo, icon tint), or
   not at all. The set of images across a blog post should look
   visually varied, not branded or uniform.

8. **Featured image text: 6–8 words max.** Use only a shortened
   version of the blog title containing the primary keyword.
   No subtitles, taglines, or full sentences.

9. **Alt text carries over.** The visual concept description from the
   Image Brief becomes the image's alt text for SEO. Ensure it is
   specific and descriptive.

10. **No generic stock-photo aesthetics.** Every image should look
    intentionally designed, not like a default AI generation or
    a stock photo with text slapped on it.

11. **Mobile readability.** Any text on images must be legible at
    mobile viewport sizes. Keep text minimal. If text would be
    unreadable on a phone screen, remove it.

---

*MASTER BLOG CREATION PROMPT — Version 3.3*
*All sections integrated: Brief · Structure · SEO · AEO · GEO ·
E-E-A-T · Voice & Craft · Mobile-First Readability · AI Detection Defense ·
Polish · Publishing Readiness · Canva Image Creation · Manual Design Specs*
