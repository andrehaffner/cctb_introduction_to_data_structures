import matplotlib.pyplot as pyplot
import networkx as netx
from time import sleep
# Program developed by André, Amanda, Grecia, Sam and Wesley


# Creating graphic and adding nodes/edges
myGraphic = netx.Graph()
myGraphic.add_node("A")
myGraphic.add_node("B")
myGraphic.add_node("C")
myGraphic.add_node("D")
myGraphic.add_node("E")
myGraphic.add_edge("A", "A")
myGraphic.add_edge("B", "B")
myGraphic.add_edge("C", "C")
myGraphic.add_edge("D", "D")
myGraphic.add_edge("E", "E")


# alphabet tuple // line string // options string (\n is jump line and \t is paragraph)
alphabet = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
line = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
options = "\n\n\t1. Display the graphic\n\t2. Print vertices/nodes\n\t3. Print edges" \
          "\n\t4. Add vertex\n\t5. Delete vertex\n\t0. Exit"


# Our program is a loop so it never stops
while True:
    try:
        # Starting program (sleep() makes our code wait few a few seconds for a cleaner prompt)
        sleep(1)
        print(line)
        print("\nRunning program...")
        sleep(1)
        print(myGraphic)

        # Getting user input
        chosen_option = int(input("\nOptions:" + options + "\n\nChoose one: "))

        # ~~ only int inputs pass down here, strings are caught in ValueError exception ~~ #

        # 1. Display graphic
        if chosen_option == 1:
            print("")
            netx.draw(myGraphic,
                      width=5,
                      font_size=20,
                      font_weight="bold",
                      with_labels=True,
                      node_color = "red",
                      node_size = 3000)
            pyplot.margins(0.2)
            pyplot.show()
            print("")
            sleep(1)

        # 2. Print vertices
        elif chosen_option == 2:
            print("\n\tVertices:", myGraphic.nodes, "\n")
            sleep(1)

        # 3. Print edges
        elif chosen_option == 3:
            print("\n\tEdges:", myGraphic.edges, "\n")
            sleep(1)

        # 4. Add vertice
        elif chosen_option == 4:
            while True:
                n = input("\n\tEnter the vertex you want to add: ").upper()
                if n not in alphabet:
                    print("\n\t\t- Vertex's name must be a letter!")
                elif n in myGraphic.nodes:
                    print(f"\n\t\t- Vertex {n} already exists!")
                else:
                    myGraphic.add_node(n)
                    myGraphic.add_edge(n, "A")
                    # print nodes after adding a new one
                    print(f"\n\t\tVertex added!\n\t\tVertices: {myGraphic.nodes}\n")
                    break
            sleep(1)

        # 5. Remove vertice
        elif chosen_option == 5:

            n = input(f"\n\tVertices: {myGraphic.nodes}\n\tEnter the vertex you want to remove: ", ).upper()
            if n not in myGraphic.nodes:
                print("\t\t- Error: that vertex doesn't exists\n")
            else:
                myGraphic.remove_node(n)
                print(f"\n\t\tVertex removed!\n\t\tVertices: {myGraphic.nodes}\n")
            sleep(1)

        # 0. Exit
        elif chosen_option == 0:
            print("\n\tBye, thank you for using our graphic program!")
            print("Shutting down...")
            break

        # Other numbers
        else:
            print(f"\n\t- Number {chosen_option} is not an option!\n")

    # If input is nt a number (int() function on line 27 will return error)
    except ValueError:
        print("\n\t- Input error: only numbers accepted!\n")


"""

For the power point apresentation, i suggest that we introduce our program as an infinit while loop, that keeps asking 
for the user to intercact with it.

To cover the possibility of the user not inputing an int, we used try/except

And for choosing which path to go in accord to the input, we have an if, elif, else statement

So, each interaction the user makes generates a result: error messages, prints, displays, accordingly to the input

"""
