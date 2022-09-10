run:
	docker build -t notanothersqli .
	docker run -d --restart=always --name notanothersqli -p 2002:80 notanothersqli
clean:
	docker container rm -f notanothersqli
