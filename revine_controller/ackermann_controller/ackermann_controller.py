#include "rclcpp/rclcpp.hpp"
#include "ackermann_msgs/msg/ackermann_drive_stamped.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "nav_msgs/msg/odometry.hpp"

class AckermannController : public rclcpp::Node
{
public:
    AckermannController() : Node("ackermann_controller")
    {
        // Create publishers
        ackermann_pub_ = this->create_publisher<ackermann_msgs::msg::AckermannDriveStamped>(
            "ackermann_cmd", 10);
            
        // Create subscribers
        cmd_vel_sub_ = this->create_subscription<geometry_msgs::msg::Twist>(
            "cmd_vel", 10,
            std::bind(&AckermannController::cmdVelCallback, this, std::placeholders::_1));
            
        // Parameters
        wheelbase_ = this->declare_parameter("wheelbase", 1.0);
        max_steering_angle_ = this->declare_parameter("max_steering_angle", 0.7);
    }

private:
    void cmdVelCallback(const geometry_msgs::msg::Twist::SharedPtr msg)
    {
        auto ackermann_cmd = ackermann_msgs::msg::AckermannDriveStamped();
        ackermann_cmd.header.stamp = this->now();
        ackermann_cmd.header.frame_id = "base_link";
        
        // Convert twist to ackermann command
        double steering_angle = atan2(msg->angular.z * wheelbase_, msg->linear.x);
        steering_angle = std::clamp(steering_angle, -max_steering_angle_, max_steering_angle_);
        
        ackermann_cmd.drive.steering_angle = steering_angle;
        ackermann_cmd.drive.speed = msg->linear.x;
        
        ackermann_pub_->publish(ackermann_cmd);
    }

    rclcpp::Publisher<ackermann_msgs::msg::AckermannDriveStamped>::SharedPtr ackermann_pub_;
    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_sub_;
    double wheelbase_;
    double max_steering_angle_;
};

int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AckermannController>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
