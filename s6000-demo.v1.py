from py2neo import Graph, Node, Relationship, NodeMatcher

#connection to db s6000-demo
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="1"
)

tx = graph.begin()
m = NodeMatcher(graph)

# definition
attacker_ip = "192.168.13.1"
victim_ip = "101.227.139.217"
log_index = 3
attack_type = "信息泄露"
relation_attack_log = "attack_related"
relation_victim_log = "victim_related"


# check existing node
check_result = graph.nodes.match("attacker", IP = attacker_ip).first()
if check_result == None:
    # create attacker node
    a = Node("attacker", IP = attacker_ip)
    tx.create(a)
else:
    _a = m.match("attacker", IP = attacker_ip).first()
    a = graph.nodes[_a.identity]

check_result = graph.nodes.match("victim", IP = victim_ip).first()
if check_result == None:
    # create victim node
    v = Node("victim", IP = victim_ip)
    tx.create(v)
else:
    _v = m.match("victim", IP = victim_ip).first()
    v = graph.nodes[_v.identity]

# create log node and relationship
l = Node("warninglog", LogIndex=log_index, ATTACKTYPE=attack_type)
al = Relationship(a, relation_attack_log, l)
tx.create(al)

vl = Relationship(v, relation_victim_log, l)
tx.create(vl)

tx.commit()  # this line of codes should be as ending code