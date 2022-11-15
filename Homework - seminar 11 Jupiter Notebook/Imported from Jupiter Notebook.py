#!/usr/bin/env python
# coding: utf-8

# In[21]:


from sympy import*
from sympy.plotting import plot

init_printing()

x = Symbol('x')
f=-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30

plot(f,(x,-10,10))


# In[20]:


from sympy import*
from sympy.plotting import plot

init_printing()

x = Symbol('x')
f=-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30

plot(f,(x,1,3))


# In[19]:


from sympy import*
from sympy.plotting import plot

init_printing()

x = Symbol('x')
f=-12*x**4*sin(cos(x))-18*x**3+5*x**2+10*x-30

plot(f,(x,-100,100))


# In[ ]: