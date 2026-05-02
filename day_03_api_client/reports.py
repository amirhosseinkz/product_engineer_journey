



def print_user_report(users):
    print("USER REPORT")
    print("=" * 30)


    for user in users:
        name = user.get("name", "Unknown")
        email = user.get("email", "Unknown")
        city = user.get("address" , {}).get("city", "Unknown")
        company = user.get("company", "Unknown")
        username = user.get("username", "Unknown")

        print(f"{name} | {email} | {city} | {company} | {username}")

    print("=" * 30)
    print(f"Total users: {len(users)}")