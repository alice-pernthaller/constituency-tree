import Node
import pretty_print
import spacy
import benepar


def get_parse_tree_string(doc):
    parse_tree_string = []
    for sent in doc.sents:
        parse_tree_string.append(sent._.parse_string.replace(" (", "("))
    return parse_tree_string


text = 'Pep wanted to know how much money Paul needed'
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('benepar', config={'model': 'benepar_en3'})
doc = nlp(text)
tree_representation = get_parse_tree_string(doc)[0]

spaced_text = tree_representation.replace('(', ' ( ').replace(')', ' ) ')
tokens = spaced_text.split()

root = Node.parse(tokens, 0, len(tokens))
pretty_print.pretty_print(root)
