import airsim
import os
import time

def main():
    client = airsim.CarClient()
    client.confirmConnection()
    client.enableApiControl(True)
    print("API Control enabled: %s" % client.isApiControlEnabled())
    car_controls = airsim.CarControls()
    client.reset()

    tmp_dir = os.path.join(".", "airsim_car_images")
    print("Saving images to %s" % tmp_dir)

    car_state = client.getCarState()
    print("car_state is: %s" % str(car_state))
    collision_info = client.simGetCollisionInfo()
    print("collision_info is: %s" % str(collision_info))

    # go forward
    car_controls.throttle = 0.9
    car_controls.steering = 0
    client.setCarControls(car_controls)
    print("Go Forward")
    time.sleep(11.3)   # let car drive a bit

    car_controls.brake = 0.8
    car_controls.steering = 1.0
    client.setCarControls(car_controls)
    print("Go Right")
    time.sleep(2.5)

    car_controls.throttle = 0.9
    car_controls.steering = 0
    client.setCarControls(car_controls)
    print("Go Forward")
    time.sleep(11)   # let car drive a bit

    car_state = client.getCarState()
    print("car_state is: %s" % str(car_state))
    collision_info1 = client.simGetCollisionInfo()
    print("collision_info is: %s" % str(collision_info1))

    car_controls.brake = 1.0
    airsim.wait_key("Hit a key to continue")
    collision_info = client.simGetCollisionInfo()
    print("collision_info is: %s" % str(collision_info))
    client.reset()
    client.enableApiControl(False)

if __name__ == "__main__":
    main()
