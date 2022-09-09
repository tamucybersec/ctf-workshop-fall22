CC := $(or $(CC),gcc)
CFLAGS := 
NAME := pancake

all: $(NAME)

clean: .PHONY
	rm -f $(NAME)

pancake: pancake.c
	$(CC) $(CFLAGS) $^ -o $@

docker: Dockerfile pancake.c
	docker build -t $(NAME) .

run: docker
	docker run --rm -d -p 3000:3000 --name $(NAME) $(NAME)


extract: docker
	$(eval id := $(shell docker create $(CONTAINER)))
	docker cp $(id):/pwn/. - | tar xv
	docker rm -v $(id)

.PHONY:
