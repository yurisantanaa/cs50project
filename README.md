#FINAL PROJECT CS50
#Yuri Buenos Aires Santana


#Inventory Management System

Description: Create a system for small businesses to manage their product inventory, including tracking product inflows and outflows.

##Features:

###Product Registration:
  => Allow users to register new products with details such as name, category, supplier, purchase price, selling price, and initial stock quantity.
  => Users can also upload images and descriptions for each product.

###Stock Control:

  =>Enable users to update stock quantities when new inventory arrives or when products are sold.
  =>Provide an interface to view current stock levels, filterable by product category, supplier, or other attributes.
  =>Implement functionality to handle returns and restocking of products.

###Reports:

  =>Generate reports on stock levels, including products with low stock or out-of-stock items.
  =>Provide sales reports showing the most popular products, total sales, and revenue over specified periods.
  =>Offer inventory valuation reports to help businesses understand the current value of their stock.


###User Roles and Permissions:

  =>Create different user roles such as Admin, Manager, and Staff, with varying levels of access to the system’s features.
  =>Allow Admins to manage user accounts, assign roles, and set permissions.

###Supplier Management:

  =>Maintain a database of suppliers with contact information and products supplied.
  =>Link products to their respective suppliers for easy reordering.

###Search and Filtering:

  =>Provide robust search functionality to find products quickly by name, category, or SKU.
  =>Allow filtering of products by various attributes such as stock level, category, or supplier.

###Audit Trail:

  =>Implement an audit trail to track changes made to the inventory, including who made the change, what was changed, and when it was changed.
  =>Provide access to audit logs for security and accountability purposes.

###Technical Implementation:

  =>Frontend: Use HTML, CSS, and JavaScript for the user interface. Consider using a frontend framework like React or Vue.js for a more dynamic experience.
  =>Backend: Use Flask to create the backend API for handling business logic and database interactions.
  =>Database: Utilize SQL (such as PostgreSQL or MySQL) to manage product, user, and supplier data.
  =>Authentication: Implement user authentication and authorization using Flask-Login or Flask-Security.
  =>Deployment: Deploy the application on a cloud service like AWS, Heroku, or DigitalOcean.

