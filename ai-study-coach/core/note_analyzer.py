import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):

    doc = nlp(text)

    keywords = []

    weak_words = [
    "process", "thing", "things", "way", "ways", "time", "times",
    "person", "people", "part", "parts", "type", "types",
    "kind", "kinds", "form", "forms", "system", "systems",
    "method", "methods", "area", "areas", "group", "groups",
    "example", "examples", "fact", "facts", "information",
    "idea", "ideas", "problem", "problems", "result", "results",
    "change", "changes", "effect", "effects", "use", "uses",
    "work", "works", "life", "case", "cases", "level", "levels",
    "point", "points", "term", "terms", "subject", "subjects",
    "topic", "topics", "class", "classes", "study", "studies",

    "object", "objects", "item", "items", "element", "elements",
    "feature", "features", "function", "functions", "structure",
    "structures", "activity", "activities", "action", "actions",
    "event", "events", "factor", "factors", "condition",
    "conditions", "property", "properties", "relationship",
    "relationships", "resource", "resources", "material",
    "materials", "source", "sources", "operation", "operations",

    "number", "numbers", "value", "values", "amount", "amounts",
    "size", "sizes", "length", "lengths", "width", "widths",
    "height", "heights", "rate", "rates", "measure", "measures",

    "data", "detail", "details", "evidence", "knowledge",
    "concept", "concepts", "meaning", "meanings", "definition",
    "definitions", "description", "descriptions",

    "step", "steps", "stage", "stages", "phase", "phases",
    "period", "periods", "year", "years", "month", "months",
    "week", "weeks", "day", "days", "hour", "hours",

    "person", "persons", "human", "humans", "individual",
    "individuals", "member", "members", "student", "students",
    "teacher", "teachers", "user", "users",

    "plant", "plants", "animal", "animals", "organism",
    "organisms", "species", "environment", "nature",

    "energy", "light", "sunlight", "water", "air", "heat",
    "sound", "gas", "matter",

    "computer", "computers", "machine", "machines", "device",
    "devices", "tool", "tools", "program", "programs",
    "software", "application", "applications", "file", "files",
    "folder", "folders", "network", "networks",

    "code", "coding", "technology", "technologies",
    "development", "developer", "developers",

    "question", "questions", "answer", "answers",
    "exercise", "exercises", "lesson", "lessons",

    "article", "articles", "book", "books", "chapter",
    "chapters", "section", "sections", "page", "pages"    
    
    ]

    for token in doc:

        if token.pos_== "NOUN" and not token.is_stop:

            word = token.text.lower()

            if word not in weak_words:
                
                if word not in keywords:

                 keywords.append(word)

    return keywords


def extract_nouns(text):

    doc = nlp(text)

    nouns = []

    for token in doc:

        if token.pos_== "NOUN":

            word = token.text.lower()

            if word not in nouns:
                nouns.append(word)

    return nouns

def extract_phrases(text):

    doc = nlp(text)

    phrases = []

    for chunk in doc.noun_chunks:

        phrase = chunk.text.lower()

        if phrase not in phrases:

            phrases.append(phrase)

    return phrases


def filter_keywords(keywords):

    weak_words = [
 "a", "an", "the",

    "thing", "things",
    "item", "items",
    "object", "objects",
    "part", "parts",
    "piece", "pieces",
    "element", "elements",

    "process", "processes",
    "system", "systems",
    "method", "methods",
    "approach", "approaches",
    "procedure", "procedures",

    "plant", "plants",
    "animal", "animals",
    "person", "people",
    "human", "humans",

    "energy",
    "light",
    "sunlight",
    "water",
    "air",
    "gas",
    "heat",

    "data",
    "information",
    "fact",
    "facts",
    "detail",
    "details",

    "computer",
    "computers",
    "machine",
    "machines",
    "device",
    "devices",
    "tool",
    "tools",

    "program",
    "programs",
    "software",
    "application",
    "applications",

    "file",
    "files",
    "folder",
    "folders",

    "code",
    "coding",

    "example",
    "examples",

    "type",
    "types",
    "kind",
    "kinds",

    "group",
    "groups",
    "set",
    "sets",

    "way",
    "ways",

    "result",
    "results",

    "change",
    "changes",

    "effect",
    "effects",

    "area",
    "areas",

    "level",
    "levels",

    "form",
    "forms",

    "use",
    "uses",

    "value",
    "values",

    "point",
    "points",

    "number",
    "numbers",

    "case",
    "cases",

    "term",
    "terms",

    "topic",
    "topics",

    "subject",
    "subjects",

    "field",
    "fields",

    "step",
    "steps",

    "stage",
    "stages",

    "structure",
    "structures",

    "function",
    "functions",

    "feature",
    "features",

    "operation",
    "operations",

    "resource",
    "resources",

    "material",
    "materials",

    "source",
    "sources",

    "factor",
    "factors",

    "property",
    "properties",

    "condition",
    "conditions",

    "relationship",
    "relationships",

    "activity",
    "activities",

    "action",
    "actions",

    "event",
    "events",

    "growth",
    "development",

    "time",
    "year",
    "years",
    "day",
    "days",

    "problem",
    "problems",

    "solution",
    "solutions"
    ]

    filtered = []

    for word in keywords:

        if word.lower() not in weak_words:

            filtered.append(word)

    return filtered