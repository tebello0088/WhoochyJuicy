
class whoozijuicy:

    def __init__(self,people):
        self.lists=people

def entryrules(self):
    # filter by digits next to alphabet ***Elders must enter the premises first*
    new_sorted_list = sorted(self.lists, key=lambda x: int(re.findall(r'\d+$', x)[0]))
    new_sorted_list.reverse()

    # People must stand in a queue
    Q_IN_queue = userlist.Queue()
    # filter the queue by alphebet
    for item in range(len(new_sorted_list) - 1):

        if int(new_sorted_list[item][1:]) == int(new_sorted_list[item + 1][1:]):
            array = []
            array.append(new_sorted_list[item])
            array.append(new_sorted_list[item + 1])

            # sort by Alphabet
            array.sort()
            new_sorted_list[item] = array[0]
            new_sorted_list[item + 1] = array[1]

    for item in new_sorted_list:
        # **No under 18 persons are allowed**
        # select the age of the person and check if the person is allowed or not
        if int(item[1:]) < 18:
            print ("This person is not allowed ", item)
        elif int(item[1:]) == 90:
            print ("This nightclub is not able to assist this person", item)
        else:
            # All those who are allowed
            Q_IN_queue.put(item)

    while not Q_IN_queue.empty():
        print("Person ", Q_IN_queue.get(), "Enters the premises")