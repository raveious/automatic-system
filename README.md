# MTU - EE5900 - Intro. to Robotics - Project 2

<iframe width="560" height="315" src="https://www.youtube.com/embed/H7ok3Q6NmVc" frameborder="0" allowfullscreen></iframe>

## Tasks
 1. Build an empty gazebo world for your Jackal (remove the obstacles).
 2. Write or include ROS node that provides teleop capability or use the ros keyboard teleop package.
 3. Write a ROS node that drives the Jackal in Gazebo with the following behavior definition:
  1. Rotate the Jackal by a random angle.
  2. Drive forward a random time
  3. Stop the Jackal and return to step 1
  4. Random movement should stop if a teleop command is presented and continue after 10 seconds if no teleop commands are presented.
 4. Develop a launch file that brings up a Jackal in the empty world and runs your random walk code alongside the tele-op interrupt

## [Tutorial Completion](https://www.clearpathrobotics.com/assets/guides/jackal/simulation.html)
- [x] [Ian Wakely](https://github.com/raveious) (leader)
- [x] [Haden Wasserbaech](https://github.com/spartanhaden)
- [x] [Akhil Kurup](https://github.com/amkurup)

## Development

After cloning this repository, follow these steps to setup the development environment
```
$ cd drunken_robot/src
$ catkin_init_workspace
$ cd ..
$ catkin_make
$ source devel/setup.bash
```

## Execution

This project can be launched using `roslaunch` by calling

```
$ roslaunch drunken_robot drunken_robot.launch
```

Assuming that you checked out this project from github, then you're going to have to go through [development instructions](#development).

### Paramaters
name | default | description
:---|:---:|:---:
delay | 2.0 | How long the random input node will wait before changing to "drunk mode"
user rate | 2 | How often random input is published
linear max | 2 | Maximum forward speed allowed in random function
linear min | -1 | Maximum backward speed allowed in random function
angular max | 2 | Maximum angle change allowed in random function
angular min | -1 | Minimum angle change allowed in random function

## Dependant packages
- https://github.com/ros-teleop/teleop_twist_keyboard
