print("Saanvi Chawla - E22CSEU1418")

class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority
        
    def __str__(self):
        return f"{self.p_id}\t{self.process}\t{self.start_time}\t\t{self.priority}"

def sort_by_p_id(item):
    return item.p_id

def sort_by_start_time(item):
    return item.start_time

def sort_by_priority(item):
    priority_order = {"Low": 0, "MID": 1, "High": 2}
    return priority_order[item.priority]

def main():
    data = [
        Flight("P1", "VSCode", 100, "MID"),
        Flight("P23", "Eclipse", 234, "MID"),
        Flight("P93", "Chrome", 189, "High"),
        Flight("P42", "JDK", 9, "High"),
        Flight("P9", "CMD", 7, "High"),
        Flight("P87", "NotePad", 23, "Low")
    ]
    
    print("Select sorting parameter:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data.sort(key=sort_by_p_id)
    elif choice == 2:
        data.sort(key=sort_by_start_time)
    elif choice == 3:
        data.sort(key=sort_by_priority)
    else:
        print("Invalid choice")
        return
    
    print("P_ID\tProcess\tStart Time\tPriority")
    for item in data:
        print(item)

if __name__ == "__main__":
    main()
