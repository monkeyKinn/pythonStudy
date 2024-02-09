have_money = True
have_friends = False

print(type(have_money))
print(type(have_friends))

# 结合判断语句使用
if have_money and have_friends:
    print("I have money and friends")
elif have_money and not have_friends:
    print("I have money but no friends")
elif not have_money and have_friends:
    print("I have no money but friends")
else:
    print("I have no money and no friends")
