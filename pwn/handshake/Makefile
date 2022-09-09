CC := $(or $(CC),gcc)
CFLAGS := -no-pie -fno-stack-protector 
CONTAINER := handshake

all: handshake

clean: .PHONY
	rm -f handshake

calculator: handshake.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile
	docker build -t $(CONTAINER) .

run: docker
	docker run -d --read-only --restart=always --name $(CONTAINER) -p 3004:4212 $(CONTAINER)

extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/handshake - | tar xv handshake
	docker rm -v $(id)

.PHONY:
