// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__STRUCT_H_
#define PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'student'
#include "pc_interfaces/msg/detail/student__struct.h"

/// Struct defined in srv/ReturnStudentAge in the package pc_interfaces.
typedef struct pc_interfaces__srv__ReturnStudentAge_Request
{
  pc_interfaces__msg__Student student;
} pc_interfaces__srv__ReturnStudentAge_Request;

// Struct for a sequence of pc_interfaces__srv__ReturnStudentAge_Request.
typedef struct pc_interfaces__srv__ReturnStudentAge_Request__Sequence
{
  pc_interfaces__srv__ReturnStudentAge_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pc_interfaces__srv__ReturnStudentAge_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ReturnStudentAge in the package pc_interfaces.
typedef struct pc_interfaces__srv__ReturnStudentAge_Response
{
  int32_t age;
} pc_interfaces__srv__ReturnStudentAge_Response;

// Struct for a sequence of pc_interfaces__srv__ReturnStudentAge_Response.
typedef struct pc_interfaces__srv__ReturnStudentAge_Response__Sequence
{
  pc_interfaces__srv__ReturnStudentAge_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pc_interfaces__srv__ReturnStudentAge_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__STRUCT_H_
