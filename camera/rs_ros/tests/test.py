import cv2
import numpy as np

from camera.rs_ros.rs_ros import RsRos


# TEST1: GET RGB/DEPTH/INFRA INTRINSICS. WORKS OK ✓
def test1(camera):
    rgb_intrinsics = camera.get_rgb_intrinsics()
    depth_intrinsics = camera.get_depth_intrinsics()
    infrared_intrinsics = camera.get_infra_intrinsics()
    print("RGB intrinsics: \n", rgb_intrinsics)
    print("Depth intrinsics: \n", depth_intrinsics)
    print("Infrared intrinsics: \n", infrared_intrinsics)

# TEST2: GET RGB IMAGE. WORKS OK ✓
def test2(camera):
    image = camera.get_rgb_image()
    cv2.imwrite("rgb_image.png", image)


# TEST3: GET DEFAULT DEPTH IMAGE and DATA. WORKS OK ✓
def test3(camera):
    depth_image = camera.get_raw_depth_data()

    print("Depth image shape: ", depth_image.shape)
    print("Depth image type: ", depth_image.dtype)
    print("Depth image: \n", depth_image[:4, :4])
    print("Max depth value: ", np.nanmax(depth_image))
    print("Min depth value: ", np.nanmin(depth_image))

    np.save("depth_data.npy", depth_image)

    depth_image = camera.get_depth_image()

    cv2.imwrite("depth_image.png", depth_image)

    depth_image = camera.get_colormap_depth_image()
    cv2.imwrite("depth_image_colormap.png", depth_image)


# TEST4: GET DEFAULT POINT CLOUD. To be Implemented
def test4(camera):
    print("Getting default point cloud")
    point_cloud = camera.get_point_cloud(method='default', save_points=True)
    print("Point cloud shape: ", np.asarray(point_cloud.points).shape)


# TEST5: GET IGEV DEPTH IMAGE. WORKS OK ✓
def test5(camera):
    depth_image = camera.get_raw_depth_data(method="igev")

    print("Depth image shape: ", depth_image.shape)
    print("Depth image type: ", depth_image.dtype)
    print("Depth image: \n", depth_image[:4, :4])
    print("Max depth value: ", np.nanmax(depth_image))
    print("Min depth value: ", np.nanmin(depth_image))
    np.save("depth_igev_data.npy", depth_image)

    igev_depth_image = camera.get_depth_image(method="igev")
    cv2.imwrite("igev_depth_image.png", igev_depth_image)
    igev_depth_image = camera.get_colormap_depth_image(method="igev")
    cv2.imwrite("igev_depth_image_colormap.png", igev_depth_image)


# TEST6: GET IGEV POINT CLOUD. WORKS OK ✓
def test6(camera):
    print("Getting point cloud using IGEV method")
    point_cloud = camera.get_point_cloud(method="igev", save_points=True, max_mm = 2000)
    print("Point cloud shape: ", np.asarray(point_cloud.points).shape)


if __name__ == "__main__":

    print("Testing Realsense ROS class")

    camera = RsRos(camera_node=f"/camera/realsense2_camera", camera_type="d405", rosmaster_ip="192.168.1.2", debug=True)

    print("Available tests: ")
    print("1. Get RGB/DEPTH/INFRA intrinsics")
    print("2. Get RGB image")
    print("3. Get default depth image")
    print("4. Get default point cloud")
    print("5. Get IGEV depth image")
    print("6. Get IGEV point cloud")
    test = input("Enter test number (1-6): ")

    match test:
        case "1":
            test1(camera)
        case "2":
            test2(camera)
        case "3":
            test3(camera)
        case "4":
            test4(camera)
        case "5":
            test5(camera)
        case "6":
            test6(camera)
        case _:
            print("Invalid test number")
