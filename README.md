# CS-340-10515-M01-Client-Server-Development
Coursework and project implementations for CS-340 (Client/Server Development). Includes MongoDB database administration, advanced aggregation pipelines, and the development of a dashboard interface for "Grazioso Salvare" search-and-rescue training data.

# How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

To write programs that are maintainable, readable, and adaptable, computer scientists rely on modularity and the Model-View-Controller (MVC) design pattern. In Project Two, this was achieved by using an independent CRUD Python module to handle all database logic separately from the Dash interface. The primary advantage of this modular approach is that any changes to the database schema or connection strings only need to be updated in one place rather than across multiple dashboard files. This module is also highly reusable; it could be used in the future to power a mobile app, a command-line tool, or an automated data-reporting service for the same database without rewriting the core logic.

# How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

Approaching a problem as a computer scientist involves understanding complex requirements into manageable technical tasks. For Grazioso Salvare, the request was broken down into a "Model" (MongoDB for high-volume animal records), a "View" (an interactive Dash table and map), and a "Controller" (Python callbacks to filter data).

# What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists create the systems that turn raw data into actionable insights, which is critical for modern business operations. For a company like Grazioso Salvare, this dashboard replaces manual record-searching with an automated, interactive tool.
