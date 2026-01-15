// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__STRUCT_HPP_
#define PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'student'
#include "pc_interfaces/msg/detail/student__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Request __attribute__((deprecated))
#else
# define DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Request __declspec(deprecated)
#endif

namespace pc_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ReturnStudentAge_Request_
{
  using Type = ReturnStudentAge_Request_<ContainerAllocator>;

  explicit ReturnStudentAge_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : student(_init)
  {
    (void)_init;
  }

  explicit ReturnStudentAge_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : student(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _student_type =
    pc_interfaces::msg::Student_<ContainerAllocator>;
  _student_type student;

  // setters for named parameter idiom
  Type & set__student(
    const pc_interfaces::msg::Student_<ContainerAllocator> & _arg)
  {
    this->student = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Request
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Request
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ReturnStudentAge_Request_ & other) const
  {
    if (this->student != other.student) {
      return false;
    }
    return true;
  }
  bool operator!=(const ReturnStudentAge_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ReturnStudentAge_Request_

// alias to use template instance with default allocator
using ReturnStudentAge_Request =
  pc_interfaces::srv::ReturnStudentAge_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace pc_interfaces


#ifndef _WIN32
# define DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Response __attribute__((deprecated))
#else
# define DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Response __declspec(deprecated)
#endif

namespace pc_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct ReturnStudentAge_Response_
{
  using Type = ReturnStudentAge_Response_<ContainerAllocator>;

  explicit ReturnStudentAge_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age = 0l;
    }
  }

  explicit ReturnStudentAge_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age = 0l;
    }
  }

  // field types and members
  using _age_type =
    int32_t;
  _age_type age;

  // setters for named parameter idiom
  Type & set__age(
    const int32_t & _arg)
  {
    this->age = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Response
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pc_interfaces__srv__ReturnStudentAge_Response
    std::shared_ptr<pc_interfaces::srv::ReturnStudentAge_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ReturnStudentAge_Response_ & other) const
  {
    if (this->age != other.age) {
      return false;
    }
    return true;
  }
  bool operator!=(const ReturnStudentAge_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ReturnStudentAge_Response_

// alias to use template instance with default allocator
using ReturnStudentAge_Response =
  pc_interfaces::srv::ReturnStudentAge_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace pc_interfaces

namespace pc_interfaces
{

namespace srv
{

struct ReturnStudentAge
{
  using Request = pc_interfaces::srv::ReturnStudentAge_Request;
  using Response = pc_interfaces::srv::ReturnStudentAge_Response;
};

}  // namespace srv

}  // namespace pc_interfaces

#endif  // PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__STRUCT_HPP_
