// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pc_interfaces:msg/Student.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__MSG__DETAIL__STUDENT__STRUCT_HPP_
#define PC_INTERFACES__MSG__DETAIL__STUDENT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__pc_interfaces__msg__Student __attribute__((deprecated))
#else
# define DEPRECATED__pc_interfaces__msg__Student __declspec(deprecated)
#endif

namespace pc_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Student_
{
  using Type = Student_<ContainerAllocator>;

  explicit Student_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit Student_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    pc_interfaces::msg::Student_<ContainerAllocator> *;
  using ConstRawPtr =
    const pc_interfaces::msg::Student_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pc_interfaces::msg::Student_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pc_interfaces::msg::Student_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pc_interfaces::msg::Student_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pc_interfaces::msg::Student_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pc_interfaces::msg::Student_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pc_interfaces::msg::Student_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pc_interfaces::msg::Student_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pc_interfaces::msg::Student_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pc_interfaces__msg__Student
    std::shared_ptr<pc_interfaces::msg::Student_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pc_interfaces__msg__Student
    std::shared_ptr<pc_interfaces::msg::Student_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Student_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const Student_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Student_

// alias to use template instance with default allocator
using Student =
  pc_interfaces::msg::Student_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace pc_interfaces

#endif  // PC_INTERFACES__MSG__DETAIL__STUDENT__STRUCT_HPP_
