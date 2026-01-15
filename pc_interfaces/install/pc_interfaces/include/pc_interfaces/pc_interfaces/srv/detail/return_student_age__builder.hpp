// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__BUILDER_HPP_
#define PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pc_interfaces/srv/detail/return_student_age__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pc_interfaces
{

namespace srv
{

namespace builder
{

class Init_ReturnStudentAge_Request_student
{
public:
  Init_ReturnStudentAge_Request_student()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pc_interfaces::srv::ReturnStudentAge_Request student(::pc_interfaces::srv::ReturnStudentAge_Request::_student_type arg)
  {
    msg_.student = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pc_interfaces::srv::ReturnStudentAge_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pc_interfaces::srv::ReturnStudentAge_Request>()
{
  return pc_interfaces::srv::builder::Init_ReturnStudentAge_Request_student();
}

}  // namespace pc_interfaces


namespace pc_interfaces
{

namespace srv
{

namespace builder
{

class Init_ReturnStudentAge_Response_age
{
public:
  Init_ReturnStudentAge_Response_age()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pc_interfaces::srv::ReturnStudentAge_Response age(::pc_interfaces::srv::ReturnStudentAge_Response::_age_type arg)
  {
    msg_.age = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pc_interfaces::srv::ReturnStudentAge_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::pc_interfaces::srv::ReturnStudentAge_Response>()
{
  return pc_interfaces::srv::builder::Init_ReturnStudentAge_Response_age();
}

}  // namespace pc_interfaces

#endif  // PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__BUILDER_HPP_
