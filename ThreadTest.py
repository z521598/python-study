#! /usr/bin/env python
# *_* coding:UTF-8 *_*
import time

import thread

from threadtest.ThreadObj import ThreadObj;
from threadtest.Counter import Counter;

# t1 = ThreadObj(2);
# t1.start();
# lock1 = thread.allocate_lock();
# lock2 = thread.allocate_lock();
# lock3 = thread.allocate_lock();
#
# c1 = Counter(lock1);
# c2 = Counter(lock2);
# c3 = Counter(lock3);
#
# c1.start();
# c2.start();
# c3.start();
# 三个不同的锁,结果不正确
# print Counter.count;

# allocate_lock 和 allocate 等价
lock = thread.allocate_lock();


c1 = Counter(lock);
c2 = Counter(lock);
c3 = Counter(lock);

c1.start();
c2.start();
c3.start();
# 三个不同的锁,结果正确
print Counter.count;


