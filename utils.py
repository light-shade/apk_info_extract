"""
@author:qh
@datetime:2019-3-15
@mood:<(*￣▽￣*)/
"""
img = ("AAABAAQAMDAAAAEAIACoJQAARgAAACAgAAABACAAqBAAAO4lAAAYGAAAAQAgAIgJAACWNgAAEBAAAAEAIABoBAAAHkAAACgAAAAwAA"
       "AAYAAAAAEAIAAAAAAAgCUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAAAAAABwbGwIcGxsPHBsbIRwbG0McGxtvHBsbohwbG8ocGxvmHBsb+BwbG/scGxvuHBsb1xwbG7ccGxuPHBsbXx0cHC0g"
       "Hx8WHBsbCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbGhoEGxoaHRwbG04bGhqQGxoayxsaGvUcGxv/Gxoa/hsaGv"
       "4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGuAcGxuuGxoacBsaGjYcGxsQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGxoaARwb"
       "GxkbGhpcGxoapxwbG+Q bGhr+Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/"
       "Gxoa8hsaGsocGxuHGxoaNRwbGwkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcGxsCHBsbPxwbG6McGxvjHBsb/BwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/"
       "IB8f/zU0NP8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxvzHBsbxhwbG3EcGxsaAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABsaGgocGxtlGxoa5RwbG/kbGhr+Gx"
       "oa/hwbG/8bGhr+Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/W1pa/q+vr/4eHR3/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4"
       "cGxv/Gxoa/RwbG/AbGhqoGxoaNRwbGwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAcGxsCGxoaIhsaGo0cGxv2Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hsaGv4cGxv/Gxoa/hsaGv4tLCz/tbW1/vz8/P5ubm7"
       "/HBsb/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+GxoazxwbG1QbGhoKAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwbGwIcGxsqHBsbmxwbG/EcGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb"
       "/xwbG/8cGxv/HBsb/x4dHf9ramr/5ubm///////Pz8//NzY2/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv"
       "/HBsb/xwbG9McGxtdHBsbDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABsaGiEcGxubGxoa8RsaGv4"
       "cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hsaGv4cGxv/Gxoa/jQ0NP6wsLD//f39/v7+/v7z8/P/iYmJ/iAfH/4cGxv/Gxoa/hsa"
       "Gv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/wbGhrNGxoaWhwbGwsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
       "AAAAAAAAAAAGxoaCBsaGoscGxvxGxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hsaGv4cGxv/Hh0d/mZlZf7u7u7//v"
       "7+/v7+/v7+/v7/z8/P/kpKSv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr6GxoaxBwbG0QbGho"
       "EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcGxsCHBsbYBwbG/YcGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8c"
       "Gxv/HBsb/xwbG/8cGxv/MC8v/76+vv/+/v7/////////////////+vr6/5aWlv8nJib/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG"
       "/8cGxv/HBsb/xwbG/8cGxv/HBsb+xwbG7QcGxsiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABsaGgEcGxs6Gxoa5BsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hsaGv4cGxv/b25u/vz8/P7//////v7+/v7+/v7//////v7+/uLi4v5aWVn/HRwc/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/0bGhqUGxoaCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwbGxUcGxudHBsb+BwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8qKSn/0tHR//////////////////////////////////////+srKz/Kyoq/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxvlHBsbRgAAAAAAAAAAAAAAAAAAAAAAAAAAGxoaAhsaGlUcGxvgGxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hsaGv51dHT/+vr6/v7+/v7//////v7+/v7+/v7//////v7+/v7+/v7x8fH/YF9f/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+GxoapBwbGxMAAAAAAAAAAAAAAAAAAAAAGxoaFxsaGp8cGxv7Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/jQ0NP7Ly8v//v7+/v7+/v7//////v7+/v7+/v7//////v7+/v7+/v7/////ycnJ/iAfH/4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa5BwbG00AAAAAAAAAAAAAAAAcGxsBHBsbRxwbG+AcGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/Hx4e/4eHh//z8/P//////////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/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr8GxoaVgAAAAAcGxvsHBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/ywrK/+srKz//f39/////////////////+bm5v9MS0v/OTg4/5aVlf/z8/P/6Ojo/0FBQf8cGxv/Tk1N/9jY2P//////////////////////////////////////1tbW/0JBQf8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv1HBsbUAAAAAAcGxvSGxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Hh0d/mRjY//j4+P+/v7+/v/////+/v7+9/f3/peXl/5eXV3/v7+//v39/f7//////v7+/nNycv4cGxv/NTQ0/rS0tP7//////v7+/v7+/v7//////v7+/v7+/v7/////9fX1/pOTk/8lJCT+Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhrnGxoaRwAAAAAcGxuvGxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/MC8v/quqqv/9/f3+/v7+/v/////+/v7+4ODg/qioqP7Z2dn//v7+/v7+/v7//////v7+/ry7u/4cGxv/ISAg/pCQkP76+vr//v7+/v7+/v7//////v7+/v7+/v7//////v7+/tfX1/9TUlL+HBsb/hwbG/8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/8bGhrWGxoaOgAAAAAcGxuDHBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8dHBz/Xl1d/+3t7f/////////////////+/v7/8vLy//Ly8v/+/v7///////////////////////Pz8/8tLCz/HBsb/2tqav/o6Oj///////////////////////////////////////r6+v+cnJz/LCsr/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxvBHBsbKwAAAAAcGxtUGxoa/RsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4mJSX/urm5/v7+/v/+/v7+/v7+/v/////+/v7+/v7+/v7+/v7//////v7+/v7+/v7//////v7+/v7+/v5oaGj/Gxoa/jw7O/7ExMT//f39/v7+/v7//////v7+/v7+/v7//////v7+/v/////r6+v+VVVV/hwcHP8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/4bGhqmHRwcGQAAAAAcGxsmGxoa0xsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv5kY2P//v7+/v/////+/v7+/v7+/v/////+/v7+/v7+/v7+/v7//////v7+/v7+/v7/////+Pj4/tHR0f5HRkb/Gxoa/hsaGv47Ojr/vr29/vv7+/7//////v7+/v7+/v7//////v7+/v/////+/v7+vr29/iopKf8bGhr+Gxoa/hwbG/8bGhr+Gxoa/hwbG/AdHBx0ISAgBQAAAAAcGxsQHBsblBwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/yopKf/Hx8f///////////////////////////////////////////////////////7+/v/s7Oz/pqWl/z08PP8cGxv/HBsb/xwbG/8cGxv/NjU1/7a2tv/39/f/////////////////////////////////+/v7/2hnZ/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG9olJCRGAAAAAAAAAAAgHx8EIB8fWxsaGu4cGxv/Gxoa/hsaGv4cGxv/Gxoa/nFxcf7z8/P//v7+/v/////+/v7+/v7+/v/////+/v7+/v7+/v7+/v7//////f39/t7e3v5/f3//MC8v/hwbG/4cGxv/Gxoa/hsaGv4cGxv/HBsb/jo6Ov6lpaX/8/Pz/v7+/v7//////v7+/v/////+/v7+/v7+/szMzP8vLi7+Gxoa/hwbG/8bGhr+Gxoa+xwbG7AqKSkcAAAAAAAAAAAAAAAAKCcnKBsaGrscGxv/Gxoa/hsaGv4cGxv/NTQ0/sLBwf79/f3//v7+/v/////+/v7+/v7+/v/////+/v7+/v7+/v7+/v7/////zc3N/llYWP4mJSX/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/h0cHP41NDT/m5ub/vLy8v7//////v7+/v/////+/v7+/v7+/vX19f+AgID+HBsb/hwbG/8bGhr+Gxoa8CgnJ2tGRUUDAAAAAAAAAAAAAAAAMjExBx0cHHMcGxvvHBsb/xwbG/8eHR3/fn19//Dw8P///////////////////////////////////////v7+//f39/+ura3/MjEx/x4dHf8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/KCcn/4yMjP/x8fH///////////////////////7+/v/R0ND/RURE/xwbG/8cGxv/HBsbxDU0NCUAAAAAAAAAAAAAAAAAAAAAAAAAADg3NyMcGxu4Gxoa/BwbG/5DQkL/x8fH/v7+/v7//////v7+/v/////+/v7+/v7+/v/////7+/v+3t7e/n19ff4nJib/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/h0cHP57e3v/6enp/v7+/v/+/v7+/v7+/v/////4+Pj+mZiY/iYlJf8bGhr0KCcnYQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFVUVAMoJydZHBsb7CMiIv+BgID/9fX1//////////////////////////////////r6+v/Av7//X19f/yIhIf8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8gHx//dXR0/9zc3P/+/v7/////////////////29ra/1hXV/4dHBywUlFRFwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABsbGwPJSQklD08PP7Q0ND//v7+/v7+/v7//////v7+/v/////+/v7++Pj4/qCgoP9CQUH+HRwc/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/JCMj/mhoaP/V1dX+/f39/v/////+/v7+/Pz8/q2trexrampOlJOTAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMTAwIZaWltr6+vr//v7+/v7+/v7//////v7+/v/////q6ur+gYGB/i8uLv8bGhr+Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/hsaGv4cGxv/Gxoa/iIhIf9ZWVn+1dXV/v7+/v/+/v7+/v7+/vT09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f4cGxv/Gxoa/hwbG/8bGhr+HBsb/xsaGv4cGxv/Gxoa/hwbG/8bGhqmHBsbBgAAAAAcGxsmHBsb7RwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/76+vv////////////39/f/R0ND/////////////////5+fn/zw8PP8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG+QcGxssAAAAABwbG3EbGhr7HBsb/xsaGv4cGxv/Gxoa/hwbG/8bGhr+HBsb/xwbG/5aWlr/+vr6/v/////+/v7+2tra/zs6Ov75+fn//v7+/v/////+/v7+qKen/xsaGv4cGxv/Gxoa/hwbG/8bGhr+HBsb/xsaGv4cGxv/Gxoa+hwbG2YAAAAAHBsbqBwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/JCMj/8PDw//+/v7///////b29v9vb2//HBsb/8rKyv/////////////////19fX/S0tL/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsbmgAAAAAcGxvTGxoa/hwbG/8bGhr+HBsb/xsaGv4cGxv/Gxoa/hwbG/9hYGD++/v7//7+/v7/////vLu7/iYlJf8bGhr+jYyM//39/f7//////v7+/v7+/v+4uLj+IyIi/xsaGv4cGxv/Gxoa/hwbG/8bGhr+HBsb/xsaGv4cGxu+AAAAABwbG/EcGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/Kyoq/8XExP///////////+7u7v9UVFT/HBsb/xwbG/9XV1f/9fX1//////////////////v7+/9dXFz/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG9gAAAAAHBsb/BsaGv4cGxv/Gxoa/hwbG/8bGhr+HBsb/xsaGv5paGj//Pz8/v/////+/v7+n56e/yEgIP5TUlL/OTg4/ignJ//m5ub+//////7+/v7//////v7+/sjIyP8rKir+HBsb/xsaGv4cGxv/Gxoa/hwbG/8bGhr+HBsb4gAAAAAcGxvvHBsb/xwbG/8cGxv/HBsb/xwbG/8cGxv/Ly4u/9DQ0P///////////+Hg4P9HRkb/nZ2d//f39/9/fn7/HBsb/7Gxsf///////////////////////v7+/3l5ef8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/8cGxvWAAAAABwbG88bGhr+HBsb/xsaGv4cGxv/Gxoa/hwbG/96eXn++/v7//7+/v7+/v7/rays/s/Pz//8/Pz+/////8fGxv4cGxv/dXV1/vz8/P/+/v7+//////7+/v7/////2dnZ/jk4OP8bGhr+HBsb/xsaGv4cGxv/Gxoa/hwbG7sAAAAAHBsboxwbG/8cGxv/HBsb/xwbG/8cGxv/MTAw/9bW1v/////////////////09PT//v7+////////////+fn5/zMyMv9HRkb/6enp///////////////////////8/Pz/kpGR/x0cHP8cGxv/HBsb/xwbG/8cGxv/HBsblQAAAAAcGxtoGxoa+hwbG/8bGhr+HBsb/xsaGv6CgYH/+vr6/v/////+/v7+//////7+/v7//////v7+/v7+/v/o6Oj+QUFB/yEgIP6FhYX/8/Pz/v/////+/v7+//////7+/v7m5eX/REND/hwbG/8bGhr+HBsb/xsaGvgdHBxfAAAAABwbGyEcGxvrHBsb/xwbG/8cGxv/LSws/+Li4v/////////////////////////////////9/f3/ysrK/0RDQ/8cGxv/HBsb/yAfH/91dHT/9PPz//////////////////7+/v+pqKj/HBsb/xwbG/8cGxv/HBsb4ikoKCkAAAAAKCgoAR0cHKUcGxv/Gxoa/h0cHP+Li4v+/f39//7+/v7//////v7+/v/////+/v7+9/f3/5mZmf4oJyf/Gxoa/hwbG/8bGhr+HBsb/x0cHP5eXV3/7+/v/v/////+/v7+//////b29v5QUFD/HBsb/hwbG/8hICCfPj09BAAAAAAAAAAAKyoqQBwbG+wcGxv/MjEx/+zs7P///////////////////////////+Pj4/9mZmb/IB8f/xwbG/8cGxv/HBsb/xwbG/8cGxv/HBsb/xwbG/9TUlL/4uHh/////////////v7+/8PDw/8hICD/HBsb6j08PEEAAAAAAAAAAAAAAABSUlIHISAgmB8eHv6SkZH//v7+/v/////+/v7+//////z8/P7ExMT/QkJC/h0cHP8bGhr+HBsb/xsaGv4cGxv/Gxoa/hwbG/8bGhr+HBsb/xwbG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")


