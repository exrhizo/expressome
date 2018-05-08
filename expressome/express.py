import argparse
import logging
import os
import sys

import cv2
import tensorflow as tf

import expressome
import openpose
import logsharing

log = logsharing.get_logger()
    

def cmu_openpose_runner(_):
    if tf.gfile.Exists(FLAGS.summary_dir):
        tf.gfile.DeleteRecursively(FLAGS.summary_dir)
    tf.gfile.MakeDirs(FLAGS.summary_dir)

    log.debug('Loading videos')

    dataset.load_videos()
    videos = dataset.videos

    for video in videos:
        log.debug('Using video ' + str(video))

    log.debug('Loading CMU openpose estimator')

    estimator = openpose.load_estimator()

    img = cv2.imread('/host/test_images/my/alex-in-car.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    rimg = cv2.resize(img, (656, 368))

    # estimator can work with different sizes
    humans = estimator.inference(rimg)

    drawn = estimator.draw_humans(rimg, humans, imgcopy=False)
    cv2.imwrite('/host/test_images/out/alex-in-car.jpg', drawn)

    # cmupose.load_graph(log_dir=FLAGS.summary_dir)

    # load_openpose_graph()
    # create_pose_files(videos)
    # sess = tf.InteractiveSession()
    # writer = tf.summary.FileWriter('./log-test-openpose-tf', sess.graph)
    # train()


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

    args.add_argument(
        '--summary_dir',
        type=str,
        default=os.path.join(os.getenv('TEST_TMPDIR', '/tmp'), 'expressome/logs'),
        help='Directory to write tensorflow summaries to.')

    FLAGS, unparsed = args.parse_known_args()

    dataset = expressome.get_dataset(FLAGS.dataset)
    if dataset is None:
        args.print_help()
        raise ValueError('Unknown dataset, ' + FLAGS.dataset)

    if FLAGS.command == 'cmu_openpose':
        tf.app.run(main=cmu_openpose_runner, argv=[sys.argv[0]] + unparsed)
    elif FLAGS.command == 'affectiva':
        print('Doesn\'t exist yet')
    else:
        args.print_help()
        raise ValueError('Command doesn\'t exist, ' + FLAGS.command)
    	