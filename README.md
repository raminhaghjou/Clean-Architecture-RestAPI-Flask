

For Create Migrations in project
1- Create Migrations folder in folder of infrastructure of project using alembic
    
    - alembic init -t generic migrations

2- Create DB Model Configurations in persistence layer
    -- cities
        -- CityDBModelConfig.py

3- Generate migration of database using alembic with models

    - alembic revision --autogenerate -m "Adding CityDBModelConfig"

4- Apply the migration

    - alembic upgrade head


export PYTHONPATH=$PYTHONPATH:"/home/ramin/anaconda3/envs/flask/lib/python3.11/site-packages"
export PYTHONPATH=$PYTHONPATH:"/home/ramin/Python-Projects/flask-clean-architecture-final"