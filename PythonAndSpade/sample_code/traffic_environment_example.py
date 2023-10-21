class TrafficLight:
    def __init__(self, color):
        self.color = color

    def change(self, new_color):
        self.color = new_color


class RoadSign:
    def __init__(self, sign_type):
        self.sign_type = sign_type


class Lane:
    def __init__(self, lane_id):
        self.lane_id = lane_id
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)


class Road:
    def __init__(self, name, num_lanes):
        self.name = name
        self.lanes = [Lane(i) for i in range(num_lanes)]


class Intersection:
    def __init__(self, name, traffic_light_color, road_sign_type):
        self.name = name
        self.traffic_light = TrafficLight(traffic_light_color)
        self.road_sign = RoadSign(road_sign_type)


class Environment:
    def __init__(self):
        road_1 = Road("Road_1", 2)  # 2 lanes
        road_2 = Road("Road_2", 3)  # 3 lanes

        intersection_1 = Intersection("Intersection_1", "Red", "Stop")
        intersection_2 = Intersection("Intersection_2", "Green", "Yield")

        # data structures to keep the data related to the environment
        self.roads = [road_1, road_2]
        self.intersections = [intersection_1, intersection_2]

    def add_road(self, road):
        self.roads.append(road)

    def add_intersection(self, intersection):
        self.intersections.append(intersection)

    # displays the environment.
    def display(self):
        for road in self.roads:
            print(f"{road.name}: ", end='')
            for lane in road.lanes:
                print(f" Lane {lane.lane_id}", end='')
            print()

        print("Intersections: ")
        for intersection in self.intersections:
            print(
                f"{intersection.name} - Traffic Light: {intersection.traffic_light.color}, Road Sign: {intersection.road_sign.sign_type}")


if __name__ == "__main__":
    env = Environment()
    env.display()
