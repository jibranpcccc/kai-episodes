# -*- coding: utf-8 -*-
"""
FUSION — "YOUR LOCAL AI CAN RETURN PERFECT JSON AND THE WRONG ANSWER"
A MASTER TECH EXPLAINER ON STRUCTURED OUTPUTS, SCHEMAS, AND VERIFICATION.
55 windows, rotating layouts (hook, rows, chain, bars, rail, note),
100% verified anchors, zero ACT mentions, zero chat lines.
"""

NAME = "BYTE-STRUCTURED-OUTPUTS"
TITLE = "YOUR LOCAL AI CAN RETURN PERFECT JSON AND THE WRONG ANSWER"
DOC_TITLE = "YOUR LOCAL AI CAN RETURN PERFECT JSON AND THE WRONG ANSWER · BYTE FORENSICS"
KICKER = "BYTE FORENSICS · STRUCTURED OUTPUTS"
SUBTITLE = "valid json is not verified truth"

W = []

def win(layout, vo, **data):
    W.append(dict(layout=layout, vo=vo, **data))

# =====================================================================
# WINDOW 1 -- HOOK. The Clean Failure Mode.
# =====================================================================
win("hook",
    vo="Your model can return perfect JSON and the wrong payment amount. "
       "Every bracket closes. Every field has the correct type. "
       "Your automation reads the response without an error, then quietly prepares the wrong record.",
    kicker="BYTE FORENSICS · SCHEMA TRAP",
    title="PERFECT JSON, WRONG ANSWER",
    sub="syntax validity does not equal factual truth",
    art="model_file",
    art_caption="THE PARSED INVOICE PAYLOAD",
    header_at="Your model can return perfect JSON",
    art_at="Your model can return perfect JSON",
    chips=[
        dict(t="EVERY BRACKET CLOSES PERFECTLY", c="cyan", at="Every bracket closes"),
        dict(t="EVERY FIELD HAS THE CORRECT TYPE", c="ghost", at="Every field has the correct type"),
        dict(t="AUTOMATION PREPARES WRONG RECORD", c="red", at="then quietly prepares the wrong record"),
    ],
    stats=[
        dict(v="100%", u="VALID", lab="JSON SYNTAX PARSER PASS", c="gold", at="Your model can return perfect JSON"),
        dict(v="0%", u="VERIFIED", lab="BUSINESS FACTUAL CERTAINTY", c="red", at="then quietly prepares the wrong record"),
    ],
    tape="SYNTAX SUCCESS MASKS SEMANTIC FAILURE",
    tape_at="quietly prepares the wrong record",
    source="json grammar · structured output execution")

# =====================================================================
# WINDOW 2 -- ROWS. Two Different Promises.
# =====================================================================
win("rows",
    vo="That is the uncomfortable part of structured outputs. They can remove a "
       "class of software failures while making a different failure look unusually "
       "clean. A parser sees a valid number. Your business needed the correct "
       "number. Those are different promises.",
    kicker="BYTE FORENSICS · THE PROMISE GAP",
    title="TWO DIFFERENT PROMISES",
    art="checklist",
    art_caption="VALID NUMBER VS CORRECT NUMBER",
    header_at="That is the uncomfortable part",
    art_at="That is the uncomfortable part",
    rows=[
        dict(rank="01", name="SOFTWARE FAILURE", val="REMOVED", sub="SYNTAX CRASHES ELIMINATED", cls="cyan",
             at="remove a class of software failures"),
        dict(rank="02", name="FACTUAL FAILURE", val="HIDDEN", sub="WRONG RECORD LOOKS CLEAN", cls="red",
             at="making a different failure look unusually clean"),
        dict(rank="03", name="PARSER VIEW", val="VALID", sub="OBEYS DATA TYPE RULES", cls="",
             at="A parser sees a valid number"),
        dict(rank="04", name="BUSINESS NEED", val="EXACT", sub="REQUIRES REAL TRUTH", cls="gold",
             at="Your business needed the correct number"),
    ],
    closing=dict(t="PARSER VALIDITY NEVER CERTIFIES FACTUAL TRUTH", c="gold",
                 at="Those are different promises"),
    source="schema constraints vs business invariants")

# =====================================================================
# WINDOW 3 -- CHAIN. Turning Emails into Entries.
# =====================================================================
win("chain",
    vo="Picture a local assistant turning order emails into accounting entries. "
       "You ask for a supplier identifier, a currency, and a total in minor units. "
       "The schema can require those fields and restrict their types.",
    kicker="BYTE FORENSICS · WORKFLOW AUDIT",
    title="TURNING EMAILS INTO ENTRIES",
    art="pipeline",
    art_caption="INVOICE EXTRACTION PIPELINE",
    header_at="Picture a local assistant",
    art_at="Picture a local assistant",
    chain=[
        dict(t="01 EMAIL", s="RAW UNSTRUCTURED TEXT", at="turning order emails into accounting entries"),
        dict(t="02 SCHEMA", s="DECLARED FIELD CONTRACT", at="supplier identifier, a currency"),
        dict(t="03 TYPING", s="RESTRICTED FIELD TYPES", at="require those fields and restrict their types"),
    ],
    compare=[
        dict(cls="good", title="SCHEMA CONTRACT",
             body="Requires supplier, currency, and total fields with strict typing.",
             at="supplier identifier, a currency, and a total"),
        dict(cls="hot", title="UNRESTRICTED SOURCE",
             body="Input text can be incomplete, ambiguous, or misleading.",
             at="The schema can require those fields"),
    ],
    source="accounting automation · local llm extraction")

# =====================================================================
# WINDOW 4 -- BARS. Allowed Values vs Real Values.
# =====================================================================
win("bars",
    vo="But an allowed currency can still be the wrong currency. A supplier "
       "identifier can be a valid string that belongs to somebody else. "
       "Passing the contract does not establish the relationship between those values and the order.",
    kicker="BYTE FORENSICS · VALUE VALIDATION",
    title="ALLOWED VALUES VS REAL VALUES",
    art="warning",
    art_caption="ORPHAN VALUE DETECTION",
    header_at="But an allowed currency can still be",
    art_at="But an allowed currency can still be",
    scale=100.0,
    bars=[
        dict(lab="CURRENCY TYPE", val="100", unit="PCT", pct=100.0, cls="cyan",
             at="allowed currency can still be"),
        dict(lab="SUPPLIER ID", val="100", unit="PCT", pct=100.0, cls="",
             at="supplier identifier can be a valid string"),
        dict(lab="REAL RELATION", val="0", unit="PCT", pct=5.0, cls="red",
             at="Passing the contract does not establish"),
    ],
    closing=dict(t="CONTRACT PASSING DOES NOT PROVE TRANSACTION BINDING", c="red",
                 at="between those values and the order"),
    source="relational integrity vs schema validation")

# =====================================================================
# WINDOW 5 -- RAIL. The Three Separate Gates.
# =====================================================================
win("rail",
    vo="There are three separate gates. Parsing asks whether this is JSON. "
       "Schema validation asks whether the record obeys the declared rules. "
       "Semantic verification asks whether these values are correct for this transaction.",
    kicker="BYTE FORENSICS · ARCHITECTURAL GATES",
    title="THE THREE SEPARATE GATES",
    art="two_die",
    art_caption="THREE INDEPENDENT GATES",
    header_at="There are three separate gates",
    art_at="There are three separate gates",
    rails=[
        dict(lab="GATE 1: PARSE", val="SYNTAX OK", pct=100.0, cls="cyan",
             at="Parsing asks whether this is JSON"),
        dict(lab="GATE 2: SCHEMA", val="RULES OK", pct=100.0, cls="gold",
             at="Schema validation asks whether the record"),
        dict(lab="GATE 3: SEMANTIC", val="FACT CHECK", pct=33.3, cls="red",
             at="Semantic verification asks whether these values"),
    ],
    closing=dict(t="EACH GATE ANSWERS A COMPLETELY DIFFERENT QUESTION", c="gold",
                 at="correct for this transaction"),
    source="software architecture · verification levels")

# =====================================================================
# WINDOW 6 -- NOTE. What Grammar Actually Does.
# =====================================================================
win("note",
    vo="A grammar operates during generation, restricting which token choices "
       "remain available. It can stop the model from writing a paragraph where "
       "your application expects an object. It does not inspect your supplier "
       "database merely because the output has a supplier field.",
    kicker="BYTE FORENSICS · GENERATION CONSTRAINTS",
    title="WHAT GRAMMAR ACTUALLY DOES",
    art="token_blocks",
    art_caption="LOGIT MASKING AT RUNTIME",
    header_at="A grammar operates during generation",
    art_at="A grammar operates during generation",
    note_head="WHAT LOGIT MASKING CAN AND CANNOT DO",
    note_items=[
        dict(t="RESTRICTS LOGITS TO TOKENS MATCHING THE GRAMMAR",
             at="restricting which token choices remain available"),
        dict(t="STOPS MODEL FROM GENERATING FREEFORM PROSE",
             at="writing a paragraph where your application expects"),
        dict(t="CANNOT QUERY YOUR DATABASE OR VERIFY BUSINESS FACTS",
             at="does not inspect your supplier database"),
    ],
    tape="GRAMMAR MASKS LOGITS, NOT TRUTH",
    tape_at="merely because the output has a supplier field",
    source="constrained decoding · grammar logit masking")

