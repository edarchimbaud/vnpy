import gettext
from time import sleep
from vnpy_scripttrader import ScriptEngine

gettext.bindtextdomain("myapp", "")
gettext.textdomain("myapp")
_ = gettext.gettext

def run(engine: ScriptEngine):
    """
    Description of the main function of the scripting strategy:
    1. the only input is the script engine ScriptEngine object, which is used to perform the query and request operations.
    2. this function is started in a separate thread, unlike other strategy modules which are event driven.
    3. while loop maintenance, please through the engine.strategy_active state to determine, to achieve a controlled exit

    Examples of application of script strategy:
    1. Customized basket delegate execution execution algorithm
    2. hedging strategy between stock index futures and a basket of stocks
    3. domestic and foreign commodity cross-exchange arbitrage
    4. customized portfolio index ticker monitoring and news notification
    5. stock market scanning stock picking trading strategies (Dragon 1 and Dragon 2)
    6. etc
    """
    vt_symbols = ["IF1912.CFFEX", "rb2001.SHFE"]

    # Subscribe to Quotes
    engine.subscribe(vt_symbols)

    # Getting Contract Information
    for vt_symbol in vt_symbols:
        contract = engine.get_contract(vt_symbol)
        msg = f"Contract Information, {contract}"
        engine.write_log(msg)

    # Runs continuously, using strategy_active to determine whether to exit the program or not
    while engine.strategy_active:
        # Polling for quotes
        for vt_symbol in vt_symbols:
            tick = engine.get_tick(vt_symbol)
            msg = f"Latest Quotes, {tick}"
            engine.write_log(msg)

        # Wait 3 seconds to advance to the next round
        sleep(3)
