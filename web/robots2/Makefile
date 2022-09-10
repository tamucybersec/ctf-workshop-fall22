run:
	docker build -t robots2 .
	docker run -d --restart=always --name robots2 -p 2009:80 robots2
clean:
	docker container rm -f robots2