# =====================================================================
# WINDOW 7 -- ROWS. The Compulsory Field Mistake.
# =====================================================================
win("rows",
    vo="The design mistake starts when every field is compulsory but "
       "uncertainty has no legal representation. An incomplete order arrives. "
       "The application still demands a total. Instead, give the contract an "
       "explicit path for missing information, such as null and a needs review status.",
    kicker="BYTE FORENSICS · CONTRACT DESIGN",
    title="THE COMPULSORY FIELD MISTAKE",
    art="checklist",
    art_caption="REPRESENTING UNCERTAINTY",
    header_at="The design mistake starts",
    art_at="The design mistake starts",
    rows=[
        dict(rank="01", name="COMPULSORY FIELD", val="FLAW", sub="FORCES HALLUCINATED VALUE", cls="red",
             at="every field is compulsory"),
        dict(rank="02", name="INCOMPLETE INPUT", val="GAP", sub="MISSING SOURCE EVIDENCE", cls="",
             at="An incomplete order arrives"),
        dict(rank="03", name="EXPLICIT NULL", val="PATH", sub="LEGAL REPRESENTATION", cls="cyan",
             at="explicit path for missing information"),
        dict(rank="04", name="NEEDS REVIEW", val="STATUS", sub="SAFE FALLBACK ROUTE", cls="gold",
             at="needs review status"),
    ],
    closing=dict(t="ALWAYS PROVIDE A LEGAL PATH FOR UNCERTAINTY", c="gold",
                 at="give the contract an explicit path"),
    source="contract design · defensive schema modeling")

# =====================================================================
# WINDOW 8 -- CHAIN. Designing What Code May Claim.
# =====================================================================
win("chain",
    vo="Then check that path in ordinary application code. You are designing "
       "what the system may claim, and what happens when it cannot justify a "
       "claim. That matters more than whether the response looks tidy.",
    kicker="BYTE FORENSICS · DEFENSIVE DESIGN",
    title="DESIGNING WHAT CODE MAY CLAIM",
    art="magnifier",
    art_caption="APPLICATION LOGIC GATE",
    header_at="Then check that path",
    art_at="Then check that path",
    chain=[
        dict(t="01 NULL CHECK", s="DETECT UNCERTAINTY", at="check that path in ordinary application code"),
        dict(t="02 JUSTIFICATION", s="AUDIT SOURCE FACTS", at="what the system may claim"),
        dict(t="03 ROUTING", s="SEND TO REVIEW", at="cannot justify a claim"),
    ],
    compare=[
        dict(cls="good", title="APPLICATION CODE",
             body="Checks fallback paths and enforces business logic before actions.",
             at="check that path in ordinary application"),
        dict(cls="hot", title="COSMETIC TIDINESS",
             body="A clean JSON response that hides unverified claims.",
             at="whether the response looks tidy"),
    ],
    source="application verification · claims auditing")

# =====================================================================
# WINDOW 9 -- BARS. Three Dimensions of Evidence.
# =====================================================================
win("bars",
    vo="The question is which part works, on which schema, in which runtime. "
       "We need separate evidence for speed, supported constraints, and task "
       "correctness. Then we can build a local workflow that uses the structure without allowing structure to impersonate evidence.",
    kicker="BYTE FORENSICS · BENCHMARK CRITERIA",
    title="THREE DIMENSIONS OF EVIDENCE",
    art="scales",
    art_caption="THREE INDEPENDENT METRICS",
    header_at="The question is which part works",
    art_at="The question is which part works",
    scale=100.0,
    bars=[
        dict(lab="GENERATION SPEED", val="DIM 1", unit="EVAL", pct=100.0, cls="cyan",
             at="separate evidence for speed"),
        dict(lab="SUPPORTED RULES", val="DIM 2", unit="EVAL", pct=75.0, cls="gold",
             at="supported constraints"),
        dict(lab="TASK ACCURACY", val="DIM 3", unit="EVAL", pct=50.0, cls="red",
             at="task correctness"),
    ],
    closing=dict(t="NEVER ALLOW STRUCTURE TO IMPERSONATE EVIDENCE", c="red",
                 at="allowing structure to impersonate evidence"),
    source="empirical evaluation · runtime validation")

# =====================================================================
# WINDOW 10 -- RAIL. The Dissection of Success.
# =====================================================================
win("rail",
    vo="Start with the benchmark that measured those dimensions separately, "
       "because collapsing them into one success percentage is exactly how this mistake survives.",
    kicker="BYTE FORENSICS · BENCHMARK RIGOR",
    title="THE DISSECTION OF SUCCESS",
    art="folder",
    art_caption="JSON SCHEMA BENCH",
    header_at="Start with the benchmark",
    art_at="Start with the benchmark",
    rails=[
        dict(lab="SEPARATE DIMS", val="RIGOROUS", pct=100.0, cls="gold",
             at="measured those dimensions separately"),
        dict(lab="SINGLE PCT", val="MISLEADING", pct=100.0, cls="red",
             at="collapsing them into one success percentage"),
    ],
    closing=dict(t="BLENDED SUCCESS PERCENTAGES HIDE CRITICAL DEFECTS", c="gold",
                 at="how this mistake survives"),
    source="json schema bench · methodology analysis")

# =====================================================================
# WINDOW 11 -- NOTE. The Schema Bench Corpus.
# =====================================================================
win("note",
    vo="The original JSON Schema Bench paper describes roughly ten thousand "
       "schemas. Its collection table totals nine thousand five hundred and "
       "fifty-eight. They come from repository configurations, service "
       "interfaces, and function definitions.",
    kicker="BYTE FORENSICS · BENCHMARK DATASET",
    title="THE SCHEMA BENCH CORPUS",
    art="folder",
    art_caption="9,558 REAL-WORLD SCHEMAS",
    header_at="The original JSON Schema Bench",
    art_at="The original JSON Schema Bench",
    note_head="COMPOSITION OF THE CORPUS",
    note_items=[
        dict(t="9,558 TOTAL SCHEMAS COLLECTED ACROSS DIVERSE DOMAINS",
             at="totals nine thousand five hundred and fifty-eight"),
        dict(t="DERIVED FROM REAL REPOSITORY CONFIGURATIONS",
             at="repository configurations"),
        dict(t="INCLUDES SERVICE INTERFACES AND TOOL CALL FUNCTIONS",
             at="service interfaces, and function definitions"),
    ],
    tape="9,558 SCHEMAS IN THE BENCHMARK CORPUS",
    tape_at="service interfaces, and function definitions",
    source="json schema bench paper · dataset table")

# =====================================================================
# WINDOW 12 -- ROWS. Denominator Forensics.
# =====================================================================
win("rows",
    vo="The paper measures efficiency, coverage, and quality separately. "
       "It excludes the trivial and ultra difficulty repository groups from its "
       "reported experiments while retaining them in the corpus. Even the "
       "denominator needs reading before we turn a benchmark into a product claim.",
    kicker="BYTE FORENSICS · CORPUS FILTERING",
    title="DENOMINATOR FORENSICS",
    art="scales",
    art_caption="EXPERIMENT FILTERING",
    header_at="The paper measures efficiency",
    art_at="The paper measures efficiency",
    rows=[
        dict(rank="01", name="EFFICIENCY", val="TOKEN MS", sub="SPEED OF GENERATION", cls="cyan",
             at="measures efficiency"),
        dict(rank="02", name="COVERAGE", val="SCHEMA PCT", sub="RULES SUPPORTED", cls="",
             at="coverage, and quality separately"),
        dict(rank="03", name="TRIVIAL GROUP", val="EXCLUDED", sub="DROPPED FROM TESTS", cls="red",
             at="excludes the trivial"),
        dict(rank="04", name="ULTRA GROUP", val="EXCLUDED", sub="DROPPED FROM TESTS", cls="gold",
             at="ultra difficulty repository groups"),
    ],
    closing=dict(t="READ THE EXPERIMENTAL DENOMINATOR CAREFULLY", c="gold",
                 at="needs reading before we turn a benchmark"),
    source="benchmark methodology · experimental exclusions")

# =====================================================================
# WINDOW 13 -- CHAIN. The Efficiency Benchmark Rig.
# =====================================================================
win("chain",
    vo="For efficiency, the authors used Llama three point one eight billion "
       "Instruct, quantized to eight bits, on one A one hundred with eighty "
       "gigabytes of memory. Batch size was one.",
    kicker="BYTE FORENSICS · TEST RIG HARDWARE",
    title="THE EFFICIENCY BENCHMARK RIG",
    art="superchip",
    art_caption="A100 80GB SXM TESTBED",
    header_at="For efficiency, the authors used",
    art_at="For efficiency, the authors used",
    chain=[
        dict(t="01 MODEL", s="LLAMA 3.1 8B INSTRUCT", at="Llama three point one eight billion"),
        dict(t="02 QUANT", s="8-BIT PRECISION", at="quantized to eight bits"),
        dict(t="03 RIG", s="A100 80GB VRAM", at="eighty gigabytes of memory"),
    ],
    compare=[
        dict(cls="good", title="TEST HARDWARE",
             body="Enterprise A100 with massive 80GB VRAM and high memory bandwidth.",
             at="one A one hundred with eighty"),
        dict(cls="hot", title="EXECUTION SETTING",
             body="Batch size fixed at one for single-stream generation.",
             at="Batch size was one"),
    ],
    source="json schema bench · efficiency setup")

