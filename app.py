import sys
import const
import config

localVarA = '神秘的魔法石'
localVarB = '消失的密室'
localVarC = '阿茲卡班的逃犯'
localVarD = '火盃的考驗'

def callGlobalVars() -> None:
    print('The count is {}'.format(const.globalCount))
    print('The amount is {}'.format(const.globalAmount))
    print('桃園三結義的大哥是{}'.format(const.globalList[0]))
    print('鬼殺隊的{}又稱頭柱'.format(const.globalDict['頭柱']))

def callConfigs() -> None:
    print('用戶姓名：{}'.format(config.name))
    print('稱謂：{}'.format(config.title))
    print('綽號：{}'.format(config.nickname))

def callLocalVars(seriesName) -> None:
    print(seriesName)
    print(localVarA)
    print(localVarB)
    print(localVarC)
    print(localVarD)

def main() -> int:
    callGlobalVars()
    callConfigs()
    callLocalVars('哈利・波特')
    print("This an output text from the main scope.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
