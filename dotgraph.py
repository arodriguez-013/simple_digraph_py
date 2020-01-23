from collections import OrderedDict

# I WROTE THIS LIBRARY TO HELP CREATE THE DOT FILES
# I ORIGINALLY WANTED TO USE THE GRAPHVIZ MODULE BUT
# LACKED PRIVILEDGES TO PIP INSTALL GRAPHVIZ ON THE 
# IDA Pro SERVERS, SO HERE WE ARE... IT WORKED REALLY 
# WELL THOUGH SO THATS NEAT. FEEL FREE TO PLAY AROUND
# WITH IT

class dotgraph():
  Name=None
  nodes=None
  edges=None

  def __init__(self, name):
    self.Name = name
    self.nodes = OrderedDict()
    self.edges = []

  def add_node(self, name, label=None):
    if name not in self.nodes:
      if label==None:
        self.nodes.update({name:""})
        # print("Node {} added".format(name))
      else:
        self.nodes.update({name:label})
        # print("Node {} added with label \"{}\"".format(name, label))
    else:
      print "\t--- node {} already exists ---".format(name)

  def update_node(self, name, new_label):
    if name not in self.nodes:
      print("ERROR: no node \"{}\" in digraph".format(name))
    else:
      self.nodes[name] = new_label

  def add_edge(self, head, tail):
    if head not in self.nodes:
      print("ERROR: head node not found in digraph: \"{}\"".format(head))
    elif tail not in self.nodes:
      print("ERROR: tail node not found in digraph: \"{}\"".format(tail))
    else:
      #print("Adding edge from {} to {}".format(head, tail))
      self.edges.append("\"{}\" -> \"{}\";\n".format(head, tail))

  def dump_to_file(self):
    filename = "graphs/{}.dot".format(self.Name)
    print("")
    print("--------------------------------------------")
    print("Generating digraph for: {}".format(self.Name))
    with open(filename, "w") as f:
      f.write("digraph \"{}\" ".format(self.Name))
      f.write("{\n")
      for n in self.nodes:
        f.write("  \"{}\"     [label = \"{}; {}\"];".format( n, n, self.nodes[n]))
        f.write("\n")
      
      f.write("\n")
      for e in self.edges:
        f.write("  " + e)
      f.write("}")

    print("digraph file generated: {}".format(filename))
    print("--------------------------------------------")
    