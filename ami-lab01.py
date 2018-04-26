#aggiungi elememto alla lista
def add_item(list):
    list.append(input('add item: '))

#elimina ricorsivamente tutte le task uguali
def recursive_remove_items(list,item):
    if list.count(item) > 0:
        list.remove(item)
        recursive_remove_items(list,item)

#not recursive version, to delete a single task
def remove_single_item(list,item):
    list.remove(item)

#elimina le task uguali dalla lista con funzione sopra
def remove_item(list):
    item = input('remove item: ')
    if list.count(item) > 0:
        #remove_single_item(list,item)
        recursive_remove_items(list,item)
    else:
        print("la task non è nella lista")

#stampa a schermo tutte le task in lista
def show_items(list):
    print('print items:')
    for item in list:
        print(item)

#main del programma
if __name__=='__main__':
    list=[]
    while True:
        n=int(input("1. insert a new task."
                    "\n2. remove a task."
                    "\n3. show all the tasks."
                    "\n4. close the program."
                    "\n--> "))
        if n==1:
            add_item(list)
        elif n==2:
            remove_item(list)
        elif n==3:
            show_items(list)
        elif n==4:
            del list
            print("fine programma")
            break
        else:
            print("non ho capito")
        print("--------------------")