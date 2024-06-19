# DiscordSRV-Baltop
 Enables you to recall the 10 most richest people on your Minecraft Server

Works with any Economy Manager that has support for MySQL/MariaDB

This setup comes with some features disabled by default, so you need to manually enable these by uncommenting what it tells you to uncomment

## Prerequisites 
- MySQL/MariaDB Database with read permissions
- A Minecraft Server with CMI or any other Economy Manager with MariaDB support
- Python & Pip

## Installation
**Database Setup**
- Install MySQL/MariaDB
- Use a database manager such as HeidiSQL (Windows) to create a database
- Create a database table named CMI or any name of your choosing

**Minecraft Setup**
- Configure CMI's ``databaseinfo.yml`` to your liking, make sure you're using an SQL user with both Read/Write permissions to your database
 - Use the name of the table you created earlier as the database name in this config
- Run the server

**Python Setup**
- Install Python3 for your distro or OS
- Install Pip for Python if you haven't already
- Make sure you installed MariaDB (assuming you're running that) & discord.py using pip
- Run the python file in your command prompt
