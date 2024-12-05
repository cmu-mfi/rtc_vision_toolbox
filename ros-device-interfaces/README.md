# ROS DEVICE INTERFACES

Some setups may need to interface with ROS devices. Classes for those devices use [websocket server](https://github.com/RobotWebTools/rosbridge_suite/tree/ros1) to interface with ROS nodes. Below are list of classes in the repo that uses ROS devices.

* `camera/zed_ros` - ZED cameras
* `camera/rs_ros` - realsense cameras
* `camera/camera_ros` - template to define a new ROS camera class
* `robot/ros_robot`- Robots using MoveIt! interfaces
* `robot/ros_template` - template to define a new ROS robot class


The folder `ros-device-interfaces` contains different setups with a docker-compose file each to launch the ROS devices. The `compose.yml` file is used to launch the ROS devices and Websocket server. 

### Setup 1

Yaskawa robot, Intel D405 and Zed-X mini are ROS devices in the setup below.

![](setup1/vision-system.png)

### Dummy Setup
