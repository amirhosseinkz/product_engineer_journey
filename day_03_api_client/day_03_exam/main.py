
import logging
import api_client
from errors import ApiClientError
from reports import print_posts_report, print_single_post_report


logging.basicConfig(level = logging.INFO , format = "%(levelname)s - %(message)s")


def main():
    logging.info("Starting API client...")

    try:
        posts = api_client.fetch_posts()
        logging.info(f"Fetched {len(posts)} posts successfully.")
        print_posts_report(posts)
        
    except ApiClientError as exc:
        logging.error(f"An error occurred while fetching posts: {exc}")
        return



    
    try:
        
        post = api_client.fetch_post_by_id(1)
        logging.info(f"Fetched details for post ID: {1}")
        print_single_post_report(post)


    except ApiClientError as exc:
            logging.error(
                    f"An error occurred while fetching post details for ID {1}: {exc}"
                )
    except ValueError as exc:

        logging.error("Invalid input: %s", exc)
            







if __name__ == "__main__":
    main()  