// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pc_interfaces:msg/Student.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__MSG__DETAIL__STUDENT__STRUCT_H_
#define PC_INTERFACES__MSG__DETAIL__STUDENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Student in the package pc_interfaces.
typedef struct pc_interfaces__msg__Student
{
  uint8_t structure_needs_at_least_one_member;
} pc_interfaces__msg__Student;

// Struct for a sequence of pc_interfaces__msg__Student.
typedef struct pc_interfaces__msg__Student__Sequence
{
  pc_interfaces__msg__Student * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pc_interfaces__msg__Student__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PC_INTERFACES__MSG__DETAIL__STUDENT__STRUCT_H_
