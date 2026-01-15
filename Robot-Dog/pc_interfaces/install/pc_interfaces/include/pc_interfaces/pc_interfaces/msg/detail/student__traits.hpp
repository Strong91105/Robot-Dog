// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pc_interfaces:msg/Student.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__MSG__DETAIL__STUDENT__TRAITS_HPP_
#define PC_INTERFACES__MSG__DETAIL__STUDENT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pc_interfaces/msg/detail/student__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace pc_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Student & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Student & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Student & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace pc_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use pc_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pc_interfaces::msg::Student & msg,
  std::ostream & out, size_t indentation = 0)
{
  pc_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pc_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const pc_interfaces::msg::Student & msg)
{
  return pc_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<pc_interfaces::msg::Student>()
{
  return "pc_interfaces::msg::Student";
}

template<>
inline const char * name<pc_interfaces::msg::Student>()
{
  return "pc_interfaces/msg/Student";
}

template<>
struct has_fixed_size<pc_interfaces::msg::Student>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<pc_interfaces::msg::Student>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<pc_interfaces::msg::Student>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PC_INTERFACES__MSG__DETAIL__STUDENT__TRAITS_HPP_
