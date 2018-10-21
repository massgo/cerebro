run:
	docker run --rm --name postgres postgres

connect:
	docker run -it --rm --link postgres:postgres postgres psql -h postgres -U postgres

