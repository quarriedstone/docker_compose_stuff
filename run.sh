docker build -t quarriedstone/rabbit .;
docker run --name rabbit -d -e HOST=10.90.137.109 quarriedstone/rabbit
