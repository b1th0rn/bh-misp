# bh-misp
The BH-MISP project tries to find useful tasks to automate in a threat intelligence process and build connections between the MISP platform and other tools. The project was started as an integration for eg0n, another community project, but it can be developed and used on its own without the eg0n integration.

The main owner of the project is [Rocco \[sheliak\] Sicilia](https://roccosicilia.com), who works on it together with members of the BitHorn community. To join the community as a threat intelligence analyst, security specialist, or coder, the best way is to join the Discord channel on [Sheliak's server](https://discord.gg/Ys5AAbsyyH): \#misp-project.

# main components

## MISP istance
The BitHorn community maintainers have set up a MISP instance for research purposes. Community researchers and external contributors can use the instance to share, review, or store threat intelligence data. This section of the file outlines the guidelines for collaborating with the project.

*Add New Event*
Create a new event if you want to share information about your analysis or other threat intelligence related to a specific incident.

*Aggregated Event*
Some events are aggregates of objects and attributes from the same category. For example, we have created an event to collect and share all IP addresses identified as scanners.
Use these events to update the collections regularly, ensuring that relevant threat intelligence is centralized and easily accessible. This helps maintain consistency and improves the efficiency of detection, analysis, and response activities across different teams or organizations.

## honeypots
...

## ioc_access
A simple set of scripts to work with the MISP API to access and export IoCs.