import redis

r = redis.Redis()

print(r.get("counter"))

r.incr("counter")
print(r.get("counter"))
