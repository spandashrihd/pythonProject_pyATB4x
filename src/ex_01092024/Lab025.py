user_type=input("enter type of user, admin, manager, guest")
user_type=user_type.lower()
match user_type:
    case "admin" | "manager":
        print("Hello sir")
    case "guest":
        print("Hello guest")
    case _:
        print("Hello there")