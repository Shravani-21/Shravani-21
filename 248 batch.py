#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=5 
print(id(x),x)
x='hi'
print(id(x),x)
x=True
print(id(x),x)


# In[2]:


id('x')


# In[3]:


id('hi')


# In[4]:


import keyword
from keyword import kwlist


# In[5]:


print(kwlist)


# In[6]:


len(kwlist)
#we have 35 keywords in python


# In[7]:


a=56
b=76
c=45


# In[8]:


a


# In[9]:


a
b


# In[10]:


print(a)
print(b)
print(c)


# In[11]:


print(a,b,c)


# In[13]:


print(a,b,sep='*',end='||')
print(c)


# In[3]:


x=6
y=7
print(id(x),x)
print(id(y),y)
x='hi'
print(id(x),x)


# In[4]:


id(x)


# In[5]:


id(y)


# In[6]:


id('hi')


# In[7]:


x=45
y=67
z=87
print(x,y,z)


# In[8]:


print(x)
print(y)
print(z)


# In[13]:


print(x,z,sep='*', end='//')
print(y)


# In[14]:


import keyword
from keyword import kwlist


# In[16]:


print(kwlist)


# In[17]:


len(kwlist)


# In[25]:


x='hi'
y='hello'
z='good morning'
print(x,y,z)
x=56
y=6
z=6
print(x+y+z)
print(x//y//z)


# In[27]:


x=6
y=6
z=5
print(x*y*z)


# In[22]:


print(x/y/z)


# In[23]:


print(x-y-z)


# In[24]:


print(x//y//z) #floor division


# In[28]:


print(x%y%z)


# In[29]:


x=2
y=4
print(y/x)


# In[30]:


x=5
y=3
print(x//y)


# In[31]:


x=2
y=3
print(x**y)


# In[32]:


x=10
y=15
x==y #equals to


# In[33]:


x!=y #not equals to


# In[34]:


x>y #greaterthan


# In[35]:


x<y #lessthan


# In[38]:


x=10
y=15
x>=y #greaterthan orequals to


# In[39]:


x=10
y=15
x<=y #lessthan or equals to


# In[40]:


x,y='hi','hello'
x==y


# In[41]:


x!=y


# In[46]:


a='hi'
b='hi'
c=[1,2,3]
d=[1,2,3]
a==b


# In[45]:


c==d


# In[48]:


print(id(a), id(b))


# In[49]:


print(a is b)


# In[50]:


print(id(c),id(d))


# In[51]:


print(c is d)


# In[52]:


print(a is not b)


# In[ ]:





# In[66]:


a= 'iam going to out side'
b='iam unhealthy today'
print (a> b)
print(a<b)
print(a>b and a<b)
print(a<b and a>b)
print(a<b or a>b)
print(a>b or a<b)


# In[62]:


a=3
b=5
if(c>1 and c<1):


# In[68]:


'1' in '1,2,3'


# In[70]:


print(1 not in [1,2,3])
print(1 in [1,2,3])


# ### bitwise operator 

# In[76]:


print(5&7)#bitwise and
print(5|7)#bitwise or
print(5^7)#bitwise nor
print(~7)#bitwise  not
print(~-1)#bitwise not


# ~x=-(x+1) formula

# In[77]:


(~8)


# leftshift

# In[78]:


9<<4

rightshift
# In[80]:


3>>2


# In[ ]:




