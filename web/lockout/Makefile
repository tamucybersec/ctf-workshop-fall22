run:
	docker build -t lockout .
	docker run -d --restart=always --name lockout -p 2009:80 lockout
stop:
	docker container rm -f lockout
