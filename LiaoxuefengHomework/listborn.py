#列表生成器
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]