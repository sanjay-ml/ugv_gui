import threading
import time
from fastapi import FastAPI
import uvicorn
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


_latest = {"x": None, "y": None, "theta": None, "timestamp": None}
_lock = threading.Lock()

app = FastAPI(title="UGV Bridge")
node=None

class BridgeNode(Node):
    def __init__(self):
        super().__init__("bridge_node")
        self.create_subscription(Pose, "/turtle1/pose", self.cb, 10)
        self.pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("BridgeNode initialized")

    def cb(self, msg):
        with _lock:
            _latest["x"] = float(msg.x)
            _latest["y"] = float(msg.y)
            _latest["theta"] = float(msg.theta)
            _latest["timestamp"] = int(time.time())

@app.get("/telemetry")
def get_telemetry():
    with _lock:
        return dict(_latest)
    
@app.post("/cmd_vel")
def cmd_vel(vx: float=0.0, wz:float=0.0):
    t=Twist()
    t.linear.x=vx
    t.angular.z=wz
    node.pub.publish(t)
    return{"sent":True}


def _start_api():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

def main():
    global node
    threading.Thread(target=_start_api, daemon=True).start()
    rclpy.init()
    node = BridgeNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
