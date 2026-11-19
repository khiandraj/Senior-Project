from rdflib import Graph
from rdflib.namespace import FOAF, RDF

g = Graph()
g.parse("node1.ttl", format="turtle")

print(f"Loaded {len(g)} triples\n")

for person in g.subjects(RDF.type, FOAF.Person):
    print("Person:  ", person)
    print("Name:    ", g.value(person, FOAF.name))
    print("Nickname:", g.value(person, FOAF.nickname))
    for friend in g.objects(person, FOAF.knows):
        print("Knows:   ", friend)