# =====================================================================
# WINDOW 14 -- BARS. Token Latency on Glaive.
# =====================================================================
win("bars",
    vo="On the Glaive dataset, median time per output token was fifteen point "
       "four zero milliseconds without constraints, six point three seven with "
       "Guidance, and twenty-nine point nine eight with the tested Llama CPP path. "
       "Those are historical measurements from that setup, not predictions for your desktop.",
    kicker="BYTE FORENSICS · GLAIVE MEASUREMENTS",
    title="TOKEN LATENCY ON GLAIVE",
    art="clock",
    art_caption="MEDIAN MS PER TOKEN",
    header_at="On the Glaive dataset",
    art_at="On the Glaive dataset",
    scale=35.0,
    bars=[
        dict(lab="UNCONSTRAINED", val="15.40", unit="MS", pct=51.3, cls="",
             at="fifteen point four zero milliseconds"),
        dict(lab="GUIDANCE", val="6.37", unit="MS", pct=21.2, cls="gold",
             at="six point three seven with Guidance"),
        dict(lab="LLAMA CPP (TESTED)", val="29.98", unit="MS", pct=99.9, cls="red",
             at="twenty-nine point nine eight with the tested"),
    ],
    closing=dict(t="THESE ARE HISTORICAL BENCHMARKS, NOT DESKTOP RULES", c="gold",
                 at="Those are historical measurements"),
    source="glaive dataset · median time per output token")

# =====================================================================
# WINDOW 15 -- RAIL. The Guidance Speedup Mechanism.
# =====================================================================
win("rail",
    vo="The apparent speedup needs its mechanism attached. Guidance could "
       "fast forward some predictable output tokens. The comparison used "
       "schemas the engines could all process, and the authors enabled prefix caching.",
    kicker="BYTE FORENSICS · ENGINE MECHANICS",
    title="THE SPEEDUP MECHANISM",
    art="token_blocks",
    art_caption="TOKEN FAST FORWARDING",
    header_at="The apparent speedup needs",
    art_at="The apparent speedup needs",
    rails=[
        dict(lab="TOKEN FORWARD", val="GUIDANCE", pct=100.0, cls="gold",
             at="fast forward some predictable output tokens"),
        dict(lab="SCHEMA FILTER", val="COMMON", pct=70.0, cls="cyan",
             at="schemas the engines could all process"),
        dict(lab="PREFIX CACHE", val="ENABLED", pct=100.0, cls="",
             at="authors enabled prefix caching"),
    ],
    closing=dict(t="PREDICTABLE SYNTAX TOKENS WERE FAST-FORWARDED", c="gold",
                 at="authors enabled prefix caching"),
    source="guidance engine architecture · parser acceleration")

# =====================================================================
# WINDOW 16 -- NOTE. Pinned Library Versions.
# =====================================================================
win("note",
    vo="Their documentation snapshot lists older libraries, including Guidance "
       "zero point two zero release candidate and Llama CPP zero point three "
       "two. That library label is not our current source revision. "
       "Do not copy the ranking onto a modern runtime and call it a fresh test.",
    kicker="BYTE FORENSICS · VERSION SNAPSHOT",
    title="PINNED LIBRARY VERSIONS",
    art="caveat",
    art_caption="HISTORICAL REVISIONS",
    header_at="Their documentation snapshot lists",
    art_at="Their documentation snapshot lists",
    note_head="LIBRARIES IN THE REPORTED RUN",
    note_items=[
        dict(t="GUIDANCE 0.2.0-RC SNAPSHOT USED IN PAPER",
             at="Guidance zero point two zero release candidate"),
        dict(t="LLAMA.CPP 0.3.2 PYTHON WRAPPER PATH TESTED",
             at="Llama CPP zero point three two"),
        dict(t="CURRENT RUNTIMES FEATURE MAJOR GRAMMAR UPGRADES",
             at="That library label is not our current source"),
    ],
    tape="DO NOT COPY OLD RANKINGS TO MODERN RUNTIMES",
    tape_at="modern runtime and call it a fresh test",
    source="reproduction notes · library revisions")

# =====================================================================
# WINDOW 17 -- ROWS. The Coverage Gap.
# =====================================================================
win("rows",
    vo="Coverage used a different model: Llama three point two one billion "
       "Instruct, with two examples, greedy decoding, and one sampled output. "
       "Compilation had a forty-second limit, followed by another forty seconds for generation.",
    kicker="BYTE FORENSICS · COVERAGE CRITERIA",
    title="THE COVERAGE PROTOCOL",
    art="chip",
    art_caption="LLAMA 3.2 1B INSTRUCT",
    header_at="Coverage used a different model",
    art_at="Coverage used a different model",
    rows=[
        dict(rank="01", name="MODEL", val="1B INSTRUCT", sub="LLAMA 3.2 1B", cls="cyan",
             at="Llama three point two one billion"),
        dict(rank="02", name="DECODING", val="GREEDY", sub="2 EXAMPLES SUPPLIED", cls="",
             at="greedy decoding"),
        dict(rank="03", name="COMPILE CAP", val="40 SEC", sub="GRAMMAR COMPILATION", cls="gold",
             at="forty-second limit"),
        dict(rank="04", name="GEN LIMIT", val="40 SEC", sub="TOKEN GENERATION", cls="gold",
             at="another forty seconds for generation"),
    ],
    closing=dict(t="COVERAGE EVALUATION CARRIED STRICT TIMEOUT LIMITS", c="gold",
                 at="followed by another forty seconds"),
    source="json schema bench · coverage methodology")

# =====================================================================
# WINDOW 18 -- CHAIN. Acceptance vs Compliance.
# =====================================================================
win("chain",
    vo="In the hard repository collection, the tested Llama CPP path accepted "
       "sixty-one percent of schemas, but produced compliant output for "
       "thirty-nine percent of the collection. Acceptance and observed compliance "
       "were separate measurements. Neither number means factual invoice accuracy.",
    kicker="BYTE FORENSICS · HARD REPOSITORIES",
    title="ACCEPTANCE VS COMPLIANCE",
    art="scales",
    art_caption="ACCEPTANCE VS OBSERVATION",
    header_at="In the hard repository collection",
    art_at="In the hard repository collection",
    chain=[
        dict(t="01 ACCEPT", s="61% SCHEMAS COMPILED", at="accepted sixty-one percent of schemas"),
        dict(t="02 COMPLY", s="39% COMPLIANT OUTPUT", at="compliant output for thirty-nine percent"),
        dict(t="03 FACT", s="INDEPENDENT ACCURACY", at="factual invoice accuracy"),
    ],
    compare=[
        dict(cls="good", title="SCHEMA ACCEPTANCE",
             body="Grammar compiler accepts the schema without throwing a compile error.",
             at="accepted sixty-one percent"),
        dict(cls="hot", title="TASK ACCURACY",
             body="Factual accuracy of extracted values is entirely unmeasured by coverage.",
             at="Neither number means factual invoice accuracy"),
    ],
    source="hard repository collection · llama.cpp path")

# =====================================================================
# WINDOW 19 -- BARS. Quality on Mathematics.
# =====================================================================
win("bars",
    vo="Quality had its own result. On the grade school mathematics benchmark, "
       "Llama three point one eight billion scored eighty point one percent "
       "without constraints and eighty-three point eight with Guidance. "
       "That is a gain of three point seven percentage points under the paper's conditions.",
    kicker="BYTE FORENSICS · GSM8K EVALUATION",
    title="QUALITY ON MATHEMATICS",
    art="gauge",
    art_caption="GSM8K ACCURACY SCORE",
    header_at="Quality had its own result",
    art_at="Quality had its own result",
    scale=100.0,
    bars=[
        dict(lab="UNCONSTRAINED", val="80.1", unit="PCT", pct=80.1, cls="",
             at="eighty point one percent without constraints"),
        dict(lab="GUIDANCE", val="83.8", unit="PCT", pct=83.8, cls="gold",
             at="eighty-three point eight with Guidance"),
        dict(lab="GAIN", val="+3.7", unit="PTS", pct=37.0, cls="cyan",
             at="gain of three point seven percentage points"),
    ],
    closing=dict(t="CONSTRAINED DECODING YIELDED A 3.7 POINT GAIN", c="gold",
                 at="under the paper's conditions"),
    source="gsm8k · llama 3.1 8b · quality experiment")

# =====================================================================
# WINDOW 20 -- RAIL. The Remaining Error Margin.
# =====================================================================
win("rail",
    vo="It also leaves sixteen point two percent outside the exact match score. "
       "Better task accuracy is valuable. It is not a theorem that every "
       "structurally valid answer is true.",
    kicker="BYTE FORENSICS · ACCURACY CEILING",
    title="THE REMAINING ERROR MARGIN",
    art="warning",
    art_caption="16.2% MISS RATE",
    header_at="It also leaves sixteen point two",
    art_at="It also leaves sixteen point two",
    rails=[
        dict(lab="ERROR", val="16.2 PCT", pct=16.2, cls="red",
             at="sixteen point two percent outside"),
        dict(lab="ACCURATE", val="83.8 PCT", pct=83.8, cls="gold",
             at="Better task accuracy is valuable"),
    ],
    closing=dict(t="STRUCTURAL VALIDITY IS NEVER A PROOF OF TRUTH", c="red",
                 at="structurally valid answer is true"),
    source="error analysis · exact match criteria")

