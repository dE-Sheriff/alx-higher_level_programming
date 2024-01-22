#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
* print_python_list_info - prints info about a python list
* @o: the python object as param
* Returns: Nothing
*/
void print_python_list_info(PyObject *o)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *object;

	if (0 == strcmp(o->ob_type->tp_name, "list"))
	{
		list = (PyListObject *)o;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			object = list->ob_item[i];
			printf("Element %ld: %s\n", i, object->ob_type->tp_name);
		}
	}
}