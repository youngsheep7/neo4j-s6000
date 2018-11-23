from py2neo import Graph, Node, Relationship, NodeMatcher

#connection to db
g = Graph(    "http://localhost:11004",
    username="neo4j",
    password="123")

tx = g.begin()
a = Node("attacker", name="Alice")
tx.create(a)  # delete can also be create
b = Node("victim", name="Bob")
ab = Relationship(a, "attack", b)
tx.create(ab)
tx.commit()   # this line of codes should be as ending code
g.exists(ab)

"""
tx = g.begin()
a = Node("Person", name="Alice")
tx.create(a)
b = Node("Person", name="Bob")
ab = Relationship(a, "KNOWS", b)
tx.create(ab)
tx.commit()
g.exists(ab)
"""