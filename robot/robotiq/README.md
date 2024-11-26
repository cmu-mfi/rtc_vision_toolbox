## Troubleshooting Tests

- `AttributeError: module 'serial' has no attribute 'Serial'`

    ```shell
    $ pip uninstall serial
    $ pip install pyserial
    ```
- `could not open port /dev/ttyUSB0: [Errno 13] Permission denied: '/dev/ttyUSB0'`

    First ensure the gripper is connected to `ttyUSB0`. If it is connected to a different port, then change the port in the `robotiq.py` file.
    
    ```shell
    $ sudo usermod -a -G dialout $USER
    $ sudo reboot
    ```