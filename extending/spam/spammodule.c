#include <python3.2/Python.h> //always include before all other headers as it introduces #defs
//----------------------------------------------------------------------------------------//
static PyObject * 
spam_system(
            PyObject *self,//points to this func or an object in case of C++ method
            PyObject *args //receives parameters for the function call as a python tuple reference
           )
{
    const char *command; 
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command)) //converts python parameter types recd. to C values
        return NULL;                            //returns NULL and raises an exception if mapping fails

    sts = system(command);
    return PyLong_FromLong(sts);
}
//----------------------------------------------------------------------------------------//
static PyMethodDef SpamMethods[] = //function/method map for python to call into module
{
    {
      "system",                     //string name of the function 
      spam_system,                  //name of the function
      METH_VARARGS,                 //indicates TUPLE only params, METH_VARARGS|METH_KEYWORDS indicates
                                    //tuples and dicts. Then another PyObject * kwars must be recd. by
                                    //module func and PyArg_ParseTupleAndKeywords(...) must be used
      "Execute a shell command."    //description
    },
    
    {NULL, NULL, 0, NULL}        /* Sentinel */
};
//----------------------------------------------------------------------------------------//
static struct PyModuleDef spammodule = //Module def to give method map table to python in the mod. init func
{
   PyModuleDef_HEAD_INIT,

   "spam",   /* name of module */

   NULL, //spam_doc, /* module documentation, may be NULL */

   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */

   SpamMethods
};
//----------------------------------------------------------------------------------------//
PyMODINIT_FUNC PyInit_spam(void) //Inits module and passes maps & exceptions etc to python
{
    return PyModule_Create(&spammodule);
}
//----------------------------------------------------------------------------------------//
int
main(int argc, char *argv[])
{
    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("spam", PyInit_spam);

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(argv[0]);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("spam");
}
//----------------------------------------------------------------------------------------//
