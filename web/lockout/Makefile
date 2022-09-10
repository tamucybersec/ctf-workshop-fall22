run:
	docker build -t lockout .
	docker run -d --restart=always --name tamuctf-lockout -p 2000:80 lockout
stop:
	docker container rm -f tamuctf-lockout
