## Tensorflow Summary

1. Tensorflow is an open source platform for high performance numerical computation.
2. **Tensor** is a data structure used to represent data(of same type) in multi-dimensional array.
3. **Rank** of a tensor is number of dimension of an object.It is also calles **order** or **degree**.
4. **Shape of Tensor** is the number of elements in each dimension.
5. **Constant** is a data structure which once assigned, its value cannot be changed at execution time(should be initialised with a value).
6. **Variable** : 
 * To store state of a graph
 * Mutable
 * Needs to be initialised during declaration.
 * Shape should be specified when constructing graph.
 * tf.assign() is used to change the value of the variable in future.
7. **Placeholder**:
 * Variable which doesn’t hold an initial value. Value to it can be assigned later in the program. 
 * The datatype of placeholder must be specified during the creation of the placeholder.
8. **Graph** is a flowchart of operations which need to be performed on input(Does not hold values).
9. **Session** :
 * Allows executing operations specified in a data flow graph.
 * It allocates resources.
 * Stores actual value of intermediate result.
10. **Eager Execution** means evaluating operations immediately, without building graphs.

