📌 GraphQL CRM with Filters

This project is a CRM system built with Django, Graphene-Django, and Django-Filter.
It exposes a GraphQL API that supports filtering, searching, and sorting of Customers, Products, and Orders.

🚀 Features

Customer Management – Create, update, delete, and search customers.

Product Management – Manage product catalog with price, stock, and filtering options.

Order Management – Place and view orders with filtering on dates, customers, products, and totals.

Advanced Search Filters using django-filter:

Customers → by name, email, creation date, phone patterns.

Products → by name, price range, stock levels.

Orders → by customer, product, total amount, and date ranges.

Sorting & Pagination → results can be ordered (ASC/DESC) and paginated with Relay-style connections.