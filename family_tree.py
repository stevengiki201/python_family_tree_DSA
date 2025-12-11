def family_tree():
    members={
        "me": {"father": "olaf", "mother": "lili","gender":"male"},
        "olaf": {"father": "lars", "mother": "kate","gender":"male"},
        "lili": {"father": "carl", "mother": "emma","gender":"female"},
        "lars": {"father": "", "mother": "","gender":"male"},
        "kate": {"father": "", "mother": "", "gender":"female"},
        "carl": {"father": "", "mother": "", "gender":"male"},
        "emma": {"father": "", "mother":"","gender":"female"}}
    return members

def find_father(name, family):
    return family.get(name, {}).get("father", "not found in family tree so no such child")
def find_mother(name, family):
    return family.get(name, {}).get("mother", "not found in the  family tree so no such child")
def find_siblings(name, family):
    #Just find yourself the siblings ...................
    pass  
def count_members(family):
    return len(family)
def count_males(family):
    return sum(1 for info in family.values() if info.get("gender")=="male")
def count_females(family):
    return sum(1 for info in family.values() if info.get("gender")=="female")




def main_menu():
    global member
    while True:
        title="Family tree system management".center(50,"*")
        print(title)
        print("*"*len(title))
        print("\n \n")
        menu=["1-show members in a family tree","2-Find father","3-Find mother","4-Find siblings","5-how many members in family","6-how many males","7-how many females","8-exit"]
        for item in menu:
            print(item)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("showing members in a family tree")
            for member in family_tree().keys():
                print(member)
        elif choice == 2:
            print("Finding Father")
            for member in family_tree().keys():
                print(member.center(100))

            sibling_name = input("Enter the name to find the father: ")
            father = find_father(sibling_name, family_tree())
            print(f"The father of {sibling_name} is {father}")
        elif choice == 3:
            print("Finding Mother")
            for member in family_tree().keys():
                print(member.center(100))
            sibling_name = input("Enter the name to find the mother: ")
            mother = find_mother(sibling_name, family_tree())
            print(f"The mother of {sibling_name} is {mother}")
        elif choice == 4:
            parent_name=input('Enter parent name: '.lower())
            child_name=""
            for key, value in family_tree().items():
                mother = value['mother']
                father = value['father']
                if parent_name==father or parent_name ==mother:
                    child_name=key
                    print(f"The child is {child_name}")
                    break
            if not child_name:
                print("No such child in family tree")




            
        elif choice == 5:
            print("counting members in the family")
            number_of_members = count_members(family_tree())
            print(f"The total number of members in family is : {number_of_members}")
        elif choice == 6:
            print("Counting males")
            males= count_males(family_tree())
            print(f"The total number of males in family is  : {males}")
        elif choice == 7:
            print("Counting females")
            females= count_females(family_tree())
            print(f"The total number of females in family is  : {females}")
        elif choice == 8:
            print("Exiting the program goodbye!")
            break
        else:
            print("Invaild choice please try again")
    
if __name__ == "__main__":
    main_menu()



