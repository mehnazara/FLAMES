def all_char(z):
    for char in z:
        if char == " ":
            z.remove(char)
    return z

def uncommon_count(a, b):
    uncommon_count = 0
    for char in a:
        if char not in b:
            uncommon_count += 1
    return uncommon_count

def to_check_for_uncommon_chars(x, y):
    playerl = list(x)
    crushl = list(y)
    new_playerl = all_char(playerl)
    new_crushl = all_char(crushl)
    player_count = uncommon_count(new_playerl, new_crushl)
    crush_count = uncommon_count(new_crushl, new_playerl)
    total = player_count + crush_count
    abstract_list = []
    for item in new_playerl:
        num1 = 0
        num2 = 0
        if item in new_crushl:
            if item not in abstract_list:
                num1 = new_playerl.count(item)
                num2 = new_crushl.count(item)
                abstract_list.append(item)
                if num1 > num2:
                    total += (num1 - num2)
                elif num2 > num1:
                    total += (num2 - num1)
                elif num1 == num2:
                    total += 0
    return total

def flames(c):
    for i in range(1,7):
        num = c
        num2 = num - i
        if num2 % 6 == 0:
            if i == 1:
                print("Bad Luck: you get S - Siblings, I think you just got bro-zoned")
                break
            elif i == 2:
                print("Aha, you get F - Friendship. I guess that's a good start")
                break
            elif i == 3:
                print("Jackpot! You get L - Love. Have you confessed yet?")
                break
            elif i == 4:
                print("Welp, you get A - Affection. Cute!")
                break
            elif i == 5:
                print("Congratulations! It's M - Marriage. Invite me, will you?")
                break
            else:
                print("You should be looking for a truce because it's E - Enemies!")




first_name = input(
"Hello! I see you have arrived at this silly game of 'FLAMES'.\n"
"This version automatically generates the final result.\nShall we begin to find your fate with your crush?\n" 
"What's your name? : ")
second_name = input(
"It'll be our little secret.\n"
"Enter your crush's name: ")
player = first_name.lower()
crush = second_name.lower()
count = to_check_for_uncommon_chars(player, crush)
if count > 0:
    flames(count)
else:
    print("Maximum similarity found. Consider yourselves to be soulmates!!!")





