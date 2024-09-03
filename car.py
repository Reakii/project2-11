class BMW:
    def start(self):
        return "BMW is starting..."

    def stop(self):
        return "BMW is stopping..."

class Ferrari:
    def start(self):
        return "Ferrari is starting..."

    def stop(self):
        return "Ferrari is stopping..."


def vehicle_actions(vehicle):
    print(vehicle.start())
    print(vehicle.stop())


bmw = BMW()
ferrari = Ferrari()


vehicle_actions(bmw)
vehicle_actions(ferrari)
