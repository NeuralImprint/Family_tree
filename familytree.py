import networkx as nx
import matplotlib.pyplot as plt

def ankit_family_tree():
    print("Namaste! Family Tree Program mein aapka swagat hai.\n")

    family_tree = nx.DiGraph()

    self_name = input("Enter your name: ").strip()
    family_tree.add_node(self_name)

    valid_relationships = {
        "papa", "mummy", "bhai", "behen",
        "dadaji", "dadiji",
        "nanaji", "naniji",
        "chacha", "chachi",
        "beta", "beti"
    }

    print("\nPlease enter family members and their relationship to you.")
    print("Type 'done' when finished.\n")
    print("Allowed relationships:", ", ".join(valid_relationships))

    while True:
        relation = input("\nEnter the relationship (or type 'done'): ").strip().lower()
        if relation == "done":
            break
        if relation not in valid_relationships:
            print("Invalid relationship. Please try again.")
            continue

        name = input(f"Enter the name of your {relation}: ").strip()

        family_tree.add_node(name)

        if relation in {"papa", "mummy", "dadaji", "dadiji", "nanaji", "naniji", "chacha", "chachi"}:
            # They are parent/older generation
            family_tree.add_edge(name, self_name, relation=relation)
        elif relation in {"bhai", "behen"}:
            
            family_tree.add_edge(self_name, name, relation="bhai-behen")
            family_tree.add_edge(name, self_name, relation="bhai-behen")
        elif relation in {"beta", "beti"}:
            
            family_tree.add_edge(self_name, name, relation=relation)
        else:
            
            family_tree.add_edge(self_name, name, relation=relation)

    print("\nFamily Tree Created Successfully!")

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(family_tree, k=0.5, iterations=100)

    nx.draw(family_tree, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)

    edge_labels = nx.get_edge_attributes(family_tree, 'relation')
    nx.draw_networkx_edge_labels(family_tree, pos, edge_labels=edge_labels, font_color='darkred')

    plt.title(f"Family Tree of {self_name}", fontsize=16)
    plt.show()

ankit_family_tree()
