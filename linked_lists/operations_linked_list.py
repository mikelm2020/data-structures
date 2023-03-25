from node import Node

# Creación de los nodos enlazados (linked list)
head = None
for count in range(1, 6):
    head = Node(count, head)

# Recorrer e imprimir valores de la lista
probe = head
while probe != None:
    print(probe.data)
    probe = probe.next

# Busqueda de un elemento
probe = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f"Target item {target_item} has been found!")
else:
    print(f"Target item {target_item} is not in the linked list!")

# Ahora vamos a crear la operación de reemplazo de un elemento
probe = head
target_item = 3
new_item = "Z"

while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replaced the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")

# Insertar un nuevo nodo al inicio de la lista
head = Node("F", head)

# Insertar un nuevo nodo al final de la lista
new_node = Node("K")
if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node

# Eliminar un nodo al inicio de la lista
removed_item = head.data
head = head.next
print(removed_item)

# Eliminar un nodo al final de la lista
removed_item = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None

print(removed_item)

# Agregar un nodo en una posición determinada
new_item = input("Enter new item: ")
index = int(input("Enter the position to insert the new item: "))
if head is None or index < 0:
    head = Node("Py", head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)

# Eliminar un nodo en una posición determinada
index = 3
if index <= 0 or head.next is None:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next
    print(removed_item)