# =====================================================================
# WINDOW 21 -- NOTE. Three Tests for Three Claims.
# =====================================================================
win("note",
    vo="Constrained generation can help, but three success stories require "
       "three tests. A fast engine may support fewer schemas. "
       "An accepted schema may contain rules the engine does not enforce.",
    kicker="BYTE FORENSICS · TEST METHODOLOGY",
    title="THREE TESTS FOR THREE CLAIMS",
    art="checklist",
    art_caption="TRIPLE VERIFICATION",
    header_at="Constrained generation can help",
    art_at="Constrained generation can help",
    note_head="THREE INDEPENDENT EVALUATIONS",
    note_items=[
        dict(t="ACCURACY: COMPLIANT OUTPUT CAN STILL BE FACTUALLY FALSE",
             at="three success stories require three tests"),
        dict(t="SPEED: A FAST ENGINE MAY REJECT COMPLEX SCHEMAS",
             at="fast engine may support fewer schemas"),
        dict(t="SUPPORT: ACCEPTED SCHEMAS MAY SILENTLY DROP RULES",
             at="accepted schema may contain rules the engine does not enforce"),
    ],
    tape="ONE SUCCESS CLAIM DOES NOT PROVE THE OTHERS",
    tape_at="engine does not enforce",
    source="experimental design · independent verification")

# =====================================================================
# WINDOW 22 -- ROWS. Benchmark vs Production.
# =====================================================================
win("rows",
    vo="A compliant answer may still fail the task. This benchmark gives us "
       "better questions. It does not certify our purchase orders, our "
       "runtime build, or our choice of a smaller model for a new workload.",
    kicker="BYTE FORENSICS · REALITY CHECK",
    title="BENCHMARK VS PRODUCTION",
    art="question",
    art_caption="APPLICATION CONTEXT",
    header_at="A compliant answer may still fail",
    art_at="A compliant answer may still fail",
    rows=[
        dict(rank="01", name="COMPLIANT ANSWER", val="RISK", sub="CAN STILL FAIL THE TASK", cls="red",
             at="compliant answer may still fail the task"),
        dict(rank="02", name="PURCHASE ORDERS", val="UNCERTIFIED", sub="NEEDS REAL VALIDATION", cls="",
             at="does not certify our purchase orders"),
        dict(rank="03", name="RUNTIME BUILD", val="CUSTOM", sub="DEPENDS ON LOCAL VERSION", cls="gold",
             at="our runtime build"),
        dict(rank="04", name="MODEL CHOICE", val="AUDIT", sub="TASK SPECIFIC SIZING", cls="cyan",
             at="choice of a smaller model for a new workload"),
    ],
    closing=dict(t="BENCHMARKS PROVIDE QUESTIONS, NOT CERTIFICATES", c="gold",
                 at="new workload"),
    source="production engineering · local workload audit")

# =====================================================================
# WINDOW 23 -- CHAIN. Runtime Grammar Documentation.
# =====================================================================
win("chain",
    vo="Open the actual runtime documentation. In the pinned Llama CPP "
       "revision reviewed for this episode, JSON Schema conversion supports a "
       "subset of the standard. The grammar documentation says unsupported "
       "features can be skipped silently.",
    kicker="BYTE FORENSICS · RUNTIME INTERNALS",
    title="RUNTIME GRAMMAR DOCUMENTATION",
    art="caveat",
    art_caption="LLAMA.CPP GRAMMAR SOURCE",
    header_at="Open the actual runtime documentation",
    art_at="Open the actual runtime documentation",
    chain=[
        dict(t="01 SCHEMA", s="JSON SCHEMA INPUT", at="JSON Schema conversion supports"),
        dict(t="02 SUBSET", s="GRAMMAR CONVERTER", at="supports a subset of the standard"),
        dict(t="03 SILENT", s="UNSUPPORTED DROPPED", at="unsupported features can be skipped silently"),
    ],
    compare=[
        dict(cls="good", title="STANDARD SCHEMA",
             body="Contains full draft definitions including formats, boundaries, and items.",
             at="subset of the standard"),
        dict(cls="hot", title="SILENT DROP",
             body="Grammar converter silently ignores unsupported properties without errors.",
             at="skipped silently"),
    ],
    source="llama.cpp grammar parser documentation")

# =====================================================================
# WINDOW 24 -- BARS. Silent Drops vs Hard Errors.
# =====================================================================
win("bars",
    vo="That is a sharper limitation than a clean error saying your schema is "
       "rejected. A request can be accepted while an important rule does not "
       "become a generation constraint. The independent validator catches "
       "what your generation path did not guarantee.",
    kicker="BYTE FORENSICS · SILENT FAILURE",
    title="SILENT DROPS VS HARD ERRORS",
    art="warning",
    art_caption="UNENFORCED RULES",
    header_at="That is a sharper limitation",
    art_at="That is a sharper limitation",
    scale=100.0,
    bars=[
        dict(lab="REQUEST ACCEPT", val="100", unit="PCT", pct=100.0, cls="cyan",
             at="request can be accepted"),
        dict(lab="RULE ENFORCED", val="PART", unit="SUB", pct=50.0, cls="red",
             at="important rule does not become a generation constraint"),
        dict(lab="VALIDATOR CATCH", val="100", unit="PCT", pct=100.0, cls="gold",
             at="independent validator catches"),
    ],
    closing=dict(t="INDEPENDENT VALIDATION MUST AUDIT GENERATION GAPS", c="red",
                 at="what your generation path did not guarantee"),
    source="schema parsing · defensive runtime validation")

# =====================================================================
# WINDOW 25 -- RAIL. Unsupported Schema Constraints.
# =====================================================================
win("rail",
    vo="The details are concrete. That revision lists minimum and maximum "
       "support for integers, but not general number values. It lists missing "
       "email and web address string formats, and no unique items constraint.",
    kicker="BYTE FORENSICS · CONSTRAINTS AUDIT",
    title="UNSUPPORTED SCHEMA CONSTRAINTS",
    art="checklist",
    art_caption="SPECIFIC CONVERTER LIMITS",
    header_at="The details are concrete",
    art_at="The details are concrete",
    rails=[
        dict(lab="INTEGER MIN/MAX", val="SUPPORTED", pct=100.0, cls="gold",
             at="minimum and maximum support for integers"),
        dict(lab="NUMBER FLOAT", val="UNSUPPORTED", pct=0.0, cls="red",
             at="not general number values"),
        dict(lab="FORMAT: EMAIL/URI", val="UNSUPPORTED", pct=0.0, cls="red",
             at="missing email and web address"),
        dict(lab="UNIQUE ITEMS", val="UNSUPPORTED", pct=0.0, cls="red",
             at="no unique items constraint"),
    ],
    closing=dict(t="CRITICAL STRING FORMATS AND FLOATS WERE SILENTLY DROPPED", c="red",
                 at="no unique items constraint"),
    source="pinned llama.cpp schema converter revision")

# =====================================================================
# WINDOW 26 -- NOTE. The Integer Minor Unit Trap.
# =====================================================================
win("note",
    vo="A schema containing those rules can look stronger than the grammar it "
       "becomes. Integer minor units make a money contract easier to state "
       "precisely. But an allowed integer can still be the wrong amount, so "
       "the accounting comparison remains essential.",
    kicker="BYTE FORENSICS · MONEY CONTRACTS",
    title="THE INTEGER MINOR UNIT TRAP",
    art="magnifier",
    art_caption="CENTS VS DOLLARS",
    header_at="A schema containing those rules",
    art_at="A schema containing those rules",
    note_head="MONEY CONTRACT DESIGN RULES",
    note_items=[
        dict(t="SCHEMA CAN LOOK FAR STRONGER THAN CONVERTED GRAMMAR",
             at="look stronger than the grammar it becomes"),
        dict(t="USE INTEGER MINOR UNITS (CENTS) TO AVOID FLOAT AMBIGUITY",
             at="Integer minor units make a money contract easier"),
        dict(t="ALLOWED INTEGER DOES NOT PROVE CORRECT INVOICE TOTAL",
             at="allowed integer can still be the wrong amount"),
    ],
    tape="ACCOUNTING COMPARISON REMAINS ESSENTIAL",
    tape_at="accounting comparison remains essential",
    source="financial schema modeling · minor units arithmetic")

# =====================================================================
# WINDOW 27 -- ROWS. The Prompt Injection Blindspot.
# =====================================================================
win("rows",
    vo="There is another trap. For ordinary structured responses, that schema "
       "is not injected into the prompt. It constrains the output, but the "
       "model does not automatically read your field descriptions from it.",
    kicker="BYTE FORENSICS · PROMPT INJECTION",
    title="THE PROMPT INJECTION BLINDSPOT",
    art="prompt_stream",
    art_caption="SCHEMA VS PROMPT",
    header_at="There is another trap",
    art_at="There is another trap",
    rows=[
        dict(rank="01", name="PROMPT", val="EMPTY", sub="NO AUTO INJECTION", cls="red",
             at="not injected into the prompt"),
        dict(rank="02", name="SCHEMA", val="LOGITS", sub="CONSTRAINS OUTPUT SHAPE", cls="cyan",
             at="constrains the output"),
        dict(rank="03", name="FIELD DESCRIPTIONS", val="UNREAD", sub="MODEL NEVER SEES THEM", cls="gold",
             at="model does not automatically read your field descriptions"),
    ],
    closing=dict(t="ORDINARY GRAMMARS DO NOT INJECT FIELD DESCRIPTIONS", c="gold",
                 at="read your field descriptions from it"),
    source="llama.cpp server api · response_format implementation")

