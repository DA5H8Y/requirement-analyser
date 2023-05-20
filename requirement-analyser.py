import spacy
from spacy.matcher import DependencyMatcher

pattern = [
    {
        "RIGHT_ID": "anchor",
        "RIGHT_ATTRS": {"TEXT": {"IN": ["shall", "should", "may", "will"]}}
    }
    ,
    {
        "LEFT_ID": "anchor",
        "REL_OP": ".",
        "RIGHT_ID": "reqVerb",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "reqVerb",
        "REL_OP": ">",
        "RIGHT_ID": "nsubj_id",
        "RIGHT_ATTRS": {"DEP": "nsubj"}
    },
    {
        "LEFT_ID": "reqVerb",
        "REL_OP": ">",
        "RIGHT_ID": "dobj_id",
        "RIGHT_ATTRS": {"DEP": "dobj"}
    },
    {
        "LEFT_ID": "nsubj_id",
        "REL_OP": ">",
        "RIGHT_ID": "nsubj_compound_id",
        "RIGHT_ATTRS": {"DEP": "compound"}
    },
    {
        "LEFT_ID": "dobj_id",
        "REL_OP": ">",
        "RIGHT_ID": "dobj_compound_id",
        "RIGHT_ATTRS": {"DEP": "compound"}
    },
]

nlp = spacy.load("en_core_web_sm")
matcher = DependencyMatcher(nlp.vocab)
matcher.add("aux_verb_compound", [pattern])

# Example sentence
sentence = "The Control System shall prevent engine overspeed."

doc = nlp(sentence)

from spacy import displacy

#displacy.serve(doc, style="ent", auto_select_port=True)

matches = matcher(doc)

for match_id, token_ids in matches:
    for i in range(len(token_ids)):
        print(pattern[i]["RIGHT_ID"] + ":", doc[token_ids[i]].text)