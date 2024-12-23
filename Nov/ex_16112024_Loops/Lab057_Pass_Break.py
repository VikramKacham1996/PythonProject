for i in range(1, 10,1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass # pass is a placeholder statement that does nothing
    #it's used when a statement is syntactically required but no action is needed.

# |i|condition|o/p
#|0|0==6->false|0/p_ nothing will be printed
#|1|1==6->false|0/p_ nothing will be printed
#|2|2==6->false|0/p_ nothing will be printed
#|3|3==6->false|0/p_ nothing will be printed


#|4|4==6->false|0/p_ nothing will be printed
#|5|5==5->false|0/p_ 5
#|6|6==6->false|0/p_ 6
#|7|7==6->false|0/p_ nothing will be printed
#|8|8==6->false|0/p_ nothing will be printed
#|9|9==6->false|0/p_ loop finished

