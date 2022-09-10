run:
	docker build -t secret-number .
	docker run -d --restart=always --name secret-number -p 2005:80 secret-number
stop:
	docker container rm -f secret-number
