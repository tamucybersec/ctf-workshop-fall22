run:
	docker build -t hidden .
	docker run -d --restart=always --name hidden -p 2000:80 hidden
clean:
	docker container rm -f hidden
