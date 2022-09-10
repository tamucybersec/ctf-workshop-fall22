run:
	docker build -t serialkiller .
	docker run -d --restart=always --name serialkiller -p 2008:80 serialkiller
stop:
	docker container rm -f serialkiller
