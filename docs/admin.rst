

Admin Panel Documentation
=========================

Introduction
------------

The admin panel in this Django project provides a convenient way to manage users and contact messages in our case. This documentation outlines how to use the admin panel for administration tasks.

Accessing the Admin Panel
-------------------------

To access the admin panel:

1. Ensure you have superuser privileges. If you haven't created a superuser account, follow these steps:

   a. Open a terminal.

   b. Navigate to your project directory.

   c. Run the following command and follow the prompts to create a superuser account:

      ```bash
      python manage.py createsuperuser
      ```

2. Start the development server:

   ```bash
   python manage.py runserver

 


Open a web browser and go to the following URL:
http://localhost:8000/admin/

Replace localhost:8000 with your project's domain and port if necessary.



Admin Dashboard
The admin dashboard provides an overview of the available admin management options:

App List: The admin dashboard displays available apps with registered models for admin management.

Search Bar: You can search for specific objects using the search bar.

Navigation: The admin dashboard provides a navigation menu to manage users and contact messages.

Managing Users
Creating Users
To create a new user, navigate to the "Users" section in the admin dashboard.

Click "Add user."

Fill in the user details, including username, email, password, and other required fields.

Click "Save" to create the user.

Editing Users
To edit a user's profile, find the user in the "Users" section.

Click on the user's name to access the user's profile.

Make the necessary changes and click "Save."

Deleting Users
To delete a user, find the user in the "Users" section.

Select the user or click on the user's name to access their profile.

Click "Delete" and confirm the action.

Managing Contact Messages
Viewing Contact Messages
To view contact messages, navigate to the "Contact Messages" section in the admin dashboard.

You'll see a list of contact messages with details.

Responding to Contact Messages
To respond to a contact message, click on the message in the "Contact Messages" section.

You can add a response or reply to the message.

Click "Save" to save the response.

Deleting Contact Messages
To delete a contact message, find the message in the "Contact Messages" section.

Select the message.

Click "Delete" and confirm the action.

Conclusion
The admin panel in your Django project simplifies the process of managing users and contact messages. This documentation provides you with a guide on how to effectively use the admin panel for your administrative tasks.