# =====================================================================
# WINDOW 28 -- CHAIN. Tool Calling vs Plain Structure.
# =====================================================================
win("chain",
    vo="Tool calling is a documented exception. Describe the expected fields "
       "and their meaning in the messages as well. Otherwise, you can force "
       "the right shape without giving the model enough instructions to fill that shape usefully.",
    kicker="BYTE FORENSICS · PROMPT CONTRACT",
    title="TOOL CALLING VS PLAIN STRUCTURE",
    art="caveat",
    art_caption="MESSAGE SPECIFICATIONS",
    header_at="Tool calling is a documented exception",
    art_at="Tool calling is a documented exception",
    chain=[
        dict(t="01 TOOL CALL", s="DOCS INJECTED", at="Tool calling is a documented exception"),
        dict(t="02 MESSAGES", s="STATE FIELD MEANINGS", at="Describe the expected fields and their meaning"),
        dict(t="03 FILL SHAPE", s="USEFUL OUTPUT", at="giving the model enough instructions"),
    ],
    compare=[
        dict(cls="good", title="EXPLICIT MESSAGES",
             body="System messages define the semantics and source mapping for each field.",
             at="meaning in the messages as well"),
        dict(cls="hot", title="BLIND SHAPE FORCING",
             body="Enforcing an object syntax without giving guidance produces random values.",
             at="force the right shape without giving the model"),
    ],
    source="structured prompting · system instructions")

# =====================================================================
# WINDOW 29 -- BARS. A Documented Request.
# =====================================================================
win("bars",
    vo="The PowerShell example assumes a local server is already running and "
       "the model files are present. It sends a chat request with the schema "
       "inside the response format wrapper that the reviewed server source actually reads.",
    kicker="BYTE FORENSICS · API INTEGRATION",
    title="A DOCUMENTED REQUEST",
    art="laptop",
    art_caption="LOCAL SERVER CHAT API",
    header_at="The PowerShell example assumes",
    art_at="The PowerShell example assumes",
    scale=100.0,
    bars=[
        dict(lab="LOCAL SERVER", val="RUNNING", unit="HTTP", pct=100.0, cls="cyan",
             at="local server is already running"),
        dict(lab="MODEL GGUF", val="LOADED", unit="VRAM", pct=100.0, cls="gold",
             at="model files are present"),
        dict(lab="RESPONSE FORMAT", val="WRAPPER", unit="JSON", pct=100.0, cls="",
             at="schema inside the response format wrapper"),
    ],
    closing=dict(t="USE THE EXACT RESPONSE FORMAT WRAPPER EXPECTED BY THE SERVER", c="gold",
                 at="server source actually reads"),
    source="powershell client · llama.cpp server endpoint")

# =====================================================================
# WINDOW 30 -- RAIL. Explicit Paths in the Prompt.
# =====================================================================
win("rail",
    vo="The prompt specifies the same keys, allows null when evidence is "
       "missing, and marks the supplied order as data. This is a documentation "
       "checked request, not a recording of a successful local run.",
    kicker="BYTE FORENSICS · PROMPT HYGIENE",
    title="EXPLICIT PATHS IN THE PROMPT",
    art="checklist",
    art_caption="DATA VS INSTRUCTIONS",
    header_at="The prompt specifies the same keys",
    art_at="The prompt specifies the same keys",
    rails=[
        dict(lab="PROMPT KEYS", val="MATCHED", pct=100.0, cls="cyan",
             at="prompt specifies the same keys"),
        dict(lab="NULL ALLOWED", val="MISSING", pct=100.0, cls="gold",
             at="allows null when evidence is missing"),
        dict(lab="DATA BOUNDARY", val="ISOLATED", pct=100.0, cls="",
             at="marks the supplied order as data"),
    ],
    closing=dict(t="ALWAYS SEPARATE UNTRUSTED ORDER DATA FROM INSTRUCTIONS", c="gold",
                 at="documentation checked request"),
    source="prompt isolation · prompt injection defense")

# =====================================================================
# WINDOW 31 -- NOTE. Post-Generation Verification.
# =====================================================================
win("note",
    vo="After the response arrives, require a complete result. A token limit "
       "can leave a partial object. Parse it, validate it with the intended "
       "schema draft, and enable the format checks your validator supports "
       "when your contract uses them.",
    kicker="BYTE FORENSICS · POST PROCESSING",
    title="POST-GENERATION VERIFICATION",
    art="magnifier",
    art_caption="TRIPLE POST-CHECK",
    header_at="After the response arrives",
    art_at="After the response arrives",
    note_head="THREE STEPS AFTER RECEIVING RESPONSE",
    note_items=[
        dict(t="CHECK COMPLETION: VERIFY NO PREMATURE TOKEN TRUNCATION",
             at="token limit can leave a partial object"),
        dict(t="SYNTAX PARSE: INDEPENDENT PARSE OF THE RETURNED PAYLOAD",
             at="Parse it, validate it with the intended schema draft"),
        dict(t="FORMAT CHECKS: ENABLE EMAIL, URI, AND REGEX IN VALIDATOR",
             at="enable the format checks your validator supports"),
    ],
    tape="VERIFY COMPLETION BEFORE VALIDATING THE SCHEMA",
    tape_at="when your contract uses them",
    source="post-generation pipeline · independent validator")

# =====================================================================
# WINDOW 32 -- ROWS. Business Rule Verification.
# =====================================================================
win("rows",
    vo="Those checks are not universally automatic. Then apply business rules: "
       "the supplier must exist, the currency must match the order, and the "
       "total must agree with the source arithmetic. Put a mismatch into review.",
    kicker="BYTE FORENSICS · BUSINESS INVARIANTS",
    title="BUSINESS RULE VERIFICATION",
    art="checklist",
    art_caption="INVARIANT ENFORCEMENT",
    header_at="Those checks are not universally automatic",
    art_at="Those checks are not universally automatic",
    rows=[
        dict(rank="01", name="SUPPLIER EXISTS", val="DB LOOKUP", sub="MUST BE REGISTERED", cls="cyan",
             at="supplier must exist"),
        dict(rank="02", name="CURRENCY MATCH", val="PO MATCH", sub="AGREES WITH ORDER", cls="",
             at="currency must match the order"),
        dict(rank="03", name="SOURCE MATH", val="AUDITED", sub="SUM EQUALS ITEMS", cls="gold",
             at="total must agree with the source arithmetic"),
        dict(rank="04", name="MISMATCH ROUTE", val="REVIEW", sub="HALT AUTOMATION", cls="red",
             at="Put a mismatch into review"),
    ],
    closing=dict(t="ANY SOURCE ARITHMETIC MISMATCH HALTS AUTOMATION", c="red",
                 at="mismatch into review"),
    source="business rule engine · invoice invariants")

# =====================================================================
# WINDOW 33 -- CHAIN. Bounded Retries & Correction.
# =====================================================================
win("chain",
    vo="Keep retries bounded. Asking the same model to repair an uncertain "
       "amount does not create new evidence. A useful correction names a "
       "rejected field and the rule it violated; a missing fact still needs "
       "an unknown state or another source.",
    kicker="BYTE FORENSICS · RETRY LOGIC",
    title="BOUNDED RETRIES & CORRECTION",
    art="warning",
    art_caption="RETRY LOOP AUDIT",
    header_at="Keep retries bounded",
    art_at="Keep retries bounded",
    chain=[
        dict(t="01 ATTEMPT", s="BOUNDED TO 1 OR 2", at="Keep retries bounded"),
        dict(t="02 FEEDBACK", s="NAME SPECIFIC RULE", at="useful correction names a rejected field"),
        dict(t="03 UNKNOWN", s="FALLBACK TO SOURCE", at="missing fact still needs an unknown state"),
    ],
    compare=[
        dict(cls="good", title="TARGETED REPAIR",
             body="Names the exact rejected field and rule to allow schema correction.",
             at="rule it violated"),
        dict(cls="hot", title="BLIND RE-PROMPT",
             body="Repeatedly asking the model to fix numbers generates hallucinations.",
             at="does not create new evidence"),
    ],
    source="retry policy · error recovery architecture")

# =====================================================================
# WINDOW 34 -- BARS. Managing Uncertainty.
# =====================================================================
win("bars",
    vo="Store the original input beside the proposed record so a reviewer can "
       "see why the application stopped. The contract should make uncertainty "
       "manageable, rather than making uncertainty disappear from the interface.",
    kicker="BYTE FORENSICS · AUDIT TRAIL",
    title="MANAGING UNCERTAINTY",
    art="folder",
    art_caption="ORIGINAL VS PROPOSED",
    header_at="Store the original input beside",
    art_at="Store the original input beside",
    scale=100.0,
    bars=[
        dict(lab="ORIGINAL INPUT", val="SAVED", unit="LOG", pct=100.0, cls="cyan",
             at="Store the original input"),
        dict(lab="PROPOSED RECORD", val="STAGED", unit="DIFF", pct=100.0, cls="gold",
             at="beside the proposed record"),
        dict(lab="HUMAN REVIEW", val="ALIGNED", unit="AUDIT", pct=100.0, cls="",
             at="see why the application stopped"),
    ],
    closing=dict(t="CONTRACTS MUST MAKE UNCERTAINTY AUDITABLE, NOT INVISIBLE", c="gold",
                 at="disappear from the interface"),
    source="audit trail architecture · compliance logging")

