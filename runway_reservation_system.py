import datetime

# This class represents a node in the BST.
class runway_bst(object):
    def __init__(root, start_time=None, end_time=None, flight_number=None):
        root.start_time = datetime.datetime.strptime(start_time, "%H:%M")
        root.end_time = datetime.datetime.strptime(end_time, "%H:%M")
        root.flight_number = flight_number
        # Left and right child
        root.left = None
        root.right = None

    def insert(root, start_time=None, end_time=None, flight_number=None):
        """
        This method makes flight reservation by inserting the node into the Binary search tree 
        based on the start_time.
        """
        # Base case
        if root is None:
            root = runway_bst(start_time, end_time, flight_number)
        else:
            # consider start_time of every node for node key value comparision
            if(datetime.datetime.strptime(start_time, "%H:%M") >= root.start_time):
                if root.right is None:
                    root.right = runway_bst(start_time, end_time, flight_number)
                else:
                    root.right.insert(start_time, end_time, flight_number)
            else:
                if root.left is None:
                    root.left = runway_bst(start_time, end_time, flight_number)
                else:
                    root.left.insert(start_time, end_time, flight_number)

    
    def valid_interval(root, start_time, end_time):
        """
        This method validates the interval duration to be 30 mins exact.
        It uses datetime strptime to convert string to Date object. 
        And then perform comparisons on datetime objects.
        """
        request_start_time = datetime.datetime.strptime(start_time, "%H:%M")
        request_end_time = datetime.datetime.strptime(end_time, "%H:%M")

        tdelta = request_end_time - request_start_time
        if int(tdelta.total_seconds()/60) == 30:
            return True
        else:
            return False


    def busy_runway(root, start_time, end_time):
        """
        This method will check if the given time slot is available and no other flight is scheduled
        This returns True if the flight can be scheduled
        Returns None, if an overlap is found.
        """
        if root.left is not None:
            l = root.left.busy_runway(start_time, end_time)
            # overlap case
            if l is None: return None 

        if root.start_time is not None:
            # check if the requested interval overlaps any existing interval.
            # Convert string to Date object using strptime and then perform comparisons on datetime objects.
            if(root.start_time <= datetime.datetime.strptime(start_time, "%H:%M") <= root.end_time or root.start_time <= datetime.datetime.strptime(end_time, "%H:%M") <= root.end_time):
                return None

        if root.right is not None:
            r = root.right.busy_runway(start_time, end_time)
            # overlap case
            if r is None: return None 
        return True


 
    def make_reservation(root, flight_start_time, flight_end_time, flight_number):
        """
        This method has the logical implementation to make the reservation for a particular flight
        Before booking the reservation it will validate if the slot is getting booked for 30 minutes only
        It also checks if the no other flight is scheduled over the runway during that time 
        Driver method which makes the reservation and calls all the helper methods.
        """
        # validate if the slot is getting booked for 30 minutes only
        if not root.valid_interval(flight_start_time, flight_end_time):
            print("Please provide a half an hour interval, in 24 Hour clock military format.")

        # check if no other flight is scheduled over the runway during that time
        elif root.busy_runway(flight_start_time, flight_end_time) is None:
            print("Runway is booked during: {} to {}".format(flight_start_time, flight_end_time))
        
        # schedule the flight
        else:
            root.insert(flight_start_time, flight_end_time, flight_number)
            print("Runway reservation made for flight number {} from {} to {}".format(flight_number, flight_start_time, flight_end_time))
    
    # inorder traversal: left, root, right
    def inorder(root, vals):
        """
        This method does inorder traversal (left, root, right) and appends start_time to the list.
        Returns the list
        """
        if root.left:
            root.left.inorder(vals)

        if root.start_time:
            vals.append(root.start_time)

        if root.right:
            root.right.inorder(vals)
        return vals
            
if __name__ == '__main__':
    
	# Root node of BST
    test = runway_bst('11:00', '11:30', 'GOI9872')
    test.make_reservation('11:35', '12:05', 'JET9874')
    test.make_reservation('12:30', '13:00', 'JET9243')
    
    #Following case should fail. Runway is busy
    test.make_reservation('10:45', '11:15', 'VIS9000')
    test.make_reservation('12:45', '13:15', 'IND3360')
    test.make_reservation('13:45', '14:45', 'IND3361')

    # New booking. Should pass
    test.make_reservation('10:10', '10:40', 'JET9243')
    test.make_reservation('09:30', '10:00', 'AIR2781')

    # test cases
    # test.make_reservation('10:30', '11:00', 'JET9245') # fail
    # test.make_reservation('09:30', '10:10', 'AIR2782') # fail
    # test.make_reservation('08:30', '09:00', 'AIR2787') # pass
    # test.make_reservation('08:35', '09:05', 'AIR2787') # fail
    # test.make_reservation('11:35', '12:05', 'JET9879') # fail
    # test.make_reservation('13:00', '13:30', 'IND3361') # fail

    # verfiying if the data inserted is BST or not 
    res = []
    res = test.inorder(res)
    print([datetime.datetime.strftime(r, "%H:%M") for r in res])
