run:
	docker build -t credits .
	docker run -d --restart=always --name credits -p 2007:80 credits
stop:
	docker container rm -f credits
