from pc_interfaces.srv import ReturnStudentAge
from pc_interfaces.msg import Student

import rclpy
from rclpy.node import Node


class CalculateAgeService(Node):

    def __init__(self):
        super().__init__('calculate_age_service_node')
        self.srv = self.create_service(ReturnStudentAge, 'calculate_age_service', self.calculate_age_cb)

    def calculate_age_cb(self, request, response):
        response.age = 2025 - request.student.year_of_birth
        self.get_logger().info(f'Incoming request: Student {request.student.name} was born in {request.student.year_of_birth}')
        self.get_logger().info(f'Student {request.student.name} is {response.age}')

        return response


def main():
    rclpy.init()

    calculate_age_service = CalculateAgeService()

    rclpy.spin(calculate_age_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()