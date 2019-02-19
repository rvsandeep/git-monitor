## Github as a Growth Monitor

GitHub has become a defacto standard for organizations to host code and manage a major chunk of development activities. It's vast community of active developers are a catalyst to the fast paced progress of product. Also, the global community helps to onboard anyone new to GitHub easily.

Along with being a Version Control Application GitHub provides a variety of features to track state of a project, plan milestones, track bugs, contributions and so on. As an organization evolves, the house keeping activities become overwhelmingly tedious and companies move to deploying separate tools for managing and tracking projects. Instead, GitHub Data could be leveraged to track project health, bug status and monitor progress. A majority of open source projects/in-house projects depend on other projects, Github data could be used to develop a dependency graph and across various projects and enable the developers to understand project outreach.

### Business Value

* Monitoring Platform for developers to track software track and be up-to-date with progressing software world.
* Understand the open source community code better and determine creditworthy of a library.
* Avoid security loopholes or vulnerabilities that arise due to dependencies on 3rd party libraries.

### Tech Stack

![pipeline](resources/pipeline.png)

### Engineering Challenge

* Parsing version information of packages from different platforms.
* Determining direct and indirect dependencies of packages.
* Visualizing relevant data and removing irrelevant nodes.

### MVP

* Parse the Libraries IO data to extract relations between different packages.
* Visualize the relations in graph database.
