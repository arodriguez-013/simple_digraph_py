from collections import OrderedDict

class Digraph():
  Name=None
  nodes=None
  edges=None
  debug = False

  def __init__(self, name, debug=None):
    self.Name = name
    self.nodes = OrderedDict()
    self.edges = []
    
    if debug:
      self.debug = True

  def add_node(self, name, label=None):
    if name not in self.nodes:
      if label==None:
        self.nodes.update({name:""})
        if self.debug:
          print("Node {} added".format(name))
      else:
        self.nodes.update({name:label})
        if self.debug:
          print("Node {} added with label \"{}\"".format(name, label))
    else:
      if self.debug:
        print("\t--- node {} already exists ---".format(name))

  def update_node(self, name, new_label):
    if name not in self.nodes:
      if self.debug:
        print("ERROR: no node \"{}\" in graph".format(name))
    else:
      self.nodes[name] = new_label

  def add_edge(self, head, tail):
    if head not in self.nodes:
      if self.debug:
        print("ERROR: head node not found in graph: \"{}\"".format(head))
    elif tail not in self.nodes:
      if self.debug:
        print("ERROR: tail node not found in graph: \"{}\"".format(tail))
    else:
      if self.debug:
        print("Adding edge from {} to {}".format(head, tail))
      self.edges.append("\"{}\" -> \"{}\";\n".format(head, tail))

  def dump_to_file(self):
    filename = "{}.dot".format(self.Name)
    print("")
    print("--------------------------------------------")
    print("Generating dot file for graph: {}".format(self.Name))
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

    print("dot file generated: {}".format(filename))
    print("--------------------------------------------")
    