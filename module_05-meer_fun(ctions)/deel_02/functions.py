import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return personCash['gold'] + copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + platinum2gold(personCash['platinum'])

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    journeyCosts = ((people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)) * JOURNEY_IN_DAYS
    return round(copper2gold(journeyCosts), 2)


##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lst = []
    for x in range(len(list)):
        if list[x][key] == value:
            lst.append(list[x])
    return lst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    lst = []
    for x in range(len(friends)):
        if friends[x]['adventuring'] and friends[x]['shareWith']:
            lst.append(friends[x])
    return lst

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    horsesCosts = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    tentsCosts = tents * COST_TENT_GOLD_PER_WEEK * 2
    return silver2gold(horsesCosts) + tentsCosts

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    lst = []
    for item in items:
        itemText = f"{item['amount']}{item['unit']} {item['name']}"
        lst.append(itemText)
    return ', '.join(lst)

def getItemsValueInGold(items:list) -> float:
    gold = 0
    for item in items:
        if item['price']['type'] == 'copper':
            gold += copper2gold(item['price']['amount'] * item['amount'])

        if item['price']['type'] == 'silver':
            gold += silver2gold(item['price']['amount']* item['amount'])

        if item['price']['type'] == 'gold':
            gold += item['price']['amount'] * item['amount']

        if item['price']['type'] == 'platinum':
            gold += platinum2gold(item['price']['amount']* item['amount'])
    return gold

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totalGold = 0
    for cash in people:
        totalGold += copper2gold(cash['cash']['copper'])
        totalGold += silver2gold(cash['cash']['silver'])
        totalGold += cash['cash']['gold']
        totalGold += platinum2gold(cash['cash']['platinum'])
    return round(totalGold, 2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    lstInvestors = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            lstInvestors.append(investor)
    return lstInvestors

def getAdventuringInvestors(investors:list) -> list:
    lstAdventuringInvestors = []
    for investor in getInterestingInvestors(investors):
        if investor['adventuring']:
            lstAdventuringInvestors.append(investor)
    return lstAdventuringInvestors

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totalCosts = 0

    adventuringInvestors = getAdventuringInvestors(investors)

    for investor in adventuringInvestors:
        totalCosts += getItemsValueInGold(gear)

    # investorHorse = getNumberOfHorsesNeeded(len(adventuringInvestors))
    # investorTent = getNumberOfTentsNeeded(len(adventuringInvestors))

    investorJourneyCosts = getJourneyFoodCostsInGold(len(adventuringInvestors), len(adventuringInvestors))
    investorRentalCosts = getTotalRentalCost(len(adventuringInvestors), len(adventuringInvestors))
    
    totalCosts += investorJourneyCosts + investorRentalCosts
    return totalCosts

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()