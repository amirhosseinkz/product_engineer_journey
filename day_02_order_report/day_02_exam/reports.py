from pathlib import Path





def print_books(books , authors):
    print("BOOK INVENTORY REPORT")
    print("=" * 60)

    categories = {}
    total_inventory_value = 0



    for book in books:
        total_price = book.inventory_value()
        author_info = authors.get(book.author, {})
        country = author_info.get("country", "Unknown")
        total_inventory_value += total_price

        if book.category not in categories:
            categories[book.category] = 0
        categories[book.category] += 1
            

        print(
            
            book.id,
            "|",
          
            book.title,
            "|",
         
            book.author,
            "|",
            country,
            "|",
          
            book.category,
            "|",
          
            f"Stock: {book.stock}",
            "|",
 
            f"Value: ${total_price:.2f}",
        )

    print("=" * 60)
    print(f"Total books: {len(books)}")
    print(f"Total inventory value: ${total_inventory_value:.2f}")

    for category, count in categories.items():
          print(f"Total {category} books: {count}")
   
  



   