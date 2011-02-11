Method Pickle
=============

MethodPickle (methodpickle) is a quick library that allows simple pickling
and unpickling of function and method invocation.  Function & method module
loading is handled automatically, and methods can be specified by name as
well.

The ability to pickle a method invocation allows for queueing and delayed
execution of arbitrary code.  This is useful for parallelization, logging,
queueing, etc.

Contact::
    Steve Lacy <github@slacy.com>
    Twitter: @sklacy
    http://slacy.com/blog

Features & Usage
----------------

Please see the unit tests in test.py for some more verbose examples, but
I'll go through a quick example here.::

  from methodpickle.defer import defer

  def some_function(x, y):
      return x*x + y*y

  def some_class(object):
      def __init__(self, x):
          self._x = x

      def calc(self, y):
          return (self._x * self._x + y * y)

  if __name__ == '__main__':
      storable_func = defer(some_function, 5, 4)

      method_str = pickle.dumps(storable_func)

      # You can now take method_str and do whatever you like with it.  Write
      # it to a database, send it to another process, whatever.

      # Then, you can unpickle the stored method invocation, and run it,
      # like this:
      recovered_func = pickle.loads()
      assert(recovered_func.run() == 5*5 + 4*4)

      # It even supports pickling of classmethods.  Note that your class
      # must support pickling and the methods should have no side effects.

      i = some_class(2)
      storable_classmethod = defer(i, 3)

      classmethod_str = storable_method.dumps()
      recovered_classmethod = pickle.loads(classmethod_str)
      assert(recovered_classmethod.run() == 2*2 + 3*3)

For convenience, there's also a decorator form of the defer function, called
deferred.  Again, see the implementation or test.py for more details.
