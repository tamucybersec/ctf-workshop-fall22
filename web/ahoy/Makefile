run:
	docker build -t ahoy .
	docker run -d --restart=always --name ahoy -p 2005:80 ahoy
stop:
	docker container rm -f ahoy
