# GraphQL API template in flask 

## Overview

A simple graphql interface with flask, SQLAlchemy, SQLite and Graphene. Based on the graphene docs:

[Graphene Flask Example](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tutorial/)

The architecture has been redesigned to Flask Blueprint/ App Factory standards because y'all be killin me wit these single-page flask apps. Stop That! Likewise, I've tacked on a cheeky breakfast cereals database that I borrowed from Kaggle just to make it a bit more fun.

## How it works

If you know the app_factory patterns for Flask, this should all be straight forward to understand. Rather than screw around with engines and declaritives for the database, this has been abstracted out with an unbound instance of the SQLAlchemy object created at blueprint level which encorporates engines, sessions, ORM, connection pools et al. This is then passed up to top level, where it's init'd and bound to the app within the app context and created, alongside a top level instance of Migrate just to keep DB migrations simple should this template ever be used for another project. At the blueprint level, tables are created using the SQLAlchemy object and object relational mapping; with Classes inhereting from the SQLAlchemy Model object representing tables.

Consequently Graphene has been used to interact with GraphQL as opposed to Adiadne; Graphene is 'code-first' as opposed to Ariadnes 'schema first' approach. This means that schemas are derived from code (objects) as opposed to objects being derived from schemas. As ORM is being used for the database, utilizing ORM for the interaction with the database allows models to essentially be 'copy-pasted' from DB logic to API logic, eliminating a level of complexity.

<< TALK ABOUT GraphQL LOGIC >>

The main point of difference between GraphQL and REST APIs is that GraphQL utilizes one endpoint to retrieve all data as opposed to REST APis where multiple endpoints deliver specific data. As per standard, this endpoint sits at

<client address>/graphql 
 
 NB. In this version of the app the endpoint currently sits at a top-level route, however a better, more modular design pattern would be to encorporate this into the GraphQL blueprint itself, for the sake of brevity though this sits on top-level currently. The GraphQL GUI has been incorporated for the purpose of demonstration, however obviously for web services this is superfluous.
 
Any questions, holla at me, otherwise feel free to mess around with the queries, fork to your hearts content.

LG,

AlexJJGreen

### test query for api ui

{
  allCereals {
    edges {
      node {
        id
        name
      }
    }
  }
}


