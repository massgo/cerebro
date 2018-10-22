run:
	docker run --rm --name postgres -p 5432:5432 postgres

connect:
	docker run -it --rm --link postgres:postgres postgres psql -h postgres -U postgres

download:
	wget -c https://www.usgo.org/mm/tdlista.txt

load: download
	./cerebro.py

clean:
	rm -rf tdlista.txt
