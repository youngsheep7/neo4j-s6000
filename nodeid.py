from py2neo import Graph, Node, Relationship, NodeMatcher

#connection to db s6000-demo
g = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1"
)

''' below block is to firstly create 2 nodes
tx = g.begin()
a = Node("attacker", name="Bob")
tx.create(a)
tx.commit()   # this line of codes should be as ending code
'''

tx = g.begin()
m = NodeMatcher(g)
n1 = m.match("attacker", name = "Alice").first()
n2 = m.match("attacker", name = "Bob").first()
ab = Relationship(g.nodes[n1.identity], "love", g.nodes[n2.identity])
tx.create(ab)
tx.commit()   # this line of codes should be as ending code