from rclpy.node import Node
from tf2_ros import TransformBroadcaster, Buffer, TransformListener
from geometry_msgs.msg import TransformStamped

class TFWrapper(Node):
    def __init__(self):
        super().__init__('ekf_tf_wrapper')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.02, self.rebroadcast)

    def rebroadcast(self):
        try:
            t = self.tf_buffer.lookup_transform('base_link', 'odom', rclpy.time.Time())
            # เพิ่ม callerid
            t._connection_header = {'callerid': 'ekf_filter_node'}
            self.tf_broadcaster.sendTransform(t)
        except Exception:
            pass

def main():
    import rclpy
    rclpy.init()
    node = TFWrapper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

