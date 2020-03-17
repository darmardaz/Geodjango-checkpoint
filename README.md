# Geo-Django app
### After build
Run script from main folder:

`./run_after_build`

To run tests:

`docker-compose exec web pytest`

To run load-testing with artillery:

- install artillery `npm i -g artillery`

- run scenarios from scenarios folder `artillery run "file_name"`

Load-test scenarios run order:

- `check_voivodeship.yml`
- `create_event.yml`
- `read_event.yml`
- `read_events.yml`


