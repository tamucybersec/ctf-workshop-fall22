run:
	docker build -t robots .
	docker run -d --restart=always --name robots -p 2003:80 robots
clean:
	docker container rm -f robots
