run:
	docker build -t better-header .
	docker run -d --restart=always --name better-header -p 2004:5000 better-header
stop:
	docker container rm -f better-header