# =====================================================================
# WINDOW 35 -- RAIL. Sizing Qwen 2.5 7B.
# =====================================================================
win("rail",
    vo="For a concrete memory budget, use Qwen two point five seven billion "
       "Instruct in its official four bit mixed GGUF artifact. Its two shards "
       "total about four point six eight gigabytes, or four point three six gibibytes.",
    kicker="BYTE FORENSICS · HARDWARE BUDGET",
    title="SIZING QWEN 2.5 7B",
    art="gguf_blocks",
    art_caption="Q4_K_M GGUF SHARDS",
    header_at="For a concrete memory budget",
    art_at="For a concrete memory budget",
    rails=[
        dict(lab="SHARDS", val="2 FILES", pct=50.0, cls="",
             at="Its two shards total"),
        dict(lab="FILE PAYLOAD", val="4.68 GB", pct=100.0, cls="gold",
             at="four point six eight gigabytes"),
        dict(lab="IN GIBIBYTES", val="4.36 GiB", pct=93.1, cls="cyan",
             at="four point three six gibibytes"),
    ],
    closing=dict(t="PUBLISHED WEIGHT PAYLOAD IS 4.36 GIBIBYTES", c="gold",
                 at="four point three six gibibytes"),
    source="qwen2.5-7b-instruct · official q4_k_m gguf")

# =====================================================================
# WINDOW 36 -- NOTE. Weights vs Graphics Allocation.
# =====================================================================
win("note",
    vo="Both files are needed. That is a published file payload, not a "
       "measured graphics allocation. We have not established this model's "
       "accuracy on your contract. It gives us a named architecture for honest capacity arithmetic.",
    kicker="BYTE FORENSICS · CAPACITY REALITY",
    title="WEIGHTS VS GRAPHICS ALLOCATION",
    art="superchip",
    art_caption="VRAM OVERHEADS",
    header_at="Both files are needed",
    art_at="Both files are needed",
    note_head="CAPACITY ARITHMETIC RULES",
    note_items=[
        dict(t="FILE SIZE ON DISK IS NOT YOUR FINAL VRAM CONSUMPTION",
             at="published file payload, not a measured graphics allocation"),
        dict(t="MODEL CONTRACT ACCURACY MUST BE EMPIRICALLY BENCHMARKED",
             at="established this model's accuracy on your contract"),
        dict(t="USE KNOWN ARCHITECTURE PARAMETERS FOR HONEST PLANNING",
             at="named architecture for honest capacity arithmetic"),
    ],
    tape="FILE SIZE IS NEVER TOTAL VRAM ALLOCATION",
    tape_at="honest capacity arithmetic",
    source="gpu memory management · allocation overheads")

# =====================================================================
# WINDOW 37 -- ROWS. Architecture Parameters.
# =====================================================================
win("rows",
    vo="Its configuration has twenty-eight layers, four key value heads, and "
       "a head dimension of one hundred and twenty-eight. Count both keys and "
       "values. At sixteen bits per element, that gives fifty-six kibibytes per cached position.",
    kicker="BYTE FORENSICS · CACHE MATH",
    title="ARCHITECTURE PARAMETERS",
    art="die",
    art_caption="QWEN 7B ARCHITECTURE",
    header_at="Its configuration has twenty-eight layers",
    art_at="Its configuration has twenty-eight layers",
    rows=[
        dict(rank="01", name="LAYERS", val="28", sub="TRANSFORMER BLOCKS", cls="cyan",
             at="twenty-eight layers"),
        dict(rank="02", name="KV HEADS", val="4", sub="GQA ATTENTION HEADS", cls="",
             at="four key value heads"),
        dict(rank="03", name="HEAD DIM", val="128", sub="CHANNELS PER HEAD", cls="gold",
             at="head dimension of one hundred and twenty-eight"),
        dict(rank="04", name="PER TOKEN", val="56 KiB", sub="16-BIT KV CACHE", cls="gold",
             at="fifty-six kibibytes per cached position"),
    ],
    closing=dict(t="EACH CACHED TOKEN OCCUPIES 56 KIBIBYTES AT FP16", c="gold",
                 at="fifty-six kibibytes"),
    source="qwen 2.5 7b config · gqa kv cache arithmetic")

# =====================================================================
# WINDOW 38 -- CHAIN. Context KV Cache Scaling.
# =====================================================================
win("chain",
    vo="Eight thousand one hundred and ninety-two positions require zero "
       "point four three seven five gibibytes of ideal cache payload. "
       "Thirty-two thousand seven hundred and sixty-eight positions require "
       "one point seven five gibibytes. Context costs memory even when the answer is tiny.",
    kicker="BYTE FORENSICS · CONTEXT SCALING",
    title="CONTEXT KV CACHE SCALING",
    art="kv_cache",
    art_caption="8K VS 32K CONTEXT",
    header_at="Eight thousand one hundred and ninety-two",
    art_at="Eight thousand one hundred and ninety-two",
    chain=[
        dict(t="01 8K CTX", s="0.4375 GiB CACHE", at="zero point four three seven five gibibytes"),
        dict(t="02 32K CTX", s="1.7500 GiB CACHE", at="one point seven five gibibytes"),
        dict(t="03 SCALING", s="LINEAR 4x GROWTH", at="Context costs memory even when"),
    ],
    compare=[
        dict(cls="good", title="8K CONTEXT",
             body="Ideal FP16 cache footprint is under 0.5 GiB for short prompts.",
             at="positions require zero point four"),
        dict(cls="hot", title="32K CONTEXT",
             body="Long document prompts consume 1.75 GiB before model execution buffers.",
             at="Thirty-two thousand seven hundred"),
    ],
    source="kv cache sizing formula · linear context expansion")

# =====================================================================
# WINDOW 39 -- BARS. Quantized Cache: Q8_0 Blocks.
# =====================================================================
win("bars",
    vo="Eight bit cache is not exactly half. The reviewed Q eight zero block "
       "stores thirty-two quantized values plus a two byte scale, giving "
       "thirty-four bytes per block. Here, eight thousand one hundred and "
       "ninety-two positions become about zero point two three two gibibytes.",
    kicker="BYTE FORENSICS · QUANTIZED CACHE",
    title="QUANTIZED CACHE: Q8_0 BLOCKS",
    art="cache_grid",
    art_caption="Q8_0 QUANTIZATION BLOCK",
    header_at="Eight bit cache is not exactly half",
    art_at="Eight bit cache is not exactly half",
    scale=34.0,
    bars=[
        dict(lab="VALUES", val="32", unit="BYTE", pct=94.1, cls="cyan",
             at="stores thirty-two quantized values"),
        dict(lab="SCALE", val="2", unit="BYTE", pct=5.9, cls="gold",
             at="two byte scale"),
        dict(lab="TOTAL BLOCK", val="34", unit="BYTE", pct=100.0, cls="gold",
             at="thirty-four bytes per block"),
        dict(lab="8K CACHE", val="0.23", unit="GiB", pct=50.0, cls="",
             at="zero point two three two gibibytes"),
    ],
    closing=dict(t="Q8_0 BLOCK STORES 32 VALUES PLUS 2 SCALE BYTES (34 BYTES)", c="gold",
                 at="thirty-four bytes per block"),
    source="llama.cpp k-quants · q8_0 memory format")

# =====================================================================
# WINDOW 40 -- RAIL. Cache Footprint vs Context.
# =====================================================================
win("rail",
    vo="At thirty-two thousand seven hundred and sixty-eight, about zero point "
       "nine three zero. These are calculated payloads. Padding, temporary "
       "buffers, and the runtime's allocation strategy remain outside the equation.",
    kicker="BYTE FORENSICS · BUFFER OVERHEADS",
    title="CACHE FOOTPRINT VS CONTEXT",
    art="memory_bank",
    art_caption="RUN-TIME BUFFERS",
    header_at="At thirty-two thousand seven hundred",
    art_at="At thirty-two thousand seven hundred",
    rails=[
        dict(lab="32K Q8 CACHE", val="0.930 GiB", pct=93.0, cls="gold",
             at="about zero point nine three zero"),
        dict(lab="PADDING & BUFFERS", val="EXTRA", pct=50.0, cls="red",
             at="Padding, temporary buffers"),
        dict(lab="RUNTIME STRATEGY", val="ALLOC", pct=70.0, cls="",
             at="allocation strategy remain outside"),
    ],
    closing=dict(t="CALCULATED PAYLOADS DO NOT INCLUDE RUNTIME SCRATCH BUFFERS", c="red",
                 at="outside the equation"),
    source="memory management · runtime allocation strategies")

# =====================================================================
# WINDOW 41 -- NOTE. A Realistic Planning Example.
# =====================================================================
win("note",
    vo="Here is a planning example, not a fit test. Add that short eight bit "
       "cache to the file payload, then assume one point five gibibytes for "
       "everything else. The total is about six point zero nine gibibytes.",
    kicker="BYTE FORENSICS · TOTAL FOOTPRINT",
    title="A REALISTIC PLANNING EXAMPLE",
    art="vram_module",
    art_caption="6.09 GiB PLANNING TOTAL",
    header_at="Here is a planning example",
    art_at="Here is a planning example",
    note_head="QWEN 7B VRAM STACK",
    note_items=[
        dict(t="MODEL WEIGHTS (Q4_K_M GGUF): 4.36 GiB",
             at="short eight bit cache to the file payload"),
        dict(t="KV CACHE (8K Q8_0): 0.23 GiB",
             at="short eight bit cache"),
        dict(t="CUDA CONTEXT & COMPUTE BUFFERS RESERVE: 1.50 GiB",
             at="assume one point five gibibytes for everything else"),
    ],
    tape="TOTAL BUDGET: 6.09 GIBIBYTES VRAM",
    tape_at="total is about six point zero nine gibibytes",
    source="budget calculation · 4.36 + 0.23 + 1.50 = 6.09 gib")

