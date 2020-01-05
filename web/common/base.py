
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

'''
1.  def findElementNew(self, locator):常用元素定位,加入了显示等待和元素判断可见.locator传元祖:("id", "value1");
2.  def findElement(self, locator):常用元素定位,加入了显示等待;
3.  def findElements(self, locator):复数定位,可以通过下标选取元素;
4.  def sendKeys(self, locator, text=''):输入值,locator传元祖:("id", "value1"),text传入要输入的值;
5.  def click(self, locator):locator传元祖:("id", "value1")点击元素;
6.  def clear(self, locator):locator传元祖:("id", "value1"),清空输入框;
7.  def clearSendKeys(self, locator, text):先清空再输入;
8.  def isSelected(self, locator):通过is_selected判断元素是否被选中，返回bool值,选中返回Ture ,没选中返回False;
9.  def isElementExist(self, locator):判断元素是否定位到或是否存在。直接去定位元素,定位到就返回T,报错就返回F;
10. def isElementExist2(self, locator):判断元素是否定位到或是否存在。定位一组元素,打印长度,0为F,1为T;
11. def is_title(self, _title=''):判断title是否等于预期。''内输入预期抬头. 返回bool值,通过EC.title_is判断;
12. def is_title_contains(self, _title=''):判断title是否包含预期。''内输入预期抬头.返回bool值;
13. def is_text_in_element(self, locator, text=''):判断元素locator存在指定文本text,可结合17使用;
14. def is_value_in_element(self, locator, _value=''):判断元素locator的值为_value;
15. def is_alert(self, timeout=3):判断alert弹出;
16. def get_title(self):通过self.driver.title获取title;
17. def get_text(self, locator):通过self.findElementNew(locator).text获取文本,可结合13使用;
18. def get_attribute(self, locator, name):获取定位到元素的属性;
19. def js_focus_element(self, locator):聚焦元素;
20. def js_scroll_top(self):滚动到顶部;
21. def js_scroll_end(self,x=0):滚动到底部;
22. def select_by_index(self, locator, index=0):下拉框,通过索引,index是索引第几个，从0开始，默认选第一个;
23. def select_by_value(self, locator, value):通过value属性选择被选项;
24. def select_by_text(self, locator, text):通过文本值选择被选项;
25. def switch_iframe(self, id_index_locator):切换iframe;
26. def switch_handle(self, window_name):根据handle切换页面;
27. def switch_alert(self):切换alert;
28. def move_to_element(self, locator):鼠标悬停操作;
'''


class Base():
    '''基于原生的selenium做二次封装'''

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self, locator):
        ''' 001
        定位到元素，返回元素对象，没定位到，Timeout异常，isinstance判断一个对象的变量类型,判断locator的类型为元祖。
        如果给出的locator不是元祖，则给出错误提示。
        如果是，则返回元素定位。
        '''
        # isinstance类型检查，定义locator为tuple（元祖）
        if not isinstance(locator, tuple):
            # 如果locator不是元祖，则执行以下：
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:  # 如果locator是元祖，则执行以下：
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            # locator[0]为元祖的第一个元素, locator[1]为元祖的第二个值。
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            # expected_conditions.presence_of_element_located(locator):元素locator出现。
            return ele

    def findElement(self, locator):
        ''' 002
        定位到元素，返回元素对象，没定位到，Timeout异常，isinstance判断一个对象的变量类型,判断locator的类型为元祖。
        如果给出的locator不是元祖，则给出错误提示。
        如果是，则返回元素定位。
        '''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self, locator):
        ''' 003
        定位到一组元素，返回元素对象，没定位到，Timeout异常，isinstance判断一个对象的变量类型,判断locator的类型为元祖。
        如果给出的locator不是元祖，则给出错误提示。
        如果是，则返回元素定位。
        '''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []  # 这里返回一个list

    def sendKeys(self, locator, text=''):
        ''' 004
        定位到一个元素，再输入文本。
        :param locator: 元素
        :param text: 文本，默认为一个空字符串。
        :return:
        '''
        ele = self.findElementNew(locator)
        ele.send_keys(text)

    def click(self, locator):
        ''' 005
        点击一个元素。
        :param locator: 元素
        :return:
        '''
        ele = self.findElementNew(locator)
        ele.click()

    def clear(self, locator):
        ''' 006
        定位一个输入框，清空
        :param locator:
        :return:
        '''
        ele = self.findElementNew(locator)
        ele.clear()

    def clearSendKeys(self, locator, text):
        ''' 007
        先清空再输入。
        :param locator:
        :param text:
        :return:
        '''
        ele = self.findElementNew(locator)
        ele.clear()
        ele.send_keys(text)

    def isSelected(self, locator):
        ''' 008
        判断元素是否被选中，返回bool值
        '''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        ''' 009
        判断元素是否定位到或是否存在。
        :param locator:
        :return:
        '''
        try:
            # 定位到返回True
            self.findElementNew(locator)
            return True
        except:
            # 报错则返回Fales
            return False

    def isElementExist2(self, locator):
        ''' 010
        判断元素是否定位到或是否存在。
        定位一组元素，返回元素list。
        打印list长度，如果等于0，则是元素不存在。等于1则定位到元素，大于1则定位到元素组，打印元素个数N。
        :param locator:
        :return:
        '''

        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self, _title=''):
        ''' 011
        判断title是否等于预期。
        等于则返回Ture
        不等于则返回Fales
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title=''):
        ''' 012
        判断title是否包含预期。
        包含则返回Ture
        不包含于则返回Fales
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text=''):
        ''' 013
        判断元素locator存在指定文本text
        :param locator: 元素
        :param text: 指定文本
        :return: 存在返回True，不存在返回False
        '''
        if not isinstance(locator, tuple):
            # isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value=''):
        ''' 014
        返回bool值, value为空字符串，返回Fasle
        判断元素locator的值为_value
        :param locator: 元素
        :param _value: 元素的值
        :return: 存在返回True，不存在返回False
        '''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        ''' 015
        判断alert弹出。
        EC.alert_is_present:定位弹窗,打印弹窗内容,如果可以打印,则回返弹窗,如果报错,则没有弹窗.
        '''
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            print("活捉一个弹窗")
            return result
        except:
            print("没有找到弹窗")
            return False

    def get_title(self):
        ''' 016
        获取title'''
        return self.driver.title

    def get_text(self, locator):
        ''' 017
        获取文本'''
        try:
            t = self.findElementNew(locator).text
            return t
        except:
            print("获取text失败，返回'' ")
            return ""

    def get_attribute(self, locator, name):
        ''' 018
        获取定位到元素的属性'''
        try:
            element = self.findElementNew(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回'' " % name)
            return ""

    def js_focus_element(self, locator):
        ''' 019
        聚焦元素'''
        target = self.findElementNew(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        ''' 020
        滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        ''' 021
        滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        ''' 022
        通过索引,index是索引第几个，从0开始，默认选第一个'''
        element = self.findElementNew(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        ''' 023
        通过value属性选择被选项'''
        element = self.findElementNew(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        ''' 024
        通过文本值选择被选项'''
        element = self.findElementNew(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        ''' 025
        切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElementNew(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")

    def switch_handle(self, window_name):
        ''' 026
        根据handle切换页面'''

        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        ''' 027
        切换alert'''
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    def move_to_element(self, locator):
        ''' 028
        鼠标悬停操作'''
        ele = self.findElementNew(locator)
        ActionChains(self.driver).move_to_element(ele).perform()
