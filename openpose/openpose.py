import tensorflow as tf
import cv2
import scipy.misc


def load_graph(log_dir=None):
    tf.reset_default_graph()

    embed_writer = None
    if log_dir:
        embed_writer = tf.summary.FileWriter(log_dir + "/embed")

    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('/tmp/openpose_model.ckpt.meta')
        new_saver.restore(sess, '/tmp/openpose_model.ckpt')

        if embed_writer is not None:
            embed_writer.add_graph(sess.graph)

        test_image(sess)


    # print(repr(sess.graph))
    # writer.add_graph(sess.graph)


# print('The input placeholder is expecting an array of shape {} and type {}'.format(inputs.shape, inputs.dtype))


def test_image(sess):
    # print("=====  NAMES  =====")
    # for name in [tensor.name for tensor in tf.get_default_graph().as_graph_def().node]:
    #     print(name)
    inputs = tf.get_default_graph().get_tensor_by_name('inputs:0')
    body = tf.get_default_graph().get_tensor_by_name('concat_stage7:0')

    # img = cv2.imread('openpose/alex-in-car.jpg')
    img = cv2.imread('openpose/dance-tut-pose.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    res_img = cv2.resize(img, (656, 368))
    prep_img = res_img.reshape([1, 368, 656, 3])
        
    output_img = sess.run(body, feed_dict={
            inputs: prep_img
        })
    
    print(output_img.shape)    

    for i in range(0, output_img.shape[3]):
        chan = output_img[0,:,:,i]
        print('saving %d' % i)
        scipy.misc.imsave('/tmp/openpose_img_%d.jpg' % i, chan)

    print("Number of bytes per")
    print(output_img.nbytes)
        # print(chan.shape)

def video_pose():
    pass

# load_openpose_graph()
# create_pose_files(videos)
# sess = tf.InteractiveSession()
# writer = tf.summary.FileWriter('./log-test-openpose-tf', sess.graph)
# train()
