CC := $(or $(CC),gcc)
CFLAGS := 
CONTAINER := shredder

all: shredder

clean: .PHONY
	rm -f shredder

shredder: shredder.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile shredder
	docker build -t $(CONTAINER) .

run: docker
	docker run -d --read-only --restart=always --name shredder -p 3003:6000 shredder

extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/shredder - | tar xv shredder
	docker rm -v $(id)

dist: extract
	zip shredder.zip shredder shredder.c

.PHONY:
