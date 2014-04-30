#!/bin/bash
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Do a POST petition"}' http://localhost:5000/todo/api/v1.0/tasks
