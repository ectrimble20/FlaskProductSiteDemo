from productsite import create_flask_app

app = create_flask_app()

if __name__ == '__main__':
    app.run(debug=True, host="localhost")


"""
Okay, so I think we're going to need a few things:

Users-
Products-
Reviews
Ratings
Orders
CustomerServiceTickets

Considerations:
might need something like "reorder" like a way for the vendor to know what products to order
from suppliers
"""