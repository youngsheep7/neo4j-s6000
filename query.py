
from py2neo import Graph, NodeMatcher, Node, Relationship

g = Graph(
    "http://localhost:11004",
    username="neo4j",
    password="123"
)

matcher = NodeMatcher(g)

print(matcher.match("attacker").first())  # matcher.match("attacker").first()
print(matcher.match("attacker", name = "Alice").first()) # Return the first item that matches the given criteria.

a= g.nodes.match("attacker", name ="Alice").first()
print(a)

b= g.nodes.get(24)
print (b)