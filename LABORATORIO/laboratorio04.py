# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data, son=None):
        self.data = data
        self.sons = []
        self.father = None
        self.cost = None
        self.set_son(son)

    #Se pueden pasar varios hijos
    def set_son(self, son):
        #self.son = son
        if (son is not None):
          self.sons.append(son)
          if self.sons is not None:
              for s in self.sons:
                  s.father = self

    def get_sons(self):
        return self.sons

    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost
    #obtencion de los datos
    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def on_list(self, node_list):
        listed = False
        for n in node_list:
            if self.equal(n):
                listed = True
        return listed

    def __str__(self):
        return str(self.get_data()) #str representa los datos

def search_heuristic_solution(init_node, solution, visited, number):
    visited.append(init_node.get_data())
    if init_node.get_data() == solution:
        return init_node
    else:
        # Expandir nodos sucesores (hijos)
        for i in range(number - 1):
            node_data = init_node.get_data().copy()
            temp = node_data[i]
            node_data[i] = node_data[i+1]
            node_data[i+1] = temp
            new_son = Node(node_data)
            init_node.set_son(new_son)
            new_son.set_father(init_node)

        for son_node in init_node.get_sons():
            if not son_node.get_data() in visited and improvement(init_node, son_node):
                # Llamada recursiva
                solutn = search_heuristic_solution(son_node, solution, visited, number)
                if solutn is not None:
                    return solutn
        return None


def improvement(father_node, son_node):
    father_quality = 0
    son_quality = 0
    father_data = father_node.get_data()
    son_data = son_node.get_data()

    for n in range(1, len(father_data)):
        if father_data[n] > father_data[n - 1]:
            father_quality = father_quality + 1
        if son_data[n] > son_data[n - 1]:
            son_quality = son_quality + 1

    if son_quality >= father_quality:
        return True
    else:
        return False

if __name__ == "__main__":
  n = int(input("Introduzca la cantidad de números que desea ordenar: "))
  initial_state = list(range(n, 0, -1))
  solution_state = list(reversed(initial_state))

  visited_nodes = []
  initial_node = Node(initial_state)
  number = len(initial_state)
  solution_node = search_heuristic_solution(initial_node, solution_state, visited_nodes, number)

  result = []
  node = solution_node
  while node.get_father() is not None:
      result.append(node.get_data())
      node = node.get_father()
  result.append(initial_state)
  result.reverse()
  #print(result)
  total=0
  for i in range(len(result)):
      total = total+i
      print(f'{i+1}: ',result[i])
print('total = ',len(result))