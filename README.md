IP Monitoring and Downtime Tracker using Python & SQL Server
This Python script continuously monitors a list of IP addresses by pinging them and logs the results into a SQL Server database. It tracks availability, response time, and downtime, and maintains both real-time and historical status records.

**Features
Ping Monitoring: Pings all IPs from the ip table at regular intervals and checks their status (Up/Down).

Downtime Tracking: Calculates and logs the duration of downtime for each IP address.

Response Matrix: Records the ping response time for each IP and saves it in a matrix format for analysis.

Real-Time View: Updates a live_ping_status table for quick insights into currently down IPs with a downtime counter.

Historical Logging: Stores all ping events and downtime logs in the ip_ping_status table for audit and review.

Auto Table Management: Automatically adds new columns for new IPs in the PingResponse matrix table if they don't exist.

**Tables Used
ip: Contains a list of IP addresses to monitor.

ip_ping_status: Logs all ping events with timestamps, statuses, and calculated downtimes.

live_ping_status: Keeps track of the current status of each IP with a counter for how long it has been down.

PingResponse: A matrix-like table where each row represents a timestamp and each column represents an IP's response time.

**Technologies Used
Python 3

pandas – Data manipulation

pyodbc – Database connection

subprocess – Execute ping commands

socket – Fetch local IP

SQL Server – Backend database

**How It Works
Connects to the SQL Server database.

Fetches the IP list from the ip table.

Pings each IP every second for 60 seconds.

Stores results in three tables:

ip_ping_status: Historical record.

live_ping_status: Latest real-time status with downtime counter.

PingResponse: Tabular matrix of ping response times.

Calculates downtime for each IP when it goes down by checking past records.

Ensures schema consistency by adding missing columns dynamically in PingResponse.

**Output
Real-time logs for network monitoring

Downtime statistics and trends

A tabular snapshot of ping response data over time

