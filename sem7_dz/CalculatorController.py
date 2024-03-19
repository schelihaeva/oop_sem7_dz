# Все связующий и управляющий скрипт

import CalculatorView
import CalculatorOperation
import CalculatorLog

def button_click():
    value_lst, kind_oper = CalculatorView.get_value()
    CalculatorLog.logwrite("User input: ", value_lst) 
    result = CalculatorOperation.calc(value_lst, kind_oper)
    CalculatorLog.logwrite("Result of calculations is: ", result)
    CalculatorView.output(result)