# =====================================================================
# WINDOW 42 -- ROWS. Sizing for 8GB GPUs.
# =====================================================================
win("rows",
    vo="That reserve is an assumption. On an eight gigabyte class card, begin "
       "with one slot and modest context, then inspect real allocation and "
       "leave room for the display. A schema cannot rescue a budget that was only a file size.",
    kicker="BYTE FORENSICS · 8GB HARDWARE TIER",
    title="SIZING FOR 8GB GPUS",
    art="dual_slot",
    art_caption="8GB VRAM MARGIN",
    header_at="That reserve is an assumption",
    art_at="That reserve is an assumption",
    rows=[
        dict(rank="01", name="CARD CAPACITY", val="8.0 GB", sub="TOTAL PHYSICAL VRAM", cls="gold",
             at="eight gigabyte class card"),
        dict(rank="02", name="SERVER SLOTS", val="1 SLOT", sub="CONCURRENCY CEILING", cls="cyan",
             at="begin with one slot"),
        dict(rank="03", name="CONTEXT LEN", val="MODEST", sub="AVOID CACHE SPILL", cls="",
             at="modest context"),
        dict(rank="04", name="DISPLAY HEAD", val="RESERVE", sub="OS DESKTOP BUFFER", cls="red",
             at="leave room for the display"),
    ],
    closing=dict(t="SCHEMAS CANNOT RESCUE AN UNDERSIZED VRAM BUDGET", c="red",
                 at="budget that was only a file size"),
    source="rtx 4060 / 3070 8gb sizing guidelines")

# =====================================================================
# WINDOW 43 -- CHAIN. 12GB to 24GB Scaling.
# =====================================================================
win("chain",
    vo="Twelve gigabyte and sixteen gigabyte classes give this same example "
       "more planning room. Spend it on context or additional work after "
       "checking the real buffers. At twenty-four gigabytes, concurrency "
       "becomes a candidate to measure, not a free multiplication of throughput.",
    kicker="BYTE FORENSICS · WORKSTATION TIERS",
    title="12GB TO 24GB SCALING",
    art="motherboard",
    art_caption="MULTI-TIER EXPANSION",
    header_at="Twelve gigabyte and sixteen gigabyte",
    art_at="Twelve gigabyte and sixteen gigabyte",
    chain=[
        dict(t="01 12-16GB", s="COMFORTABLE BUFFERS", at="Twelve gigabyte and sixteen"),
        dict(t="02 24GB", s="CONCURRENCY TESTING", at="twenty-four gigabytes"),
        dict(t="03 METRIC", s="MEASURE REAL THROUGHPUT", at="candidate to measure"),
    ],
    compare=[
        dict(cls="good", title="16GB CARDS",
             body="Room for longer context windows and larger execution batch sizes.",
             at="Spend it on context or additional work"),
        dict(cls="hot", title="24GB SLOTS",
             body="Parallel slots scale memory linearly; throughput gains must be measured.",
             at="not a free multiplication of throughput"),
    ],
    source="hardware tiers · rtx 4070ti / 4080 / 4090 capacity")

# =====================================================================
# WINDOW 44 -- BARS. Apple Silicon Unified Memory.
# =====================================================================
win("bars",
    vo="Active workflows still need their applicable cache and execution "
       "resources. On a Mac with sixty-four or one hundred and twenty-eight "
       "gigabytes of unified memory, the operating system and other applications share that total.",
    kicker="BYTE FORENSICS · UNIFIED MEMORY",
    title="APPLE SILICON UNIFIED MEMORY",
    art="mac_mini",
    art_caption="SHARED UNIFIED POOL",
    header_at="Active workflows still need their",
    art_at="Active workflows still need their",
    scale=128.0,
    bars=[
        dict(lab="MAC 64GB", val="64", unit="GB", pct=50.0, cls="cyan",
             at="Mac with sixty-four"),
        dict(lab="MAC 128GB", val="128", unit="GB", pct=100.0, cls="gold",
             at="one hundred and twenty-eight"),
        dict(lab="SHARED POOL", val="OS", unit="APP", pct=35.0, cls="red",
             at="operating system and other applications share"),
    ],
    closing=dict(t="UNIFIED MEMORY IS SHARED WITH OS AND ALL RUNNING APPS", c="gold",
                 at="share that total"),
    source="apple silicon unified memory architecture")

# =====================================================================
# WINDOW 45 -- RAIL. Runtime Server Flags.
# =====================================================================
win("rail",
    vo="The flags change different things. GPU layers controls where eligible "
       "model layers are stored. Context size controls configured capacity; "
       "parallel controls server slots. Cache type flags choose key and value representations.",
    kicker="BYTE FORENSICS · SERVER CONFIGURATION",
    title="RUNTIME SERVER FLAGS",
    art="router",
    art_caption="LLAMA-SERVER FLAGS",
    header_at="The flags change different things",
    art_at="The flags change different things",
    rails=[
        dict(lab="-ngl (GPU LAYERS)", val="OFFLOAD", pct=100.0, cls="gold",
             at="GPU layers controls where eligible"),
        dict(lab="-c (CONTEXT SIZE)", val="CAPACITY", pct=75.0, cls="cyan",
             at="Context size controls configured capacity"),
        dict(lab="-np (PARALLEL)", val="SLOTS", pct=50.0, cls="",
             at="parallel controls server slots"),
        dict(lab="-ctk / -ctv", val="CACHE TYPE", pct=80.0, cls="gold",
             at="Cache type flags choose key and value"),
    ],
    closing=dict(t="EACH FLAG CONTROLS A SPECIFIC HARDWARE RESOURCE", c="gold",
                 at="key and value representations"),
    source="llama.cpp server cli options documentation")

# =====================================================================
# WINDOW 46 -- NOTE. Flags vs Factual Correctness.
# =====================================================================
win("note",
    vo="Flash Attention selects an attention execution path when supported. "
       "None makes a supplier identifier correct. Keep one slot for the "
       "initial contract check, inspect startup allocation, and expand after "
       "the complete workflow behaves as intended.",
    kicker="BYTE FORENSICS · RUNTIME DISCIPLINE",
    title="FLAGS VS FACTUAL CORRECTNESS",
    art="warning",
    art_caption="FACTUAL INTEGRITY",
    header_at="Flash Attention selects an attention",
    art_at="Flash Attention selects an attention",
    note_head="CRITICAL RUNTIME TRUTHS",
    note_items=[
        dict(t="FLASH ATTENTION OPTIMIZES SPEED AND MEMORY BANDWIDTH",
             at="Flash Attention selects an attention execution path"),
        dict(t="NO RUNTIME FLAG MAKES EXTRACTED VALUES FACTUALLY CORRECT",
             at="None makes a supplier identifier correct"),
        dict(t="VERIFY SINGLE-SLOT WORKFLOW INTEGRITY BEFORE EXPANDING",
             at="Keep one slot for the initial contract check"),
    ],
    tape="NO ENGINE FLAG GUARANTEES FACTUAL ACCURACY",
    tape_at="complete workflow behaves as intended",
    source="production deployment rules · runtime validation")

# =====================================================================
# WINDOW 47 -- ROWS. Energy Math: The Power Scenario.
# =====================================================================
win("rows",
    vo="For energy, suppose, purely hypothetically, a generation draws one "
       "hundred and eighty watts for thirty seconds. That is one point five "
       "watt hours. Repeating it doubles that to three.",
    kicker="BYTE FORENSICS · ENERGY FORENSICS",
    title="THE ENERGY SCENARIO",
    art="power_rails",
    art_caption="WATT-HOUR CONSUMPTION",
    header_at="For energy, suppose, purely hypothetically",
    art_at="For energy, suppose, purely hypothetically",
    rows=[
        dict(rank="01", name="POWER DRAW", val="180 W", sub="GPU + SYSTEM DRAW", cls="gold",
             at="draws one hundred and eighty watts"),
        dict(rank="02", name="RUNTIME", val="30 SEC", sub="DURATION PER INVOICE", cls="",
             at="thirty seconds"),
        dict(rank="03", name="PASS 1 ENERGY", val="1.5 Wh", sub="INITIAL ATTEMPT", cls="cyan",
             at="one point five watt hours"),
        dict(rank="04", name="RETRY PASS 2", val="3.0 Wh", sub="DOUBLED POWER COST", cls="red",
             at="Repeating it doubles that to three"),
    ],
    closing=dict(t="EVERY RETRY LOOP EXACTLY DOUBLES INVOICE ENERGY", c="red",
                 at="doubles that to three"),
    source="power calculations · joules = watts * seconds")

# =====================================================================
# WINDOW 48 -- CHAIN. Energy Per Correct Record.
# =====================================================================
win("chain",
    vo="If the first attempt produced three hundred output tokens, the "
       "generation-only figure would be five milliwatt hours per token. "
       "These are invented inputs, not readings from this model. "
       "Fewer parsing errors alone cannot tell us the energy per correct accepted record.",
    kicker="BYTE FORENSICS · METRIC RIGOR",
    title="ENERGY PER CORRECT RECORD",
    art="meter",
    art_caption="MILLIWATT-HOURS / TOKEN",
    header_at="If the first attempt produced three hundred",
    art_at="If the first attempt produced three hundred",
    chain=[
        dict(t="01 TOKENS", s="300 OUTPUT TOKENS", at="three hundred output tokens"),
        dict(t="02 RATE", s="5 mWh PER TOKEN", at="five milliwatt hours per token"),
        dict(t="03 GOAL", s="ENERGY / VALID FACT", at="energy per correct accepted record"),
    ],
    compare=[
        dict(cls="good", title="ENERGY PER CORRECT RECORD",
             body="Total energy divided by successfully verified, correct database entries.",
             at="energy per correct accepted record"),
        dict(cls="hot", title="ENERGY PER RAW TOKEN",
             body="Ignores whether tokens formed a valid or completely hallucinated invoice.",
             at="invented inputs, not readings"),
    ],
    source="energy efficiency metrics · useful work analysis")

