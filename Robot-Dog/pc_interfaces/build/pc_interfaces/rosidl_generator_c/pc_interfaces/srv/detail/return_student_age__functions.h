// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice

#ifndef PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__FUNCTIONS_H_
#define PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "pc_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "pc_interfaces/srv/detail/return_student_age__struct.h"

/// Initialize srv/ReturnStudentAge message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * pc_interfaces__srv__ReturnStudentAge_Request
 * )) before or use
 * pc_interfaces__srv__ReturnStudentAge_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Request__init(pc_interfaces__srv__ReturnStudentAge_Request * msg);

/// Finalize srv/ReturnStudentAge message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Request__fini(pc_interfaces__srv__ReturnStudentAge_Request * msg);

/// Create srv/ReturnStudentAge message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * pc_interfaces__srv__ReturnStudentAge_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
pc_interfaces__srv__ReturnStudentAge_Request *
pc_interfaces__srv__ReturnStudentAge_Request__create();

/// Destroy srv/ReturnStudentAge message.
/**
 * It calls
 * pc_interfaces__srv__ReturnStudentAge_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Request__destroy(pc_interfaces__srv__ReturnStudentAge_Request * msg);

/// Check for srv/ReturnStudentAge message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Request__are_equal(const pc_interfaces__srv__ReturnStudentAge_Request * lhs, const pc_interfaces__srv__ReturnStudentAge_Request * rhs);

/// Copy a srv/ReturnStudentAge message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Request__copy(
  const pc_interfaces__srv__ReturnStudentAge_Request * input,
  pc_interfaces__srv__ReturnStudentAge_Request * output);

/// Initialize array of srv/ReturnStudentAge messages.
/**
 * It allocates the memory for the number of elements and calls
 * pc_interfaces__srv__ReturnStudentAge_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__init(pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array, size_t size);

/// Finalize array of srv/ReturnStudentAge messages.
/**
 * It calls
 * pc_interfaces__srv__ReturnStudentAge_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__fini(pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array);

/// Create array of srv/ReturnStudentAge messages.
/**
 * It allocates the memory for the array and calls
 * pc_interfaces__srv__ReturnStudentAge_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
pc_interfaces__srv__ReturnStudentAge_Request__Sequence *
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__create(size_t size);

/// Destroy array of srv/ReturnStudentAge messages.
/**
 * It calls
 * pc_interfaces__srv__ReturnStudentAge_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__destroy(pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array);

/// Check for srv/ReturnStudentAge message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__are_equal(const pc_interfaces__srv__ReturnStudentAge_Request__Sequence * lhs, const pc_interfaces__srv__ReturnStudentAge_Request__Sequence * rhs);

/// Copy an array of srv/ReturnStudentAge messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__copy(
  const pc_interfaces__srv__ReturnStudentAge_Request__Sequence * input,
  pc_interfaces__srv__ReturnStudentAge_Request__Sequence * output);

/// Initialize srv/ReturnStudentAge message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * pc_interfaces__srv__ReturnStudentAge_Response
 * )) before or use
 * pc_interfaces__srv__ReturnStudentAge_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Response__init(pc_interfaces__srv__ReturnStudentAge_Response * msg);

/// Finalize srv/ReturnStudentAge message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Response__fini(pc_interfaces__srv__ReturnStudentAge_Response * msg);

/// Create srv/ReturnStudentAge message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * pc_interfaces__srv__ReturnStudentAge_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
pc_interfaces__srv__ReturnStudentAge_Response *
pc_interfaces__srv__ReturnStudentAge_Response__create();

/// Destroy srv/ReturnStudentAge message.
/**
 * It calls
 * pc_interfaces__srv__ReturnStudentAge_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Response__destroy(pc_interfaces__srv__ReturnStudentAge_Response * msg);

/// Check for srv/ReturnStudentAge message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Response__are_equal(const pc_interfaces__srv__ReturnStudentAge_Response * lhs, const pc_interfaces__srv__ReturnStudentAge_Response * rhs);

/// Copy a srv/ReturnStudentAge message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Response__copy(
  const pc_interfaces__srv__ReturnStudentAge_Response * input,
  pc_interfaces__srv__ReturnStudentAge_Response * output);

/// Initialize array of srv/ReturnStudentAge messages.
/**
 * It allocates the memory for the number of elements and calls
 * pc_interfaces__srv__ReturnStudentAge_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__init(pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array, size_t size);

/// Finalize array of srv/ReturnStudentAge messages.
/**
 * It calls
 * pc_interfaces__srv__ReturnStudentAge_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__fini(pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array);

/// Create array of srv/ReturnStudentAge messages.
/**
 * It allocates the memory for the array and calls
 * pc_interfaces__srv__ReturnStudentAge_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
pc_interfaces__srv__ReturnStudentAge_Response__Sequence *
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__create(size_t size);

/// Destroy array of srv/ReturnStudentAge messages.
/**
 * It calls
 * pc_interfaces__srv__ReturnStudentAge_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
void
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__destroy(pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array);

/// Check for srv/ReturnStudentAge message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__are_equal(const pc_interfaces__srv__ReturnStudentAge_Response__Sequence * lhs, const pc_interfaces__srv__ReturnStudentAge_Response__Sequence * rhs);

/// Copy an array of srv/ReturnStudentAge messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pc_interfaces
bool
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__copy(
  const pc_interfaces__srv__ReturnStudentAge_Response__Sequence * input,
  pc_interfaces__srv__ReturnStudentAge_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // PC_INTERFACES__SRV__DETAIL__RETURN_STUDENT_AGE__FUNCTIONS_H_
