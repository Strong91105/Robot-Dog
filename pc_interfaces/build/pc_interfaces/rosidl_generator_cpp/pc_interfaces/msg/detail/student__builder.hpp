// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pc_interfaces:msg/Student.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__MSG__DETAIL__STUDENT__BUILDER_HPP_
#define PC_INTERFACES__MSG__DETAIL__STUDENT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pc_interfaces/msg/detail/student__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pc_interfaces
{

namespace msg
{


}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pc_interfaces::msg::Student>()
{
  return ::pc_interfaces::msg::Student(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace pc_interfaces

#endif  // PC_INTERFACES__MSG__DETAIL__STUDENT__BUILDER_HPP_