# =====================================================================
# WINDOW 49 -- BARS. Creating Adversarial Test Orders.
# =====================================================================
win("bars",
    vo="Before trusting the automation, create orders whose correct outputs "
       "you can verify. Include a missing amount, an unknown supplier, a "
       "currency mismatch, and a plausible but incorrect total.",
    kicker="BYTE FORENSICS · VERIFICATION SUITE",
    title="CREATING ADVERSARIAL ORDERS",
    art="checklist",
    art_caption="EDGE-CASE TEST CASES",
    header_at="Before trusting the automation",
    art_at="Before trusting the automation",
    scale=100.0,
    bars=[
        dict(lab="MISSING AMOUNT", val="NULL", unit="TEST", pct=100.0, cls="cyan",
             at="Include a missing amount"),
        dict(lab="UNKNOWN SUPPLIER", val="FAIL", unit="TEST", pct=100.0, cls="red",
             at="unknown supplier"),
        dict(lab="CURRENCY MISMATCH", val="HALT", unit="TEST", pct=100.0, cls="gold",
             at="currency mismatch"),
        dict(lab="PLAUSIBLE TOTAL", val="AUDIT", unit="TEST", pct=100.0, cls="",
             at="plausible but incorrect total"),
    ],
    closing=dict(t="TEST HARNESS MUST EXERCISE ALL BUSINESS ERROR PATHS", c="gold",
                 at="incorrect total"),
    source="software testing · adversarial validation suites")

# =====================================================================
# WINDOW 50 -- RAIL. The Triaged Metric Dashboard.
# =====================================================================
win("rail",
    vo="Include a response that stops halfway through. Measure correct "
       "records accepted, incorrect records that slip through, and cases "
       "correctly sent to review. Keep parsing success on the dashboard, but "
       "give it the limited meaning it deserves.",
    kicker="BYTE FORENSICS · DASHBOARD METRICS",
    title="THE TRIAGED DASHBOARD",
    art="magnifier",
    art_caption="FOUR CORE METRICS",
    header_at="Include a response that stops",
    art_at="Include a response that stops",
    rails=[
        dict(lab="CORRECT ACCEPTED", val="PRIMARY", pct=100.0, cls="gold",
             at="Measure correct records accepted"),
        dict(lab="INCORRECT SLIPPED", val="ZERO", pct=0.0, cls="red",
             at="incorrect records that slip through"),
        dict(lab="SENT TO REVIEW", val="EXPECTED", pct=60.0, cls="cyan",
             at="cases correctly sent to review"),
        dict(lab="PARSING SUCCESS", val="SYNTAX", pct=100.0, cls="",
             at="Keep parsing success on the dashboard"),
    ],
    closing=dict(t="PARSING SUCCESS IS MERELY STEP ZERO OF VERIFICATION", c="gold",
                 at="limited meaning it deserves"),
    source="production telemetry · accuracy dashboards")

# =====================================================================
# WINDOW 51 -- NOTE. Controlled A/B Comparisons.
# =====================================================================
win("note",
    vo="Compare constrained and unconstrained generation with the same model, "
       "inputs, and acceptance rules. Record the runtime revision and schema "
       "version. More valid objects is one result.",
    kicker="BYTE FORENSICS · A/B TESTING",
    title="CONTROLLED A/B COMPARISONS",
    art="scales",
    art_caption="A/B TEST DISCIPLINE",
    header_at="Compare constrained and unconstrained",
    art_at="Compare constrained and unconstrained",
    note_head="CONTROLLED TEST PROTOCOL",
    note_items=[
        dict(t="KEEP MODEL, WEIGHTS, AND SYSTEM PROMPTS IDENTICAL",
             at="same model, inputs, and acceptance rules"),
        dict(t="PIN AND RECORD EXACT RUNTIME COMMIT AND SCHEMA VERSION",
             at="Record the runtime revision and schema version"),
        dict(t="SEPARATE RAW VALID OBJECTS FROM CORRECT BUSINESS ACTIONS",
             at="More valid objects is one result"),
    ],
    tape="ISOLATE THE GRAMMAR IMPACT UNDER IDENTICAL PROMPTS",
    tape_at="schema version",
    source="scientific methodology · controlled benchmarking")

# =====================================================================
# WINDOW 52 -- ROWS. Local Evidence Integrity.
# =====================================================================
win("rows",
    vo="More correct accepted records is another. Switching models or review "
       "policy between runs changes the question. Your local evidence should "
       "describe the workflow you intend to use, including the cases where it is supposed to stop.",
    kicker="BYTE FORENSICS · AUDIT PROTOCOL",
    title="LOCAL EVIDENCE INTEGRITY",
    art="caveat",
    art_caption="PRODUCTION WORKFLOW",
    header_at="More correct accepted records is another",
    art_at="More correct accepted records is another",
    rows=[
        dict(rank="01", name="CORRECT RECORDS", val="TARGET", sub="REAL PRODUCTIVITY", cls="gold",
             at="More correct accepted records"),
        dict(rank="02", name="MODEL DRIFT", val="INVALID", sub="CHANGES THE QUESTION", cls="red",
             at="Switching models or review policy"),
        dict(rank="03", name="INTENDED FLOW", val="AUDITED", sub="REPRESENTS REAL WORK", cls="cyan",
             at="workflow you intend to use"),
        dict(rank="04", name="STOP CONDITIONS", val="MANDATORY", sub="MUST HALT SAFELY", cls="gold",
             at="cases where it is supposed to stop"),
    ],
    closing=dict(t="EVALUATE WHERE THE SYSTEM IS SUPPOSED TO HALT", c="gold",
                 at="supposed to stop"),
    source="workflow certification · stop-state verification")

# =====================================================================
# WINDOW 53 -- CHAIN. The Three-Stage Architecture.
# =====================================================================
win("chain",
    vo="Use the grammar to keep the model inside an output contract. "
       "Use a validator to check that contract independently. "
       "Use source comparisons and business rules to decide whether the proposed values deserve action.",
    kicker="BYTE FORENSICS · FINAL ARCHITECTURE",
    title="THE THREE-STAGE ARCHITECTURE",
    art="pipeline",
    art_caption="THREE-STAGE DEFENSE",
    header_at="Use the grammar to keep the model",
    art_at="Use the grammar to keep the model",
    chain=[
        dict(t="01 GRAMMAR", s="CONSTRAIN OUTPUT SHAPE", at="grammar to keep the model inside"),
        dict(t="02 VALIDATOR", s="INDEPENDENT SCHEMA CHECK", at="validator to check that contract"),
        dict(t="03 BUSINESS", s="VERIFY SOURCE FACTS", at="source comparisons and business rules"),
    ],
    compare=[
        dict(cls="good", title="DEFENSIVE ARCHITECTURE",
             body="Combines grammar logit masking, validator rules, and business logic.",
             at="decide whether the proposed values"),
        dict(cls="hot", title="NAIVE TRUST",
             body="Treating a valid JSON closing bracket as proof of factual truth.",
             at="output contract"),
    ],
    source="production defense · defense-in-depth pipeline")

# =====================================================================
# WINDOW 54 -- BARS. The Investigation Protocol.
# =====================================================================
win("bars",
    vo="Structured outputs make those stages easier to connect. "
       "The closing bracket is the end of the object. "
       "It is not the end of the investigation.",
    kicker="BYTE FORENSICS · VERIFICATION PRINCIPLE",
    title="THE CLOSING BRACKET TRUTH",
    art="warning",
    art_caption="END OF OBJECT != TRUTH",
    header_at="Structured outputs make those stages",
    art_at="Structured outputs make those stages",
    scale=100.0,
    bars=[
        dict(lab="OBJECT PARSE", val="100", unit="PCT", pct=100.0, cls="cyan",
             at="closing bracket is the end"),
        dict(lab="FACT AUDIT", val="BEGIN", unit="STAGE", pct=100.0, cls="gold",
             at="end of the investigation"),
    ],
    closing=dict(t="THE CLOSING BRACKET IS NOT THE END OF THE INVESTIGATION", c="gold",
                 at="end of the investigation"),
    source="verification engineering · closing principle")

# =====================================================================
# WINDOW 55 -- RAIL. Subscribe to Byte Forensics.
# =====================================================================
win("rail",
    vo="If this saved you a broken automation and a weekend of debugging, "
       "subscribe. Byte Forensics breaks down local AI hardware and runtime "
       "behavior with real numbers. No hype. See you in the next breakdown.",
    kicker="BYTE FORENSICS · ENGINEERING TRUTH",
    title="NO HYPE. REAL NUMBERS.",
    art="tok_speed_dial",
    art_caption="BYTE FORENSICS",
    header_at="If this saved you a broken automation",
    art_at="If this saved you a broken automation",
    rails=[
        dict(lab="DEBUGGING HOURS", val="SAVED", pct=100.0, cls="cyan",
             at="weekend of debugging"),
        dict(lab="BYTE FORENSICS", val="NUMBERS", pct=100.0, cls="gold",
             at="breaks down local AI hardware"),
        dict(lab="CHANNEL HYPE", val="ZERO", pct=0.0, cls="red",
             at="No hype"),
    ],
    closing=dict(t="SUBSCRIBE FOR HARDWARE FORENSICS AND REAL NUMBERS", c="gold",
                 at="See you in the next breakdown"),
    source="byte forensics · hardware & runtime diagnostics")