user_permission_info = {
            "android.permission.ACCESS_SURFACE_FLINGER": [
                "访问Surface Flinger",
                "Android平台上底层的图形显示支持，一般用于游戏或照相机预览界面和底层模式的屏幕截图"
            ],
            "android.permission.ACCESS_WIFI_STATE": [
                "获取WiFi状态",
                "获取当前WiFi接入的状态以及WLAN热点的信息"
            ],
            "android.permission.ACCOUNT_MANAGER": [
                "账户管理",
                "获取账户验证信息，主要为GMail账户信息，只有系统级进程才能访问的权限"
            ],
            "android.permission.AUTHENTICATE_ACCOUNTS": [
                "验证账户",
                "允许一个程序通过账户验证方式访问账户管理ACCOUNT_MANAGER相关信息"
            ],
            "android.permission.BATTERY_STATS": [
                "电量统计",
                "获取电池电量统计信息"
            ],
            "android.permission.BIND_APPWIDGET": [
                "绑定小插件",
                "允许一个程序告诉appWidget服务需要访问小插件的数据库，只有非常少的应用才用到此权限"
            ],
            "android.permission.BIND_DEVICE_ADMIN": [
                "绑定设备管理",
                "请求系统管理员接收者receiver，只有系统才能使用"
            ],
            "android.permission.BIND_INPUT_METHOD ": [
                "绑定输入法",
                "请求InputMethodService服务，只有系统才能使用"
            ],
            "android.permission.BIND_REMOTEVIEWS": [
                "绑定RemoteView",
                "必须通过RemoteViewsService服务来请求，只有系统才能用"
            ],
            "android.permission.BIND_WALLPAPER": [
                "绑定壁纸",
                "必须通过WallpaperService服务来请求，只有系统才能用"
            ],
            "android.permission.BLUETOOTH": [
                "使用蓝牙",
                "允许程序连接配对过的蓝牙设备"
            ],
            "android.permission.BLUETOOTH_ADMIN": [
                "蓝牙管理",
                "允许程序进行发现和配对新的蓝牙设备"
            ],
            "android.permission.BRICK": [
                "变成砖头",
                "能够禁用手机，非常危险，顾名思义就是让手机变成砖头"
            ],
            "android.permission.BROADCAST_PACKAGE_REMOVED": [
                "应用删除时广播",
                "当一个应用在删除时触发一个广播"
            ],
            "android.permission.BROADCAST_SMS": [
                "收到短信时广播",
                "当收到短信时触发一个广播"
            ],
            "android.permission.BROADCAST_STICKY": [
                "连续广播",
                "允许一个程序收到广播后快速收到下一个广播"
            ],
            "android.permission.BROADCAST_WAP_PUSH": [
                "WAP PUSH广播",
                "WAP PUSH服务收到后触发一个广播"
            ],
            "android.permission.CALL_PHONE": [
                "拨打电话",
                "允许程序从非系统拨号器里输入电话号码"
            ],
            "android.permission.CALL_PRIVILEGED": [
                "通话权限",
                "允许程序拨打电话，替换系统的拨号器界面"
            ],
            "android.permission.CAMERA": [
                "拍照权限",
                "允许访问摄像头进行拍照"
            ],
            "android.permission.CHANGE_COMPONENT_ENABLED_STATE": [
                "改变组件状态",
                "改变组件是否启用状态"
            ],
            "android.permission.CHANGE_CONFIGURATION": [
                "改变配置",
                "允许当前应用改变配置，如定位"
            ],
            "android.permission.CHANGE_NETWORK_STATE": [
                "改变网络状态",
                "改变网络状态如是否能联网"
            ],
            "android.permission.CHANGE_WIFI_MULTICAST_STATE": [
                "改变WiFi多播状态",
                "改变WiFi多播状态"
            ],
            "android.permission.CHANGE_WIFI_STATE": [
                "改变WiFi状态",
                "改变WiFi状态"
            ],
            "android.permission.CLEAR_APP_CACHE": [
                "清除应用缓存",
                "清除应用缓存"
            ],
            "android.permission.CLEAR_APP_USER_DATA": [
                "清除用户数据",
                "清除应用的用户数据"
            ],
            "android.permission.CWJ_GROUP": [
                "底层访问权限",
                "允许CWJ账户组访问底层信息"
            ],
            "android.permission.CELL_PHONE_MASTER_EX": [
                "手机优化大师扩展权限",
                "手机优化大师扩展权限"
            ],
            "android.permission.CONTROL_LOCATION_UPDATES": [
                "控制定位更新",
                "允许获得移动网络定位信息改变"
            ],
            "android.permission.DELETE_CACHE_FILES": [
                "删除缓存文件",
                "允许应用删除缓存文件"
            ],
            "android.permission.DELETE_PACKAGES": [
                "删除应用",
                "允许程序删除应用"
            ],
            "android.permission.DEVICE_POWER": [
                "电源管理",
                "允许访问底层电源管理"
            ],
            "android.permission.DIAGNOSTIC": [
                "应用诊断",
                "允许程序到RW到诊断资源"
            ],
            "android.permission.DISABLE_KEYGUARD": [
                "禁用键盘锁",
                "允许程序禁用键盘锁"
            ],
            "android.permission.DUMP": [
                "转存系统信息",
                "允许程序获取系统dump信息从系统服务"
            ],
            "android.permission.EXPAND_STATUS_BAR": [
                "状态栏控制",
                "允许程序扩展或收缩状态栏"
            ],
            "android.permission.FACTORY_TEST": [
                "工厂测试模式",
                "允许程序运行工厂测试模式"
            ],
            "android.permission.FLASHLIGHT": [
                "使用闪光灯",
                "允许访问闪光灯"
            ],
            "android.permission.FORCE_BACK": [
                "强制后退",
                "允许程序强制使用back后退按键，无论Activity是否在顶层"
            ],
            "android.permission.GET_ACCOUNTS": [
                "访问账户Gmail列表",
                "访问GMail账户列表"
            ],
            "android.permission.GET_PACKAGE_SIZE": [
                "获取应用大小",
                "获取应用的文件大小"
            ],
            "android.permission.GET_TASKS": [
                "获取任务信息",
                "允许程序获取当前或最近运行的应用"
            ],
            "android.permission.GLOBAL_SEARCH": [
                "允许全局搜索",
                "允许程序使用全局搜索功能"
            ],
            "android.permission.HARDWARE_TEST": [
                "硬件测试",
                "访问硬件辅助设备，用于硬件测试"
            ],
            "android.permission.INJECT_EVENTS": [
                "注射事件",
                "允许访问本程序的底层事件，获取按键、轨迹球的事件流"
            ],
            "android.permission.INSTALL_LOCATION_PROVIDER": [
                "安装定位提供",
                "安装定位提供"
            ],
            "android.permission.INSTALL_PACKAGES": [
                "安装应用程序",
                "允许程序安装应用"
            ],
            "android.permission.INTERNAL_SYSTEM_WINDOW": [
                "内部系统窗口",
                "允许程序打开内部窗口，不对第三方应用程序开放此权限"
            ],
            "android.permission.INTERNET": [
                "访问网络",
                "访问网络连接，可能产生GPRS流量"
            ],
            "android.permission.KILL_BACKGROUND_PROCESSES": [
                "结束后台进程",
                "允许程序调用killBackgroundProcesses(String).方法结束后台进程"
            ],
            "android.permission.MANAGE_ACCOUNTS": [
                "管理账户",
                "允许程序管理AccountManager中的账户列表"
            ],
            "android.permission.MANAGE_APP_TOKENS": [
                "管理程序引用",
                "管理创建、摧毁、Z轴顺序，仅用于系统"
            ],
            "android.permission.MTWEAK_USER": [
                "高级权限",
                "允许mTweak用户访问高级系统权限"
            ],
            "android.permission.MTWEAK_FORUM": [
                "社区权限",
                "允许使用mTweak社区权限"
            ],
            "android.permission.MASTER_CLEAR": [
                "软格式化",
                "允许程序执行软格式化，删除系统配置信息"
            ],
            "android.permission.MODIFY_AUDIO_SETTINGS": [
                "修改声音设置",
                "修改声音设置信息"
            ],
            "android.permission.MODIFY_PHONE_STATE": [
                "修改电话状态",
                "修改电话状态，如飞行模式，但不包含替换系统拨号器界面"
            ],
            "android.permission.MOUNT_FORMAT_FILESYSTEMS": [
                "格式化文件系统",
                "格式化可移动文件系统，比如格式化清空SD卡"
            ],
            "android.permission.MOUNT_UNMOUNT_FILESYSTEMS": [
                "挂载文件系统",
                "挂载、反挂载外部文件系统"
            ],
            "android.permission.NFC": [
                "允许NFC通讯",
                "允许程序执行NFC近距离通讯操作，用于移动支持"
            ],
            "android.permission.PERSISTENT_ACTIVITY": [
                "永久Activity",
                "创建一个永久的Activity，该功能标记为将来将被移除"
            ],
            "android.permission.PROCESS_OUTGOING_CALLS": [
                "处理拨出电话",
                "允许程序监视，修改或放弃播出电话"
            ],
            "android.permission.READ_CALENDAR": [
                "读取日程提醒",
                "允许程序读取用户的日程信息"
            ],
            "android.permission.READ_CONTACTS": [
                "读取联系人",
                "允许应用访问联系人通讯录信息"
            ],
            "android.permission.READ_FRAME_BUFFER": [
                "屏幕截图",
                "读取帧缓存用于屏幕截图"
            ],
            "com.android.browser.permission.READ_HISTORY_BOOKMARKS": [
                "读取收藏夹和历史记录",
                "读取浏览器收藏夹和历史记录"
            ],
            "android.permission.READ_INPUT_STATE": [
                "读取输入状态",
                "读取当前键的输入状态，仅用于系统"
            ],
            "android.permission.READ_LOGS": [
                "读取系统日志",
                "读取系统底层日志"
            ],
            "android.permission.READ_PHONE_STATE": [
                "读取电话状态",
                "访问电话状态"
            ],
            "android.permission.READ_SMS": [
                "读取短信内容",
                "读取短信内容"
            ],
            "android.permission.READ_SYNC_SETTINGS": [
                "读取同步设置",
                "读取同步设置，读取Google在线同步设置"
            ],
            "android.permission.READ_SYNC_STATS": [
                "读取同步状态",
                "读取同步状态，获得Google在线同步状态"
            ],
            "android.permission.REBOOT": [
                "重启设备",
                "允许程序重新启动设备"
            ],
            "android.permission.RECEIVE_BOOT_COMPLETED": [
                "开机自动允许",
                "允许程序开机自动运行"
            ],
            "android.permission.RECEIVE_MMS": [
                "接收彩信",
                "接收彩信"
            ],
            "android.permission.RECEIVE_SMS": [
                "接收短信",
                "接收短信"
            ],
            "android.permission.RECEIVE_WAP_PUSH": [
                "接收Wap Push",
                "接收WAP PUSH信息"
            ],
            "android.permission.RECORD_AUDIO": [
                "录音",
                "录制声音通过手机或耳机的麦克"
            ],
            "android.permission.REORDER_TASKS": [
                "排序系统任务",
                "重新排序系统Z轴运行中的任务"
            ],
            "android.permission.RESTART_PACKAGES": [
                "结束系统任务",
                "结束任务通过restartPackage(String)方法，该方式将在外来放弃"
            ],
            "android.permission.SEND_SMS": [
                "发送短信",
                "发送短信"
            ],
            "android.permission.SET_ACTIVITY_WATCHER": [
                "设置Activity观察其",
                "设置Activity观察器一般用于monkey测试"
            ],
            "com.android.alarm.permission.SET_ALARM": [
                "设置闹铃提醒",
                "设置闹铃提醒"
            ],
            "android.permission.SET_ALWAYS_FINISH": [
                "设置总是退出",
                "设置程序在后台是否总是退出"
            ],
            "android.permission.SET_ANIMATION_SCALE": [
                "设置动画缩放",
                "设置全局动画缩放"
            ],
            "android.permission.SET_DEBUG_APP": [
                "设置调试程序",
                "设置调试程序，一般用于开发"
            ],
            "android.permission.SET_ORIENTATION": [
                "设置屏幕方向",
                "设置屏幕方向为横屏或标准方式显示，不用于普通应用"
            ],
            "android.permission.SET_PREFERRED_APPLICATIONS": [
                "设置应用参数",
                "设置应用的参数，已不再工作具体查看addPackageToPreferred(String) 介绍"
            ],
            "android.permission.SET_PROCESS_LIMIT": [
                "设置进程限制",
                "允许程序设置最大的进程数量的限制"
            ],
            "android.permission.SET_TIME": [
                "设置系统时间",
                "设置系统时间"
            ],
            "android.permission.SET_TIME_ZONE": [
                "设置系统时区",
                "设置系统时区"
            ],
            "android.permission.SET_WALLPAPER": [
                "设置桌面壁纸",
                "设置桌面壁纸"
            ],
            "android.permission.SET_WALLPAPER_HINTS": [
                "设置壁纸建议",
                "设置壁纸建议"
            ],
            "android.permission.SIGNAL_PERSISTENT_PROCESSES": [
                "发送永久进程信号",
                "发送一个永久的进程信号"
            ],
            "android.permission.STATUS_BAR": [
                "状态栏控制",
                "允许程序打开、关闭、禁用状态栏"
            ],
            "android.permission.SUBSCRIBED_FEEDS_READ": [
                "访问订阅内容",
                "访问订阅信息的数据库"
            ],
            "android.permission.SUBSCRIBED_FEEDS_WRITE": [
                "写入订阅内容",
                "写入或修改订阅内容的数据库"
            ],
            "android.permission.SYSTEM_ALERT_WINDOW": [
                "显示系统窗口",
                "显示系统窗口"
            ],
            "android.permission.UPDATE_DEVICE_STATS": [
                "更新设备状态",
                "更新设备状态"
            ],
            "android.permission.USE_CREDENTIALS": [
                "使用证书",
                "允许程序请求验证从AccountManager"
            ],
            "android.permission.USE_SIP": [
                "使用SIP视频",
                "允许程序使用SIP视频服务"
            ],
            "android.permission.VIBRATE": [
                "使用振动",
                "允许振动"
            ],
            "android.permission.WAKE_LOCK": [
                "唤醒锁定",
                "允许程序在手机屏幕关闭后后台进程仍然运行"
            ],
            "android.permission.WRITE_APN_SETTINGS": [
                "写入GPRS接入点设置",
                "写入网络GPRS接入点设置"
            ],
            "android.permission.WRITE_CALENDAR": [
                "写入日程提醒",
                "写入日程，但不可读取"
            ],
            "android.permission.WRITE_CONTACTS": [
                "写入联系人",
                "写入联系人，但不可读取"
            ],
            "android.permission.WRITE_EXTERNAL_STORAGE": [
                "写入外部存储",
                "允许程序写入外部存储，如SD卡上写文件"
            ],
            "android.permission.WRITE_GSERVICES": [
                "写入Google地图数据",
                "允许程序写入Google Map服务数据"
            ],
            "com.android.browser.permission.WRITE_HISTORY_BOOKMARKS": [
                "写入收藏夹和历史记录",
                "写入浏览器历史记录或收藏夹，但不可读取"
            ],
            "android.permission.WRITE_SECURE_SETTINGS": [
                "读写系统敏感设置",
                "允许程序读写系统安全敏感的设置项"
            ],
            "android.permission.WRITE_SETTINGS": [
                "读写系统设置",
                "允许读写系统设置项"
            ],
            "android.permission.WRITE_SMS": [
                "编写短信",
                "允许编写短信"
            ],
            "android.permission.WRITE_SYNC_SETTINGS": [
                "写入在线同步设置",
                "写入Google在线同步设置"
            ],
            "android.permission.ACCESS_NETWORK_STATE":[
                "获取网络状态",
                "获取网络信息状态，如当前的网络连接是否有效"
            ]
        }