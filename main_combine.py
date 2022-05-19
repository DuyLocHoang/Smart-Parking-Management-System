import argparse
import yaml
from coordinates_generator import CoordinatesGenerator
from combine import MotionDetector
from colors import *
import logging
# from ALPR import MotionDetector

def main():
    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    image_file = args.image_file
    data_file = args.data_file
    # start_frame = args.start_frame

    if image_file is not None:
        with open(data_file, "w+") as points:
            generator = CoordinatesGenerator(image_file, points, COLOR_RED)
            generator.generate()

    with open(data_file, "r") as data:
        points = yaml.safe_load(data)
        print(points)
        detector = MotionDetector(args.video_file, points,args.weight_file,args.config_file,args.class_file)
        detector.detect_motion()


def parse_args():
    parser = argparse.ArgumentParser(description='Generates Coordinates File')

    parser.add_argument("--image",
                        dest="image_file",
                        required=False,
                        help="Image file to generate coordinates on",
                        default="images/parking_lot_1.png")

    parser.add_argument("--video",
                        dest="video_file",
                        required=True,
                        help="Video file to detect motion on",
                        default="videos/parking_lot_1.mp4")

    parser.add_argument("--data",
                        dest="data_file",
                        required=True,
                        help="Data file to be used with OpenCV",
                        default="data/coordinates_1.yml")

    # parser.add_argument("--start-frame",
    #                     dest="start_frame",
    #                     required=False,
    #                     default=1,
    #                     help="Starting frame on the video")
    parser.add_argument("--weight",
                        dest="weight_file",
                        required=True,
                        help='Path to weight file',
                        default="weights/yolov3.weights")
    parser.add_argument("--config",
                        dest="config_file",
                        required=True,
                        help='Path to config file',
                        default="cfg/yolov3.cfg")
    parser.add_argument("--classes",
                        dest="class_file",
                        required=True,
                        help='Path to class file',
                        default="yolov3.txt")
    return parser.parse_args()

# run :
"""
python main_combine.py --image images/parking_lot_1.png --data data/coordinates_1.yml --video videos/parking_lot_1.mp4 --start-frame 400 --weight weights/yolov3_10000.weights --config cfg/yolov3_tan.cfg"""

"""
python main_combine.py --image images/parking_lot_1.png --data data/coordinates_1.yml --video videos/parking_lot_1.mp4 --weight weights/yolov3.weights --config cfg/yolov3.cfg --classes yolov3.txt

"""


if __name__ == '__main__':
    main()
