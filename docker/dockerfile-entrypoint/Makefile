build:
	docker build -t ctop .
run:
	docker run -it ctop
run2:
	docker exec -it ctop -d 2
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
