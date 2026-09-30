from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    employee_ids = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    employee_ids.insert_at_front(103)
    employee_ids.insert_at_front(102)
    employee_ids.insert_at_front(101)

    # TODO: 3) Display the list to verify insertion
    print("Initial Linked List")
    employee_ids.display()

    # TODO: 4) Call recursive_sum and print the result
    total_sum = employee_ids.recursive_sum(employee_ids.head)
    print(f"\nSum of all IDs (Recursive): {total_sum}")

    # TODO: 5) Call recursive_search with a target and print result
    target_id = 102
    found = employee_ids.recursive_search(employee_ids.head, target_id)

    missing_id = 999
    found_missing = employee_ids.recursive_search(employee_ids.head, missing_id)
    print(f"Is ID {Mmissing_id} in list? {found_missing}")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("\nReversing list...")
    employee_ids.head = employee_ids.recursive_reverse(employee_ids.head)
    employee_ids.display()

    


# 