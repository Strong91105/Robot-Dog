// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pc_interfaces:srv/ReturnStudentAge.idl
// generated code does not contain a copyright notice
#include "pc_interfaces/srv/detail/return_student_age__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `student`
#include "pc_interfaces/msg/detail/student__functions.h"

bool
pc_interfaces__srv__ReturnStudentAge_Request__init(pc_interfaces__srv__ReturnStudentAge_Request * msg)
{
  if (!msg) {
    return false;
  }
  // student
  if (!pc_interfaces__msg__Student__init(&msg->student)) {
    pc_interfaces__srv__ReturnStudentAge_Request__fini(msg);
    return false;
  }
  return true;
}

void
pc_interfaces__srv__ReturnStudentAge_Request__fini(pc_interfaces__srv__ReturnStudentAge_Request * msg)
{
  if (!msg) {
    return;
  }
  // student
  pc_interfaces__msg__Student__fini(&msg->student);
}

bool
pc_interfaces__srv__ReturnStudentAge_Request__are_equal(const pc_interfaces__srv__ReturnStudentAge_Request * lhs, const pc_interfaces__srv__ReturnStudentAge_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // student
  if (!pc_interfaces__msg__Student__are_equal(
      &(lhs->student), &(rhs->student)))
  {
    return false;
  }
  return true;
}

bool
pc_interfaces__srv__ReturnStudentAge_Request__copy(
  const pc_interfaces__srv__ReturnStudentAge_Request * input,
  pc_interfaces__srv__ReturnStudentAge_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // student
  if (!pc_interfaces__msg__Student__copy(
      &(input->student), &(output->student)))
  {
    return false;
  }
  return true;
}

pc_interfaces__srv__ReturnStudentAge_Request *
pc_interfaces__srv__ReturnStudentAge_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__srv__ReturnStudentAge_Request * msg = (pc_interfaces__srv__ReturnStudentAge_Request *)allocator.allocate(sizeof(pc_interfaces__srv__ReturnStudentAge_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pc_interfaces__srv__ReturnStudentAge_Request));
  bool success = pc_interfaces__srv__ReturnStudentAge_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pc_interfaces__srv__ReturnStudentAge_Request__destroy(pc_interfaces__srv__ReturnStudentAge_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pc_interfaces__srv__ReturnStudentAge_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__init(pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__srv__ReturnStudentAge_Request * data = NULL;

  if (size) {
    data = (pc_interfaces__srv__ReturnStudentAge_Request *)allocator.zero_allocate(size, sizeof(pc_interfaces__srv__ReturnStudentAge_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pc_interfaces__srv__ReturnStudentAge_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pc_interfaces__srv__ReturnStudentAge_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__fini(pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      pc_interfaces__srv__ReturnStudentAge_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

pc_interfaces__srv__ReturnStudentAge_Request__Sequence *
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array = (pc_interfaces__srv__ReturnStudentAge_Request__Sequence *)allocator.allocate(sizeof(pc_interfaces__srv__ReturnStudentAge_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pc_interfaces__srv__ReturnStudentAge_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__destroy(pc_interfaces__srv__ReturnStudentAge_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pc_interfaces__srv__ReturnStudentAge_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__are_equal(const pc_interfaces__srv__ReturnStudentAge_Request__Sequence * lhs, const pc_interfaces__srv__ReturnStudentAge_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pc_interfaces__srv__ReturnStudentAge_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pc_interfaces__srv__ReturnStudentAge_Request__Sequence__copy(
  const pc_interfaces__srv__ReturnStudentAge_Request__Sequence * input,
  pc_interfaces__srv__ReturnStudentAge_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pc_interfaces__srv__ReturnStudentAge_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pc_interfaces__srv__ReturnStudentAge_Request * data =
      (pc_interfaces__srv__ReturnStudentAge_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pc_interfaces__srv__ReturnStudentAge_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pc_interfaces__srv__ReturnStudentAge_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pc_interfaces__srv__ReturnStudentAge_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
pc_interfaces__srv__ReturnStudentAge_Response__init(pc_interfaces__srv__ReturnStudentAge_Response * msg)
{
  if (!msg) {
    return false;
  }
  // age
  return true;
}

void
pc_interfaces__srv__ReturnStudentAge_Response__fini(pc_interfaces__srv__ReturnStudentAge_Response * msg)
{
  if (!msg) {
    return;
  }
  // age
}

bool
pc_interfaces__srv__ReturnStudentAge_Response__are_equal(const pc_interfaces__srv__ReturnStudentAge_Response * lhs, const pc_interfaces__srv__ReturnStudentAge_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // age
  if (lhs->age != rhs->age) {
    return false;
  }
  return true;
}

bool
pc_interfaces__srv__ReturnStudentAge_Response__copy(
  const pc_interfaces__srv__ReturnStudentAge_Response * input,
  pc_interfaces__srv__ReturnStudentAge_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // age
  output->age = input->age;
  return true;
}

pc_interfaces__srv__ReturnStudentAge_Response *
pc_interfaces__srv__ReturnStudentAge_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__srv__ReturnStudentAge_Response * msg = (pc_interfaces__srv__ReturnStudentAge_Response *)allocator.allocate(sizeof(pc_interfaces__srv__ReturnStudentAge_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pc_interfaces__srv__ReturnStudentAge_Response));
  bool success = pc_interfaces__srv__ReturnStudentAge_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pc_interfaces__srv__ReturnStudentAge_Response__destroy(pc_interfaces__srv__ReturnStudentAge_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pc_interfaces__srv__ReturnStudentAge_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__init(pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__srv__ReturnStudentAge_Response * data = NULL;

  if (size) {
    data = (pc_interfaces__srv__ReturnStudentAge_Response *)allocator.zero_allocate(size, sizeof(pc_interfaces__srv__ReturnStudentAge_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pc_interfaces__srv__ReturnStudentAge_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pc_interfaces__srv__ReturnStudentAge_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__fini(pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      pc_interfaces__srv__ReturnStudentAge_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

pc_interfaces__srv__ReturnStudentAge_Response__Sequence *
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array = (pc_interfaces__srv__ReturnStudentAge_Response__Sequence *)allocator.allocate(sizeof(pc_interfaces__srv__ReturnStudentAge_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pc_interfaces__srv__ReturnStudentAge_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__destroy(pc_interfaces__srv__ReturnStudentAge_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pc_interfaces__srv__ReturnStudentAge_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__are_equal(const pc_interfaces__srv__ReturnStudentAge_Response__Sequence * lhs, const pc_interfaces__srv__ReturnStudentAge_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pc_interfaces__srv__ReturnStudentAge_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pc_interfaces__srv__ReturnStudentAge_Response__Sequence__copy(
  const pc_interfaces__srv__ReturnStudentAge_Response__Sequence * input,
  pc_interfaces__srv__ReturnStudentAge_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pc_interfaces__srv__ReturnStudentAge_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pc_interfaces__srv__ReturnStudentAge_Response * data =
      (pc_interfaces__srv__ReturnStudentAge_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pc_interfaces__srv__ReturnStudentAge_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pc_interfaces__srv__ReturnStudentAge_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pc_interfaces__srv__ReturnStudentAge_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
