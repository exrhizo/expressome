import argparse
# import logging
import os
import sys

# import cv2
# import tensorflow as tf

import expressome
import openpose

def run_openpose(dataset):
    print('Running openpose Runner!')


    dataset.load_videos()
    videos = dataset.videos

    for video in videos:
        print('Using video ', str(video))

    openpose.process_video(videos[0].path(), '/host/test_images/out_openpose/')



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument(
            'command',
            type=str,
            help='What command to use: cmupose, affectiva')

    args.add_argument(
            'dataset',
            type=str,
            help='The dataset to use.')

    # args.add_argument(
    #     '--summary_dir',
    #     type=str,
    #     default=os.path.join(os.getenv('TEST_TMPDIR', '/tmp'), 'expressome/logs'),
    #     help='Directory to write tensorflow summaries to.')

    FLAGS, unparsed = args.parse_known_args()

    dataset = expressome.get_dataset(FLAGS.dataset)
    if dataset is None:
        args.print_help()
        raise ValueError('Unknown dataset, ' + FLAGS.dataset)

    if FLAGS.command == 'openpose':
        run_openpose(dataset)
    elif FLAGS.command == 'affectiva':
        print('Doesn\'t exist yet')
    else:
        args.print_help()
        raise ValueError('Command doesn\'t exist, ' + FLAGS.command)
    	