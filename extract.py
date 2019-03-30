"""
@author:qh
@datetime:2019-3-15
@mood:<(*￣▽￣*)/
"""

import os
import re
import base64
import requests
import json
import shutil
import zipfile
import hashlib
from tkinter import *
from tkinter import ttk
from TkinterDnD2 import *
from TkinterDnD2 import TkinterDnD
from threading import Thread
from pyaxmlparser import APK
from pyaxmlparser.utils import NS_ANDROID
from fake_useragent import UserAgent
from utils import user_permission_info, img


class ApkR(APK):
    def __init__(self, apk):
        super().__init__(apk)

    def get_permission(self, **attribute_filter):
        tag = self.xml.findall('.//uses-permission')
        if len(tag) == 0:
            return None
        permission_list = []
        for item in tag:
            skip_this_item = False
            for attr, val in list(attribute_filter.items()):
                attr_val = item.get(NS_ANDROID + attr)
                if attr_val != val:
                    skip_this_item = True
                    break
            if skip_this_item:
                continue
            value = item.get(NS_ANDROID + 'name')
            if value is not None:
                permission_list.append(value)
        return permission_list


class ApkExtract(object):
    def __init__(self):
        self.on_off = True
        self.tostring = {
            'info': '',
            'package_name': '',
            'package_version_code': '',
            'package_version_name': '',
            'game_name': '',
            'md5_value': '',
            'empty': '',
            'apk_size': ''
        }
        with open('C:\Windows\Temp\Icon.ico', 'wb') as fp:
            fp.write(base64.b64decode(img))
        self.app = self.make_app()
        self.app.mainloop()

    @staticmethod
    def get_icon():
        save_icon_path = '{}.png'.format(file_path[:-4])
        shutil.copyfile('C:\Windows\Temp\Temp.png', save_icon_path)

    # 检查病毒
    def check_virus(self):
        def _get_response():
            sha_value = self.app.children['en'].get()
            if not sha_value:
                return '请等待MD值提取完成后再检测', '#4c4f8b'
            ua = UserAgent(verify_ssl=False).random
            headers = {
                'User-Agent': ua
            }
            try:
                res = requests.get('https://www.virustotal.com/ui/files/{}'.format(sha_value), headers=headers).json()
            except requests.exceptions.ConnectionError as e:
                return '查询失败，请检查网络', '#4c4f8b'
            else:
                if res.get('data'):
                    a = res['data']['attributes']['last_analysis_stats']['malicious']
                    # print(res)
                    with open('check_results.json', 'w', encoding='utf-8') as f2:
                        f2.write(json.dumps(res, ensure_ascii=False, indent=4))
                    return '共{}个引擎检测到恶意文件！'.format(a), 'red'
                else:
                    return '没有检测到病毒，文件安全！', 'green'

        def _main():
            lb2 = self.app.children['lb2']
            lb2.config(text='正在检测中...', fg='#4c4f8b')
            data = _get_response()
            lb2.config(text=data[0], fg=data[1])

        t = Thread(target=_main, )
        t.start()

    def show_permission(self):
        if self.on_off:
            self.app.geometry('510x640')
            self.on_off = False

        else:
            self.app.geometry('510x292')
            self.on_off = True

    @staticmethod
    def get_prm_info(item_list):
        permission_info = []
        unknown_per = []
        for item in item_list:
            if user_permission_info.get(item):
                permission_info.append(user_permission_info.get(item))
            else:
                unknown_per.append(['未知权限', item])
        permission_info_list = permission_info + unknown_per
        return permission_info_list

    def drag_and_drop(self, event):
        global file_path
        file_path = event.data.strip('{}')

        def _get_info():
            apk = ApkR(file_path)
            ic_data = apk.icon_data
            package_name = apk.package
            apk_size = '{:.1f}MB'.format(os.path.getsize(file_path) / 1024 / 1024)
            package_version_code = apk.version_code
            package_version_name = apk.version_name
            game_name = apk.application
            ele = apk.get_permission()
            a = self.get_prm_info(ele)
            lbx = self.app.children['lbx']
            lbx.delete(0, END)
            for index, item in enumerate(a):
                text = '* {}                -{}'.format(item[0], item[1])
                lbx.insert(index, text + ' ' * 16)
            show_info = '{}安装所需权限（{}）'.format(game_name, len(a))
            lbx.insert(0, '{:>60} '.format(show_info))
            lbx.insert(1, '')
            lbx.insert(END, '')
            lbx.insert(END, '')
            lbx.insert(END, '')
            self.tostring['info'].set(file_path)
            self.tostring['apk_size'].set(apk_size)
            self.tostring['package_name'].set(package_name)
            self.tostring['package_version_code'].set(package_version_code)
            self.tostring['package_version_name'].set(package_version_name)
            self.tostring['game_name'].set(game_name)
            _show_img(ic_data)

        def _show_img(icon_data):
            with open('C:\Windows\Temp\Temp.png', 'wb+') as f1:
                f1.write(icon_data)
            fr1 = self.app.children['lb']
            try:
                ic_path = PhotoImage(file="C:\Windows\Temp\Temp.png")
                fr1['image'] = ic_path
                fr1.image = ic_path
            except TclError:
                fr1['image'] = ''
                fr1.image = ''
                fr1['text'] = '未找到Icon图标'

        def _refresh():
            self.tostring['md5_value'].set('')
            lb2 = self.app.children['lb2']
            lb2['text'] = ''

        def _get_md5_value():
            if not os.path.isfile(file_path):
                return
            my_hash = hashlib.md5()
            total_size = os.path.getsize(file_path)
            file_size = 0
            iter_size = int(total_size / 100)
            with open(file_path, 'rb') as f:
                while True:
                    b = f.read(iter_size)
                    file_size += len(b)
                    md5_value = '{}%'.format(int(round(float(file_size / total_size) * 100)))
                    sys.stdout.flush()
                    self.tostring['md5_value'].set(md5_value)
                    if not b:
                        break
                    my_hash.update(b)
            md5_value = my_hash.hexdigest().upper()
            print('222')
            self.tostring['md5_value'].set(md5_value)

        def _main():
            _refresh()
            _get_info()
            t = Thread(target=_get_md5_value(), )
            t.start()
            # _get_md5_value()

        m = Thread(target=_main, name='aa')
        m.start()

    def make_app(self):
        window = TkinterDnD.Tk()

        sw = 510
        sh = 292
        ww = window.winfo_screenwidth()
        wh = window.winfo_screenheight()
        x = int((ww - sw) / 3)
        y = int((wh - sh) / 3)
        window.geometry('{}x{}+{}+{}'.format(sw, sh, x, y))
        window.title('APK信息提取工具')
        window.resizable(False, False)
        window.iconbitmap('C:\Windows\Temp\Icon.ico')

        self.tostring['info'] = StringVar()
        self.tostring['package_name'] = StringVar()
        self.tostring['package_version_code'] = StringVar()
        self.tostring['package_version_name'] = StringVar()
        self.tostring['game_name'] = StringVar()
        self.tostring['md5_value'] = StringVar()
        self.tostring['empty'] = StringVar()
        self.tostring['apk_size'] = StringVar()

        Label(window, name='lb', borderwidth=2, relief='ridge', background='#f3f3f3').place_configure(width=190,
                                                                                                      height=190, x=10,
                                                                                                      y=10, )

        LabelFrame(window, width=280, height=196, text='  游戏详情  ', ).place_configure(x=210, y=5)
        Label(window, text='游戏名称：', fg='#0000ff').place(x=226, y=30)
        ttk.Entry(window, state='readonly', textvariable=self.tostring['game_name'], foreground='#0000ff').place_configure(
            width=180, x=290, y=30)

        Label(window, text='游戏大小：', fg='#ff8c00').place(x=226, y=65)
        ttk.Entry(window, state='readonly', textvariable=self.tostring['apk_size'], foreground='#ff8c00').place_configure(
            width=180, x=290, y=65)

        Label(window, text='包名：', fg='#008000').place(x=226, y=100)
        ttk.Entry(window, state='readonly', textvariable=self.tostring['package_name'],
                  foreground='#008000').place_configure(width=180, x=290, y=100)

        Label(window, text='版本号：', fg='#ff00ff').place(x=226, y=135)
        ttk.Entry(window, state='readonly', textvariable=self.tostring['package_version_code'],
                  foreground='#ff00ff').place_configure(width=180, x=290, y=135)

        Label(window, text='版本名：', fg='#8b0000').place(x=226, y=170)
        ttk.Entry(window, state='readonly', textvariable=self.tostring['package_version_name'],
                  foreground='#8b0000').place_configure(width=180, x=290, y=170)

        fr2 = Frame(window, width=140, height=30)
        fr2.pack_propagate(0)
        ttk.Button(fr2, text='获取Icon', command=self.get_icon).place_configure(x=0, y=0, width=60, height=30)

        ttk.Button(fr2, text='病毒检测', command=self.check_virus).place_configure(x=70, y=0, width=60, height=30)
        fr2.place(x=10, y=218)

        Label(window, name='lb2', font=('Hack', 10, 'bold')).place_configure(x=200, y=228)

        ttk.Button(window, text='查看权限', command=self.show_permission).place_configure(width=70, height=30, x=420, y=218)

        # 提取MD5值
        Label(window, text='MD5值：', font=('Arial', 8,), fg='#4156f4').place(x=10, y=260)
        ttk.Entry(window, state='readonly', width=40, name='en', textvariable=self.tostring['md5_value'],
                  foreground='#4156f4').place(x=60, y=260)

        Label(window, text='注：将apk文件拖入工作区').place_configure(x=350, y=260)

        lbf = LabelFrame(text='  详情  ')
        lbf.place_configure(x=10, y=320, width=480, height=310)
        lb = Listbox(window, name='lbx', bg='#f9fef9', state='normal')
        sb = Scrollbar(lb)
        sb.pack(side=RIGHT, fill=Y)
        sb2 = Scrollbar(lb, orient=HORIZONTAL)
        sb2.pack(side=BOTTOM, fill=X)
        lb.config(yscrollcommand=sb.set)
        lb.config(xscrollcommand=sb2.set)
        lb.place_configure(x=20, y=340, width=460, height=280)
        sb.config(command=lb.yview)
        sb2.config(command=lb.xview)
        window.drop_target_register(DND_FILES)
        window.dnd_bind('<<Drop>>', self.drag_and_drop)
        return window

    def __del__(self):
        os.remove('C:\Windows\Temp\Icon.ico')
        os.remove('C:\Windows\Temp\Temp.png')


if __name__ == '__main__':
    new = ApkExtract()