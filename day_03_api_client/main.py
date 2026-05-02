import logging
import api_client
from errors import ApiClientError
from reports import print_user_report




logging.basicConfig(level = logging.INFO , format = "%(asctime)s - %(levelname)s - %(message)s")




def main():

    logging.info("Starting API client...")


    try:
        users = api_client.fetch_users()
        for user in users:
            user_id = user.get("id" , "Unknown")
        
            if(user_id == 1):
                try:
                   logging.info(f"Fetching details for user ID: {user_id}")
                   user_details = api_client.fetch_users_by_id(user_id)
                   logging.info(f"User details for ID {user_id}: {user_details}")
                except ApiClientError as exc:
                    logging.error(f"An error occurred while fetching user details for ID {user_id}: {exc}")
    except ApiClientError as exc:
        logging.error(f"An error occurred while fetching users: {exc}")
        return



    print_user_report(users)
    logging.info("Finished successfully")


   




if __name__ == "__main__":
    main()