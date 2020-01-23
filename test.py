import digraph

if __name__=='__main__':
  dot = digraph.Digraph('EXAMPLE_GRAPH')

  dot.add_node('START')
  dot.add_node('n1')
  dot.add_node('n2')
  dot.add_node('n3')
  dot.add_node('n4')
  dot.add_node('n5')
  dot.add_node('END')

  dot.add_edge('START', 'n1')
  dot.add_edge('n1', 'n2')
  dot.add_edge('n2', 'n3')
  dot.add_edge('n2', 'n4')
  dot.add_edge('n4', 'n1')
  dot.add_edge('n3', 'n5')
  dot.add_edge('n5', 'END')

  dot.dump_to_file()