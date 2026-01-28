// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__TRAITS_HPP_
#define PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pc_interfaces/srv/detail/return_student_age__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'student'
#include "pc_interfaces/msg/detail/student__traits.hpp"

namespace pc_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const ReturnStudentAge_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: student
  {
    out << "student: ";
    to_flow_style_yaml(msg.student, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ReturnStudentAge_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: student
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "student:\n";
    to_block_style_yaml(msg.student, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ReturnStudentAge_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace pc_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use pc_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pc_interfaces::srv::ReturnStudentAge_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  pc_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pc_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pc_interfaces::srv::ReturnStudentAge_Request & msg)
{
  return pc_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pc_interfaces::srv::ReturnStudentAge_Request>()
{
  return "pc_interfaces::srv::ReturnStudentAge_Request";
}

template<>
inline const char * name<pc_interfaces::srv::ReturnStudentAge_Request>()
{
  return "pc_interfaces/srv/ReturnStudentAge_Request";
}

template<>
struct has_fixed_size<pc_interfaces::srv::ReturnStudentAge_Request>
  : std::integral_constant<bool, has_fixed_size<pc_interfaces::msg::Student>::value> {};

template<>
struct has_bounded_size<pc_interfaces::srv::ReturnStudentAge_Request>
  : std::integral_constant<bool, has_bounded_size<pc_interfaces::msg::Student>::value> {};

template<>
struct is_message<pc_interfaces::srv::ReturnStudentAge_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace pc_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const ReturnStudentAge_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: age
  {
    out << "age: ";
    rosidl_generator_traits::value_to_yaml(msg.age, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ReturnStudentAge_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: age
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "age: ";
    rosidl_generator_traits::value_to_yaml(msg.age, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ReturnStudentAge_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace pc_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use pc_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pc_interfaces::srv::ReturnStudentAge_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  pc_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pc_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const pc_interfaces::srv::ReturnStudentAge_Response & msg)
{
  return pc_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<pc_interfaces::srv::ReturnStudentAge_Response>()
{
  return "pc_interfaces::srv::ReturnStudentAge_Response";
}

template<>
inline const char * name<pc_interfaces::srv::ReturnStudentAge_Response>()
{
  return "pc_interfaces/srv/ReturnStudentAge_Response";
}

template<>
struct has_fixed_size<pc_interfaces::srv::ReturnStudentAge_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<pc_interfaces::srv::ReturnStudentAge_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<pc_interfaces::srv::ReturnStudentAge_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<pc_interfaces::srv::ReturnStudentAge>()
{
  return "pc_interfaces::srv::ReturnStudentAge";
}

template<>
inline const char * name<pc_interfaces::srv::ReturnStudentAge>()
{
  return "pc_interfaces/srv/ReturnStudentAge";
}

template<>
struct has_fixed_size<pc_interfaces::srv::ReturnStudentAge>
  : std::integral_constant<
    bool,
    has_fixed_size<pc_interfaces::srv::ReturnStudentAge_Request>::value &&
    has_fixed_size<pc_interfaces::srv::ReturnStudentAge_Response>::value
  >
{
};

template<>
struct has_bounded_size<pc_interfaces::srv::ReturnStudentAge>
  : std::integral_constant<
    bool,
    has_bounded_size<pc_interfaces::srv::ReturnStudentAge_Request>::value &&
    has_bounded_size<pc_interfaces::srv::ReturnStudentAge_Response>::value
  >
{
};

template<>
struct is_service<pc_interfaces::srv::ReturnStudentAge>
  : std::true_type
{
};

template<>
struct is_service_request<pc_interfaces::srv::ReturnStudentAge_Request>
  : std::true_type
{
};

template<>
struct is_service_response<pc_interfaces::srv::ReturnStudentAge_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__TRAITS_HPP_
