class Ride:
    count = 0

    @classmethod
    def start(cls):
        cls.count += 1

    @classmethod
    def stop(cls):
        cls.count -= 1


r1 = Ride()
r2 = Ride()

r1.start()
r2.start()

r2.stop()

print(Ride.count)
