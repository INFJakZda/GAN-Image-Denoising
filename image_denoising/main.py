import argparse
import os
import shutil
import cv2

from image_denoising.resources import Resources
from image_denoising.noise import add_noise


def noise_images(args, resources):
    # create folder for results
    results_dir = resources.get_resource_path(args.data_path + '_' + args.noise_mode)
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)

    resources_dir = resources.get_resource_path(args.data_path)
    for filename in os.listdir(resources_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(resources_dir, filename)
            image = cv2.imread(file_path)
            image_noisy = add_noise(image, args.noise_mode)
            dest_path = os.path.join(results_dir, args.noise_mode + "_" + filename)
            cv2.imwrite(dest_path, image_noisy)
            continue
        else:
            continue


def main():
    resources_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
    resources = Resources(resources_dir)

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    p_noise = subparsers.add_parser('noise')
    p_noise.add_argument('--data_path', type=str, default='lena', help='Data folder in resources')
    p_noise.add_argument('--noise_mode', choices=['gauss', 'sp', 'speckle'], help='Noise mode')
    p_noise.set_defaults(run_command=noise_images)

    args = parser.parse_args()

    args.run_command(args, resources)


if __name__ == '__main__':
    main()
