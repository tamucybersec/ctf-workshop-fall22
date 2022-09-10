run:
	docker build -t serialkiller .
	docker run -d --restart=always --name tamuctf-serialkiller -p 2001:80 serialkiller
stop:
	docker container rm -f tamuctf-serialkiller
